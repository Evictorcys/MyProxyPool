import time
from multiprocessing import Process
from proxypool.api import app
from proxypool.fetcher import fetcher
from proxypool.tester import Tester
from proxypool.db import RedisClient
from proxypool.config import *


class Scheduler():
    def schedule_tester(self, cycle=TESTER_CYCLE):
        """
        定时测试代理
        """
        tester = Tester()
        while True:
            print('测试器开始运行')
            tester.run()
            time.sleep(cycle)
    
    def schedule_fetcher(self, cycle=FETCHER_CYCLE):
        """
        定时获取代理
        """
        fetcher = fetcher()
        while True:
            print('开始抓取代理')
            fetcher.run()
            time.sleep(cycle)
    
    def schedule_api(self):
        """
        开启API
        """
        app.run(API_HOST, API_PORT)
    
    def run(self):
        print('代理池开始运行')
        
        if TESTER_ENABLED:
            tester_process = Process(target=self.schedule_tester)
            tester_process.start()
        
        if FETCHER_ENABLED:
            fetcher_process = Process(target=self.schedule_fetcher)
            fetcher_process.start()
        
        if API_ENABLED:
            api_process = Process(target=self.schedule_api)
            api_process.start()
