import os, re
from os import environ

id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

# Bot information
SESSION = environ.get('SESSION', 'Media_search')
API_ID = int(environ['API_ID'])
API_HASH = environ['API_HASH']
BOT_TOKEN = environ['BOT_TOKEN']
USERBOT_STRING_SESSION = environ.get('USERBOT_STRING_SESSION')
USER_SESSION = environ.get('USER_SESSION', 'User_Bot')



# Bot settings
CACHE_TIME = int(environ.get('CACHE_TIME', 1800))
USE_CAPTION_FILTER = bool(environ.get('USE_CAPTION_FILTER', False))





PICS = (environ.get('PICS', 'https://telegra.ph/file/ea3867e6aab2eab7b8129.jpg https://telegra.ph/file/bc07fcbaeb366ff65d005.jpg https://telegra.ph/file/a317d57287939709fb990.jpg https://telegra.ph/file/7a0bbc5d681a5bfd58398.jpg https://telegra.ph/file/0604448434d2a20317a82.jpg https://telegra.ph/file/9353acbc10ab3a69834d7.jpg https://telegra.ph/file/fcc9ebe22a7a2cc090434.jpg https://telegra.ph/file/9fabb8df3e53a0cd67aa9.jpg https://telegra.ph/file/2de607d22dde277d052ac.jpg https://telegra.ph/file/ebef13d4970e8b3890b8f.jpg https://telegra.ph/file/eb40522f8856591fa4c1b.jpg https://telegra.ph/file/b2179df41ca9c35f3dee3.jpg https://telegra.ph/file/1aff95f3fd9e5b1263243.jpg https://telegra.ph/file/bc0db6afb659a9b81c4ad.jpg https://telegra.ph/file/5c8fc7cc44e099332aef5.jpg https://telegra.ph/file/658e0735ccea58591c412.jpg https://telegra.ph/file/9d83407247aebdfaa4f59.jpg https://telegra.ph/file/75002282e9ed6286be6fb.jpg https://telegra.ph/file/3246e9d9d861eefdbf769.jpg https://telegra.ph/file/1504bf3312d700cd20015.jpg https://telegra.ph/file/f6eab888a8d7ef4f747d1.jpg https://telegra.ph/file/e4fa3d4b1f8153e537f36.jpg https://telegra.ph/file/38e0935ad62053b552b84.jpg https://telegra.ph/file/59e809b023f8b224a5f95.jpg https://telegra.ph/file/55facdc90cface306a235.jpg https://telegra.ph/file/913bcfb38509836c262c2.jpg https://telegra.ph/file/83f27796c4c1093538c01.jpg https://telegra.ph/file/9d76e41a4517f07a3ccdb.jpg https://telegra.ph/file/8ea21e9dd60732669f425.jpg https://telegra.ph/file/32a9934d67bccfa96acf7.jpg https://telegra.ph/file/c1f2a054f9e94a4d4b529.jpg https://telegra.ph/file/3dd504084ccde6da382d5.jpg https://telegra.ph/file/fe50f7642ecd6fe7c96d4.jpg https://telegra.ph/file/2a17e7f1966cc5d691abd.jpg')).split()
PIC = (environ.get('PIC', 'https://telegra.ph/file/7e56d907542396289fee4.jpg https://telegra.ph/file/9aa8dd372f4739fe02d85.jpg https://telegra.ph/file/adffc5ce502f5578e2806.jpg https://telegra.ph/file/6937b60bc2617597b92fd.jpg https://telegra.ph/file/09a7abaab340143f9c7e7.jpg https://telegra.ph/file/5a82c4a59bd04d415af1c.jpg https://telegra.ph/file/323986d3bd9c4c1b3cb26.jpg https://telegra.ph/file/b8a82dcb89fb296f92ca0.jpg https://telegra.ph/file/31adab039a85ed88e22b0.jpg https://telegra.ph/file/c0e0f4c3ed53ac8438f34.jpg https://telegra.ph/file/eede835fb3c37e07c9cee.jpg https://telegra.ph/file/e17d2d068f71a9867d554.jpg https://telegra.ph/file/8fb1ae7d995e8735a7c25.jpg https://telegra.ph/file/8fed19586b4aa019ec215.jpg https://telegra.ph/file/8e6c923abd6139083e1de.jpg https://telegra.ph/file/0049d801d29e83d68b001.jpg')).split()
MALIK_PH = environ.get("MALIK_PH", "https://telegra.ph/file/0547d69b90b596ad6bae1.jpg")
VIDEO_VD = environ.get("VIDEO_VD", "https://telegra.ph/file/566ff238e36d9f2425568.mp4")
PHT = environ.get("PHT", "https://telegra.ph/file/9b77b96a9d2f5dda7764b.jpg")
PHTT = environ.get("PHTT", "https://telegra.ph/file/7dc82878492b8f64bb7eb.jpg")
M_NT_F = environ.get("M_NT_F", "https://telegra.ph/file/b9c8a8240590623ba43ee.jpg")
TUTORIAL = environ.get("M_NT_F", "https://telegra.ph/file/b9c8a8240590623ba43ee.jpg")



