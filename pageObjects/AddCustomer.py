import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By

class AddCustomer:
    # Add customer Page
    lnkCustomers_menu_xpath = "/html/body/div[3]/aside/div/div[4]/div/div/nav/ul/li[4]/a"
    lnkCustomers_menuitem_xpath = "/html/body/div[3]/aside/div/div[4]/div/div/nav/ul/li[4]/ul/li[1]/a"
    btnAddnew_xpath = "/html/body/div[3]/div[1]/form[1]/div/div/a"
    txtEmail_xpath = "//input[@id='Email']"
    txtPassword_xpath = "//input[@id='Password']"
    txtcustomerRoles_xpath = "//div[@class='k-multiselect-wrap k-floatwrap']"
    lstitemAdministrators_xpath = "//li[contains(text(),'Administrators')]"
    lstitemRegistered_xpath = "//li[contains(text(),'Registered')]"
    lstitemGuests_xpath = "//li[contains(text(),'Guests')]"
    lstitemVendors_xpath = "//li[contains(text(),'Vendors')]"
    drpmgrOfVendor_xpath = "//*[@id='VendorId']"
    rdMaleGender_id = "Gender_Male"
    rdFeMaleGender_id = "Gender_Female"
    txtFirstName_id = "FirstName"
    txtLastName_id = "LastName"
    txtDob_id = "DateOfBirth"
    txtCompanyName_id = "Company"
    txtAdminContent_id = "AdminComment"
    btnSave_xpath = "//button[@name='save']"


    def __init__(self, driver):
        self.driver = driver

    def clickOnCustomersMenu(self):
        self.driver.find_element(By.XPATH , self.lnkCustomers_menu_xpath).click()

    def clickOnCustomersMenuItem(self):
        self.driver.find_element(By.XPATH , self.lnkCustomers_menuitem_xpath).click()

    def clickOnAddnew(self):
        self.driver.find_element(By.XPATH ,self.btnAddnew_xpath).click()

    def setEmail(self,email):
        self.driver.find_element(By.XPATH ,self.txtEmail_xpath).send_keys(email)

    def setPassword(self,password):
        self.driver.find_element(By.XPATH ,self.txtPassword_xpath).send_keys(password)

    def setCustomerRoles(self,role):
        self.driver.find_element(By.XPATH ,self.txtcustomerRoles_xpath).click()
        time.sleep(3)
        if role == 'Registered':
            self.listitem = self.driver.find_element(By.XPATH ,self.lstitemRegistered_xpath)
        elif role=='Administrators':
            self.listitem=self.driver.find_element(By.XPATH ,self.lstitemAdministrators_xpath)
        elif role=='Guests':
            # Here user can be Registered( or) Guest, only one
            time.sleep(3)
            self.driver.find_element(By.XPATH , "//*[@id='SelectedCustomerRoleIds_taglist']/li/span[2]").click()
            self.listitem = self.driver.find_element(By.XPATH ,self.lstitemGuests_xpath)
        elif role=='Registered':
            self.listitem = self.driver.find_element(By.XPATH ,self.lstitemRegistered_xpath)
        elif role=='Vendors':
            self.listitem = self.driver.find_element(By.XPATH ,self.lstitemVendors_xpath)
        else:
            self.listitem = self.driver.find_element(By.XPATH ,self.lstitemGuests_xpath)
        time.sleep(3)
        #self.listitem.click()
        self.driver.execute_script("arguments[0].click();", self.listitem)

    def setManagerOfVendor(self,value):
        drp=Select(self.driver.find_element(By.XPATH ,self.drpmgrOfVendor_xpath))
        drp.select_by_visible_text(value)

    def setGender(self,gender):
        if gender=='Male':
            self.driver.find_element(By.ID ,self.rdMaleGender_id).click()
        elif gender=='Female':
            self.driver.find_element(By.ID ,self.rdFeMaleGender_id).click()
        else:
            self.driver.find_element(By.ID ,self.rdMaleGender_id).click()

    def setFirstName(self, fname):
        self.driver.find_element(By.ID ,self.txtFirstName_id).send_keys(fname)

    def setLastName(self, lname):
        self.driver.find_element(By.ID ,self.txtLastName_id).send_keys(lname)

    def setDob(self, dob):
        self.driver.find_element(By.ID ,self.txtDob_id).send_keys(dob)

    def setCompanyName(self, comname):
        self.driver.find_element(By.ID ,self.txtCompanyName_id).send_keys(comname)

    def setAdminContent(self, content):
        self.driver.find_element(By.ID ,self.txtAdminContent_id).send_keys(content)

    def clickOnSave(self):
        self.driver.find_element(By.XPATH ,self.btnSave_xpath).click()