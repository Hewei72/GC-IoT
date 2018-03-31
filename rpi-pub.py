import paho.mqtt.client as mqtt

## This is the IP address of your laptop
broker_address="192.168.1.100"

print("creating new instance")
client = mqtt.Client("pub5") #create new instance

print("connecting to broker")
client.connect(broker_address) #connect to broker

topic = "gcpiper123"
print("Publishing message to topic: " + topic)
client.publish(topic,"Greetings from Raspberry PI using Paho-mqtt")

#################
## Alternatively you can send a single message without creating an instance
##print "sending now"
##mqtt.single("test","Hi from paho",hostname="192.168.1.2")
