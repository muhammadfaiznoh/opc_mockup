FROM apache/superset

# Install module
RUN pip install psycopg2


CMD /bin/sh -c "superset db upgrade && superset fab create-admin --username admin --firstname Superset --lastname Admin --email admin@superset.com --password admin  && superset init && superset run -p 8088 -h 0.0.0.0"
