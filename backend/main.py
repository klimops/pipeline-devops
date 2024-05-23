from fastapi import FastAPI
import uvicorn
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title='API')
app.add_middleware(
    CORSMiddleware,
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
    allow_origins=["http://localhost", "http://localhost:3000"]
)

@app.get("/get_data")
async def hello_world():
    return {"message": "Acessando pelo frontend"}

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)
