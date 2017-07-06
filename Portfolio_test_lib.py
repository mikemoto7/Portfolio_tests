
from test_flags import _product_called_from_test
_product_called_from_test = True


import sys
sys.path.append("../lib_for_test")

from general_test_lib import do_test_runstring
import general_test_lib

general_test_lib.product_dir_path = "../Portfolio"







