import sys
from convert import *
file_path = "doom.wad"
file = open(file_path, "rb")
screen = "ENDOOM"
type = file.read(4)
numLumps = get_lsb_int(file.read(4))
dirPos = get_lsb_int(file.read(4))
file.seek(dirPos)

pos = -1
size = -1
name = ""

while name != screen:
    pos = get_lsb_int(file.read(4))
    size = get_lsb_int(file.read(4))
    name = file.read(8).decode().strip('\x00')
file.seek(pos)
print(file.read(size))
print(size)