from appium import webdriver # 导入 appium 的 webdriver 库，用于自动化测试移动应用程序
from appium.webdriver.extensions.android.nativekey import AndroidKey # 导入 AndroidKey 模块，用于模拟 Android 设备的按键操作
from selenium.webdriver.common.by import By # 导入 By 模块，用于定位元素

# 创建一个字典用于存储配置参数
caps = dict()
# 配置连接参数
# 设置系统为 Android
caps['platformName'] = 'Android'
# 设置平台版本为 7.1.1（模拟器-关于平板-版本号）
caps['platformVersion'] = '7.1.1'
# 设置设备名称为 Android（可以换）
caps['deviceName'] = 'Android'
# 设置应用程序的包名--设置
caps['appPackage'] = 'com.android.settings'
# 设置应用程序的界面名
caps['appActivity'] = '.Settings'
# 有需要输入中文，需要设置为 True
caps['unicodeKeyboard'] = True
# 重置键盘设置，恢复原来的输入法
caps['resetKeyboard'] = True
# 禁用应用程序的重置，不需要重置 APP 状态，就设置为 True
caps['noReset'] = True
# 设置新命令的超时时间为 6000 毫秒
caps['newCommandTimeout'] = 6000
# 设置自动化引擎为 UiAutomator2
caps['automationName'] = 'UiAutomator2'

# 创建 Appium WebDriver 实例，连接到 Appium 服务器，加载驱动
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', caps)
# 定位元素--WLAN
WLAN = driver.find_element(By.XPATH, '//*[@text="WLAN"]')
# 定位元素--声音
sy = driver.find_element(By.XPATH, '//*[@text="声音"]')
# 滑动
# 从一个元素滑动到另外一个元素
# 手的操作是往上，内容是往下加载
driver.drag_and_drop(sy, WLAN)