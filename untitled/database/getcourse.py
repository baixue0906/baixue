from database.dbutils import dbutils
from utils.commonutlis import strtolist


def comparecourse(package_guid,userid,active_code):
    #获取P 课程
    dbhandle = dbutils()
    packagesaleinfo=dbhandle.selectPackageContainsSale(package_guid)
    print(package_guid+" 包含的s课："+packagesaleinfo[0][2])
    list=strtolist(packagesaleinfo[0][2])
    #大P课里包含s课
    # plist=[]
    # for i in list:
    #     salesinfo=dbhandle.selectSaleCourse(i)
    #     plist.append(salesinfo[0])
    # print("P中包含的课：")
    # print(plist)

    #获取购买课程
    buylist=[]
    buy_course=dbhandle.selectPaidCourse(userid,active_code)

    buylist2=[]
    for s in buy_course:
        buylist2.append(s[0])
        salesinfo=dbhandle.selectSaleCourse(s[0])
        buylist.append(salesinfo[0])

    print("购买课程有：")
    print(buylist)


    #list中有，buylist2中没有的
    a = set(list).difference(set(buylist2))
    #差集P中有的，购买课中没有
    print("差集P中有的，购买课中没有：")
    print(a)

    plist=[]
    for i in a:
        salesinfo=dbhandle.selectSaleCourse(i)
        plist.append(salesinfo[0])
    print("差集P中有的，购买课中没有具体课程：")
    print(plist)

    dbhandle.close()



comparecourse("P57804","33399496","E202008051103500511669604")