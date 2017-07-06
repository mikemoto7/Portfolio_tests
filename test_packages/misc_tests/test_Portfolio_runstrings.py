import pytest

from Portfolio_test_lib import do_test_runstring


# @pytest.mark.usefixtures("oneTimeSetUp", "setUp")
@pytest.mark.usefixtures()
class TestPortfolio():

    # @pytest.fixture(autouse=True)
    # def classSetup(self, setup):
    #     pass



    # Testcases interactive:

    '''
    def test_runstring_cl(self):
        do_test_runstring("Portfolio.py --cl")

    def test_runstring_cl_l(self):
        do_test_runstring("Portfolio.py --cl l")

    def test_runstring_cl_7(self):
        do_test_runstring("Portfolio.py --cl 7")

    def test_runstring_cl_debug_1(self):
        do_test_runstring("Portfolio.py --cl 7 --debug 1")
    '''


    # Testcases from docstring:


    def test_runstring_price_web_update(self):
        do_test_runstring("Portfolio.py --price_web_update --pfile demo_data_file.xml")

    def test_runstring_ac_web_update(self):
        do_test_runstring("Portfolio.py --ac_web_update --pfile demo_data_file.xml")

    def test_runstring_stats(self):
        do_test_runstring("Portfolio.py --stats --pfile demo_data_file.xml")

    def test_runstring_xml(self):
        do_test_runstring("Portfolio.py --xml --pfile demo_data_file.xml")

    def test_runstring_price_web_update_xml(self):
        do_test_runstring("Portfolio.py --price_web_update --xml --pfile demo_data_file.xml")

    def test_runstring_pt_show(self):
        do_test_runstring("Portfolio.py --pt show --pfile demo_data_file.xml")

    def test_runstring_pt_show_percent(self):
        do_test_runstring("Portfolio.py --pt show_percent --pfile demo_data_file.xml")

    def test_runstring_pt_show_ac_misc_totals(self):
        do_test_runstring("Portfolio.py --pt show_ac_misc_totals --pfile demo_data_file.xml")

    def test_runstring_pt_lp(self):
        do_test_runstring("Portfolio.py --pt lp --pfile demo_data_file.xml")

    def test_runstring_pt_add(self):
        do_test_runstring("Portfolio.py --pt add:'Small Value',Non_Retirement,50000:'Small Value',Retirement,20000:Healthcare,Retirement,50000 --pfile demo_data_file.xml")

    def test_runstring_inv_show(self):
        do_test_runstring("Portfolio.py --inv show --pfile demo_data_file.xml")

    def test_runstring_inv_diff_1file(self):
        do_test_runstring("Portfolio.py --inv diff --pfile demo_data_file.xml")

    def test_runstring_inv_diff_2file(self):
        do_test_runstring("Portfolio.py --inv diff --pfile demo_data_file.xml1,demo_data_file.xml2")

    def test_runstring_inv_lots(self):
        do_test_runstring("Portfolio.py --inv lots --pfile demo_data_file.xml")

    def test_runstring_all_not_silent(self):
        do_test_runstring("Portfolio.py --all --pfile demo_data_file.xml")

    def test_runstring_all_silent(self):
        do_test_runstring("Portfolio.py --all --silent --pfile demo_data_file.xml")

    def test_runstring_noindent(self):
        do_test_runstring("Portfolio.py --noindent  --all  --pfile demo_data_file.xml")

    def test_runstring_h(self):
        do_test_runstring("Portfolio.py --h")

    def test_runstring_xmlfile(self):
        do_test_runstring("Portfolio.py --xmlfile  --pfile demo_data_file.xml")

    def test_runstring_pdt(self):
        do_test_runstring("Portfolio.py --pdt --pfile demo_data_file.xml")

    def test_runstring_debug_1(self):
        do_test_runstring("Portfolio.py --debug 1  --all  --pfile demo_data_file.xml")

    def test_runstring_debug_2(self):
        do_test_runstring("Portfolio.py --debug 2  --all  --pfile demo_data_file.xml")

    def test_runstring_debug_12(self):
        do_test_runstring("Portfolio.py --debug 12  --all  --pfile demo_data_file.xml")

    def test_runstring_price_web_update_pt_show(self):
        do_test_runstring("Portfolio.py --price_web_update --pt show --pfile demo_data_file.xml")

    def test_runstring_price_web_update_inv_show(self):
        do_test_runstring("Portfolio.py --price_web_update --inv show --pfile demo_data_file.xml")

    def test_runstring_price_web_update_ac_web_update_pt_show(self):
        do_test_runstring("Portfolio.py --price_web_update --ac_web_update --pt show%lp%add:Small_Value,Retirement,13000%show_percent%lp_diff --pfile demo_data_file.xml")

    def test_runstring_price_web_update_pt_lp(self):
        do_test_runstring("Portfolio.py --price_web_update --pt lp --pfile demo_data_file.xml")

    def test_runstring_price_web_update_pt_show_percent(self):
        do_test_runstring("Portfolio.py --price_web_update --pt show_percent%lp%add:Large_Blend,Retirement,13000%show_percent%lp --pfile demo_data_file.xml")

    def test_runstring_price_web_update_inv_diff(self):
        do_test_runstring("Portfolio.py --price_web_update --inv diff --pfile demo_data_file.xml")

    def test_runstring_price_web_update_pt_show_percent_bigger_add(self):
        do_test_runstring("Portfolio.py --price_web_update --pt show_percent%lp%add:Small_Growth,Non_Retirement,30000:Energy,Non_Retirement,15000:Large_Value,Non_Retirement,15000:Global,Non_Retirement,15000:REIT,Non_Retirement,15000:Healthcare,Non_Retirement,15000%show_percent%lp_diff --pfile demo_data_file.xml")

    def test_runstring_price_web_update_pt_add(self):
        do_test_runstring("Portfolio.py --price_web_update --pt add:Small_Growth,Non_Retirement,30000:Energy,Non_Retirement,15000:Large_Value,Non_Retirement,15000:Global,Non_Retirement,15000:REIT,Non_Retirement,15000:Healthcare,Non_Retirement,15000%lp_diff --pfile demo_data_file.xml")

    def test_runstring_price_web_update_pt_show_ac_misc_totals(self):
        do_test_runstring("Portfolio.py --price_web_update --pt show_ac_misc_totals --pfile demo_data_file.xml")






