from aiohttp import ClientSession
from typing import Literal
from .routes import SoundCloud, Utility, TikTok, Twitter, YouTube

class vileWrapper:
    session: ClientSession
    api_key: str
    soundcloud: SoundCloud
    tiktok: TikTok
    twitter: Twitter
    youtube: YouTube
    utility: Utility
    def __init__(self, api_key: str) -> None:
        self.api_key: str = api_key
        self.session: ClientSession = ClientSession(
            base_url="http://api.vile.bot",
            headers={"Authorization": api_key}
        )
        self.soundcloud = SoundCloud(self)
        self.utility = Utility(self)
        self.tiktok = TikTok(self)
        self.twitter = Twitter(self)
        self.youtube = YouTube(self)
        
    async def request(self, method: Literal["GET", "POST"], endpoint: str, **kwargs):

        async with self.session.request(method, endpoint, **kwargs) as r:
            try:

                if r.content_type.startswith(("image/", "video/", "audio/")):
                    data = await r.read()

                else:
                    data = await r.json()

            except Exception as e:
                raise ValueError(f"Invalid JSON response: {e}") from e

            if isinstance(data, dict) and "detail" in data:
                raise ValueError(data["detail"])

            return data


    async def close(self) -> None:
        await self.session.close()

