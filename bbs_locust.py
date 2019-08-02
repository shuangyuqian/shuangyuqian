# coding=utf-8
import requests
from locust import HttpLocust,TaskSet,task
from requests.packages.urllib3.exceptions import InsecureRequestWarning
import os
from random import randint
# 禁用安全请求警告
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

class bbs(TaskSet):
    # 访问bbs论坛首页
    @task(1)
    def open_ixdex(self):
        # 定义请求头
        header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36"}

        req = self.client.get("/bbs/forum.php",  headers=header, verify=False)
        if req.status_code == 200:
            print("success")
        else:
            print("fails")

class UserBehavior(TaskSet):   
    def on_start(self):
        self.login()

    # 随机返回登录用户
    def login_user():
        users = {"admin":admin,"shuang":123456,"syq1997":123456}
        data = randint(1, 3)
        username = "user"+str(data)
        password = users[username]
        return username, password

    @task(2)
    def login(self):
        username, password = login_user()
        self.client.post("/bbs/member.php?mod=logging&action=login&loginsubmit=yes&infloat=yes&lssubmit=yes&inajax=1", {"username":username, "password":password})
        if req.status_code == 200:
            print("login success")
        else:
            print("login fails")

class User(HttpLocust):
    host = "http://49.234.156.107"
    task_set = bbs
    task_set = UserBehavior
    min_wait = 3000  # 单位为毫秒
    max_wait = 6000  # 单位为毫秒

if __name__ == "__main__":
    os.system("locust -f C:\\Users\\Administrator\\Desktop\\bbs_locust.py ")