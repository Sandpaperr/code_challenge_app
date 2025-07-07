from fastapi import FastAPI, Request, Response
from fastapi.middleware.cors import CORSMiddleware
from clerk_backend_api import Clerk
import os


clerk_SDK = Clerk(bearer_auth=os.getenv("CLERK_SECRET_KEY"))


app = FastAPI()

# Add Middleware
app.add_middleware(
    CORSMiddleware, 
    allow_origins=["*"], 
    allow_credentials=True, 
    allow_methods=["*"], 
    allow_headers=["*"]
    )