#part 1

DEL_SEC = int(os.environ.get("DEL_SEC", "10"))

DEL_SECOND = int(os.environ.get("DEL_SECOND", "300"))
CREATOR_USERNAME = os.environ.get("CREATOR_USERNAME", "sahid_malik")
CREATOR_NAME = os.environ.get("CREATOR_NAME", "sahid malik")
BOT_USERNAME = os.environ.get("BOT_USERNAME", "hjhjvjjjvbot")

#part 2
MALIK = environ.get("malik", "https://telegra.ph/file/a35a995c9c411048adfab.jpg")
MALIK5 = environ.get("malik5", "https://telegra.ph/file/a00c405a374d21ea7cfb7.jpg")


AUTO_DELETE = is_enabled((environ.get('AUTO_DELETE', "True")), True)
AUTO_DELETE2 = is_enabled((environ.get('AUTO_DELETE2', "True")), True)

#part 3

FILTER_BUTTONS = os.environ.get("FILTER_BUTTONS", "10")
DB_AUTO_DELETE = is_enabled((environ.get('DB_AUTO_DELETE', "True")), True)
AUTO_FFILTER = is_enabled((environ.get('AUTO_FFILTER', "True")), True)

REQ_GRP = [int(req_grp) if id_pattern.search(req_grp) else req_grp for req_grp in environ.get('REQ_GRP', '0').split()]

REQ_GRPOUP = int(environ.get('REQ_GRPOUP'))

# Admins, Channels & Users
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '').split()]
CHANNELS = [int(ch) if id_pattern.search(ch) else ch for ch in environ.get('CHANNELS', '0').split()]
auth_users = [int(user) if id_pattern.search(user) else user for user in environ.get('AUTH_USERS', '').split()]
AUTH_USERS = (auth_users + ADMINS) if auth_users else []
auth_channel = environ.get('AUTH_CHANNEL')
auth_grp = environ.get('AUTH_GROUP')
AUTH_CHANNEL = int(auth_channel) if auth_channel and id_pattern.search(auth_channel) else None
AUTH_GROUPS = [int(ch) for ch in auth_grp.split()] if auth_grp else None

# MongoDB information
DATABASE_URI = environ.get('DATABASE_URI', "")
DATABASE_NAME = environ.get('DATABASE_NAME', "Rajappan")
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'Telegram_files')

