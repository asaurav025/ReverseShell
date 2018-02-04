import paho.mqtt.client as mqtt
import threading
import time
import test


def Output():
	test.Main()

t1 = threading.Thread(target=Output, args=[])

t1.start()

# Do not use an publicly available broker
broker = "broker.hivemq.com"
port = 1883

username =None
password = None

# Set an topic for target to listen
topic = "target/"


client1 = mqtt.Client()

# Uncomment to input username and password
# client1.username_pw_set(username, password)

client1.connect(broker, port, 60)
print("Connected")

time.sleep(0.5)
client1.loop_start()
print('>>>' ,end="")

while True:
	command = input()
	client1.publish(topic,payload=command)

client1.loop_stop()
client1.disconnect()


