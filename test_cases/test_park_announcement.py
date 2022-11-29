# coding=utf-8
import allure
import pytest
from common.request_util import RequestUtil
from test import Test
from common.parameterize_util import ddt, read_testcase

@allure.epic("小昆山园区公告模块测试case")
@allure.feature('小昆山园区公告模块功能')
class Test_Park_Announcement:
    @allure.story('小昆山园区公告模块接口')
    @allure.severity('blocker')
    @allure.description("这里是对小昆山园区公告模块用例的一些详细说明")
    @allure.issue("https://www.tapd.cn/44308309/bugtrace/bugs/view/1144308309001010744",
                  name='点击跳转缺陷地址')
    @allure.testcase("https://www.tapd.cn/44308309/sparrow/test_plan/detail/1144308309001000216?action_timestamp"
                     "=84116516&dialog_preview_id=tcase_1144308309001020610", name='点击我跳转TAPD')
    # 执行失败后重试， 重试3次，每次重试间隔2秒
    @pytest.mark.flaky(reruns=3, reruns_delay=2)
    @pytest.mark.parametrize("args_name", read_testcase('\\park_announcement_data.yaml'))  ##读取测试用例的get_park_announcement_data.yaml文件中的参数及值，赋值给变量args_name
    def test_park_announcement(self, args_name):
        res = RequestUtil("base_test_url", Test()).standard_yaml(args_name)


if __name__ == '__main__':
    pytest.main(['-vs', './test_park_announcement.py'])
