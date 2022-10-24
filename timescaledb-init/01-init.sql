CREATE DATABASE metabase;

CREATE EXTENSION IF NOT EXISTS timescaledb;

DROP TABLE IF EXISTS gps_data;
    CREATE TABLE gps_data (
        device_id VARCHAR(255),
        sensor_timestamp TIMESTAMP NOT NULL,
        latitude double precision,
        longitude double precision,
        speed double precision,
        bearing double precision,
        altitude double precision,
        accuracy INTEGER,
        battery double precision,
        forwarded_ip VARCHAR(255),
        real_ip VARCHAR(255)
    );

SELECT create_hypertable('gps_data', 'sensor_timestamp');