# -*- coding: utf-8 -*-
'''
@author: CrazyCatOxO
'''

from lxml import html
from PyQt5.QtWidgets import QApplication
import time
import requests
import random


class tatungSpider(requests.Session):
    def login(self, account, password):
        loginUrl = 'https://stucis.ttu.edu.tw/login.php'
        seltopUrl = 'https://stucis.ttu.edu.tw/menu/seltop.php'      #most important url
        headers = {'user_agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'}
        
        if account == '' or password == '':
            raise Exception('account or password is empty')
            
        data = {'ID': account, 'PWD': password, 'Submit':'%B5n%A4J%A8t%B2%CE'}
        self.headers.update(headers)
        self.post(loginUrl, data=data)
        response = self.get(seltopUrl)
        
        if 'Not login or session expire!' in response.text:
            raise Exception('account or password is incorrect')
    
    
    def checkExpire(self, response):
        if 'Not login or session expire!' in response.text:
            raise Exception('session expired')
    

    def grabSelectedCodeWithCheckExpired(self, account, password):
        selectedCourseUrl = 'https://stucis.ttu.edu.tw/selcourse/ListSelected.php'
        response = self.get(selectedCourseUrl)
        if 'Not login or session expire!' in response.text:
            self.login(account, password)
        tree = html.fromstring(response.content)
        selectedCodeSet = set(tree.xpath('/html/body/table/tr/td[2]/font/b/text()'))
        return selectedCodeSet
    
        
    def submitCourseCodeWithCheckExpire(self, codeSet, account, password):
        submitUrl = 'https://stucis.ttu.edu.tw/selcourse/DoAddDelSbj.php?AddSbjNo='
        for code in codeSet:
            response = self.get(submitUrl+code)
            if 'Not login or session expire!' in response.text:
                self.login(account, password)
                time.sleep(random.random())
                self.get(submitUrl+code)
            time.sleep(random.random())
            
        selectedCodeSet = self.grabSelectedCodeWithCheckExpired(account, password)
        return codeSet.intersection(selectedCodeSet)


    def updateAllData(self):
        depClassUrl = 'https://stucis.ttu.edu.tw/selcourse/ListClassCourse.php'
        response = self.get(depClassUrl)
        tree = html.fromstring(response.content)
        depNameList = tree.xpath('//select[@name="SelDepNo"]/option/text()')
        depCodeList = tree.xpath('//select[@name="SelDepNo"]/option/@value')
        length = len(depNameList)
        
        with open('./departmentCode/departmentCodeAndName.txt', 'w', encoding='utf-8') as f:
            for i in range(length):
                f.write(depCodeList[i] + ' ' + depNameList[i] + '\n')
        
        for i in range(length):
            data = {'SelDepNo': depCodeList[i], 'SelClassNo': 'UL1.'}
            response = self.post(depClassUrl, data=data)
            tree = html.fromstring(response.content)
            classNameList = tree.xpath('//select[@name="SelClassNo"]/option/text()')
            classCodeList = tree.xpath('//select[@name="SelClassNo"]/option/@value')
            length = len(classCodeList)
            
            with open('./departmentCode/'+depCodeList[i]+'.txt', 'w', encoding='utf-8') as f:
                for i in range(length):
                    f.write(classCodeList[i] + ' ' + classNameList[i] + '\n')
                    
            
        #the simplest way
    def simpleStart(account, password, wantedCodeSet):
        spider = tatungSpider()
        spider.login(account, password)
        spider.submitCourseCode(wantedCodeSet)
        selectedCodeSet = spider.grabSelectedCode()
        return wantedCodeSet.intersection(selectedCodeSet)
        

        
