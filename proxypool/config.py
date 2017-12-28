# Redis host address
REDIS_HOST = 'localhost'

# Redis port
REDIS_PORT = 6379

# Redis password,if you don't need,fill 'None'
REDIS_PASSWORD = '628817cai'

REDIS_KEY = 'proxies'

# Proxy score
MAX_SCORE = 100
MIN_SCORE = 
INITIAL_SCORE = 10

# Valid proxy status codes
VALID_STATUS_CODES = [200, 302]

# Pool threshold
POOL_THRESHOLD = 1000

# Check cycle
TESTER_CYCLE = 20
# Fetch cycle
FETCHER_CYCLE = 300

# Test url, normally fill with the url you are about to fetch.
TEST_URL = 'http://www.baidu.com'

# API config
API_HOST = '0.0.0.0'
API_PORT = 5555

# ON_OFF button
TESTER_ENABLED = True
FETCHER_ENABLED = True
API_ENABLED = True

# Test batch size
BATCH_TEST_SIZE = 10
