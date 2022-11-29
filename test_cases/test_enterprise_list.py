# coding=utf-8
import pytest
from common.request_util import RequestUtil
from test import Test
from common.parameterize_util import ddt, read_testcase


class Test_Enterprise_List:
    @pytest.mark.run(order=4)  # x是整数(可以是正数也可以是负数)
    @pytest.mark.parametrize("args_name", read_testcase('\\enterprise_list_data.yaml'))  ##读取测试用例的enterprise_list_data.yaml文件中的参数及值，赋值给变量args_name
    def test_enterprise_list(self, args_name):
        res = RequestUtil("base_test_url", Test()).standard_yaml(args_name)


if __name__ == '__main__':
    pytest.main(['-vs', './test_enterprise_list.py'])
