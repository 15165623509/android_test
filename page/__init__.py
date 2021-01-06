from selenium.webdriver.common.by import By

'''display配置信息'''
# 设置-显示按钮
setting_display = By.XPATH, "//*[@text='显示']"
# 设置-显示-搜索按钮
setting_display_search = By.ID, "com.android.settings:id/search"
# 设置-显示-搜索-输入框
setting_display_search_input = By.ID, "android:id/search_src_text"
# 设置-显示-搜索-返回
setting_display_search_return = By.CLASS_NAME, "android.widget.ImageButton"

'''more配置信息'''
# 设置-更多按钮
setting_more = By.XPATH, "//*[@text='更多']"
# 设置-更多按钮-移动网络按钮
setting_more_mobile_network = By.XPATH, "//*[@text='移动网络']"
# 设置-更多按钮-移动网络按钮-首选网络类型
setting_more_mobile_network_first = By.XPATH, "//*[@text='首选网络类型']"
# 设置-更多按钮-移动网络按钮-首选网络类型-2G
setting_more_mobile_network_first_2G = By.XPATH, "//*[@text='2G']"
# 设置-更多按钮-移动网络按钮-首选网络类型-3G
setting_more_mobile_network_first_3G = By.XPATH, "//*[@text='3G']"










