import requests
from faker import id_generator, timestamp_generator, latlon_generator, speed_generator, bearing_generator, altitude_generator, battery_generator

def post_request_gen():
    while True:
        r = requests.post(f'http://192.168.0.13:9000/producer/feedqs?id={id_generator()}&timestamp={timestamp_generator()}&lat={latlon_generator()}&lon={latlon_generator()}&speed={speed_generator()}&bearing={bearing_generator()}&altitude={altitude_generator()}&batt={battery_generator()}',
        {})
        print(r.json())

post_request_gen()