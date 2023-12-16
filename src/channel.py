import os
import json
from googleapiclient.discovery import build


class Channel:
    """Класс для ютуб-канала"""

    api_key: str = os.getenv('YouTube_API_KEY')

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""

        self.channel_id = channel_id

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        channel = Channel.get_service().channels().list(id=self.channel_id, part='snippet,statistics').execute()
        info_channel_print = json.dumps(channel, indent=2, ensure_ascii=False)
        print(info_channel_print)

    @classmethod
    def get_service(cls):
        """Возвращает объект для работы с YouTube API"""
        #api_key: str = os.getenv('YT_API_KEY')
        youtube = build('youtube', 'v3', developerKey=cls.api_key)
        return youtube

