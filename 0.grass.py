"""
2   草地
49  黑曜石
152 紅石磚
"""
#滿滿的大平台
from mcpi.minecraft import Minecraft

mc=Minecraft.create()

mc.player.setTilePos(0,70,0)

x,y,z=mc.player.getTilePos()
mc.setBlocks(x+30,y-5,z+30,x-30,y-1,z-30,2)
mc.setBlocks(x+30,y,z+30,x-30,y+100,z-30,0)

mc.setSign(x+1,y,z,63,4,"X+","","EAST")
mc.setSign(x,y,z+1,63,8,"Z+","","SOUTH")
