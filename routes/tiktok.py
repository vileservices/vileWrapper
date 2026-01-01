from typing import TYPE_CHECKING
from ..model import TikTokPost, TikTokProfile, TikTokPosts

if TYPE_CHECKING:
    from .. import vileWrapper

class TikTok:
    api: "vileWrapper"

    def __init__(self, api: "vileWrapper") -> None:
        self.api: "vileWrapper" = api

    async def post(self, url: str) -> TikTokPost:
        """Get TikTok post information"""

        data = await self.api.request(
            "GET",
            "/tiktok/post",
            params={'url': url}
        )

        return TikTokPost(**data)

    async def profile(self, username: str) -> TikTokProfile:
        """Get TikTok profile information"""

        data = await self.api.request(
            "GET",
            "/tiktok/profile",
            params={'username': username}
        )

        return TikTokProfile(**data)


    async def posts(self, username: str) -> TikTokPosts:
        """Get TikTok user posts"""

        data = await self.api.request(
            "GET",
            "/tiktok/posts",
            params={'username': username}
        )

        return TikTokPosts(**data)