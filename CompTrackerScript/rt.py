import time, csv
from selenium import webdriver
from selenium.webdriver.support import ui
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from sys import argv

#run .py, with log.txt file as argument
script, input_file= argv

#assign to text.txt file
filename = 'log'

print("-----------------------------------------------------OPENING SITE")

driver = webdriver.Chrome("C:/Users/Enoch Kong/Desktop/CT SCRIPT/chromedriver.exe")
driver.get("https://secure.studentlogbook.com/CompTracker50/CompTrackerWebsite/Home/Login")

def login():
    print("-----------------------------------------------------LOGGING IN")

    institutioncode = 'mc'
    loginid = 'kongem'
    password = '8578'

    inputElement = driver.find_element_by_id("institutionCode")
    inputElement.send_keys(institutioncode)
    inputElement = driver.find_element_by_id("loginID")
    inputElement.send_keys(loginid)
    inputElement = driver.find_element_by_id("password")
    inputElement.send_keys(password)
    inputElement.send_keys(Keys.ENTER)
    time.sleep(2)

def create_record():
    driver.find_element_by_name('create-button-progress').click()
    print("-----------------------------------------------------CREATING RECORD")
    driver.implicitly_wait(5)
    time.sleep(1)

def select_logbook():
    button1 = driver.find_element_by_xpath("//select[@name='Practicum']/option[text()='CP 3']")
    print("-----------------------------------------------------SELECTING CP3")
    button1.click()
    time.sleep(1)

    button2 = driver.find_element_by_xpath("//select[@name='recordType']/option[text()='LB, SA & CAs']")
    print("-----------------------------------------------------SELECTING LOGBOOK OPTION")
    button2.click()
    time.sleep(1)

    driver.find_element_by_id('submitCreateRecord').click()
    print("-----------------------------------------------------PREPARING TO CREATE RECORDS")
    driver.implicitly_wait(10)
    time.sleep(6)

def preceptor():
    button3 = driver.find_element_by_id('submitPreceptorList_chzn').click()
    print("-----------------------------------------------------FILLING IN PRECEPTOR")
    cel = 'Coreen, Corning (CEL Alternative)'
    celtext = driver.find_element_by_xpath("//*[@id='submitPreceptorList_chzn']/div/div/input").send_keys('Corning, Coreen (CEL Alternate)', Keys.ENTER)

def resetlog(num):
    userinput = input("WOULD YOU LIKE TO RESET LOG.TXT?: ")
    if userinput == "YES" or userinput == "yes" or userinput == "y" or userinput == "Y":
        with open('log.txt', 'r+') as f:
            resetDataArray = (f.readlines())
            f.seek(0)
            f.truncate()
            f.seek(0)
            f.write(resetDataArray[0][2:])
            for n in range(1, num):
                f.write("0" + resetDataArray[n][2:])

        print("-----------------------------------------------------LOG.TXT RESET")
        driver.quit()
    else:
        driver.quit()

login()
create_record()
select_logbook()
preceptor()

print("-----------------------------------------------------READING LOG.TXT")
#count lines in document
num_lines = sum(1 for line in open(filename+'.txt'))
print (num_lines)
current_file = open(input_file)

#create arrays
holdData = []
indData = []

i = 0

allDataArray = (current_file.readlines())

#separate array numbers from log info
allEntries = 0
for i in range(1, num_lines):
    intDigits = allDataArray[i][:2]
    if int(intDigits) > 0:
        for n in range(0, int(intDigits)):
            textinfo = allDataArray[i][6:]
            holdData.append(textinfo)
    else:
        pass

    allEntries = allEntries + int(intDigits)

#define counters
totalSingle = 0
totalPOP = 0
totalIMRT = 0
totalMulti = 0
totalMatch = 0
totalExtend = 0
totalTang = 0

#create counts for total number of technique
for i in range(1, num_lines):
    dataHolder = allDataArray[i]
    indData = dataHolder.split(' ')
    numberEntries = int(indData[0])
    technique = (indData[1])

    if technique == 'SIN':
        totalSingle = totalSingle + numberEntries
    if technique == 'POP':
        totalPOP = totalPOP + numberEntries
    if technique == 'MUL':
        totalMulti = totalMulti + numberEntries
    if technique == 'IMR':
        totalIMRT = totalIMRT + numberEntries
    if technique == 'MAT':
        totalMatch = totalMatch + numberEntries
    if technique == 'EXT':
        totalExtend = totalExtend + numberEntries
    if technique == 'TAN':
        totalTang = totalTang + numberEntries

