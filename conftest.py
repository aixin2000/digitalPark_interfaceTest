import pytest
from common.yaml_util import YamlUtil


# @pytest.fixture(scope="function")
# def exe_sql():
#     print("����ִ��֮ǰ")
#     yield
#     print("����ִ��֮��")


# �����еĽӿ�����֮ǰִ��
@pytest.fixture(scope="session", autouse=True)
def clear_extract():
    YamlUtil().clear_yaml()
