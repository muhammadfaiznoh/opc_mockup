FROM python:3.7-slim

RUN pip install \
    asyncua==1.0.2

WORKDIR /opt/opc_mockup/datagenerator

COPY ../../datagenerator /opt/opc_mockup/datagenerator

CMD [ "python" ,"./opc_data_generator.py"]