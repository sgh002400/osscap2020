from matrix import *
import LED_display as LMD
import threading

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
                LMD.set_pixel(y, 15-x, 0)
            elif array[y][x] == 1:
                LMD.set_pixel(y, 15-x, 4)
            else:
                continue
        print()

arrayScreen = [[0 for col in range(16)] for row in range(32)]

arrayNumDict = { 1: [[0, 1, 0], [1, 1, 0], [0, 1, 0], [0, 1, 0], [1, 1, 1]], 
                 2: [[0, 1, 0], [1, 0, 1], [0, 0, 1], [0, 1, 0], [1, 1, 1]], 
                 3: [[1, 1, 0], [0, 0, 1], [1, 1, 0], [0, 0, 1], [1, 1, 0]], 
                 4: [[1, 0, 1], [1, 0, 1], [0, 1, 1], [0, 0, 1], [0, 0, 1]], 
                 5: [[0, 1, 1], [1, 0, 0], [1, 1, 1], [0, 0, 1], [1, 1, 0]], 
                 6: [[0, 1, 1], [1, 0, 0], [1, 1, 0], [1, 0, 1], [0, 1, 0]], 
                 7: [[0, 1, 0], [1, 0, 1], [1, 0, 1], [0, 0, 1], [0, 0, 1]], 
                 8: [[1, 1, 1], [1, 0, 1], [1, 1, 1], [1, 0, 1], [1, 1, 1]], 
                 9: [[1, 1, 1], [1, 0, 1], [1, 1, 1], [0, 0, 1], [0, 0, 1]], 
                 0: [[1, 1, 1], [1, 0, 1], [1, 0, 1], [1, 0, 1], [1, 1, 1]] } 

arrayAlphabetDict = {}

arrayBlk = arrayNumDict[1] #그때 그때 정해주는 변수

iScreenDy = 32
iScreenDx = 16
top = 5 #그때 그때 정해주는 변수
left = 5 #그때 그때 정해주는 변수

iScreen = Matrix(arrayScreen)
oScreen = Matrix(iScreen)
currBlk = Matrix(arrayBlk)
tempBlk = iScreen.clip(top, left, top+currBlk.get_dy(), left+currBlk.get_dx())
tempBlk = tempBlk + currBlk
oScreen.paste(tempBlk, top, left) #top, left에 적절한 값 넣어줘야함.
LED_init()
draw_matrix(oScreen); print()


#arrayBlk갱신 -> currBlk=Matrix(arrayBlk) 갱신 -> tempBlk(두줄) 갱신