# coding=utf-8
import json
import yaml
from config.config import *


# 读取测试用例
from common.yaml_util import YamlUtil


def read_testcase(yaml_name):
    with open(f'{DATA_Path}' + yaml_name, mode='r', encoding='GBK') as f:
        caseinfo = yaml.load(f, yaml.FullLoader)
        if len(caseinfo) >= 2:  # 判断yaml用例文件中有几条用例，当用例大于等于2时，直接返回caseinfo
            return caseinfo
        else:  # 当等于1时，因为数据驱动后的caseinfo是字典列表我们就需要对caseinfo解包
            if "parameterize" in dict(*caseinfo).keys():
                new_caseinfo = ddt(*caseinfo)
                return new_caseinfo
            else:
                return caseinfo


def ddt(caseinfo):
    if "parameterize" in caseinfo.keys():
        caseinfo_str = json.dumps(caseinfo)
        for param_key, param_value in caseinfo["parameterize"].items():
            key_list = param_key.split("-")
            # print("------key和value------")
            # print(key_list, param_value)
            length_flag = True
            # print("------data数据列表------")
            # 规范yaml数据文件的写法
            data_list = YamlUtil().read_data_yaml(f'{DATA_Ddt}' + param_value)
            for data in data_list:
                # print(data)
                if len(data) != len(key_list):
                    length_flag = False
                    break
            # 替换值
            # print("------替换值------")
            new_caseinfo = []
            if length_flag:
                for x in range(1, len(data_list)):  # 循环数据的行数
                    temp_caseinfo = caseinfo_str
                    for y in range(0, len(data_list[x])):  # 循环数据列
                        if data_list[0][y] in key_list:
                            # 替换原始的yaml里面的$ddt{}
                            # 数字类型去掉“”
                            if isinstance(data_list[x][y], int) or isinstance(data_list[x][y], float):
                                temp_caseinfo = temp_caseinfo.replace('"$ddt{' + data_list[0][y] + '}"',
                                                                      str(data_list[x][y]))
                            else:
                                temp_caseinfo = temp_caseinfo.replace("$ddt{" + data_list[0][y] + "}",
                                                                      str(data_list[x][y]))
                    print(temp_caseinfo)

                    new_caseinfo.append(json.loads(temp_caseinfo))
            return new_caseinfo
    else:
        return caseinfo
