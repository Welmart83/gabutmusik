from dotenv import load_dotenv
from os import path, getenv, mkdir


if path.exists("local.env"):
    load_dotenv("local.env")
else:
    load_dotenv()

if not path.exists("search"):
    mkdir("search")


class Configs:
    API_ID = 15638315
    API_HASH = 1ab900848c1e5f3529f79f729e88b621
    BOT_TOKEN = 5245012700:AAFvOT_XmlL6n75rQb8aE0b04FwNt46sqbI
    OWNER_ID = 1992156749
    SESSION = BQC3rIM0sBvLsR1_afGxY26i8OHUmgH3blZBcZaOO-6KlCtdJN_YgkGrgNGY6cSiPFTqlmi3kJpJqp3LsfT0wukQe_0U1c8VBHJiVZUHjB7f2NosuFSGuUZDwJzEEJYMKgvwxEiMAQKy-4UMG9ZpKgLBrQoUCt3L1HJkRBMSEzpbMIthbAnBfTmRN8SujNniqnOV0bbiRnAmh5GG1NHlqExNO1AOYzhTxTRJfG_mKGvKXZdQdaIOYbAQgHNIvH1mO6S_2MrVC_w9VwxtaewxRDDvdzrm2kf_LQld4H7hiu5EEFKw7kBSlkbls4YF-zHPGeid8suCGaw3krcd5acrOsxhfKUcwQA
    CHANNEL_LINK = https://t.me/channel_bangjajo
    GROUP_LINK = https://t.me/ampun_jago
    UPSTREAM_REPO = https://github.com/Kayzyu/EnakeunMusic
    AUTO_LEAVE = 1800


config = Configs()
