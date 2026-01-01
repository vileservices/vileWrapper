from typing import TYPE_CHECKING
from ..model import SoundCloudTrack, SoundCloudProfile, SoundCloudTracks

if TYPE_CHECKING:
    from .. import vileWrapper

class SoundCloud:
    api: "vileWrapper"

    def __init__(self, api: "vileWrapper") -> None:
        self.api: "vileWrapper" = api

    async def track(self, url: str) -> SoundCloudTrack:
        """Get SoundCloud track information"""

        data = await self.api.request(
            "GET",
            "/soundcloud/track",
            params={'url': url}
        )

        return SoundCloudTrack(**data)

    async def profile(self, username: str) -> SoundCloudProfile:
        """Get SoundCloud profile information"""

        data = await self.api.request(
            "GET",
            "/soundcloud/profile",
            params={'username': username}
        )

        return SoundCloudProfile(**data)

    async def tracks(self, username: str) -> SoundCloudTracks:
        """Get SoundCloud tracks from a profile"""

        data = await self.api.request(
            "GET",
            "/soundcloud/tracks",
            params={'username': username}
        )

        return SoundCloudTracks(**data)