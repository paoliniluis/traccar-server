import random, datetime

def latlon_generator():
    return random.uniform(-90.0, 90.0)

def speed_generator():
    return random.uniform(0.0, 120.0)

def bearing_generator():
    return random.uniform(0.0, 360.0)

def battery_generator():
    return random.uniform(0.0, 100.0)

def altitude_generator():
    return random.uniform(-500.0, 5000.0)

def id_generator():
    return random.randint(10000, 20000)

def timestamp_generator():
    return datetime.datetime.timestamp(datetime.datetime.now())