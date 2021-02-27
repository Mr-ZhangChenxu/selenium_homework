import pytest

from wecom_addmember.page.main_page import MainPage


class TestAddMember:

    def setup(self):
        '''
        实例化MainPage()
        打开企业微信后台管理主页
        :return:
        '''
        self.mainpage = MainPage()

    # 添加一个联系人
    def test_addmember(self):
        name = "a02"
        account = "a02"
        phonenum = "13312345672"
        name_list = self.mainpage.goto_add_member().add_member(name, account, phonenum).get_members()
        assert name in name_list

    # 添加多个联系人
    @pytest.mark.parametrize('name, account, phonenum',[
        ('a001', 'a001', '13212345671'),
        ('a002', 'a002', '13212345672'),
        ('a003', 'a003', '13212345673'),
    ], ids=['member1', 'member2', 'member3'])
    def test_addmembers(self, name, account, phonenum):
        name_list = self.mainpage.goto_add_member().add_member(name, account, phonenum).get_members()
        assert name in name_list

    def teardown(self):
        '''
        回到首页
        :return:
        '''
        self.mainpage.goto_menu_index()

