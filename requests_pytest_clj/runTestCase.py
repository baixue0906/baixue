import pytest
from datetime import datetime




def main():
    # 执行用例
    CURRENT_TIME = datetime.now().strftime('%H_%M_%S')
    print(CURRENT_TIME)
    HTML_NAME = 'testReport_%s.html'%(CURRENT_TIME)
    args = ['--reruns', '1', '--html=' + './report/' + HTML_NAME]
    pytest.main(args)

if __name__ == '__main__':
    main()