print("-----------------------------------------------------RECORDING NUMBER OF EACH TECHNIQUE")
#SINGLE
if totalSingle > 0:
    inputSingle = driver.find_element_by_id('numbers_2189')
    inputSingle.send_keys(Keys.CONTROL, "a")
    inputSingle.send_keys(Keys.DELETE)
    inputSingle.send_keys(totalSingle)
    driver.find_element_by_id('2189').click()

#POP
if totalPOP > 0:
    inputPOP = driver.find_element_by_id('numbers_2190')
    inputPOP.send_keys(Keys.CONTROL, "a")
    inputPOP.send_keys(Keys.DELETE)
    inputPOP.send_keys(totalPOP)
    driver.find_element_by_id('2190').click()

#MULTI
if totalMulti > 0:
    inputMulti = driver.find_element_by_id('numbers_2194')
    inputMulti.send_keys(Keys.CONTROL, "a")
    inputMulti.send_keys(Keys.DELETE)
    inputMulti.send_keys(totalMulti)
    driver.find_element_by_id('2194').click()

#IMRT
if totalIMRT> 0:
    inputIMRT = driver.find_element_by_id('numbers_2195')
    inputIMRT.send_keys(Keys.CONTROL, "a")
    inputIMRT.send_keys(Keys.DELETE)
    inputIMRT.send_keys(totalIMRT)
    driver.find_element_by_id('2195').click()

#MATCH
if totalMatch > 0:
    inputMatch = driver.find_element_by_id('numbers_2196')
    inputMatch.send_keys(Keys.CONTROL, "a")
    inputMatch.send_keys(Keys.DELETE)
    inputMatch.send_keys(totalMatch)
    driver.find_element_by_id('2196').click()

#EXTEND
if totalExtend > 0:
    inputExtend = driver.find_element_by_id('numbers_2191')
    inputExtend.send_keys(Keys.CONTROL, "a")
    inputExtend.send_keys(Keys.DELETE)
    inputExtend.send_keys(totalExtend)
    driver.find_element_by_id('2191').click()

#TANG
if totalTang > 0:
    inputTang = driver.find_element_by_id('numbers_2192')
    inputTang.send_keys(Keys.CONTROL, "a")
    inputTang.send_keys(Keys.DELETE)
    inputTang.send_keys(totalTang)
    driver.find_element_by_id('2192').click()

#input date
print("-----------------------------------------------------INPUTTING DATE")
compDate = allDataArray[0]
inputElement = driver.find_element_by_id('applyDateToAll')
inputElement.send_keys(compDate)

#click all dates
button4 = driver.find_element_by_xpath("//*[@id='applyDateToAllButton']/span/img")
button4.click()

#click create entries
print("-----------------------------------------------------CREATING ENTRIES")
button5 = driver.find_element_by_xpath("//*[@id='createCompetencyButton']/span")
button5.click()
time.sleep(2)

print("-----------------------------------------------------PREPARING TO FILL ENTRIES")

#Go to first textbox
button6 = driver.find_element_by_xpath("//*[@id='selectedPracticumID']")
button6.click()

actions = ActionChains(driver)
actions.send_keys(Keys.TAB, Keys.TAB, Keys.TAB, Keys.TAB, Keys.TAB, Keys.TAB, Keys.TAB, Keys.TAB, Keys.TAB, Keys.TAB, Keys.TAB, Keys.TAB, Keys.TAB, Keys.TAB, Keys.TAB, Keys.TAB, Keys.TAB, Keys.TAB, Keys.TAB, Keys.TAB, Keys.TAB)
actions.perform()

print("-----------------------------------------------------FILLING ENTRIES")

#navigate through textboxes, fill in entries
for i in range(0, len(holdData)):
    type = ActionChains(driver)
    type.send_keys(holdData[i])
    type.send_keys(Keys.TAB)
    type.send_keys('a', Keys.ENTER)
    type.send_keys(Keys.TAB)
    type.send_keys('i', Keys.ENTER)
    type.send_keys(Keys.TAB, Keys.TAB, Keys.TAB, Keys.TAB, Keys.TAB, Keys.TAB, Keys.TAB, Keys.TAB)
    type.perform()

print("-----------------------------------------------------COMPLETED " + str(len(holdData)) + " ENTRIES")
current_file.close()
resetlog(num_lines)
