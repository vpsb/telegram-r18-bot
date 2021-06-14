from __future__ import annotations
from typing import Union
import requests

from .message import Message
from .. import constants



class Telegram:
    def __init__(self, bot_token: str) -> None:
        self.bot_token = bot_token
        self._http = requests.Session()

    def _method_url(self, method: str):
        return f"{constants.TELEGRAM_API_URL}/bot{self.bot_token}/{method}"

    def sendMessage(self, chat_id, text: str):
        url = self._method_url("sendMessage")
        data = {
            "chat_id": chat_id,
            "text": text
        }
        resp = self._http.post(url, data=data)
        return Message(**resp.json())
    
    def sendPhoto(self, chat_id, photo: Union[str, bytes], caption: str = None):
        url = self._method_url("sendPhoto")
        data = {
            "chat_id": chat_id,
            "caption": caption
        }
        files = {}

        if isinstance(photo, str):
            data["photo"] = photo
        else:
            files["photo"] = photo
        
        resp = self._http.post(url, data=data, files=files)
        return Message(**resp.json())