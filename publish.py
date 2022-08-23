import paho.mqtt.client as paho
from paho import mqtt
from time import sleep
from ultra import distance


broker = "broker.hivemq.com"  
port = 1883
timeout = 60

username = '' 
password = ''

topic = "ultrasonic"

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
 
def on_publish(client,userdata,result):
	print("data published \n")
	

client1 = paho.Client("device1",userdata=None,protocol=paho.MQTTv5)
client1.username_pw_set(username=username,password=password)
client1.on_connect = on_connect
client1.on_publish = on_publish
client1.connect(broker,port,timeout)


while True:
	message = distance()
	ret = client1.publish(topic,payload=message,qos=0)
	print(f"messange sended : {message}")
	sleep(1)
