import paho.mqtt.client as mqtt

host="localhost"
port=1883
topic="topic"
msg="Hello"


def on_connect(mosq, obj, rc):
    print("Connected")

def on_publish(client, userdata, mid):
    print("published")

mqttc = mqtt.Client()
mqttc.connect(host, port, 60)
mqttc.on_connect = on_connect
mqttc.on_publish = on_publish
mqttc.publish(topic,msg, 0)
mqttc.loop_forever()
