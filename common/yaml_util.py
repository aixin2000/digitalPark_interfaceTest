import os
import yaml


# 读取
from config.config import *


class YamlUtil:

    # 读取
    def read_yaml(self, key):
        with open(os.getcwd() + '/extract.yaml', encoding='gb2312', mode='r') as f:
            value = yaml.load(f, yaml.FullLoader)
            return value[key]

    # 写入
    def write_yaml(self, data):
        with open(os.getcwd() + '/extract.yaml', encoding='gb2312', mode='a') as f:
            yaml.dump(data, stream=f, allow_unicode=True)

    # 清空
    def clear_yaml(self):
        with open(os.getcwd() + '/extract.yaml', encoding='gb2312', mode='w') as f:
            f.truncate()

    # 读取测试用例
    def read_testcase(self, yaml_name):
        with open(f"{DATA_Path}" + yaml_name, mode='r', encoding='gb2312') as f:
            value = yaml.load(f, yaml.FullLoader)
            return value

    # 读取ddt_data数据驱动文件
    def read_data_yaml(self, readyaml):
        with open(readyaml, "r", encoding="gb2312") as f:
            data = yaml.load(stream=f, Loader=yaml.FullLoader)
            return data

    # 读取config.yaml
    def read_config(self, one_node, two_node):
        with open(f"{DATA_Config}" + './/config.yaml', encoding='gb2312') as f:
            value = yaml.load(f, yaml.FullLoader)
            return value[one_node][two_node]
