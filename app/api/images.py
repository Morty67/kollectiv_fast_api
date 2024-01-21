import io

from PIL import Image
from fastapi import APIRouter, File, UploadFile, HTTPException, Form
from fastapi.responses import StreamingResponse

from tasks import send_email_message

router = APIRouter()


@router.post("/optimize-image/")
async def optimize_image(
    file: UploadFile = File(...),
    quality: int = 50,
    email: str = Form(...),
):
    try:
        image = Image.open(io.BytesIO(await file.read()))
        optimized_image = image.copy()

        # Store the optimized image in bytes
        output = io.BytesIO()
        optimized_image.save(output, format="JPEG", quality=quality)
        output.seek(0)

        # Calling selery to send an email with an optimized image
        send_email_message.delay(output.read(), email)

        # Returning the optimized image to the client
        return StreamingResponse(io.BytesIO(output.read()), media_type="image/jpeg")

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

