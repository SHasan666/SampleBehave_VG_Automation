#!/usr/bin/python
# -*- coding: utf-8 -*-


from selenium import webdriver
from features.steps.utilities_custom_usage import *
from features.steps.PageObject_Landing import *
import configfiles.config as config


chrome_driver_path_used = config.chrome_driver_path
delay_min = 3 # sec
delay_medium = 5 # sec
delay_max = 9 # sec
desired_cap = {
                'platform': "Windows 10",
                'browserName': "chrome",
                'version': "66",
            }

class HandleClassImpl:
    def __init__(self):
        pass

    def perform_initial_setup(self, global_list_variables):
        print ('Performing initial set up, invoking browser')
        del global_list_variables[:]
        global_list_variables.append(webdriver.Remote(
                command_executor='http://mdhasan1234:ee94f3c5-92a6-4cd3-b1b0-842520ff0fac@ondemand.saucelabs.com:80/wd/hub',
                desired_capabilities=desired_cap))
        #global_list_variables.append(webdriver.Chrome(executable_path=chrome_driver_path_used))
        global_list_variables[0].maximize_window()
        global_list_variables[0].implicitly_wait(10)
        global_list_variables.append('success')
        return True


    def landingPageNavigate(self, global_list_variables, url_home_page):
        print ('Performing landingPageNavigate')
        chrome_web_driver = global_list_variables[0]
        landing_page = LandingPage(chrome_web_driver)
        landing_page.method_home_page_launch_home_url(chrome_web_driver, url_home_page)
        global_list_variables.append('success')
        return

    def searchForFund(self, global_list_variables, fund_Number):
        print ('Performing searchForFund')
        chrome_web_driver = global_list_variables[0]
        landing_page = LandingPage(chrome_web_driver)
        landing_page.searchFund(chrome_web_driver,fund_Number)
        global_list_variables.append('success')
        return

    def WaitForOverviewPage(self, global_list_variables , title):
        print ('Performing WaitForOverviewPage')
        chrome_web_driver = global_list_variables[0]
        landing_page = LandingPage(chrome_web_driver)
        landing_page.waitForOverviewPage(chrome_web_driver,title)

        global_list_variables.append('success')
        return

    def verifyFundName(self, global_list_variables , fundName):
        print ('Performing verifyFundName')
        chrome_web_driver = global_list_variables[0]
        landing_page = LandingPage(chrome_web_driver)
        check = landing_page.verifyFundName(chrome_web_driver,fundName)
        if "failure" in check:
            global_list_variables.append('failure')
        global_list_variables.append('success')
        return

    def verifyExpenseRatio(self, global_list_variables , expenseRatio):
        print ('Performing verifyExpenseRatio')
        chrome_web_driver = global_list_variables[0]
        landing_page = LandingPage(chrome_web_driver)
        check = landing_page.verifyExpenseRatio(chrome_web_driver,expenseRatio)
        if "failure" in check:
            global_list_variables.append('failure')
        global_list_variables.append('success')
        return


    def final_verification(self, global_list_variables,):
        print ('Performing final verification for each step pass or fail')
        chrome_web_driver = global_list_variables[0]
        session = chrome_web_driver.session_id


        compare_success = UtilitiesCustom()
        check = compare_success.method_utilities_compare_all_success_failure(global_list_variables,session)
        if "FAIL" in check:
            chrome_web_driver.close()
            chrome_web_driver.quit()
            raise Exception(' ******* Failure is observed in a particular step')

        chrome_web_driver.close()
        chrome_web_driver.quit()
        return


obj_handle_impl = HandleClassImpl()
