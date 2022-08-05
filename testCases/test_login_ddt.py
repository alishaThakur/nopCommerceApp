from datetime import time

import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from selenium.webdriver.chrome.service import Service
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from utilities import ELUtils

class Test_002_DDT_Login:
    baseURL = ReadConfig.getApplicationURL()
    path = ".//TestData//LoginData.xlsx"
    logger = LogGen.loggen()


    @pytest.marl.regression
    def test_login(self):
            self.logger.info("************ test_002_DDT_Login *********")
            self.logger.info("************ Verifying Login Test *********")
            print("Done till here")
            serv_obj = Service("C:\Drivers\chromedriver_win32 (1)\chromedriver.exe")
            self.driver = webdriver.Chrome(service=serv_obj)
            self.driver.get(self.baseURL)

            self.lp = LoginPage()
            self.rows = ELUtils.getRowCount(self.path, "Sheet1")
            print("Number of Rows:" ,  self.rows)
            lst_status = []
            for r in range(2, self.rows+1):
                self.username= ELUtils.readData(self.path , "Sheet1", r,1)
                self.password = ELUtils.readData(self.path, "Sheet1", r, 2)
                self.exp = ELUtils.readData(self.path, "Sheet1", r, 3)
                self.lp.setUserName(self.username)
                self.lp.setPassword(self.password)
                self.lp.clickLogin()
                time.sleep(5)

                act_title = self.driver.title
                exp_title = "Dashboard / nopCommerce administration"



                if act_title == exp_title:
                        if self.exp == 'Pass':
                            self.logger.info("**** passed ****")
                            self.lp.clickLogout();
                            lst_status.append("Pass")
                        elif self.exp == 'Fail':
                            self.logger.info("**** failed ****")
                            self.lp.clickLogout();
                            lst_status.append("Fail")

                elif act_title != exp_title:
                        if self.exp == 'Pass':
                            self.logger.info("**** failed ****")
                            lst_status.append("Fail")
                        elif self.exp == 'Fail':
                            self.logger.info("**** passed ****")
                            lst_status.append("Pass")
                print(lst_status)
                if "Fail" not in lst_status:
                        self.logger.info("******* DDT Login test passed **********")
                        self.driver.close()
                        assert True
                else:
                        self.logger.error("******* DDT Login test failed **********")
                        self.driver.close()
                        assert False

                self.logger.info("******* End of Login DDT Test **********")
                self.logger.info("**************** Completed  TC_LoginDDT_002 ************* ");

