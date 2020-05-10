import paho.mqtt.client as mqtt

host = "localhost"
port =1883
topic ="topic"

def on_connect(mosq, obj, rc):
    mqttc.subscribe(topic, 0)

def on_message(mosq, obj, msg):
    global message
    print(str(msg.payload))

def on_subscribe(mosq, obj, mid, granted_qos):
    print("Subscribed to : " + str(topic))

mqttc = mqtt.Client()

mqttc.on_message = on_message
mqttc.on_connect = on_connect
mqttc.on_subscribe = on_subscribe

mqttc.connect(host, port, 60)
mqttc.loop_forever()
