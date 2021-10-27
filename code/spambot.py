import mcpi.minecraft as minecraft
import mcpi.block as block
import mcpi.entity as entity
import time
mc = minecraft.Minecraft.create()

def spambot(count, userMessage):
    message=""
    counter=1
    while counter < count:
        message = message + userMessage
        counter=counter+1
        time.sleep(1)
        mc.postToChat(message)

while True:
    spambot(13, "Hej Mor")
    time.sleep(0.3)