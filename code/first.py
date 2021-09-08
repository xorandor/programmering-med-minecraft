import mcpi.minecraft as minecraft
import mcpi.block as block
import mcpi.entity as entity
import time
mc = minecraft.Minecraft.create()

pos = mc.player.getPos()
print(pos)
mc.player.setTilePos(0,0,0)
pos = mc.player.getPos()
print(pos)
mc.spawnEntity(0, 2, 0, entity.CHICKEN.id)
mc.spawnEntity(0, 3, 0, entity.CHICKEN.id)
mc.spawnEntity(0, 4, 0, entity.CHICKEN.id)
mc.spawnEntity(0, 5, 0, entity.CHICKEN.id)
mc.spawnEntity(0, 6, 0, entity.CHICKEN.id)
mc.spawnEntity(0, 7, 0, entity.CHICKEN.id)
mc.spawnEntity(0, 8, 0, entity.CHICKEN.id)
mc.spawnEntity(0, 9, 0, entity.CHICKEN.id)