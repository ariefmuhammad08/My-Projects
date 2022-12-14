import logging

import json
import time
from datetime import datetime
from kafka import KafkaConsumer

from . import database


class Consumer(KafkaConsumer):
    """
    Consumer with DB Loader

    Kafka Consumer wrapped with Postgres Data Loader functionality.
    Inherited from KafkaConsumer.

    params:
    - bootstrap_servers: str. Kafka instance hostname (bootstrap).
    - topic: str. Topic for consumer to pull (subscribe) data.
    - db_config: dict. Database connection configuration.
    - tablename: str. Target table for final data.
    """
    def __init__(self, bootstrap_servers: str, topic: str, db_config: dict, tablename: str):
        super().__init__(
            topic,
            bootstrap_servers = [bootstrap_servers],
            value_deserializer = self._deserializer
        )
        self.active = False
        self.database = database.get_engine(**db_config)
        self.tablename = tablename
    

    # Public Methods
    def start(self):
        """
        Start Consumer

        Start consumer activity.
        """
        self.active = True
        self._consume()
    
    def stop(self):
        """
        Stop Consumer

        Stop consumer activity.
        """
        self.active = False
    

    # Private Methods
    def _consume(self):
        while(self.active):
            data = self.poll(timeout_ms=500)
            for _, messages in data.items():
                for message in messages:
                    fmt_data = self._format_data(message.value)
                    database.insert_data(self.database, fmt_data, self.tablename)

            logging.info("Fetching another batch...")
            time.sleep(10)

    def _deserializer(self, data: bytes) -> dict:
        return json.loads(data.decode("utf-8"))
    
    def _format_data(self, data: dict) -> list:
        event = {
            "page_type": data["core"]["page_type"], # page_type
            "page_url": data["core"]["page_url"],  # page_url
            "user_id": data["user"]["user_id"],   # user_id
            "session_id": data["user"]["session_id"],# session_id
            "event_timestamp": datetime.fromtimestamp(data["event_timestamp"]),   # event_timestamp
        }
        return event