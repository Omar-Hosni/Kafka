from kafka imoprt KafkaProducer
import json 
from data import get_register_user

def json_serializer(data):
  return json.dumps(data).encode('utf-8')


producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
                        value_serializer=json_serializer)

if __name__ == '__main__':
  register_user = get_register_user()
  js_data = json_serializer(register_user)
  topic_name = 'etl'
  producer.send(topic_name, js_data)
  
