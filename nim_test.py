from selenium import webdriver
from time import sleep
import xlrd
from dotenv import load_dotenv
import os
from random import uniform

load_dotenv()

DataNim = []
DataSucces = []

def TestingAkun():
    BaseUrl = os.getenv("BaseURL")
    op = webdriver.ChromeOptions()
    op.add_argument("headless")
    
    #login test
    for i in range(len(DataNim)):
        browser = webdriver.Chrome(os.getenv('Chrome_driver'))
        browser.get(BaseUrl)
        browser.implicitly_wait(7)
        username_element = browser.find_element_by_name("username")
        username_element.send_keys(DataNim[i])
        password_element = browser.find_element_by_name("password")
        password_element.send_keys(DataNim[i])
        sleep(3)
        browser.find_element_by_name("login").click()
        print("Lagi Coba login akun : {}".format(DataNim[i]))
        browser.implicitly_wait(uniform(1,2.5))
        sleep(3)
        if browser.current_url == BaseUrl:
            print("{} Gagal Login".format(DataNim[i]))
            browser.implicitly_wait(uniform(1,2))
            sleep(2)
            browser.close()
        else:
            print("{} Berhasil Login".format(DataNim[i]))
            DataSucces.append(DataNim[i])
            browser.implicitly_wait(uniform(1,2))
            sleep(2)
            browser.close()
    sleep(uniform(0.5,2))

def GetData():
    wb = xlrd.open_workbook(FileName)
    sheet = wb.sheet_by_index(0)
    for i in range(1,sheet.nrows):
        DataNim.append(sheet.cell_value(i,0))
    TestingAkun()

if __name__ == "__main__":
    print("Program ini hanya dapat membaca Excel File")
    FileName = input("Nama File Excel dengan extensinya[.xlsx/xls] : ")
    GetData()
    # print(DataNim)