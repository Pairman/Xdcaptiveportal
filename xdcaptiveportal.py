'''
# 西安电子科技大学校园网登录工具

# 作者

[Pairman](https://github.com/Pairman)

# 免责信息

本程序仅供学习交流使用，使用本程序造成的任何后果由用户自行负责。

# 依赖

```Python>=3``` , ```requests```

# 用法

```
用法：
    python3 xddailyup.py [参数]
参数：
    -h,--help                   输出帮助信息
    -u,--username <学号>        指定学号
    -p,--password <密码>        指定密码
    -d,--debug                  进入调试模式
```

# 致谢

[使用Github Action自动填写疫情通](https://cnblogs.com/soowin/p/13461451.html)

[西安电子科技大学疫情通、晨午晚检自动上报工具](https://github.com/jiang-du/Auto-dailyup)

[西安电子科技大学(包含广州研究院)晨午晚检自动上报工具](https://github.com/HANYIIK/Auto-dailyup)

[西安电子科技大学晨午晚检自动上报工具](https://github.com/cunzao/ncov)

# 开源协议

GNU General Public License v3.0 (gpl-3.0)
'''

from getopt import getopt
from requests import Session
from sys import argv

opts=getopt(argv[1:],"hu:p:d",["help","username=","password=","debug"])[0]

USERNAME,PASSWORD,DEBUG="","",False

helpMsg="""Xdcaptiveportal - 西安电子科技大学校园网登录工具 1.0 (2022 Nov 7, Pairman)
本程序仅供学习交流使用，使用本程序造成的任何后果由用户自行负责。
用法：
    python3 %s [参数]
参数：
    -h,--help                   输出帮助信息
    -u,--username <学号>        指定学号
    -p,--password <密码>        指定密码
    -d,--debug                  进入调试模式
"""%(argv[0])

if len(argv)==1:
    print(helpMsg)
    exit()

for opt,arg in opts:
    if opt in ("-h","--help"):
        print(helpMsg)
        exit()
    if opt in ("-u","--username"):
        USERNAME=arg
    if opt in ("-p","--password"):
        PASSWORD=arg
    if opt in ("-d","--debug"):
        DEBUG=1

print("本程序仅供学习交流使用，使用本程序造成的任何后果由用户自行负责。")

if USERNAME=="":
    print("请指定学号！")
    exit()
if PASSWORD=="":
    print("请指定密码！")
    exit()

currentUploadMsg={
    "action":"login",
    "ac_id":"8",
    "user_ip":"",
    "nas_ip":"",
    "user_mac":"",
    "url":"",
    "username":USERNAME,
    "password":PASSWORD,
    "save_me":"1"
}

conn=Session()
logined=False
for i in range(3):
    result=None
    try :
        result=conn.post(url="https://w.xidian.edu.cn/srun_portal_pc.php",data=currentUploadMsg,verify=not DEBUG)
        # if result.json()['e']==0:
        if result.status_code==200:
            logined=True
            print("登录成功")
            break
        print("登录失败：",result.status_code)
    except:
        print("登录失败：异常")
if not logined:
    print("登录失败，正在退出")
    exit()