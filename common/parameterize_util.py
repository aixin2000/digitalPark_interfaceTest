import json
# from common.yaml_util import YamlUtil
import os
import yaml
import yaml
from config.config import *


# ��ȡ��������
from common.yaml_util import YamlUtil


def read_testcase(yaml_name):
    with open(f'{DATA_Path}' + yaml_name, mode='r', encoding='gb2312') as f:
        caseinfo = yaml.load(f, yaml.FullLoader)
        if len(caseinfo) >= 2:  # �ж�yaml�����ļ����м������������������ڵ���2ʱ��ֱ�ӷ���caseinfo
            return caseinfo
        else:  # ������1ʱ����Ϊ�����������caseinfo���ֵ��б����Ǿ���Ҫ��caseinfo���
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
            # print("------key��value------")
            print(key_list, param_value)
            length_flag = True
            # print("------data�����б�------")
            # �淶yaml�����ļ���д��
            data_list = YamlUtil().read_data_yaml(f'{DATA_Ddt}' + param_value)
            for data in data_list:
                print(data)
                if len(data) != len(key_list):
                    length_flag = False
                    break
            # �滻ֵ
            # print("------�滻ֵ------")
            new_caseinfo = []
            if length_flag:
                for x in range(1, len(data_list)):  # ѭ�����ݵ�����
                    temp_caseinfo = caseinfo_str
                    for y in range(0, len(data_list[x])):  # ѭ��������
                        if data_list[0][y] in key_list:
                            # �滻ԭʼ��yaml�����$ddt{}
                            # ��������ȥ������
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
