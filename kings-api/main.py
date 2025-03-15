from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from typing import Dict

# run the application with 'uvicorn main:app --reload'
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # 👈 Allow frontend requests
    allow_credentials=True,
    allow_methods=["*"],  # 👈 Allow all HTTP methods (GET, POST, etc.)
    allow_headers=["*"],  # 👈 Allow all headers
)

kings = {
    "name": "King David",
    "reign": "1010–970 BC",
    "nation": "Unified Kingdom",
    "children": [
        {
            "name": "King Solomon",
            "reign": "970–931 BC",
            "nation": "Unified Kingdom",
            "children": [
                {
                    "name": "Rehoboam",
                    "reign": "931–913 BC",
                    "nation": "Judah",
                    "children": []
                },
                {
                    "name": "Jeroboam I",
                    "reign": "931–910 BC",
                    "nation": "Israel",
                    "children": []
                }
            ]
        }
    ]
}

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/kings")
async def get_kings() -> Dict:
    return kings
