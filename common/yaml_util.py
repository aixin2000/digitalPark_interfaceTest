import os
import yaml


# ��ȡ
from config.config import *


class YamlUtil:

    # ��ȡ
    def read_yaml(self, key):
        with open(os.getcwd() + '/extract.yaml', encoding='gb2312', mode='r') as f:
            value = yaml.load(f, yaml.FullLoader)
            return value[key]

    # д��
    def write_yaml(self, data):
        with open(os.getcwd() + '/extract.yaml', encoding='gb2312', mode='a') as f:
            yaml.dump(data, stream=f, allow_unicode=True)

    # ���
    def clear_yaml(self):
        with open(os.getcwd() + '/extract.yaml', encoding='gb2312', mode='w') as f:
            f.truncate()

    # ��ȡ��������
    def read_testcase(self, yaml_name):
        with open(f"{DATA_Path}" + yaml_name, mode='r', encoding='gb2312') as f:
            value = yaml.load(f, yaml.FullLoader)
            return value

    # ��ȡddt_data���������ļ�
    def read_data_yaml(self, readyaml):
        with open(readyaml, "r", encoding="gb2312") as f:
            data = yaml.load(stream=f, Loader=yaml.FullLoader)
            return data

    # ��ȡconfig.yaml
    def read_config(self, one_node, two_node):
        with open(f"{DATA_Config}" + './/config.yaml', encoding='gb2312') as f:
            value = yaml.load(f, yaml.FullLoader)
            return value[one_node][two_node]
