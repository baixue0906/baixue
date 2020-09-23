import requests
import re
d = {"city":"10001"}

variable_regexp = r"\$([\w_]+)"
r = re.findall(variable_regexp, '{"city": "$city", "month": "3"}')
print(r)
v = d.get(r[0])
result = '{"city": "$city", "month": "3"}'.replace('$'+r[0], v)
print(result)


# session = requests.session()
# session.post(url='http://118.24.91.97:9000/api/login/',
#              headers={"Content-Type":"application/x-www-form-urlencoded"},
#              data={"username": "admin", "password": "huicehuice123"})
#
# res = session.post(url='http://118.24.91.97:9000/api/get_salesMonthly/',
#              headers={"Content-Type":"application/json"},
#              json={"city": "110000", "month": "3"})
# print(res.text)