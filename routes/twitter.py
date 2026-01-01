from typing import TYPE_CHECKING
from ..model import Tweet, TwitterProfile

if TYPE_CHECKING:
    from .. import vileWrapper

class Twitter:
    api: "vileWrapper"

    def __init__(self, api: "vileWrapper") -> None:
        self.api: "vileWrapper" = api

    async def tweet(self, url: str) -> Tweet:
        """Get Twitter tweet information"""

        data = await self.api.request(
            "GET",
            "/twitter/tweet",
            params={'url': url}
        )

        return Tweet(**data)

    async def profile(self, username: str) -> TwitterProfile:
        """Get Twitter profile information"""

        data = await self.api.request(
            "GET",
            "/twitter/profile",
            params={'username': username}
        )

        return TwitterProfile(**data)
