# coding=utf-8
import pytest
from common.yaml_util import YamlUtil
from log.loggerController import log


# @pytest.fixture(scope="function")
# def exe_sql():
#     print("用例执行之前")
#     yield
#     print("用例执行之后")


# 在所有的接口请求之前执行
@pytest.fixture(scope="session", autouse=True)
def clear_extract():
    YamlUtil().clear_yaml()


@pytest.fixture(scope="function", autouse=True)
def setupteardown():
    print('\n')
    log.info('------------------------------ 接口测试开始执行 ------------------------------')
    yield
    log.info('------------------------------ 接口测试结束 ------------------------------')



