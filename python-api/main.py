from fastapi import FastAPI, Request

import datetime, os, databases

app = FastAPI()

database = databases.Database(f"postgres://{os.environ['POSTGRES_USER']}:{os.environ['POSTGRES_PASSWORD']}@{os.environ['POSTGRES_HOST']}/{os.environ['POSTGRES_DB']}")

@app.on_event("startup")
async def startup_event():
    await database.connect()

@app.on_event("shutdown")
async def shutdown_event():
    await database.disconnect()


@app.post("/")
async def getInformation(request: Request, id: str, timestamp: int, lat: float, lon: float, speed: int, bearing: int, altitude: float, accuracy: int, batt: int):
    values = {}
    forwarded_ip = request.headers['x-forwarded-for']
    real_ip = request.headers['x-real-ip']

    query = '''INSERT INTO gps_data
        (
        device_id,
        sensor_timestamp,
        latitude,
        longitude,
        speed,
        bearing,
        altitude,
        accuracy,
        battery,
        forwarded_ip,
        real_ip
        )
        VALUES
        (:id,
        :timestamp,
        :lat,
        :lon,
        :speed,
        :bearing,
        :altitude,
        :accuracy,
        :batt,
        :forwarded_ip,
        :real_ip
        )
        '''
        
    values['id'] = id
    values['timestamp'] = datetime.datetime.fromtimestamp(timestamp) - datetime.timedelta(hours=os.environ['TIMEZONE_DIFFERENCE'])
    values['lat'] = lat
    values['lon'] = lon
    values['speed'] = speed
    values['bearing'] = bearing
    values['altitude'] = altitude
    values['accuracy'] = accuracy
    values['batt'] = batt
    values['forwarded_ip'] = forwarded_ip
    values['real_ip'] = real_ip
    
    await database.execute(query=query, values=values)