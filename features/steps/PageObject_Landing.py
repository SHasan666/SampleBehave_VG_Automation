#!/usr/bin/python
# -*- coding: utf-8 -*-

import time
from page_objects import PageObject, PageElement
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions


delay_min = 3 # sec
delay_medium = 5 # sec
delay_max = 9 # sec


class LandingPage(PageObject):
    global_search_field = PageElement(xpath="//input[@id='vgn-subUtilityBarSearchInput']")
    fund_name = PageElement(xpath="//h1[@class='vuiHeadSize2 vuiMarginBottom7px ng-binding']")
    expenseRatio=PageElement(xpath="// div[ @ id = 'expenseRatioData']")

    def method_home_page_launch_home_url(self, current_web_driver, url_home_page):
        self.get(url_home_page)
        # time.sleep(delay_max)
        WebDriverWait(current_web_driver,delay_max).until(expected_conditions.title_contains('Vanguard Financial Advisor Services'))
        return

    def searchFund(self , current_web_driver , fundNumber):
        self.global_search_field = fundNumber
        self.global_search_field= Keys.ENTER
        return

    def waitForOverviewPage(self, current_web_driver , title):

        WebDriverWait(current_web_driver, delay_max).until(
            expected_conditions.title_contains(title))
        return

    def verifyFundName(self, current_web_driver, expected):
        time.sleep(10)
        actual_text = self.fund_name.text
        if expected not in actual_text:
            return "failure"
            #raise Exception(' ******* Following expected "' + expected + '" text is not found in ' + actual_text)

        return "Pass"

    def verifyExpenseRatio(self, current_web_driver, expected):
        time.sleep(10)
        actual_text = self.expenseRatio.text
        if expected not in actual_text:
            return "failure"
            #raise Exception(' ******* Following expected "' + expected + '" text is not found in ' + actual_text)

        return "Pass"
