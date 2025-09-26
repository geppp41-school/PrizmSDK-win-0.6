import sys
from convert import *
file_path:str = "doom.wad"
file = open(file_path, "rb")

#sizes for file header   size: 12 bytes
headerSizeBytes = 12
typeSizeBytes = 4
numLumpsSizeBytes = 4
directoryLocationSizeBytes = 4
#lump data    size: 16 bytes
lumpSizeBytes = 16
filePosSizeBytes = 4
fileSizeBytes = 4
fileNameSizeBytes = 8



type:bytearray = str(file.read(4)).replace("b", "").replace("\'", "")
print(f"Type: {type}    Memory usage: {sys.getsizeof(type)}")
file.seek(typeSizeBytes, 1)#increases target position
#target, whence
#0 <= whence <= 2
#whence = 0   |   relative to start of file    also default
#whence = 1   |   relative to current position so it can be negative 
#whence = 2   |   relative to end of file and offset should be negative 

numLumps:int = get_lsb_int(file.read(numLumpsSizeBytes)) #get least significant bit integer 
#all ints in doom wad files will be stored as a lsb and are 4 byets long
print(f"Number of Lumps: {numLumps}   Memory usage: {sys.getsizeof(numLumps)}")

file.seek(numLumpsSizeBytes, 1)
directoryPos = get_lsb_int(file.read(directoryLocationSizeBytes))#relative to start of file
print(f"Directory Offset: {directoryPos}   Memory usage: {sys.getsizeof(directoryPos)}")

file.seek(directoryPos, 0)

filePos = file.read(filePosSizeBytes)
file.seek(filePosSizeBytes, 1)
fileSize = file.read(fileSizeBytes)
file.seek(fileSizeBytes, 1)
fileName = file.read(fileNameSizeBytes)

print()