# Others
LOG_CHANNEL2 = int(environ.get('LOG_CHANNEL2', 0))
LOG_CHANNEL = int(environ.get('LOG_CHANNEL', 0))
SUPPORT_CHAT = environ.get('SUPPORT_CHAT', 'm_house786')
P_TTI_SHOW_OFF = is_enabled((environ.get('P_TTI_SHOW_OFF', "False")), False)
IMDB = is_enabled((environ.get('IMDB', "False")), False)
SINGLE_BUTTON = is_enabled((environ.get('SINGLE_BUTTON', "False")), False)
CUSTOM_FILE_CAPTION = environ.get("CUSTOM_FILE_CAPTION", None)
BATCH_FILE_CAPTION = environ.get("BATCH_FILE_CAPTION", CUSTOM_FILE_CAPTION)
IMDB_TEMPLATE = environ.get("IMDB_TEMPLATE", None) #<b>🏷 Title: <a href={url}>{title}</a>\n🎭 Genres: {genres}\n📆 Year: <a href={url}/releaseinfo>{year}</a>")
LONG_IMDB_DESCRIPTION = is_enabled(environ.get("LONG_IMDB_DESCRIPTION", "False"), False)
SPELL_CHECK_REPLY = is_enabled(environ.get("SPELL_CHECK_REPLY", "True"), True)
MAX_LIST_ELM = environ.get("MAX_LIST_ELM", None)
INDEX_REQ_CHANNEL = int(environ.get('INDEX_REQ_CHANNEL', LOG_CHANNEL))
FILE_STORE_CHANNEL = [int(ch) for ch in (environ.get('FILE_STORE_CHANNEL', '')).split()]
MELCOW_NEW_USERS = is_enabled((environ.get('MELCOW_NEW_USERS', "True")), True)
PROTECT_CONTENT = is_enabled((environ.get('PROTECT_CONTENT', "False")), False)
PUBLIC_FILE_STORE = is_enabled((environ.get('PUBLIC_FILE_STORE', "True")), True)

SHORTENER_API = environ.get("SHORTENER_API", "iQ2iqO9EXFbcjek412Dg5j6stWu2")
SHORTENER_WEBSITE = environ.get("SHORTENER_WEBSITE", "shareus.in")
SHORT_URL = is_enabled((environ.get('SHORT_URL', "True")), True)
TUTORIAL_LINK = environ.get("TUTORIAL_LINK", "https://youtu.be/MKNd7AP5xLE")



LOG_STR = "Current Cusomized Configurations are:-\n"
LOG_STR += ("IMDB Results are enabled, Bot will be showing imdb details for you queries.\n" if IMDB else "IMBD Results are disabled.\n")
LOG_STR += ("P_TTI_SHOW_OFF found , Users will be redirected to send /start to Bot PM instead of sending file file directly\n" if P_TTI_SHOW_OFF else "P_TTI_SHOW_OFF is disabled files will be send in PM, instead of sending start.\n")
LOG_STR += ("SINGLE_BUTTON is Found, filename and files size will be shown in a single button instead of two separate buttons\n" if SINGLE_BUTTON else "SINGLE_BUTTON is disabled , filename and file_sixe will be shown as different buttons\n")
LOG_STR += (f"CUSTOM_FILE_CAPTION enabled with value {CUSTOM_FILE_CAPTION}, your files will be send along with this customized caption.\n" if CUSTOM_FILE_CAPTION else "No CUSTOM_FILE_CAPTION Found, Default captions of file will be used.\n")
LOG_STR += ("Long IMDB storyline enabled." if LONG_IMDB_DESCRIPTION else "LONG_IMDB_DESCRIPTION is disabled , Plot will be shorter.\n")
LOG_STR += ("Spell Check Mode Is Enabled, bot will be suggesting related movies if movie not found\n" if SPELL_CHECK_REPLY else "SPELL_CHECK_REPLY Mode disabled\n")
LOG_STR += (f"MAX_LIST_ELM Found, long list will be shortened to first {MAX_LIST_ELM} elements\n" if MAX_LIST_ELM else "Full List of casts and crew will be shown in imdb template, restrict them by adding a value to MAX_LIST_ELM\n")
LOG_STR += f"Your current IMDB template is {IMDB_TEMPLATE}"

DELL_SEC = int(os.environ.get("DELL_SECOND", "60"))
DELL_SECOND = int(os.environ.get("DELL_SECOND", "60"))

MBGH = """Hay {}.\n\n {} results are already available for your query"""
MAINTENANCE_MODE = is_enabled((environ.get('MAINTENANCE_MODE', "False")), False)
PM_MAINTENANCE_MODE = is_enabled((environ.get('PM_MAINTENANCE_MODE', "False")), False)



SHORT_URLL = is_enabled((environ.get('SHORT_URLL', "False")), False)
SHORTENER_API2 = environ.get("SHORTENER_API", None)
LONG_MEGHA_URL = environ.get("LONG_MEGHA_URL", False)


