from confluent_kafka import Producer

# Kafka producer konfiguratsiyasi
conf = {'bootstrap.servers': "192.168.100.20:9092"}
producer = Producer(**conf)

# Xabar yuborish funksiyasi
def delivery_report(err, msg):
    if err is not None:
        print(f'Xabarni yetkazib berishda xato: {err}')
    else:
        print(f'Xabar muvaffaqiyatli yuborildi: {msg.topic()} [{msg.partition()}]')

# Kafka'ga xabar yuborish
for i in range(1):
    value = input('Xabar kiriting: ')
    producer.produce('my-topic', key='key', value=value, callback=delivery_report)
producer.flush()  # Yuborilmagan xabarlar bo'lsa, ularni Kafka'ga yuboradi