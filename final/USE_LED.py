from matrix import *
import LED_display as LMD
import threading
import time

def LED_init():
    thread=threading.Thread(target=LMD.main, args=())
    thread.setDaemon(True)
    thread.start()
    return

def draw_matrix(m):
    array = m.get_array()
    for y in range(m.get_dy()):
        for x in range(m.get_dx()):
            if array[y][x] == 0:
                LMD.set_pixel(y, x, 0)
            elif array[y][x] == 1:
                LMD.set_pixel(y, x, 4)
            else:
                continue
        print()

iScreenDy = 16
iScreenDx = 32

arrayScreen = [[0 for col in range(32)] for row in range(16)]

arrayNumDict = { 1: [[0, 1, 0], [1, 1, 0], [0, 1, 0], [0, 1, 0], [1, 1, 1]], 
                 2: [[0, 1, 0], [1, 0, 1], [0, 0, 1], [0, 1, 0], [1, 1, 1]], 
                 3: [[1, 1, 0], [0, 0, 1], [1, 1, 0], [0, 0, 1], [1, 1, 0]], 
                 4: [[1, 0, 1], [1, 0, 1], [0, 1, 1], [0, 0, 1], [0, 0, 1]], 
                 5: [[0, 1, 1], [1, 0, 0], [1, 1, 1], [0, 0, 1], [1, 1, 0]], 
                 6: [[0, 1, 1], [1, 0, 0], [1, 1, 0], [1, 0, 1], [0, 1, 0]], 
                 7: [[0, 1, 0], [1, 0, 1], [1, 0, 1], [0, 0, 1], [0, 0, 1]], 
                 8: [[1, 1, 1], [1, 0, 1], [1, 1, 1], [1, 0, 1], [1, 1, 1]], 
                 9: [[1, 1, 1], [1, 0, 1], [1, 1, 1], [0, 0, 1], [0, 0, 1]], 
                 0: [[1, 1, 1], [1, 0, 1], [1, 0, 1], [1, 0, 1], [1, 1, 1]],
                 ':': [[0, 0, 0], [0, 1, 0], [0, 0, 0], [0, 1, 0], [0, 0, 0]] } 

arrayAlphabetDict = {'A': [[1, 1, 1], [1, 0, 1], [1, 1, 1], [1, 0, 1], [1, 0, 1]],
                     'B': [[1, 1, 0], [1, 0, 1], [1, 1, 0], [1, 0, 1], [1, 1, 0]],
                     'C': [[0, 1, 0], [1, 0, 1], [1, 0, 0], [1, 0, 1], [0, 1, 0]],
                     'D': [[1, 1, 0], [1, 0, 1], [1, 0, 1], [1, 0, 1], [1, 1, 0]],
                     'E': [[1, 1, 1], [1, 0, 0], [1, 1, 1], [1, 0, 0], [1, 1, 1]],
                     'F': [[1, 1, 1], [1, 0, 0], [1, 1, 1], [1, 0, 0], [1, 0, 0]],
                     'G': [[0, 1, 0], [1, 0, 1], [1, 1, 0], [1, 0, 1], [0, 1, 0]],
                     'H': [[1, 0, 1], [1, 0, 1], [1, 1, 1], [1, 0, 1], [1, 0, 1]],
                     'I': [[1, 1, 1], [0, 1, 0], [0, 1, 0], [0, 1, 0], [1, 1, 1]],
                     'J': [[1, 1, 1], [0, 1, 0], [0, 1, 0], [1, 0, 1], [0, 1, 0]],
                     'K' : [[1, 0, 1], [1, 1, 0], [1, 0, 0], [1, 1, 0], [1, 0, 1]],
                     'L' : [[1, 0, 0], [1, 0, 0], [1, 0, 0], [1, 0 ,0], [1, 1, 1]],
                     'M' : [[1, 0, 1], [1, 1, 1], [1, 0, 1], [1, 0, 1], [1, 0, 1]],
                     'N' : [[1, 0, 1], [1, 1, 1], [1, 1, 1], [1, 0, 1], [1, 0, 1]],
                     'O' : [[0, 1, 0], [1, 0, 1], [1, 0, 1], [1, 0, 1], [0, 1, 0]],
                     'P' : [[1, 1, 0], [1, 0, 1], [1, 1, 0], [1, 0, 0], [1, 0, 0]],
                     'Q' : [[0, 1, 0], [1, 0, 1], [1, 0, 1], [1, 1, 1], [0, 1, 1]],
                     'R' : [[1, 1, 0], [1, 0, 1], [1, 1, 0], [1, 0, 1], [1, 0, 1]],
                     'S' : [[1, 1, 0], [1, 0, 1], [0, 1, 0], [1, 0, 1], [0, 1, 1]],
                     'T' : [[1, 1, 1], [0, 1, 0], [0, 1, 0], [0, 1, 0], [0, 1, 0]],
                     'U' : [[1, 0, 1], [1, 0, 1], [1, 0, 1], [1, 0, 1], [1, 1, 1]],
                     'V' : [[1, 0, 1], [1, 0, 1], [1, 0, 1], [1, 0, 1], [0, 1, 0]],
                     'W' : [[1, 0, 1], [1, 0, 1], [1, 0, 1], [1, 1, 1], [1, 0, 1]],
                     'X' : [[1, 0, 1], [1, 0, 1], [0, 1, 0], [1, 0, 1], [0, 1, 0]],
                     'Y' : [[1, 0, 1], [1, 0, 1], [0, 1, 0], [0, 1, 0], [0, 1, 0]],
                     'Z' : [[1, 1, 1], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]]}

LED_init()
iScreen = Matrix(arrayScreen)
oScreen = Matrix(iScreen)

count = 0
top = 0
left = 5

for i in ['A', 'L', 'A', 'R', 'M', 'M', 'U', 'S', 'I', 'C', 'V', 'O', 'L', 'U', 'M', 'E']:
    arrayBlk = arrayAlphabetDict[i]
    currBlk = Matrix(arrayBlk)
    tempBlk = iScreen.clip(top, left, top+currBlk.get_dy(), left+currBlk.get_dx())
    tempBlk = tempBlk + currBlk
    oScreen.paste(tempBlk, top, left)
    left += 4
    count+=1
    if count==5:
        top = 5
        left = 6
    if count==10:
        top = 11
        left = 2

top = 5
left = 25
for i in range(2):
    arrayBlk = arrayNumDict[':']
    currBlk = Matrix(arrayBlk)
    tempBlk = iScreen.clip(top, left, top+currBlk.get_dy(), left+currBlk.get_dx())
    tempBlk = tempBlk + currBlk
    oScreen.paste(tempBlk, top, left)

draw_matrix(oScreen); print()
#arrayBlk갱신 -> currBlk=Matrix(arrayBlk) 갱신 -> tempBlk(두줄) 갱신