### 文心一格签到程序
需要准备[chrome浏览器](https://www.google.com/chrome/)和对应版本的[chromedriver](https://chromedriver.chromium.org/downloads)<br>
因为本代码只做签到，不含登录等，需要手动登录保持cookie。<br>
将chromedriver放到代码文件路径<br>
```
from selenium import webdriver
from selenium.webdriver.common.by import By
import time



def get_driver():   
    '''获得浏览器驱动对象'''   
    chromedriver = 'chromedriver'   
    chrome_options = webdriver.ChromeOptions()

    # 配置打开指定用户（如果没有多用户可以不配置）
    chrome_options.add_argument(r"--user-data-dir=.\Chrome\User Data") #.换成对应路径
    chrome_options.add_argument("--profile-directory=Default")
    
    # 启动
    driver = webdriver.Chrome(executable_path=chromedriver,options=chrome_options)   
    return driver

driver = get_driver()

# 文心一格签到
driver.get('https://yige.baidu.com/points')
driver.implicitly_wait(30)
try:
    a = driver.find_element(By.XPATH,"//span[text()='立即签到']")
except:
    print("未找到签到按钮，请手动处理")
else:
    a.click()
time.sleep(2)
driver.quit()
```
