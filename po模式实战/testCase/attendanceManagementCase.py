# -*- coding:utf-8 -*-
# @author: zhong
# @project:untitled11
# @file: attendanceManagementCase.py
# @time: 2020/11/5 10:42
# @desc:考勤管理测试用例
import socket
import time
import unittest
from po模式实战.pages.attendanceManagementPage import AttendanceManagementPageActionObj as PAO
class AttendanceManagementCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """
        前置条件，访问到网址
        :return:
        """
        PAO.to_page()
    def test_punch_clock(self):
        """
        打卡功能测试用例，打卡状态建议做接口测试（数据计算逻辑通常在接口层面进行测试
        打卡成功后，新建一行打卡记录，打卡记录的记录内容正确
        :return:
        """
        """1 打卡"""
        # 点击打卡按钮
        PAO.punchClock()
        # 获取本地时间
        local_time = time.localtime()
        # 刷新页面
        PAO.driver.refresh()
        """2 获取最新一行打卡记录的值"""
        # 获取打卡日期，具体到天
        punch_date = PAO.sign_table_date_boxes()[0].text
        # 获取打卡时间，具体到秒（去掉最后一位秒数，避免打卡时间误差）
        punch_time = PAO.sign_table_time_boxes()[0].text[:-1]
        # 获取打卡状态
        punch_status = PAO.sign_table_status_boxes()[0].text
        # 获取打卡ip
        punch_ip = PAO.sign_table_ip_boxes()[0].text
        """3 断言"""
        self.assertEqual(punch_date, time.strftime("%Y-%m-%d", local_time), msg="断言打卡日期")
        self.assertEqual(punch_time, time.strftime("%H:%M:%S", local_time)[:-1], msg="断言打卡时间")
        self.assertIn(punch_status, ["正常", "迟到", "早退", "加班"], msg="断言打卡状态")
        self.assertEqual(punch_ip, self.__get_ip(), msg="断言打卡ip")
    @staticmethod
    def __get_ip():
        """
        获取本地ip，生成一个UDP包，把自己的IP放到UPD协议中，然后从UPD包中获取本机的IP
        :return:
        """
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
if __name__ == '__main__':
    unittest.main()






