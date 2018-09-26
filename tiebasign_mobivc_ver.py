import selenium.webdriver,time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = selenium.webdriver.Chrome()

url = 'https://tieba.baidu.com/'
driver.get(url)

# log in
try:
    driver.find_element_by_xpath('/html/body/div[1]/ul/li[4]/div/a').click()
    WebDriverWait(driver,10).until(EC.presence_of_element_located((By.ID,"TANGRAM__PSP_10__footerULoginBtn")))
    driver.find_element_by_class_name('tang-pass-footerBarULogin').click()

    username = input('请输入用户名：')
    password = input("请输入密码：")

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "TANGRAM__PSP_10__userName")))
    driver.find_element_by_xpath('//*[@id="TANGRAM__PSP_10__userName"]').send_keys(username)
    driver.find_element_by_xpath('//*[@id="TANGRAM__PSP_10__password"]').send_keys(password)
    driver.find_element_by_xpath('//*[@id="TANGRAM__PSP_10__submit"]').click()

    time.sleep(2)
    # 如果有手机验证
    if  EC.presence_of_all_elements_located((By.ID, "TANGRAM__25__content")):
        WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.ID, "TANGRAM__25__button_send_mobile")))
        driver.find_element_by_id('TANGRAM__25__button_send_mobile').click()
        code = input("请输入手机验证码")
        driver.find_element_by_xpath('//*[@id="TANGRAM__25__input_vcode"]').send_keys(code)
        driver.find_element_by_xpath('//*[@id="TANGRAM__25__button_submit"]').click()

    WebDriverWait(driver,10).until(EC.presence_of_all_elements_located((By.ID, "likeforumwraper")))
    url_pool = driver.find_elements_by_class_name('unsign')
    for eve_url in url_pool:
        eve_tieba_url = 'https://tieba.baidu.com/'+eve_url.get_attribute('href')
        print(eve_tieba_url)
        driver.get(eve_tieba_url)
        WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".j_signbtn sign_btn_bright j_cansign")))
        driver.find_element_by_xpath('/html/body/div[2]/div/div[1]/div[4]/div/div[3]/div[2]/div[1]/div/div/div[2]/a').click()
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".j_signbtn signstar_signed")))

finally:
    driver.quit()