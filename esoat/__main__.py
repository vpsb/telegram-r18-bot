from esoat import constants
import os

from .telegram import Telegram
from .reddit import util as reddit_utils
from .reddit import Reddit

channel_id = os.environ.get("CHANNEL_ID")
bot = Telegram(os.environ.get("BOT_TOKEN"))
reddit_client = Reddit()


for sub in ("hentai", "animetitties", "ecchi", "pantsu"):
    posts = reddit_client.top(sub)

    for post in (x["data"] for x in posts["data"]["children"]):
        permalink =  constants.REDDIT_URL + post["permalink"]
        if image_url := reddit_utils.find_image(post):
            bot.sendPhoto(channel_id, image_url, permalink)
