# coding=gbk
import pytest
import requests
import json
from common.request_util import RequestUtil
from test import Test
from common.parameterize_util import ddt, read_testcase


class Test_Register:
    @pytest.mark.parametrize("args_name", read_testcase('\\register_data.yaml'))  ##��ȡ����������get_token.yaml�ļ��еĲ�����ֵ����ֵ������args_name
    def test_register(self, args_name):
        res = RequestUtil("base_test_url", Test()).standard_yaml(args_name)


if __name__ == '__main__':
    pytest.main(['-vs', './test_register.py'])
