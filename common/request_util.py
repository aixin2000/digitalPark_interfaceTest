# coding=gbk
import jsonpath
import requests
import json
from common.yaml_util import YamlUtil
from builtins import str
import re
from log.loggerController import log
from debug_talk import DebugTalk
from test import Test


class RequestUtil:

    def __init__(self, two_node, obj):
        self.base_url = YamlUtil().read_config('base', two_node)
        self.obj = obj

    # �滻ֵ�ķ���
    # #(�滻url��params,data,json,headers)
    # #(string��int,float,list,dict)
    def replace_value(self, data):
        if data:
            # ������������
            data_type = type(data)
            # �ж���������ת����str
            if isinstance(data, dict) or isinstance(data, list):
                str_data = json.dumps(data)
            else:
                str_data = str(data)
            # print(str_data)
            for cs in range(1, str_data.count('${') + 1):
                # �滻
                if "${" in str_data and "}" in str_data:
                    start_index = str_data.index("${")
                    end_index = str_data.index("}", start_index)
                    old_value = str_data[start_index:end_index + 1]
                    print("old_value:" + old_value)
                    # ���䣺ͨ����Ķ���ͷ����ַ������÷���
                    func_name = old_value[2:old_value.index('(')]
                    args_value1 = old_value[old_value.index('(') + 1:old_value.index(')')]
                    new_value = ""
                    if args_value1 != "":
                        args_value2 = args_value1.split(',')
                        new_value = getattr(self.obj, func_name)(*args_value2)
                    else:
                        new_value = getattr(self.obj, func_name)()
                    str_data = str_data.replace(old_value, str(new_value))
                    print(f"str_data: {str_data} ")
            # ��ԭ��������
            if isinstance(data, dict) or isinstance(data, list):
                data = json.loads(str_data)
            else:
                data = data_type(str_data)
        return data

    # �淶yaml��������
    def standard_yaml(self, caseinfo):
        caseinfo_keys = caseinfo.keys()
        print(f"caseinfo_keys : {caseinfo_keys}")
        # �ж�һ���ؼ����Ƿ������name��request��validate
        if "name" in caseinfo_keys and "request" in caseinfo_keys and "validate" in caseinfo_keys:
            # �ж�request�����Ƿ������method��url
            request_keys = caseinfo["request"].keys()
            caseinfo_aa = caseinfo["request"]
            print(f"request_keys : {request_keys}")
            print(f"caseinfo : {caseinfo_aa}")
            if "method" in request_keys and "url" in request_keys:
                # print("yaml�����ܹ����ͨ��")
                log.info('yaml�����ܹ����ͨ��')
                log.info(f'�ӿ��������ƣ�{caseinfo["name"]}')
                log.info(f'����ͷ��{caseinfo["headers"]}')
                method = caseinfo['request'].pop("method")  # pop() ���������Ƴ��б��е�һ��Ԫ�أ����ҷ��ظ�Ԫ�ص�ֵ��
                # print(f"method: {method}")
                url = caseinfo['request'].pop("url")
                log.info(f'���󷽷���{method}')
                log.info(f'�滻ǰurl�����ַ��{url}')
                log.info(f"���������{caseinfo['request']}")
                # print(f"�滻ǰurl: {url}")
                res = self.send_request(method, url, **caseinfo['request'])  # caseinfo��Ҫ�����**
                return_text = res.text
                return_code = res.status_code
                log.info(f"��Ӧ�ı���{return_text}")
                log.info(f"��Ӧ״̬�룺{return_code}")
                # print(f"return_code: {return_code}")
                # print(type(return_text))
                return_json = ""
                try:
                    return_json = res.json()
                    log.info(f"��Ӧjson���ݣ�{return_json}")
                except Exception as e:
                    print("extract���صĽ������JSON��ʽ")
                log.info(f"Ԥ�ڽ����{caseinfo['validate']}")
                # print(f"caseinfo['validate']: {caseinfo['validate']}")
                # print(f"return_json: {type(return_json)}")
                # print(f"return_jsonֵ: {return_json}")

                self.assert_result(caseinfo['validate'], return_json, return_code)
                # if caseinfo['validate'] != "none":
                #     yq_resulte = caseinfo['validate']
                #     sj_resulte = return_json
                #     self.assert_result(yq_resulte, sj_resulte, return_code)
                # if return_text is str:
                #     self.assert_result(caseinfo['validate'], return_text, return_code)
                # elif return_json is dict:
                #     self.assert_result(caseinfo['validate'], return_json, return_code)

                # ��ȡֵ��д��extract.yaml�ļ�
                if "extract" in caseinfo.keys():
                    for key, value in caseinfo["extract"].items():
                        if "(.*?)" in value or "(.+?)" in value:  # ������ʽ
                            zz_value = re.search(value, return_text)
                            print(return_text)
                            print(f"zz: {zz_value}")
                            if zz_value:
                                extract_value = {key: zz_value.group(1)}
                                YamlUtil().write_yaml(extract_value)
                                print(f"extract_value : {extract_value}")
                        else:  # jsonpath
                            try:
                                resturn_json = res.json()
                                js_value = jsonpath.jsonpath(resturn_json, value)
                                if js_value:
                                    extract_value = {key: js_value[0]}
                                    YamlUtil().write_yaml(extract_value)
                                    print(extract_value)
                            except Exception as e:
                                print("extract���صĽ������JSON��ʽ,����ʹ��jsonpath��ȡ")
                return res
                # ���ԣ�
            else:
                print("��request�±������method,url")
        else:
            print("һ���ؼ��ֱ������name,request,validate")

    sess = requests.session()

    # ͳһ�����װ
    def send_request(self, method, url, **kwargs):
        method = str(method).lower()  # ת��Сд
        # ����·����ƴ�Ӻ��滻
        url = self.base_url + self.replace_value(url)
        # print(f"�滻��url:  {url}")
        log.info(f"�滻��url�����ַ:  {url}")
        # print(f"method:  {method}")
        # �����滻
        for key, value in kwargs.items():
            if key in ['params', 'data', 'json', 'headers']:
                kwargs[key] = self.replace_value(value)
                print(kwargs[key])
            elif key == "files":
                for file_key, file_path in value.items():
                    value[file_key] = open(file_path, 'rb')
        res = RequestUtil.sess.request(method, url, **kwargs)
        # print(res.text)
        # print(res.json())
        return res

    # ����
    def assert_result(self, yq_result, sj_result, return_code):
        all_flag = 0
        for yq in yq_result:
            for key, value in yq.items():
                print(key, value)
                if key == "equals":
                    flag = self.equals_assert(value, return_code, sj_result)
                    all_flag = all_flag + flag
                elif key == 'contains':
                    flag = self.contains_assert(value, sj_result)
                    all_flag = all_flag + flag
                else:
                    print("����ݲ�֧�ִ˶ζ��Է�ʽ")
        assert all_flag == 0

    # ��ȶ���
    def equals_assert(self, value, return_code, sj_result):
        flag = 0
        for assert_key, assert_value in value.items():
            print(assert_key, assert_value)
            if assert_key == "status_code":  # ״̬����
                assert_value == return_code
                if assert_value != return_code:
                    flag = flag + 1
                    print("����ʧ�ܣ����ص�״̬�벻����%s" % assert_value)
            else:
                # listΪʵ��jsonƥ�������ֵ
                lists = jsonpath.jsonpath(sj_result, '$..%s' % assert_key)
                print(f"lists: {lists}")
                if lists:
                    if assert_value not in lists:
                        flag = flag + 1
                        print("����ʧ�ܣ�" + assert_key + "������" + str(assert_value))
                else:
                    flag = flag + 1
                    print("����ʧ�ܣ����صĽ�������ڣ�" + assert_key)
            print(f"assert_key: {assert_key},assert_value: {assert_value}")
        return flag

    # ��������
    def contains_assert(self, value, sj_result):
        flag = 0
        if value not in str(sj_result):
            flag = flag + 1
            print("����ʧ�ܣ����صĽ���в�������" + value)
        return flag

