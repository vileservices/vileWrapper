# Introduction

<Note>
  Welcome to the vile API wrapper!  

  - To use this API, you need a valid **API key**, which can be obtained by contacting the developers.
  - This is a **paid API** with a base price of **$8/month**.
  - For support or questions, you can reach out to the developers directly.
</Note>

## Usage Example

```python
from vileWrapper import vileWrapper as Client

client = Client("API_KEY")

async def avatar(username: str)
    data = await client.tiktok.profile(username)
    return data.avatar

```
