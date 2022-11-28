# coding=utf-8
import pytest
import requests
import json
from common.request_util import RequestUtil
from test import Test
from common.parameterize_util import ddt, read_testcase


class Test_Request:
    # 全为正数或负数时,值越小,优先级越高
    # 既有正数又有负数时,正数优先级高(-1,2,-3的执行顺序是2,-3,-1)
    @pytest.mark.run(order=1)  # x是整数(可以是正数也可以是负数)
    # 执行失败后重试， 重试3次，每次重试间隔2秒
    @pytest.mark.flaky(reruns=3, reruns_delay=2)
    @pytest.mark.parametrize("args_name", read_testcase('\\login_data.yaml'))  ##读取测试用例的get_token.yaml文件中的参数及值，赋值给变量args_name
    def test_login(self, args_name):
        res = RequestUtil("base_test_url", Test()).standard_yaml(args_name)


if __name__ == '__main__':
    pytest.main(['-vs', './test_login.py'])
