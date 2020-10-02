# conftest.py
# 2020/10/1 1:37 下午
#环境初始化操作baixue提交1002

import pytest
from Lib.Lib_api.api_getOpterToken import *
from Lib.Lib_api.api_teacherInfo import teacherInfo

@pytest.fixture(scope='function')
def update_teacher_init():#更新老师信息的环境初始化
    tmptoken = TeacherList().test_gettmptoken()
    opterToken = TeacherList().test_gettoken()
    teacherGuid = teacherInfo().api_teacherList({'opterToken':opterToken})['data'][55]['guid'] #测试数据，测试老师的数据
    return teacherGuid
