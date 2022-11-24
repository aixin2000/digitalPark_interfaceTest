import random
import time

import yaml

from common.yaml_util import YamlUtil
from config.config import DATA_Config


class Test:
    # ��ȡ����绰����
    def randomPhone(self):
        headList = ["130", "131", "132", "133", "134", "135", "136", "137", "138", "139",
                    "147", "150", "151", "152", "153", "155", "156", "157", "158", "159",
                    "186", "187", "188", "189"]
        # print(random.choice(headList) + "".join(random.choice("0123456789") for i in range(8)))
        return random.choice(headList) + "".join(random.choice("0123456789") for i in range(8))

    # ��ȡ���ʱ��
    def get_random_time(self):
        # return str(int(time.time()))[1:6]     #��ȡ���ʱ�䣬�õ�����ʱ���
        return time.strftime('%H:%M:%S', time.localtime(time.time()))  # ��ȡ����ʱ�䣬������ʽת����ʱ����

    # ��ȡextract.yaml�ļ��е�ֵ
    def read_extract_data(self, key):
        return YamlUtil().read_yaml(key)

    # ��ȡconfig.yaml
    def read_config(self, one_node, two_node):
        with open(f"{DATA_Config}" + './config.yaml', encoding='gb2312') as f:
            value = yaml.load(f, yaml.FullLoader)
            return value[one_node][two_node]

# import requests
# from utils.logging_tool.log_control import ERROR
# from utils.other_tools.allure_data.allure_report_data import TestMetrics, AllureFileClean
# from utils.times_tool.time_control import now_time
# from utils.other_tools.get_local_ip import get_host_ip
# from utils.other_tools.exceptions import SendMessageError, ValueTypeError
# from utils import config
#
#
# class WeChatSend:
#     """
#     ��ҵ΢����Ϣ֪ͨ
#     """
#
#     def __init__(self, metrics: TestMetrics):
#         self.metrics = metrics
#         self.headers = {"Content-Type": "application/json"}
#
#     def send_text(self, content, mentioned_mobile_list=None):
#         """
#         �����ı�����֪ͨ
#         :param content: �ı����ݣ��������2048���ֽڣ�������utf8����
#         :param mentioned_mobile_list: �ֻ����б������ֻ��Ŷ�Ӧ��Ⱥ��Ա(@ĳ����Ա)��@all��ʾ����������
#         :return:
#         """
#         _data = {"msgtype": "text", "text": {"content": content, "mentioned_list": None,
#                                              "mentioned_mobile_list": mentioned_mobile_list}}
#
#         if mentioned_mobile_list is None or isinstance(mentioned_mobile_list, list):
#             # �ж��ֻ������б��е��������ͣ����Ϊint���ͣ����͵���Ϣ������
#             if len(mentioned_mobile_list) >= 1:
#                 for i in mentioned_mobile_list:
#                     if isinstance(i, str):
#                         res = requests.post(url=config.wechat.webhook, json=_data, headers=self.headers)
#                         if res.json()['errcode'] != 0:
#                             ERROR.logger.error(res.json())
#                             raise SendMessageError("��ҵ΢�š��ı����͡���Ϣ����ʧ��")
#
#                     else:
#                         raise ValueTypeError("�ֻ�����������ַ�������.")
#         else:
#             raise ValueTypeError("�ֻ������б������list����.")
#
#     def send_markdown(self, content):
#         """
#         ���� MarkDown ������Ϣ
#         :param content: ��Ϣ���ݣ�markdown��ʽ
#         :return:
#         """
#         _data = {"msgtype": "markdown", "markdown": {"content": content}}
#         res = requests.post(url=config.wechat.webhook, json=_data, headers=self.headers)
#         if res.json()['errcode'] != 0:
#             ERROR.logger.error(res.json())
#             raise SendMessageError("��ҵ΢�š�MarkDown���͡���Ϣ����ʧ��")
#
#     def _upload_file(self, file):
#         """
#         �Ƚ��ļ��ϴ�����ʱý���
#         """
#         key = config.wechat.webhook.split("key=")[1]
#         url = f"https://qyapi.weixin.qq.com/cgi-bin/webhook/upload_media?key={key}&type=file"
#         data = {"file": open(file, "rb")}
#         res = requests.post(url, files=data).json()
#         return res['media_id']
#
#     def send_file_msg(self, file):
#         """
#         �����ļ����͵���Ϣ
#         @return:
#         """
#
#         _data = {"msgtype": "file", "file": {"media_id": self._upload_file(file)}}
#         res = requests.post(url=config.wechat.webhook, json=_data, headers=self.headers)
#         if res.json()['errcode'] != 0:
#             ERROR.logger.error(res.json())
#             raise SendMessageError("��ҵ΢�š�file���͡���Ϣ����ʧ��")
#
#     def send_wechat_notification(self):
#         """ ������ҵ΢��֪ͨ """
#         text = f"""��{config.project_name}�Զ���֪ͨ��
#                                     >���Ի�����<font color=\"info\">TEST</font>
#                                     >���Ը����ˣ�@{config.tester_name}
#                                     >
#                                     > **ִ�н��**
#                                     ><font color=\"info\">��  ��  ��  : {self.metrics.pass_rate}%</font>
#                                     >����  ������<font color=\"info\">{self.metrics.total}</font>
#                                     >�ɹ���������<font color=\"info\">{self.metrics.passed}</font>
#                                     >ʧ����������`{self.metrics.failed}��`
#                                     >�쳣��������`{self.metrics.broken}��`
#                                     >������������<font color=\"warning\">{self.metrics.skipped}��</font>
#                                     >����ִ��ʱ����<font color=\"warning\">{self.metrics.time} s</font>
#                                     >ʱ�䣺<font color=\"comment\">{now_time()}</font>
#                                     >
#                                     >����ظ�����Ա�ɺ��Դ���Ϣ��
#                                     >���Ա��棬����鿴>>[���Ա������](http://{get_host_ip()}:9999/index.html)"""
#
#         WeChatSend(AllureFileClean().get_case_count()).send_markdown(text)
#
#
# if __name__ == '__main__':
#     WeChatSend(AllureFileClean().get_case_count()).send_wechat_notification()
