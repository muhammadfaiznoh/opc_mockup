ALTER DATABASE postgres SET timezone TO 'Asia/Kuala_Lumpur';
CREATE TABLE opc_sensors(
    datatime TIMESTAMP,
    opc_pressure FLOAT,
    opc_temperature FLOAT
);