# coding=gbk
from datetime import datetime
import os

# 项目根目录
ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# json报告目录
RESULT_DIR = os.path.join(ROOT_DIR, 'result')
# 报告目录
REPORT_DIR = os.path.join(ROOT_DIR, 'report')
# 测试数据所在目录
DATA_Path = os.path.join(ROOT_DIR, 'data')
# 测试数据驱动所在目录
DATA_Ddt = os.path.join(ROOT_DIR)
# 测试数据所在目录
DATA_Config = os.path.join(ROOT_DIR, 'test_cases')
# 测试环境地址
# HOST = 'http://hhr1.test.hhrchina.com'
HOST = 'http://demo.hhrchina.com'

print(DATA_Path)
