# coding=utf-8
import allure
import pytest
from common.request_util import RequestUtil
from test import Test
from common.parameterize_util import ddt, read_testcase


@allure.epic("小昆山园区列表页测试case")
@allure.feature('小昆山园区列表页功能')
class Test_Enterprise_List:
    @allure.story('小昆山园区列表页接口')
    @allure.severity('blocker')
    @allure.description("这里是对小昆山园区列表页用例的一些详细说明")
    @allure.issue("https://www.tapd.cn/44308309/bugtrace/bugs/view/1144308309001010744",
                  name='点击跳转缺陷地址')
    @allure.testcase("https://www.tapd.cn/44308309/sparrow/test_plan/detail/1144308309001000216?action_timestamp"
                     "=84116516&dialog_preview_id=tcase_1144308309001020610", name='点击我跳转TAPD')
    @pytest.mark.run(order=4)  # x是整数(可以是正数也可以是负数)
    @pytest.mark.parametrize("args_name", read_testcase(
        '\\enterprise_list_data.yaml'))  ##读取测试用例的enterprise_list_data.yaml文件中的参数及值，赋值给变量args_name
    def test_enterprise_list(self, args_name):
        res = RequestUtil("base_test_url", Test()).standard_yaml(args_name)


if __name__ == '__main__':
    pytest.main(['-vs', './test_enterprise_list.py'])
