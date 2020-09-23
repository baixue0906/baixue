#前置共享
import pytest
import requests
from Commonlib.common import login
@pytest.fixture(scope="session")
def login_fixture():
    s = requests.session()
    s = login(s)
    #print("""6666666""")
    #s.headers.update(m)
    yield s.headers
    s.close()

@pytest.fixture(scope="session")
def unlogin_fixture():
    s = requests.session()
    yield s
    s.close()