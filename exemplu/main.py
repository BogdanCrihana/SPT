from fastapi import FastAPI
from app import mqtt_client

app = FastAPI()

@app.get("/")
async def get_sensor_data():
    return mqtt_client.get_sensor_data()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
