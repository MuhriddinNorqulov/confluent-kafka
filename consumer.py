from confluent_kafka import Consumer, KafkaException

# Kafka consumer konfiguratsiyasi
conf = {
    'bootstrap.servers': "localhost:9092",
    'group.id': "my-consumer-group",
    'auto.offset.reset': 'earliest',
    'api.version.request': False,
}
consumer = Consumer(**conf)
consumer.subscribe(['my_topic60'])

# Xabarlarni qabul qilish
try:
    while True:
        msg = consumer.poll(timeout=1.0)  # 1 soniyada yangi xabarlar tekshiriladi
        if msg is None:
            continue
        if msg.error():
            raise KafkaException(msg.error())
        else:
            print(f'Qabul qilingan xabar: {msg.value().decode("utf-8")}')
except KeyboardInterrupt:
    pass
finally:
    consumer.close()