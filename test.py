import paho.mqtt.client as mqtt

# Do not use an publicly available broker
broker = "broker.hivemq.com"
port = 1883

# Set an topic for target to show output
topic_out = "output/"

# Set an topic for target to show error
topic_err = "error/"

username =None
password = None

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe(topic_out)
    client.subscribe(topic_err)

def on_message(client, userdata, msg):
    print("***********************")
    if (msg.topic == topic_out):
    	print("Output")
    else:
    	print("Enter correct command")
    print("***********************")
    output = msg.payload.decode('UTF-8')
    print(output,"\n>>>",end="")



def Main():
	client = mqtt.Client()
	client.on_connect = on_connect
	client.on_message = on_message

	# Uncomment to input username and password
	# client.username_pw_set(username, password)

	client.connect(broker, port, 60)
	client.loop_forever()
