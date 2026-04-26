from confluent_kafka import Producer
from uuid import uuid4
from json import dumps

producer_config = {
    "bootstrap.servers": "localhost:9092",
}

kafka_producer = Producer(producer_config)


def delivery_report(err, msg):
    if err is not None:
        print(f"Message delivery failed: {err}")
    else:
        print(
            f"Message {msg.value().decode('utf-8')} delivered to {msg.topic()} [{msg.partition()}] at offset {msg.offset()}"
        )
        print(dir(msg))


order = {
    "order_id": str(uuid4()),
    "product_id": "product_id",
    "user": "elisha",
    "item": "mashroom pizza",
    "quantity": 15,
}

# convert to bytes
value = dumps(order).encode("utf-8")

kafka_producer.produce(
    topic="orders",
    value=value,
    callback=delivery_report,
)
kafka_producer.flush()
