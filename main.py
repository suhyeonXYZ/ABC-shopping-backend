from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List
import uvicorn

app = FastAPI()

# CORS 
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# TEMP data
products = [
    {
        "id": 1,
        "name": "Smartphone",
        "description": "Latest model smartphone with amazing features",
        "price": 999.99,
        "image_url": "https://ssh-bucket-images.s3.ap-northeast-2.amazonaws.com/smartphone.png"
    },
    {
        "id": 2,
        "name": "Laptop",
        "description": "Powerful laptop for work and gaming",
        "price": 1499.99,
        "image_url": "https://ssh-bucket-images.s3.ap-northeast-2.amazonaws.com/laptop.png"
    },
    {
        "id": 3,
        "name": "Headphones",
        "description": "Noise-cancelling wireless headphones",
        "price": 199.99,
        "image_url": "https://ssh-bucket-images.s3.ap-northeast-2.amazonaws.com/headphone.png"
    }
]

class Product(BaseModel):
    id: int
    name: str
    description: str
    price: float
    image_url: str

@app.get("/")
async def read_root():
    return {"message": "Welcome to the Shopping Mall API"}

@app.get("/api/products", response_model=List[Product])
async def get_products():
    print("Fetching products from API...")
    return products

@app.get("/api/products", response_model=List[Product])
async def get_products():
    print("Fetching products from API...")
    response = JSONResponse(content=products)
    response.headers["Cache-Control"] = "public, max-age=60"
    return response


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True) 
