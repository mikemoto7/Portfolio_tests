#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
%(scriptName)s Script Description:

This is the script used to start test runs.

Start tests:

   %(scriptName)s
   %(scriptName)s -h
   %(scriptName)s --h
      Displays this help screen.

   %(scriptName)s --tr misc
      Test run all of the misc tests.

   %(scriptName)s --tr lf
      Rerun failed tests from the previous test run.

   %(scriptName)s --tr testcase_name
      Run a specific testcase.

   %(scriptName)s --tr list
      Display a list of the test run names.

      Test run names come from file %(tc_list_file)s

Misc options:

   %(scriptName)s --cc
      Clear the cache.


"""

import os, sys, re, getopt

scriptName = os.path.basename(__file__).replace('.pyc', '.py')
scriptDir  = os.path.dirname(os.path.realpath(__file__))

sys.path.append(scriptDir + '/lib')
sys.path.append(scriptDir + '/bin')

from printoutput import printout
from run_command import run_command
import command_list


#====================================================

tc_list_file= scriptDir + '/testcases_default.cfg'

def get_docstring():
    global tc_list_file
    return __doc__ % {'scriptName': scriptName, 'tc_list_file': tc_list_file }

def usage(exit_or_return='exit'):
    printout(get_docstring())
    if exit_or_return == 'exit':
        sys.exit(1)
    else:
        return

# def get_test_runstrings():
#     test_runstrings = []
#     for line in get_docstring().split('\n'):
#         found = re.search('^ *(' + scriptName + ' +-.+)$', line)
#         if found:
#             test_runstrings.append(found.group(1))
#     return test_runstrings

#===================================================

test_results_test_package_subdir = ''

def error_status(msg):
    print(msg)
    if test_results_test_package_subdir != '':
       run_command('echo "' + msg + '" > ' + test_results_test_package_subdir + '/STATUS_ERROR.txt')
    sys.exit(1)
 

#===================================================

if __name__ == '__main__':

    command_list.command_list(argv=sys.argv, your_scripts_help_function=[usage, 'return'])

    if len(sys.argv) == 1:
        usage()

    logfile=scriptName + '.log'
    script_logfile=scriptDir + '/' + logfile
    
    curr_dir= os.getcwd()
    if curr_dir != scriptDir:
       error_status("ERROR:  You must be cd'ed in the same directory as this script before you can run this script.")

    tr_from_user = ''
 
    try:
        opts, args = getopt.getopt(sys.argv[1:], "h", ["h", "cc", "tr="])
    except getopt.GetoptError as err:
        print("Runstring " + str(err))
        sys.exit(1)
    
    cmd_options=''
    clear_cache = False
    for opt, arg in opts:
        if opt == "-h" or opt == "--h":
            usage()
        elif opt == "--cc":
            clear_cache = True
        elif opt == "--tr":
            if arg == 'list':
                for line in open(tc_list_file, 'r').read().splitlines():
                    print(line)
                sys.exit(1)
            tr_from_user = arg
        else:
            error_status("Unrecognized runstring option: " + opt)
    
    if clear_cache == True:
       cmd = "find . -name __pycache__ | xargs rm -fr"
       rc, output, error = run_command(cmd)
    
    if not os.path.isfile(tc_list_file):
       error_status("ERROR: tc_list_file does not exist: " + tc_list_file)

    if tr_from_user == '':
       error_status("ERROR: Must specify --tr name")

    tc_name = ''
    if 'tc:' in tr_from_user:
        tc_name = tr_from_user.split(':')[1]
        tr_from_user = "tc"

    tr_match = False

    for line in open(tc_list_file, 'r').read().splitlines():
       if line == '': continue

       if line[0] == '#': continue

       tr_from_file = line.split(':')[0].strip()
       if tr_from_user+":" != tr_from_file+":":
           continue

       tr_match = True
       break

    if tr_match == False:
       error_status("ERROR: No match in the tc_list_file " + tc_list_file + " for the tr " + tr_from_user + " you specified in the runstring.")

    if line == '':
        error_status("ERROR: line is empty.")

    # print(147, line)
    rest_of_line = re.sub(tr_from_file+':(.+)$', r'\1', line).strip()
    # print(148, rest_of_line)
    if '%' in rest_of_line:
        cmd_test = rest_of_line.split('%')[0].strip()
        description = rest_of_line.split('%')[1]
    else:
        cmd_test = rest_of_line
        description = 'no_description'
 
    # print(149, cmd_test)
    if tc_name != '':
        cmd_test += tc_name
        test_package_dir_path= os.path.dirname(re.sub('^.*? +([^ ]*?)$', r'\1', cmd_test))
    else:
        test_package_dir_path= re.sub('^.*? +([^ ]*?)$', r'\1', cmd_test)
    # print(150, cmd_test)
    # print(158, test_package_dir_path)
    if test_package_dir_path == '':
        error_status("ERROR: test_package_dir_path name in cmd_test is empty.  cmd_test = " + cmd_test)
    if test_package_dir_path[0] == '-':
        error_status("ERROR: Missing test_package_dir_path name in runstring.  cmd_test = " + cmd_test)
 
    cmd = "rm -fr " + test_package_dir_path + '/*.actual '
    rc, output, error = run_command(cmd)
    if rc != 0:
        error_status("ERROR: Error on command = " + cmd) 
 
    cmd_test=re.sub("py.test", "py.test " + cmd_options + ' ', cmd_test)
    cmd_test_plus_script = 'script -q -c "' + cmd_test + '"'  # 'script' allows text font colors to be displayed in terminal screens.
    fd = open(script_logfile, 'w')
    fd.write("Command: " + cmd_test_plus_script + "\n")
    rc, output, error = run_command(cmd_test_plus_script, realtime_output=True)
    if rc != 0:
       msg = "ERROR: run_command error"
       fd.write(msg+'\n')
       fd.close()
       error_status(msg)
    if error != '':
       msg = "ERROR: run_command returned error message: " + error
       fd.write(msg+'\n')
       fd.close()
       error_status(msg)
    if re.search("error", output, re.I):
       msg = "ERROR: run_command returned error in output:\n--Begin output\n" + output + "\n--End output\n"
       fd.write(msg+'\n')
       fd.close()
       error_status(msg)
 
    # print(output)
    fd.write(output+'\n')
    msg = 'Successful test_package run_command!'
    print(msg)
    fd.write(msg+'\n')
    # $cmd_test 2>&1 | tee.py -a $script_logfile
    # $cmd_test >> $script_logfile
    # var=$(script -q /dev/null "$cmd_test" | tr -d '\r' | cat)
    # echo $var
    # echo $var | tee -a $script_logfile

    # Archive results

    test_results_main_dir = scriptDir + '/test_results'
    if not os.path.isdir(test_results_main_dir):
        os.makedirs(test_results_main_dir)

    from datetime import datetime
    curr_date = datetime.now().strftime('%Y%m%d%H%M%S')

    test_results_test_package_subdir = test_results_main_dir + '/' + curr_date
    if not os.path.isdir(test_results_test_package_subdir):
        os.makedirs(test_results_test_package_subdir)

    cmd = "mv " + script_logfile + ' ' + test_results_test_package_subdir + '/' + logfile
    rc, output, error = run_command(cmd)
    if rc != 0:
        error_status("ERROR: Error on command = " + cmd) 

    cmd = "mv report.html " + test_results_test_package_subdir
    rc, output, error = run_command(cmd)
    if rc != 0:
        error_status("ERROR: Error on command = " + cmd) 

    # Only archive .expected files related to created .actual files.
    cmd = "ls " + test_package_dir_path + '/*.actual'
    rc, output, error = run_command(cmd)
    if rc != 0:
        error_status("ERROR: Error on command = " + cmd) 

    # print(257, output)
 
    for actual_file in [x.strip() for x in output.strip().split('\n')]:
        expected_file = re.sub('.actual', '.expected', actual_file)
        cmd = "cp -pr " + expected_file + ' ' + test_results_test_package_subdir
        # print(259, output)
        rc, output, error = run_command(cmd)
        if rc != 0:
            error_status("ERROR: Error on cp command = " + cmd)

    cmd = "mv " + test_package_dir_path + '/*.actual ' + test_results_test_package_subdir
    rc, output, error = run_command(cmd)
    if rc != 0:
        error_status("ERROR: Error on command = " + cmd) 
 
    msg = 'Results files in  ' + test_results_test_package_subdir
    print(msg)
    fd.write(msg+'\n')
    fd.close()

    run_command('echo "' + cmd_test + '" > ' + test_results_test_package_subdir + '/STATUS_SUCCESS.txt')

    cmd_runstring = 'echo "' + cmd_test + '" > ' + test_results_test_package_subdir + '/RUNSTRING.txt'
    rc, output, error = run_command(cmd_runstring)
    if rc != 0:
        print("ERROR: Error on runstring command = " + cmd_runstring) 
        sys.exit(1)

    sys.exit(1)
 
 




