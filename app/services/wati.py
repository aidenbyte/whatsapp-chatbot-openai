from httpx import AsyncClient
from ..core.config import settings
from ..core.logging import logger

class WatiService:
    def __init__(self):
        self.base_url = settings.WATI_API_URL
        self.headers = {
            "Authorization": f"Bearer {settings.WATI_API_KEY}",
            "Content-Type": "application/json"
        }

    async def send_message(self, whatsapp_number: str, message: str):
        async with AsyncClient() as client:
            try:
                response = await client.post(
                    f"{self.base_url}/api/v1/sendSessionMessage/{whatsapp_number}",
                    headers=self.headers,
                    params={"messageText": message}
                )
                response.raise_for_status()
                return response.json()
            except Exception as e:
                logger.error(f"Error sending message: {str(e)}")
                raise