from selenium.webdriver.common.by import By

from wecom_addmember.page.add_member_page import AddMemberPage
from wecom_addmember.page.base_page import BasePage

# 企业微信主页PO
class MainPage(BasePage):

    base_url = "https://work.weixin.qq.com/wework_admin/frame#index"

    def goto_add_member(self):
        '''
        跳转添加成员界面
        :return:
        '''
        # 点击add_member按钮
        self.find(By.CSS_SELECTOR, ".index_service_cnt_itemWrap:nth-child(1)").click()
        # return AddMemberPage
        return AddMemberPage(self.driver)

    def goto_menu_index(self):
        '''
        回到首页
        :return:
        '''
        self.find(By.ID, "menu_index").click()
        return True