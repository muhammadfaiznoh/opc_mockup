import psycopg2

# MongoDB connection settings
MONGO_URI = 'mongodb://root:example@mongo:27017/opc_sensors'
MONGO_DB = 'mongo'

# Use MongoDB as the user database
# AUTH_TYPE = 2
AUTH_USER_REGISTRATION = True
AUTH_USER_REGISTRATION_ROLE = "Public"
AUTH_USERDB = pymongo.MongoClient(MONGO_URI)[MONGO_DB]
