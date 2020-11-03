import os

import allure
import pytest

@allure.feature('模块1')  # 一级标签
class Test:
    @pytest.mark.parametrize('number1,number2,number3', [(4, 2, 6), (2, 3, 3), (3, 3, 3)])  # 数据驱动（参数化）
    @allure.story('页面1')
    @allure.title('页面1——标题1')
    def test_abc(self, number1, number2, number3):
        print('第1次执行')
        assert number1+number2 == number3
    @pytest.mark.parametrize('num1', [6, 5, 7])
    @allure.story('页面2')
    @allure.title('页面2-标题1')
    def test_bbc(self, num1):
        assert num1 == 2
    def teardown_method(self):
        print('最后执行的方法')
    def setup_method(self):
        print('最开始执行的方法')
@allure.feature('模块2')
class Test2:
    @allure.story('页面3')
    @allure.title('页面3-标题1')
    def test_ddc(self):
        assert 1 == 2
if __name__ == '__main__':
    for one in os.listdir('./report'):
        if 'json' in one:
            os.remove(f'./report/{one}')
    # pytest.main(['test_pytest1.py', '-s', '--alluredir', './report'])
    # os.system('allure serve ./report/report')
    pytest.main(['test_pytest1.py', '-s', '--alluredir', './report'])
    os.system('allure generate ./report -o ./report/report --clean')
