import jsonpath
data = {"city":"$.city"}
data1 = {'city':'$.city'}
data_list = list(data.values())
print(data_list)
# print(data.values()[0])
print(type(data_list))
print(type(data1))