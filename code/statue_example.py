import mcpi.minecraft as minecraft
import mcpi.block as block
import mcpi.entity as entity
from statue_builder import build_2d_statue, build_3d_statue
import time
mc = minecraft.Minecraft.create()

sword = """
111             
1111            
11111           
 11111          
  11111         
   11111        
    11111   33  
     11111 333  
      1111333   
       111333   
        3333    
       333322   
      3333 222  
      33    2222
             222
             222
"""

test = """
#######  #######  #######  #######
  ###    ##       ##         ###  
  ###    ##       #######    ###  
  ###    #######       ##    ###  
  ###    ###      ###  ##    ###  
  ###    ###      ###  ##    ###  
  ###    #######  #######    ###  
"""

tree = """
   #####
  #######
 ###X#####
#######X###
 ####X####
  #######
    222
    222
"""

build_3d_statue(mc, tree)
build_2d_statue(mc, sword, "z")
