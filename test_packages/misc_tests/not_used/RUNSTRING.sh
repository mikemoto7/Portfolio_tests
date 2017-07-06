#!/bin/bash


if [ -n "$1" ]; then
   tc_list_file=$1
else
   tc_list_file=testcases_default.cfg
fi

find . -name __pycache__ | xargs rm -fr

while read line; do
   if [ -z "$line" ]; then
      continue
   fi
   commented_out=$(echo $line | cut -c1)
   if [ "$commented_out" == '#' ]; then
      continue
   fi
   cmd=$(echo $line | cut -f1 -d%)
   description=$(echo $line | cut -f2 -d%)
   # echo "Description: $description"
   echo "Command: $cmd"
   $cmd
done < $tc_list_file




