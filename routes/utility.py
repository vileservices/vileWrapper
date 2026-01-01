from typing import TYPE_CHECKING, List
from ..model import Genius

if TYPE_CHECKING:
    from .. import vileWrapper

class Utility:
    api: "vileWrapper"

    def __init__(self, api: "vileWrapper") -> None:
        self.api: "vileWrapper" = api

    async def screenshot(self, url: str) -> bytes:
        """Take a safe screenshot of a webpage"""
        
        return await self.api.request(
            "POST",
            "/screenshot",
            json={
                'safe': True,
                'url': url
            }
        )
    
    async def collage(self, urls: List[str]) -> bytes:
        """Create a collage from a list of image URLs"""

        return await self.api.request(
            "POST",
            "/collage",
            json={'urls': urls}
        )
    
    async def genius(self, q: str) -> Genius:
        """Get genius lyrics of a song"""

        data = await self.api.request(
            "GET",
            "/genius",
            params={'q': q}
        )

        return Genius(**data)
    