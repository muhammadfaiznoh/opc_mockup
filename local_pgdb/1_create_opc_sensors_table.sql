CREATE SCHEMA opc_server;
CREATE TABLE opc_server.opc_sensors(
    datatime VARCHAR(100),
    opc_pressure FLOAT,
    opc_temperature FLOAT
);