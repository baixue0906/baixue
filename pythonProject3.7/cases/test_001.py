import pytest
import xlrd
import json


def test_data():
    lines = []
    worksheet = xlrd.open_workbook('../data/testcase.xlsx').sheet_by_index(0)
    rows = worksheet.nrows
    for i in range(1, rows):
        line = worksheet.row_values(i)
        lines.append(line)
    # return lines
    print(lines)


class Test_x:
    @pytest.mark.parametrize("message", test_data())  # pytest参数化装饰器，第一个参数写自定义的参数名，第二个参数传取到的数据
    def test_x(self, message):  # 上面的参数名是什么，这里也要写什么
        retmessage = json.loads(message[10])
        retmessage = retmessage['message']
        assert retmessage == test_data()[0][10]