import requests
import urllib.request
from time import sleep
from bs4 import BeautifulSoup
import ssl
import xlwt
from xlwt import Workbook


BaseUrl = input("Masukan alamat URL : ")
BanyakData = int(input("Masukan Banyak Data : "))
NamaFile = input(
    "Masukan nama file untuk menyimpan data, [contoh: nim_blabla] : "
)
JenisFile = input('[1] Excel File, [2] Text File, :contoh: 1 atau 2] : ')
DataPerPages = 20
TotalPages = int(BanyakData / DataPerPages)
PageStart = 0
dataNim = []

def SaveDataToTxt(data, FileName):
    with open("{}.txt".format(FileName),'w') as fileHandle:
        for listData in data:
            fileHandle.write(listData+"\n")
        fileHandle.close()

def SaveDataToExcel(data, FileName):
    wb = Workbook()
    sheet = wb.add_sheet('NIM')
    sheet.write(0,0, 'NIM')
    for i in range(1,len(data)):
        sheet.write(i,0,data[i])
    wb.save(FileName+".xls")

for page in range(TotalPages + 1):
    try:
        BaseScraping = BaseUrl + str(PageStart)
        GetResponseURL = requests.get(BaseScraping, verify=False)
        soup = BeautifulSoup(GetResponseURL.text, "html.parser")
        TdGet = soup.find_all("td")
        data = 1
        for i in range(DataPerPages):
            print(TdGet[data].get_text())
            dataNim.append(TdGet[data].get_text())
            # sleep(0.5)
            data += 3
    except IndexError:
        print("Data sudah sampai akhir")
    finally:
        if JenisFile == '1':
            SaveDataToExcel(dataNim,NamaFile)
        else:
            SaveDataToTxt(dataNim,NamaFile)

    PageStart += 20
