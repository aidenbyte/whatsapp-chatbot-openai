from fastapi import APIRouter, HTTPException
from ..models.webhook import WatiMessage
from ..services.wati import WatiService
from ..core.logging import logger

router = APIRouter()
wati_service = WatiService()

@router.post("/webhook/wati")
async def wati_webhook(message: WatiMessage):
    try:
        logger.info(f"Received webhook: {message}")
        
        if message.eventType == "message":
            # Process message and send response if needed
            response = await wati_service.send_message(
                message.waId,
                f"Received your message: {message.text}"
            )
            return {"status": "success", "response": response}
            
        return {"status": "success"}
    except Exception as e:
        logger.error(f"Error processing webhook: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))