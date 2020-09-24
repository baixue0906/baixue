import requests
from config.conf import *

url = server_ip()+'/coursemgr/v1/getQualificationInfo'
r = requests.get(url=url)
print(r.json())