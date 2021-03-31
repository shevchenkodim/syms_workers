import redis
import logging

logger_services = logging.getLogger("sf_workers.services")


class RedisTools(object):

    def __init__(self, ssl, db, host, port, username, password):
        self.db = db
        self.ssl = ssl
        self.host = host
        self.port = port
        self.username = username
        self.password = password
        self.connection = None

    def check_connection(self):
        """ function for check connection """
        if self.connection is None:
            return False
        return self.connection.ping()

    def connect_to_server(self):
        """ Function for connect to server """
        try:
            self.connection = redis.Redis(
                db=self.db,
                ssl=self.ssl,
                host=self.host,
                port=self.port,
                username=self.username,
                password=self.password
            )
        except ConnectionError:
            logger_services.info(f"REDIS SERVICES [ConnectionError]")
            self.connection = None

    def close_connection(self):
        """ Function for close connection """
        if self.connection is not None:
            self.connection.close()
            logger_services.info(f"REDIS SERVICES [Close connection]")

    def set_value(self, key, value):
        """ Call to set a new value """
        if not self.check_connection():
            self.connect_to_server()
        self.connection.set(key, value)

    def get_value(self, key):
        """ Return a value for the context variable for the current context """
        if not self.check_connection():
            self.connect_to_server()
        return self.connection.get(key)


# if not DEBUG:
#     redis_instance = RedisTools(True, REDIS_DB, REDIS_HOST, REDIS_PORT, REDIS_USER, REDIS_PASSWORD)
# else:
#     redis_instance = RedisTools(False, REDIS_DB, REDIS_HOST, REDIS_PORT, None, None)
