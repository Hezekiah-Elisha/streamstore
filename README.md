# Streamstore: Apache Kafka Learning Project

A hands-on learning project demonstrating Apache Kafka fundamentals with a simple order management system. This project showcases how to build a Kafka producer and consumer to handle asynchronous order streaming.

## 📋 Project Overview

**Streamstore** is a learning application that simulates a basic order processing system using Apache Kafka. It demonstrates core Kafka concepts including:

- **Message Production**: Generating order messages and sending them to Kafka topics
- **Message Consumption**: Subscribing to topics and processing order events in real-time
- **Event-Driven Architecture**: Decoupling producers and consumers for scalable systems

### Use Case

The project models an e-commerce scenario where:
1. A **Producer** generates order messages (order ID, product, quantity, user)
2. A **Consumer/Tracker** subscribes to the orders topic and displays incoming orders in real-time
3. Kafka acts as the message broker, enabling asynchronous communication between components

## 🏗️ Architecture

```
┌──────────────┐         ┌────────┐         ┌──────────────┐
│   Producer   │────────▶│ Kafka  │────────▶│  Consumer    │
│  (produces   │  Topic: │Broker  │         │  (tracks     │
│   orders)    │  orders │        │         │   orders)    │
└──────────────┘         └────────┘         └──────────────┘
```

- **producer.py**: Generates sample order events and publishes to the "orders" topic
- **tracker.py**: Consumer that subscribes to the "orders" topic and logs received orders
- **compose.yaml**: Docker Compose configuration for running Kafka in KRaft mode

## 🚀 Quick Start

### Prerequisites

- Docker & Docker Compose
- Python 3.8+
- pip (Python package manager)

### 1. Start Kafka

```bash
docker-compose up -d
```

This starts a Kafka broker in KRaft mode (KIP-500) without requiring a separate Zookeeper instance.

Wait a few seconds for Kafka to be ready, then verify:

```bash
docker-compose logs kafka
```

### 2. Set Up Python Environment

```bash
# Create virtual environment
python3 -m venv venv

# Activate it
source venv/bin/activate  # On macOS/Linux
# or
venv\Scripts\activate  # On Windows

# Install dependencies
pip install -r requirements.txt
```

### 3. Run the Tracker (Consumer)

In one terminal, start the order tracker to listen for incoming orders:

```bash
python tracker.py
```

You should see:
```
Tracking orders...
```

### 4. Run the Producer

In another terminal, send an order message:

```bash
python producer.py
```

You should see output in the **producer** terminal:
```
Message {"order_id": "...", "product_id": "product_id", "user": "elisha", "item": "mashroom pizza", "quantity": 15} delivered to orders [0] at offset 0
```

And in the **tracker** terminal:
```
Received order: <order_id> for mashroom pizza (quantity: 15) from user elisha
```

## 📁 Project Structure

```
.
├── compose.yaml        # Docker Compose configuration for Kafka
├── producer.py         # Kafka producer - publishes order messages
├── tracker.py          # Kafka consumer - tracks incoming orders
├── requirements.txt    # Python dependencies
├── venv/              # Python virtual environment (after setup)
└── README.md          # This file
```

## 🔧 Technologies Used

- **Apache Kafka**: Distributed event streaming platform
- **Confluent Kafka Python Client**: High-level Python API for Kafka
- **Docker/Docker Compose**: Containerization and orchestration
- **KRaft Mode**: Kafka without external Zookeeper coordination

## 📚 Key Concepts Demonstrated

### Producer (`producer.py`)
- Creating a Kafka producer instance
- Building message payloads (JSON)
- Serializing data (JSON to bytes)
- Sending messages with delivery callbacks
- Handling delivery reports

### Consumer (`tracker.py`)
- Creating a Kafka consumer instance
- Subscribing to topics
- Consuming messages from offset zero
- Deserializing JSON messages
- Handling consumer errors
- Graceful shutdown with Ctrl+C

### Configuration
- Bootstrap server setup (localhost:9092)
- Consumer group management
- Auto offset reset policy
- Topic-based message routing

## 🎯 Next Steps / Learning Extensions

- Add multiple partitions to the "orders" topic for parallelism
- Implement consumer group scaling with multiple tracker instances
- Add error handling and retry logic
- Integrate a database for order persistence
- Explore Kafka streams for real-time processing
- Set up monitoring with Kafka metrics
- Implement message schemas with Avro or Protobuf

## 🛑 Cleanup

To stop and remove the Kafka container:

```bash
docker-compose down
```

To remove the volume (Kafka data):

```bash
docker-compose down -v
```

## 📖 Resources

- [Apache Kafka Documentation](https://kafka.apache.org/documentation/)
- [Confluent Kafka Python Client](https://docs.confluent.io/kafka-clients/python/current/overview.html)
- [KRaft Mode (KIP-500)](https://kafka.apache.org/documentation/#kraft)
- [Kafka Quickstart Guide](https://kafka.apache.org/quickstart)

## 📝 License

This is a learning project. Feel free to use and modify for educational purposes.
