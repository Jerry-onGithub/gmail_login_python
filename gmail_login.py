# -*- coding: utf-8 -*-
"""
Created on Sat Feb 26 14:37:07 2022

@author: Jerry
"""

import undetected_chromedriver.v2 as uc
from time import sleep


if __name__ == '__main__':
    password ='ethiopia'
    username = 'aboye0123'
    driver = uc.Chrome(version_main=103)

    driver.delete_all_cookies()
    driver.get('https://accounts.google.com/signin/v2/identifier?service=mail&passive=1209600&osid=1&continue=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&followup=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&emr=1&flowName=GlifWebSignIn&flowEntry=ServiceLogin')
    sleep(3)

    driver.find_element_by_xpath('//input[@type="email"]').send_keys(username)
    driver.find_element_by_xpath('//*[@id="identifierNext"]').click()

    sleep(5)
    driver.find_element_by_xpath('//input[@type="password"]').send_keys(password)
    driver.find_element_by_xpath('//*[@id="passwordNext"]').click()
    sleep(2)
    driver.get('https://gmail.com')
    sleep(10)