from selenium.webdriver.common.by import By
from wecom_addmember.page.base_page import BasePage


class GetMembersPage(BasePage):

    def get_members(self):
        # 显示等待，等待复选框可点击后，进行后续操作
        self.wait_for_click(10, (By.CSS_SELECTOR, ".ww_checkbox"))
        # 获取已添加成员姓名列表
        name_list = []
        member_ele = self.finds(By.CSS_SELECTOR, ".member_colRight_memberTable_td:nth-child(2)")
        # 循环获取每一个元素对title属性即每个联系人的姓名并添加到name_list
        for ele in member_ele:
            name_list.append(ele.get_attribute("title"))
        return name_list
    #
    # def goto_add_member(self):
    #     '''
    #     跳转添加成员界面
    #     :return:
    #     '''
    #     # 点击add_member按钮
    #     self.find(By.CSS_SELECTOR, ".js_add_member:nth-child(2)").click()
    #     # return AddMemberPage
    #     return AddMemberPage(self.driver)