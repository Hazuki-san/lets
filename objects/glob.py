from collections import defaultdict

import personalBestCache
import userStatsCache
from common.files import fileBuffer, fileLocks
import helpers.s3
import helpers.threadScope
from helpers.aqlHelper import AqlThresholds

try:
	with open("version") as f:
		VERSION = f.read().strip()
except:
	VERSION = "Unknown"
ACHIEVEMENTS_VERSION = 1

DATADOG_PREFIX = "lets"
db = None
redis = None
conf = None
application = None
pool = None
pascoa = {}
s3Connections = defaultdict(helpers.s3.clientFactory)
threadScope = helpers.threadScope.ThreadScope()


# Cache and objects
fLocks = fileLocks.fileLocks()
userStatsCache = userStatsCache.userStatsCache()
personalBestCache = personalBestCache.personalBestCache()
fileBuffers = fileBuffer.buffersList()
# dog = datadogClient.datadogClient()
dog = None
achievementClasses = {}
aqlThresholds = AqlThresholds()
serverPort = None
