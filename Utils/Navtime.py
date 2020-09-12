import requests
from datetime import datetime
from time import time

class NavTime:
    def __init__(self):
        self.globalTime=int(requests.get("http://worldtimeapi.org/api/timezone/Asia/Kolkata").json()["unixtime"])
        self.time=int(time())
        self.diff=self.globalTime-self.time


