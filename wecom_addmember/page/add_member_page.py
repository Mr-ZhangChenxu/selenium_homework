from selenium.webdriver.common.by import By

from wecom_addmember.page.base_page import BasePage


# 添加联系人PO
from wecom_addmember.page.get_members_page import GetMembersPage


class AddMemberPage(BasePage):

    def add_member(self, name, account, phonenum):
        # 输入姓名
        self.find(By.ID, "username").send_keys(name)
        # 输入账号
        self.find(By.ID, "memberAdd_acctid").send_keys(account)
        # 输入手机号
        self.find(By.ID, "memberAdd_phone").send_keys(phonenum)
        # 点击保存
        self.find(By.CSS_SELECTOR, ".js_btn_save").click()
        return GetMembersPage(self.driver)





