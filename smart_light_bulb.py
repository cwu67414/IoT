import paho.mqtt.client as mqtt
import time

#Create an instance of the MQTT client and set up the connection to the MQTT broker
client = mqtt.Client()
client.connect("test.mosquitto.org", 1883, 60)

#Define the MQTT topics to be used
state_topic = "smart-light-bulb/state"
brightness_level = "smart-light-bulb/brightness"

#Define the initial state of the light bulb
state = "OFF"
brightness = 0

#Define the callback function for the MQTT client
def on_message(client, userdata, message):
    global state
    global brightness
    print("Received message '" + str(message.payload) + "' on topic '" + message.topic + "' with QoS " + str(message.qos))
    if message.topic == state_topic:
        state = str(message.payload.decode("utf-8"))
        print("State is now " + state)
    elif message.topic == brightness_level:
        brightness = int(message.payload.decode("utf-8"))
        print("Brightness is now " + str(brightness))

#Set the callback function for the MQTT client
client.on_message = on_message

#Subscribe to the MQTT topics
client.subscribe(state_topic)
client.subscribe(brightness_level)

#Start the MQTT client loop
client.loop_start()

#Main loop
while True:
    #Publish the state and brightness of the light bulb
    client.publish(state_topic, state)
    client.publish(brightness_level, brightness)
    time.sleep(1)