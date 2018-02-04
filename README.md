# Reverse Shell
### This project is the implemetaion of reverse shell using MQTT protocol.




## Why MQTT?
	* Can be accessed without the having of Public IP
	* Easy to implement
	* Light Weight
	* Multiple host can control multiple targets simultaneously
	* `QOS = 2` can ensure no loss of data midway
	* Cross platform, basically any machine which can run Python 



## Things to do
	* Implementation of Change of Directory (CD) command
	* Making of Subscriber(Target Side Code) more robust
	* Making host terminal more user friendly and interactive


## Project Structure
	* There are three files in project
		* pub.py
		* sub.py
		* test.py
	* File __sub.py__ resides into the target computer,having dependency paho-mqtt
	* File __pub.py__ and __test.py__ resides into the host computer, having dependency paho-mqtt
	* Host only need to run pub.py in order to control target computer, provided sub.py is running on target computer 

### running sub.py can be automated by using systemd or any other similar services 

### All the codes are implemnted in python3 and are not tested for python2