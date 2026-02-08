# devgagan
# Note if you are trying to deploy on vps then directly fill values in ("")

from os import getenv

# VPS --- FILL COOKIES 🍪 in """ ... """ 

INST_COOKIES = """
# wtite up here insta cookies
"""

YTUB_COOKIES = """
# write here yt cookies
"""

API_ID = int(getenv("API_ID", "39944863"))
API_HASH = getenv("API_HASH", "a3924ff17fa817dd7ed78c3f50020085")
BOT_TOKEN = getenv("BOT_TOKEN", "8168100377:AAG1X2l9anpR1F_7tM62Ldd7Xw7f6Gg0pQ0")
OWNER_ID = list(map(int, getenv("OWNER_ID", "8514968568").split()))
MONGO_DB = getenv(
    "MONGO_DB",
    "mongodb+srv://sodom53905_db_user:77q9BcjDVXdOP4ib@cluster0.xj3ki6m.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
)
LOG_GROUP = getenv("LOG_GROUP", "-1003814466915")
CHANNEL_ID = int(getenv("CHANNEL_ID", "-1003814466915"))
FREEMIUM_LIMIT = int(getenv("FREEMIUM_LIMIT", "0"))
PREMIUM_LIMIT = int(getenv("PREMIUM_LIMIT", "9999"))
WEBSITE_URL = getenv("WEBSITE_URL", "upshrink.com")
AD_API = getenv("AD_API", "52b4a2cf4687d81e7d3f8f2b7bc2943f618e78cb")
STRING = getenv("STRING", None)
YT_COOKIES = getenv("YT_COOKIES", YTUB_COOKIES)
DEFAULT_SESSION = getenv("DEFAUL_SESSION", None)  # added old method of invite link joining
INSTA_COOKIES = getenv("INSTA_COOKIES", INST_COOKIES)
