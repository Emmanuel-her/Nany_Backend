from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
from app.api.bookings import router as bookings_router
from app.api.nannies import router as nannies_router
from app.core.database import client
from app.core.firebase import init_firebase

load_dotenv()

app = FastAPI(title="NannyGo! Api")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(bookings_router)
app.include_router(nannies_router)

@app.on_event("startup")
async def startup_event():
    init_firebase()

@app.on_event("shutdown")
async def shutdown_db_client():
    client.close()
