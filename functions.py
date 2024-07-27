from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import json, csv, winreg

#chrome_driver_service= Service('./chomedriver')
opt = Options()
opt.add_argument('--headless')
driver= webdriver.Chrome()

def return_driver():
    return driver

def id(element):
    #WebDriverWait(driver, 10, 1).until(EC.presence_of_element_located((By.ID, element)))
    #return driver.find_element(By.ID,element)
    return WebDriverWait(driver, 10, 1).until(EC.presence_of_element_located((By.ID, element)))

def name(element):
    return WebDriverWait(driver, 10, 1).until(EC.presence_of_element_located((By.NAME, element)))

def link_t(element):
    return WebDriverWait(driver, 10, 1).until(EC.presence_of_element_located((By.LINK_TEXT, element)))

def link_t2(element):
    return WebDriverWait(driver, 10, 1).until(EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, element)))


def xpath(element):
    return WebDriverWait(driver, 10, 1).until(EC.presence_of_element_located((By.XPATH, element)))

def css(element):
    return WebDriverWait(driver, 10, 1).until(EC.presence_of_element_located((By.CSS_SELECTOR, element)))

def get_user_pw():
    with open('elab/user_pw.json','r') as f:
        user_pw=json.load(f)
        user= user_pw['username']
        pw=user_pw['password']
    return user, pw


def desktop_path():
    key = winreg.OpenKey(winreg.HKEY_CURRENT_USER,'Software/Microsoft/Windows/CurrentVersion/Explorer/Shell Folders')
    return winreg.QueryValueEx(key,"Desktop")[0]

def get_runlist(path='D:/Programs/vscode/elab/runlist.csv'):
    
    csvfile = path
    #csvfile = path +'/runlist.csv'

    runlist = []
    c = csv.reader(open(csvfile,'r'))
    for cs in c:
        runlist.append(cs)
    return runlist



