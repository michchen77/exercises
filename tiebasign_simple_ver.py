import selenium.webdriver
import time

driver = selenium.webdriver.Chrome()

url = 'https://tieba.baidu.com/'
driver.get(url)

# log in
username = input('请输入用户名')
password = input('请输入密码')

driver.find_element_by_xpath('/html/body/div[1]/ul/li[4]/div/a').click()
time.sleep(2)
driver.find_element_by_class_name('tang-pass-footerBarULogin').click()
time.sleep(1)
driver.find_element_by_xpath('//*[@id="TANGRAM__PSP_10__userName"]').send_keys(username)
driver.find_element_by_xpath('//*[@id="TANGRAM__PSP_10__password"]').send_keys(password)
driver.find_element_by_xpath('//*[@id="TANGRAM__PSP_10__submit"]').click()

url_pool = driver.find_elements_by_class_name('u-f-item unsign')
for eve_url in url_pool:
    eve_tieba_url = 'https://tieba.baidu.com/'+eve_url
    driver.get(eve_tieba_url)
    time.sleep(2)
    driver.find_element_by_xpath('/html/body/div[2]/div/div[1]/div[4]/div/div[3]/div[2]/div[1]/div/div/div[2]/a').click()
    time.sleep(3)

driver.quit()
