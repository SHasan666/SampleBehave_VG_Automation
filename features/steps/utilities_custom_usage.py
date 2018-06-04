#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
from sauceclient import SauceClient
import ssl
class UtilitiesCustom():

    def __init__(self):
        pass

    def method_utilities_compare_all_success_failure(farg, *args): # variable number of arguments
        #chrome_web_driver = args[0]
        session = ""
        #print("**********************"+session)
        ssl._create_default_https_context = ssl._create_unverified_context
        for arg in args:
            if isinstance(arg, str):
                session = arg
                print("********************** FOUND" + session)

        sauce_client = SauceClient("mdhasan1234", "ee94f3c5-92a6-4cd3-b1b0-842520ff0fac")
        for arg in args:
            if isinstance(arg, list):
                for one_element in arg:
                    if 'failure' in str(one_element):
                        sauce_client.jobs.update_job(session, passed=False)
                        return "FAIL"

        sauce_client.jobs.update_job(session, passed=True)
        print ('All steps were successfully executed')
        return "PASS"
