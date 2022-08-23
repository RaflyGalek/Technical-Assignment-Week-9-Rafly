import paho.mqtt.client as mqtt

broker = "broker.hivemq.com"  
port = 1883
timeout = 60

username = ''
password = ''

topic = "ultrasonic"
 
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
 
    client.subscribe(topic,qos=0)
 
def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload.decode('utf-8')))
    payload_decoded = msg.payload.decode('utf-8')
    print(f"message diterima: {payload_decoded}")
          
        
client = mqtt.Client("device0")
client.username_pw_set(username=username,password=password)
client.on_connect = on_connect
client.on_message = on_message
 
client.connect(broker, port, timeout)

client.loop_forever()
