from __future__ import annotations

from typing import List, Optional, Union
from pydantic import BaseModel as BaseBaseModel, Field, ConfigDict
from datetime import datetime

class BaseModel(BaseBaseModel):
    class Config:
        exclude_none = True

class AvatarRecord(BaseModel):
    asset: str = Field(..., title="Avatar URL", description="URL of the avatar image")
    timestamp: str = Field(..., title="Timestamp", description="Time when the avatar was recorded")


class AvatarHistoryResponse(BaseModel):
    avatar_url: str = Field(..., title="Latest Avatar URL", description="URL of the most recent avatar")
    records: List[AvatarRecord] = Field(..., title="Avatar Records", description="List of all avatar changes")

class GeniusArtist(BaseModel):
    url: str
    name: str


class Genius(BaseModel):
    model_config = ConfigDict(coerce_numbers_to_str=True)
    url: str
    title: str
    artist: GeniusArtist
    thumbnail: str
    producers: Optional[List[str]]
    lyrics: str


class SoundCloudStatistics(BaseModel):
    followers: int = Field(..., title="Followers Count")
    following: int = Field(..., title="Following Count")
    tracks: int = Field(..., title="Tracks Count")
    playlists: int = Field(..., title="Playlists Count")
    likes: int = Field(..., title="Likes Count")

class SoundCloudProfile(BaseModel):
    id: int = Field(..., title="Profile ID")
    username: str = Field(..., title="Username")
    permalink: str = Field(..., title="Profile Permalink")
    url: str = Field(..., title="Profile URL")
    avatar: Optional[str] = Field(None, title="Avatar URL")
    country: Optional[str] = Field(None, title="Country")
    city: Optional[str] = Field(None, title="City")
    first_name: Optional[str] = Field(None, title="First Name")
    last_name: Optional[str] = Field(None, title="Last Name")
    full_name: Optional[str] = Field(None, title="Full Name")
    created_at: datetime = Field(..., title="Creation Timestamp")
    verified: bool = Field(..., title="Verified Account")
    statistics: SoundCloudStatistics = Field(..., title="Profile Statistics")
    description: Optional[str] = Field(None, title="Profile Description")

class MediaUpload(BaseModel):
    bitRate: int = Field(..., title="Bit Rate")
    codec: str = Field(..., title="Codec")
    sampleRate: int = Field(..., title="Sample Rate")

class SoundCloudTrack(BaseModel):
    id: int = Field(..., title="Track ID")
    kind: str = Field(..., title="Track Type")
    title: str = Field(..., title="Track Title")
    cover: Optional[str] = Field(None, title="Track Cover URL")
    created_at: datetime = Field(..., title="Creation Timestamp")
    url: str = Field(..., title="Track URL")
    likes: int = Field(..., title="Likes Count")
    plays: int = Field(..., title="Playback Count")
    description: Optional[str] = Field(None, title="Track Description") 

class SoundCloudTracks(BaseModel):
    artist: SoundCloudProfile = Field(..., title="Artist Profile")
    tracks: List[SoundCloudTrack] = Field(..., title="List of Tracks")

class TikTokStatistics(BaseModel):
    followers: int = Field(..., title="Followers Count")
    following: int = Field(..., title="Following Count")
    likes: int = Field(..., title="Likes Count")
    videos: int = Field(..., title="Videos Count")

class TikTokVideoStatistics(BaseModel):
    comments: int = Field(..., title="Comments Count")
    shares: int = Field(..., title="Shares Count")
    likes: int = Field(..., title="Likes Count")

class TikTokMedia(BaseModel):
    url: str = Field(..., title="Media URL")
    type: Optional[str] = Field(None, title="Media Type")

class TikTokMusic(BaseModel):
    id: int = Field(..., title="Music ID")
    title: str = Field(..., title="Music Title")
    author: str = Field(..., title="Music Author")
    cover: str = Field(..., title="Music Cover URL")

