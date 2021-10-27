import mcpi.minecraft as minecraft
import mcpi.block as block
import mcpi.entity as entity
import time
import random
from chat_handler import get_latest_message
mc = minecraft.Minecraft.create()

running = True

pet = None
while running:
  #split
  #tegn det
  #if branches
    chat = get_latest_message(mc)
    chatParts = chat.split(" ")
    action = chatParts[0]
    arg2 = chatParts[1]
    
    if action == "spawn":
      if arg2 == "ko":
        pet = mc.spawnEntity()
    if command=="kill":
      
    if command == "teleport":
      if entity=="pet":
        
      if cp[1]=="me":
        #tp
      
        
    
    if chat == "exit":
        mc.postToChat("Goodbye!")
        running = False

    time.sleep(0.1)
