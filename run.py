from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
import time
from functions import return_driver, id, name, css, link_t, link_t2, xpath, get_user_pw, get_runlist


driver= return_driver()
driver.get("https://sam.lablynx.com/elab")
time.sleep(3)
driver.switch_to.frame('Header')
id('tdLogin').click()
time.sleep(1)
driver.switch_to.default_content()
driver.switch_to.frame('body')
driver.switch_to.frame('fraTreeBody')
username, password= get_user_pw()
id('loginid').clear()
id('password').clear()
id('loginid').send_keys(username)
id('password').send_keys(password)
id('loginLnkImg').click()
time.sleep(1)
driver.switch_to.default_content()
driver.switch_to.frame('body')
driver.switch_to.frame('fraTreeBody')
Select(name('cboLabNo')).select_by_value('1')
name('cboLabNo').click()
css('#frmMain > table > tbody > tr > td > table:nth-child(1) > tbody > tr > td:nth-child(2) > a').click()
time.sleep(5)


requst='4128014'
driver.switch_to.default_content()
driver.switch_to.frame('body')
driver.switch_to.frame('fraTreeExplore')
id('hi3').click()
time.sleep(1)
id('hi11').click()
time.sleep(1)
driver.switch_to.default_content()
driver.switch_to.frame('body')
driver.switch_to.frame('fraTreeBody')
driver.switch_to.frame('fraMain')   
link_t(requst).click()
time.sleep(5)
driver.switch_to.default_content()
driver.switch_to.frame('body')
driver.switch_to.frame('fraTreeBody')
driver.switch_to.frame('fraMFG_vuPROJECTSAMPLES')
link_t('{}-001'.format(requst)).click()
time.sleep(10)

runlist = get_runlist()
for i in runlist:
    try:
        feat, times = i
        feat = 'Feature {} v.'.format(feat)
        times = str(int(times)-1)

        driver.switch_to.default_content()
        driver.switch_to.frame('body')
        driver.switch_to.frame('fraTreeBody')
        id('btnFiltercc_LIM_VUSAMPLETESTRUNASN_NOSAMPLETYPE').click()
        driver.switch_to.frame('fraDialog')
        id('TestAndVers').clear()
        id('TestAndVers').send_keys(feat)
        css('#divbuttons > table > tbody > tr > td:nth-child(2) > button.OkButton').click()
        driver.switch_to.default_content()
        driver.switch_to.frame('body')
        driver.switch_to.frame('fraTreeBody')
        driver.switch_to.frame('fracc_LIM_VUSAMPLETESTRUNASN_NOSAMPLETYPE')
        link_t2(feat).click()
        time.sleep(5)
        if times != '1':
            driver.switch_to.default_content()
            driver.switch_to.frame('body')
            driver.switch_to.frame('fraTreeBody')
            id('txtMultTestRun').clear()
            id('txtMultTestRun').send_keys(times)
        driver.switch_to.default_content()
        driver.switch_to.frame('body')
        driver.switch_to.frame('fraTreeBody')
        id('btnNewTestRun').click()
        time.sleep(1)
        id('btnDone').send_keys(Keys.ENTER)
    except Exception as e:
        print('when{}  error: {}'.format(feat[:-2],e ))
    else:
        print('{} run {} times successfully'.format(feat[:-2], times))
    finally:
        time.sleep(20)
driver.quit()