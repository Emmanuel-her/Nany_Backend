from fastapi import FastAPI
from app.api.bookings import router as bookings_router
from app.core.database import client

app = FastAPI(title="NannyGo! Api")

app.include_router(bookings_router)

@app.on_event("shutdown")
async def shutdown_db_client():
    client.close()
