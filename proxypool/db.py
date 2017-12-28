import redis
from proxypool.error import PoolEmptyError
from proxypool.config import REDIS_HOST,REDIS_PORT,REDIS_PASSWORD,REDIS_KEY
from proxypool.config import MAX_SCORE,MIN_SCORE,INITIAL_SCORE
from random import choice
import re

class RedisClient(object):
	def __init__(self,host = REDIS_HOST,port = REDIS_PORT,password = REDIS_PASSWORD):
		self.db = redis.StrictRedis(host = host,port = port,password =password,decode_response = True)

	def add(self,proxy,score = INITIAL_SCORE):
		if not re.match('\d+\.\d+\.\d+\.\d+\:\d+',proxy):
			print("Proxy Formal Error! ",proxy)
			return
		if not self.db.zscore(REDIS_KEY,proxy):
			return self.db.zadd(REDIS_KEY,score,proxy)

	def random(self):
		result = self.db.zrangebyscore(REDIS_KEY,MAX_SCORE,MAX_SCORE)
		if len(result):
			return choice(result)
		else:
			result = self.db.zrevrange(REDIS_KEY,0,100)
			if len(result):
				return choice(result)
			else:
				raise PoolEmptyError

	def dec_socre(self,proxy):
		score =  self.db.zscore(REDIS_KEY,proxy)
		if score and score > MIN_SCORE:
			return self.db.zincrby(REDIS_KEY,proxy,-1)
		else:
			return self.db.zrem(REDIS_KEY,proxy)

	def isexit(self,proxy):
		return not self.db.zscore(REDIS_KEY,proxy) == None

	def set_max_score(self,proxy):
		return self.db.zadd(REDIS_KEY,MAX_SCORE,proxy)

	def count(self):
		return self.db.zcard(REDIS_KEY)

	def get_all(self):
		return self.db.zrangebyscore(REDIS_KEY.MIN_SCORE,MAX_SCORE)

	def get_batch(self,start,stop):
		return self.db.zrevrange(REDIS_KEY,start,stop - 1)

if __name__ == "__main__":
	conn = RedisClient()
	result  = conn.get_batch(200,210)
	print(result)