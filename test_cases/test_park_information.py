# coding=utf-8
import pytest
import requests
import json
from common.request_util import RequestUtil
from test import Test
from common.parameterize_util import ddt, read_testcase


class Test_Park_Information:
    # 执行失败后重试， 重试3次，每次重试间隔2秒
    @pytest.mark.flaky(reruns=3, reruns_delay=2)
    # @pytest.mark.skip('暂时不执行')
    @pytest.mark.parametrize("args_name", read_testcase('\\park_information_data.yaml'))  ##读取测试用例的get_token.yaml文件中的参数及值，赋值给变量args_name
    def test_park_information(self, args_name):
        res = RequestUtil("base_test_url", Test()).standard_yaml(args_name)


if __name__ == '__main__':
    pytest.main(['-vs', './test_park_information.py'])