FROM python:3.7-slim



RUN pip install \
    asyncua==1.0.2 \
    pymongo \
    confluent_kafka\
    psycopg2-binary

WORKDIR /opt/opc_mockup/opc

COPY ../../opc /opt/opc_mockup/opc

CMD ["python", "./opc_streaming.py"]