# coding=gbk
from datetime import datetime
import os

# ��Ŀ��Ŀ¼
ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# json����Ŀ¼
RESULT_DIR = os.path.join(ROOT_DIR, 'result')
# ����Ŀ¼
REPORT_DIR = os.path.join(ROOT_DIR, 'report')
# ������������Ŀ¼
DATA_Path = os.path.join(ROOT_DIR, 'data')
# ����������������Ŀ¼
DATA_Ddt = os.path.join(ROOT_DIR)
# ������������Ŀ¼
DATA_Config = os.path.join(ROOT_DIR, 'test_cases')
# ���Ի�����ַ
# HOST = 'http://hhr1.test.hhrchina.com'
HOST = 'http://demo.hhrchina.com'

print(DATA_Path)
