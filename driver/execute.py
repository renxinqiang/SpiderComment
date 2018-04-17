#!/usr/local/bin/python3

"""
@desc 浏览器操作
@author renxinqiang
"""

from driver import Driver


class Execute(Driver):

    # 点击
    def click_ele(self,ele):
        if not ele:
            return False
        ele.click()
        pass

    # 清除内容
    def clear_ele(self,ele):
        if not ele:
            return False
        ele.clear()
        pass

    # 输入
    def send_key_ele(self,ele,con):
        if not ele or not con:
            return False
        ele.send_keys(con)
        pass

    # 选项卡
    def tab(self):
        return self.driver.window_handles

    # 选择选项卡
    def select_tab(self,number=0):
        handles = self.tab()
        return self.driver.switch_to.window(handles[number])

    # 选择ifram
    def select_ifram(self,ifram_id):
        return self.driver.switch_to.frame(ifram_id)

    # 刷新
    def refresh_page(self):
        self.driver.refresh()
        pass

    # cookie
    def get_cookie(self):
        return self.driver.get_cookies()

    def add_cookie(self,con):
        if not con:
            return False
        self.driver.add_cookie(con)
        pass

    def delete_cookie(self):
        self.driver.delete_all_cookies()
        pass