class TikTokPost(BaseModel):
    description: Optional[str] = Field(None, title="Post Description")
    id: str = Field(..., title="Post ID")
    url: str = Field(..., title="Post URL")
    created_at: datetime = Field(..., title="Creation Timestamp")
    music: Optional[TikTokMusic] = Field(None, title="Attached Music")
    statistics: TikTokVideoStatistics = Field(..., title="Post Statistics")
    media: Union[TikTokMedia, List[TikTokMedia]] = Field(..., title="Media Items")

class TikTokPosts(BaseModel):
    user: "TikTokProfile" = Field(..., title="User Profile")
    posts: List[TikTokPost] = Field(..., title="List of Posts")

class TikTokProfile(BaseModel):
    id: int = Field(..., title="Profile ID")
    secUid: str = Field(..., title="Secure UID")
    username: str = Field(..., title="Username")
    display_name: Optional[str] = Field(None, title="Display Name")
    avatar: Optional[str] = Field(None, title="Avatar URL")
    description: Optional[str] = Field(None, title="Profile Description")
    created_at: datetime = Field(..., title="Creation Timestamp")
    verified: bool = Field(..., title="Verified Account")
    private: bool = Field(..., title="Private Account")
    statistics: TikTokStatistics = Field(..., title="Profile Statistics")

class TwitterStatistics(BaseModel):
    followers: int = Field(0, title="Followers Count")
    following: int = Field(0, title="Following Count")
    posts: int = Field(0, title="Posts Count")

class TwitterLink(BaseModel):
    title: Optional[str] = Field(None, title="Link Title")
    url: str = Field(..., title="Link URL")

class TwitterProfile(BaseModel):
    url: str = Field(..., title="Profile URL")
    id: str = Field(..., title="Profile ID")
    protected: bool = Field(False, title="Protected Account")
    verified: bool = Field(False, title="Verified Account")
    created_at: datetime = Field(..., title="Creation Timestamp")
    display_name: Optional[str] = Field(None, title="Display Name")
    username: str = Field(..., title="Username")
    biography: Optional[str] = Field(None, title="Profile Biography")
    avatar: Optional[str] = Field(None, title="Avatar URL")
    banner: Optional[str] = Field(None, title="Banner URL")
    links: Optional[Union[TwitterLink, List[TwitterLink]]] = Field(None, title="Profile Links")
    statistics: TwitterStatistics = Field(..., title="Profile Statistics")

class TwitterMedia(BaseModel):
    url: str = Field(..., title="Media URL")
    type: str = Field(..., title="Media Type")

class Tweet(BaseModel):
    id: str = Field(..., title="Tweet ID")
    url: str = Field(..., title="Tweet URL")
    text: Optional[str] = Field(None, title="Tweet Text")
    author: TwitterProfile = Field(..., title="Tweet Author")
    replies: int = Field(..., title="Replies Count")
    retweets: int = Field(..., title="Retweets Count")
    likes: int = Field(..., title="Likes Count")
    bookmarks: int = Field(..., title="Bookmarks Count")
    created_at: datetime = Field(..., title="Creation Timestamp")
    media: Optional[List[TwitterMedia]] = Field(None, title="Media Items")
    possibly_sensitive: bool = Field(False, title="Possibly Sensitive")
    source: Optional[str] = Field(None, title="Tweet Source")
    lang: Optional[str] = Field(None, title="Language Code")

class YouTubeProfile(BaseModel):
    id: str = Field(..., title="Profile ID")
    created_at: str = Field(..., title="Creation Timestamp")
    username: str = Field(..., title="Username")
    description: Optional[str] = Field(None, title="Profile Description")
    avatar: str = Field(..., title="Avatar URL")

class YouTubeVideo(BaseModel):
    id: str = Field(..., title="Video ID")
    created_at: datetime = Field(..., title="Creation Timestamp")
    title: str = Field(..., title="Video Title")
    description: Optional[str] = Field(None, title="Video Description")
    thumbnail: str = Field(..., title="Thumbnail URL")
    author: YouTubeProfile = Field(..., title="Video Author")
    url: str = Field(..., title="Video URL")
