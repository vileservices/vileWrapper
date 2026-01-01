from typing import TYPE_CHECKING
from ..model import YouTubeProfile, YouTubeVideo, YouTubeVideo

if TYPE_CHECKING:
    from .. import vileWrapper

class YouTube:
    api: "vileWrapper"

    def __init__(self, api: "vileWrapper") -> None:
        self.api: "vileWrapper" = api

    async def search(self, query: str) -> YouTubeVideo:
        """Search for a YouTube video"""

        data = await self.api.request(
            "GET",
            "/youtube/search",
            params={'q': query}
        )

        return [
            YouTubeVideo(**video) 
            for video in data
        ]

    async def channel(self, argument: str) -> YouTubeProfile:
        """Get YouTube channel information"""

        data = await self.api.request(
            "GET",
            "/youtube/channel",
            params={'argument': argument}
        )

        return YouTubeProfile(**data)
