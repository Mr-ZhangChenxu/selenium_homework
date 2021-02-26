import shelve

import pytest
from selenium import webdriver
from time import sleep

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


class TestWeCom:

    def setup(self):
        '''
        复用浏览器
        Mac 启动命令：
            /Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome - -remote-debugging-port=9222
        注意：使用tab键，不要手动输入
        :return:
        '''
        # option  = Options()
        # option.debugger_address='127.0.0.1:9222' #
        # self.driver=webdriver.Chrome(options=option)
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)

    def teardown(self):
        sleep(3)
        self.driver.quit()

    # 利用获取的cookie，完成自动登录
    def test_cookie(self):
        # 复用浏览器获取登录所需cookie
        # cookies = self.driver.get_cookies()
        # print(cookies)
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        cookies = [
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.vid', 'path': '/', 'secure': False,
             'value': '1688850255897763'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.corpid', 'path': '/', 'secure': False,
             'value': '1970325132370799'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.vid', 'path': '/', 'secure': False,
             'value': '1688850255897763'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.sid', 'path': '/', 'secure': False,
             'value': '8QIFgODDHMpE2hiZltR-Bj6eff6EnmphwiZYhlcoklv_eA2KMxOkEqjqZJggJbaT'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.d2st', 'path': '/', 'secure': False,
             'value': 'a7155157'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.vst', 'path': '/', 'secure': False,
             'value': 'fX9_xfkOvVlJCKEt8UMoCgUh5CWF9liyfv5VsAi7yzRwiThXNh0vHOarPXTzcqV_lvh7JAoi_T7itm_SC4tpua9LlmS36Vvwuct7ezlmHpMbkHnJLNRzqQ14ZQ-GdxwgatlPqVl1MWt6Kai3IAnCtZ4OgcdsLWUpXQiegC-x8bhKKJhMWDvftjmlU80JhJMotL4NVyl7LoggaI3OzPw5-cgiI7lHz-IHTkZ68m5Ofm-6ZkWCqpDEaA848kXVIt0VTtuEyWpQFSm5nlwdyOAWJg'},
            {'domain': '.qq.com', 'expiry': 1613010755, 'httpOnly': False, 'name': '_gid', 'path': '/', 'secure': False,
             'value': 'GA1.2.976025277.1612923962'},
            {'domain': 'work.weixin.qq.com', 'expiry': 1612955495, 'httpOnly': True, 'name': 'ww_rtkey', 'path': '/',
             'secure': False, 'value': '2lmot5b'},
            {'domain': '.qq.com', 'expiry': 1675996355, 'httpOnly': False, 'name': '_ga', 'path': '/', 'secure': False,
             'value': 'GA1.2.550483884.1612751870'},
            {'domain': '.work.weixin.qq.com', 'expiry': 1644287853, 'httpOnly': False, 'name': 'wwrtx.c_gdpr',
             'path': '/', 'secure': False, 'value': '0'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'Hm_lpvt_9364e629af24cb52acc78b43e8c9f77d',
             'path': '/', 'secure': False, 'value': '1612924154'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.refid', 'path': '/', 'secure': False,
             'value': '21901858511561445'},
            {'domain': '.qq.com', 'expiry': 1827201412, 'httpOnly': False, 'name': 'pt_sms_phone', 'path': '/',
             'secure': False, 'value': '155******60'},
            {'domain': '.qq.com', 'expiry': 1613793402, 'httpOnly': False, 'name': 'ptui_loginuin', 'path': '/',
             'secure': False, 'value': '1152294486@qq.com'},
            {'domain': '.work.weixin.qq.com', 'expiry': 1615516358, 'httpOnly': False, 'name': 'wwrtx.i18n_lan',
             'path': '/', 'secure': False, 'value': 'zh'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ltype', 'path': '/', 'secure': False,
             'value': '1'}, {'domain': '.work.weixin.qq.com', 'expiry': 1644460153, 'httpOnly': False,
                             'name': 'Hm_lvt_9364e629af24cb52acc78b43e8c9f77d', 'path': '/', 'secure': False,
                             'value': '1612751869,1612924075'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ref', 'path': '/', 'secure': False,
             'value': 'direct'},
            {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'pgv_pvid', 'path': '/',
             'secure': False, 'value': '4790497601'},
            {'domain': '.qq.com', 'expiry': 2147483639, 'httpOnly': False, 'name': 'ptcz', 'path': '/', 'secure': False,
             'value': 'a73958fe5081ada168760dbda0b729ed19f5644874af6e93a68b72999e00e141'},
            {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'pgv_pvi', 'path': '/',
             'secure': False, 'value': '3650279424'},
            {'domain': '.qq.com', 'expiry': 1910351877, 'httpOnly': False, 'name': 'tvfe_boss_uuid', 'path': '/',
             'secure': False, 'value': 'c848a7f7a30798ba'},
            {'domain': '.qq.com', 'expiry': 2147483646, 'httpOnly': False, 'name': 'RK', 'path': '/', 'secure': False,
             'value': '0ur1kG+jVd'}]
        for cookie in cookies:
            self.driver.add_cookie(cookie)
        sleep(3)
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")

    # 使用现有 cookie 完成联系人导入
    def test_importconnect(self):
        # cookies = self.driver.get_cookies()
        # print(cookies)
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        cookies = [
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.vid', 'path': '/', 'secure': False,
             'value': '1688850255897763'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.corpid', 'path': '/', 'secure': False,
             'value': '1970325132370799'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.vid', 'path': '/', 'secure': False,
             'value': '1688850255897763'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.sid', 'path': '/', 'secure': False,
             'value': '8QIFgODDHMpE2hiZltR-Bj6eff6EnmphwiZYhlcoklv_eA2KMxOkEqjqZJggJbaT'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.d2st', 'path': '/', 'secure': False,
             'value': 'a7155157'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.vst', 'path': '/', 'secure': False,
             'value': 'fX9_xfkOvVlJCKEt8UMoCgUh5CWF9liyfv5VsAi7yzRwiThXNh0vHOarPXTzcqV_lvh7JAoi_T7itm_SC4tpua9LlmS36Vvwuct7ezlmHpMbkHnJLNRzqQ14ZQ-GdxwgatlPqVl1MWt6Kai3IAnCtZ4OgcdsLWUpXQiegC-x8bhKKJhMWDvftjmlU80JhJMotL4NVyl7LoggaI3OzPw5-cgiI7lHz-IHTkZ68m5Ofm-6ZkWCqpDEaA848kXVIt0VTtuEyWpQFSm5nlwdyOAWJg'},
            {'domain': '.qq.com', 'expiry': 1613010755, 'httpOnly': False, 'name': '_gid', 'path': '/', 'secure': False,
             'value': 'GA1.2.976025277.1612923962'},
            {'domain': 'work.weixin.qq.com', 'expiry': 1612955495, 'httpOnly': True, 'name': 'ww_rtkey', 'path': '/',
             'secure': False, 'value': '2lmot5b'},
            {'domain': '.qq.com', 'expiry': 1675996355, 'httpOnly': False, 'name': '_ga', 'path': '/', 'secure': False,
             'value': 'GA1.2.550483884.1612751870'},
            {'domain': '.work.weixin.qq.com', 'expiry': 1644287853, 'httpOnly': False, 'name': 'wwrtx.c_gdpr',
             'path': '/', 'secure': False, 'value': '0'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'Hm_lpvt_9364e629af24cb52acc78b43e8c9f77d',
             'path': '/', 'secure': False, 'value': '1612924154'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.refid', 'path': '/', 'secure': False,
             'value': '21901858511561445'},
            {'domain': '.qq.com', 'expiry': 1827201412, 'httpOnly': False, 'name': 'pt_sms_phone', 'path': '/',
             'secure': False, 'value': '155******60'},
            {'domain': '.qq.com', 'expiry': 1613793402, 'httpOnly': False, 'name': 'ptui_loginuin', 'path': '/',
             'secure': False, 'value': '1152294486@qq.com'},
            {'domain': '.work.weixin.qq.com', 'expiry': 1615516358, 'httpOnly': False, 'name': 'wwrtx.i18n_lan',
             'path': '/', 'secure': False, 'value': 'zh'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ltype', 'path': '/', 'secure': False,
             'value': '1'}, {'domain': '.work.weixin.qq.com', 'expiry': 1644460153, 'httpOnly': False,
                             'name': 'Hm_lvt_9364e629af24cb52acc78b43e8c9f77d', 'path': '/', 'secure': False,
                             'value': '1612751869,1612924075'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ref', 'path': '/', 'secure': False,
             'value': 'direct'},
            {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'pgv_pvid', 'path': '/',
             'secure': False, 'value': '4790497601'},
            {'domain': '.qq.com', 'expiry': 2147483639, 'httpOnly': False, 'name': 'ptcz', 'path': '/', 'secure': False,
             'value': 'a73958fe5081ada168760dbda0b729ed19f5644874af6e93a68b72999e00e141'},
            {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'pgv_pvi', 'path': '/',
             'secure': False, 'value': '3650279424'},
            {'domain': '.qq.com', 'expiry': 1910351877, 'httpOnly': False, 'name': 'tvfe_boss_uuid', 'path': '/',
             'secure': False, 'value': 'c848a7f7a30798ba'},
            {'domain': '.qq.com', 'expiry': 2147483646, 'httpOnly': False, 'name': 'RK', 'path': '/', 'secure': False,
             'value': '0ur1kG+jVd'}]
        for cookie in cookies:
            self.driver.add_cookie(cookie)
        sleep(3)
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        # 点击导入通讯录
        self.driver.find_element(By.CSS_SELECTOR, ".index_service_cnt_itemWrap:nth-child(2)").click()
        # 上传通讯录文件
        self.driver.find_element(By.ID, "js_upload_file_input").send_keys("/Users/zhangchenxu/Downloads/文稿/key.xls")
        # 断言，根据文件名称断言是否上传成功
        assert "key.xls" == self.driver.find_element(By.ID, "upload_file_name").text
        sleep(3)

    # 利用 shelve，完成cookie本地存储以及读取
    def test_shelve(self):
        db = shelve.open("mydb/cookies")
        # db['cookie'] = cookies
        # db.close()
        cookies = db['cookie']
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        for cookie in cookies:
            self.driver.add_cookie(cookie)
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")