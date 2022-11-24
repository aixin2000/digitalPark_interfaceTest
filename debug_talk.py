import random
import time
from common.yaml_util import YamlUtil


class DebugTalk:
    # 获取随机电话号码
    def randomPhone(self):
        headList = ["130", "131", "132", "133", "134", "135", "136", "137", "138", "139",
                    "147", "150", "151", "152", "153", "155", "156", "157", "158", "159",
                    "186", "187", "188", "189"]
        # print(random.choice(headList) + "".join(random.choice("0123456789") for i in range(8)))
        return random.choice(headList) + "".join(random.choice("0123456789") for i in range(8))

    # 获得随机数
    def get_randon_number(self, min, max):
        return random.randint(int(min), int(max))

    # 读取extract.yaml文件中的值
    def read_extract_data(self, key):
        return YamlUtil().read_yaml(key)
