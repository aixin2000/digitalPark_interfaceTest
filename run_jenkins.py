import pytest
import os

if __name__ == '__main__':
    pytest.main(['-vs', '--alluredir=D:/jenkins_home/workspace/interface-test/allure-result/',
                 '--clean-alluredir'])
    os.system('allure generate D:/jenkins_home/workspace/interface-test/allure-result/ -o '
              'D:/jenkins_home/workspace/interface-test/allure-report/ --clean')
