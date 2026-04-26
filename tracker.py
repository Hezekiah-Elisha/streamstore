from confluent_kafka import Consumer
from json import loads

kafka_consumer_config = {
    "bootstrap.servers": "localhost:9092",
    "group.id": "order-tracker",
    "auto.offset.reset": "earliest",
}

kafka_consumer = Consumer(kafka_consumer_config)
kafka_consumer.subscribe(["orders"])

print("Tracking orders...")

try:
    while True:
        msg = kafka_consumer.poll(1.0)
        if msg is None:
            continue
        if msg.error():
            print(f"Consumer error: {msg.error()}")
            continue

        value = msg.value().decode("utf-8")
        order = loads(value)
        print(
            f"Received order: {order['order_id']} for {order['item']} (quantity: {order['quantity']}) from user {order['user']}"
        )
except KeyboardInterrupt:
    print("Stopping order tracker...")
finally:
    kafka_consumer.close()
