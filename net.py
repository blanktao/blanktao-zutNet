import requests
import socket


user = "xxx" # 学号
password = "xxx" # 密码
operator = "unicom" # 运营商，电信填telecom，联通填unicom 移动cmcc
ip ="" # 有多张网卡，如虚拟机，请自寻根据ipconfig查看ip地址

def check():
    url = "http://1.1.1.1"
    response = requests.get(url)
    if "COMWebLoginID_0" not in response.text:
        print("已是登录状态！")
        exit()
    else:
        print("未登录")

def get_local_ip():
    # 获取本地IP地址
    hostname = socket.gethostname()
    local_ip = socket.gethostbyname(hostname)
    return local_ip

def login(user, password):
    check()  # Check if already logged in

    global ip
    # 编写代码判断ip是否获取成功
    if not ip:
        ip=get_local_ip()#获取本地IP地址
        if ip:
            print(f"获取ip成功: {ip}")
        else:
            print("获取ip失败")
            exit()
    url = f"http://1.1.1.1:801/eportal/?c=ACSetting&a=Login&protocol=http:&hostname=1.1.1.1&iTermType=1&wlanuserip={ip}&wlanacip=null&wlanacname=null&mac=00-00-00-00-00-00&ip={ip}&enAdvert=0&queryACIP=0&loginMethod=1"
    headers = {
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = {
        "DDDDD": f",0,{user}@{operator}",
        "upass": password,
        "R1": "0",
        "R2": "0",
        "R3": "0",
        "R6": "0",
        "para": "00",
        "0MKKey": "123456",
        "buttonClicked": "",
        "redirect_url": "",
        "err_flag": "",
        "username": "",
        "password": "",
        "user": "",
        "cmd": "",
        "Login": "",
        "v6ip": ""
    }
    response = requests.post(url, headers=headers, data=data)
    if user in response.text:
        print("登录成功!")
    else:
        # 输出错误信息
        print("登录失败，错位信息为:",response.text)


login(user, password)
