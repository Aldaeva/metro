'''
case 6 - Moskow Subway
developers: Aldaeva.A 33%, Litvinov.K 33%, Shulgin.N 33%
'''

from tkinter import *
from random import *
from math import *

class Metro(object):
    def __init__(self, x1, y1, x2, y2, color, _width, outline):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.color = color
        self._width = _width
        self.outline = outline
        c.create_oval(x1, y1, x2, y2, fill = color,
                      width = _width, outline = outline)

class Train():
    def __init__(self, location, movement, speed, amount, _list):
        self.location = location
        self.movement = movement
        self.speed = speed
        self.amount = amount
        self._list = _list
        if self.location == 'Курская':
            x = _list[1][0]
            y = _list[1][1]
        if self.location == 'Павелецкая':
            x = _list[3][0]
            y = _list[3][1]
        if self.location == 'Киевская':
            x = _list[7][0]
            y = _list[7][1]
        if self.location == 'Новослободская':
            x = _list[10][0]
            y = _list[10][1]
        if self.location == 'Октябрьская':
            x = _list[5][0]
            y = _list[5][1] - 5
        if self.location == 'Белорусская':
            x = _list[9][0]
            y = _list[9][1]
        if int(self.movement) == 1:
            c.create_oval(x+5,y-3,x+11,y+3, fill = 'yellow',
                          outline = 'yellow', tag = 'clockwise')
        if int(self.movement) == 0:
            c.create_oval(x-5,y-3,x-11,y+3, fill = 'yellow',
                          outline = 'yellow', tag = 'counter-clockwise')
    def angle(self):
        if self.location == 'Курская':
            angle = self._list[1][2]
        if self.location == 'Павелецкая':
            angle = self._list[3][2]
        if self.location == 'Киевская':
            angle = self._list[7][2]
        if self.location == 'Новослободская':
            angle = self._list[10][2]
        if self.location == 'Октябрьская':
            angle = self._list[5][2]
        if self.location == 'Белорусская':
            angle = self._list[9][2]
        return angle

a = 1
def again():
    global a
    if a == 0:
        c.after(30,start)
    else:
        pass
#train movement
def start():
    global a
    a = 0
    move_clockwise = c.find_withtag('clockwise')
    move_counter_clockwise = c.find_withtag('counter-clockwise')
    coords_list = []
    for i in move_clockwise:
        coords_list.append(c.coords(i)[0:2])
    for i in move_counter_clockwise:
        coords_list.append(c.coords(i)[0:2])
    angle_list = []
    angle_list.append(train1.angle())
    angle_list.append(train3.angle())
    angle_list.append(train5.angle())
    angle_list.append(train7.angle())
    angle_list.append(train2.angle())
    angle_list.append(train4.angle())
    angle_list.append(train6.angle())
    speed_list = []
    speed_list.append(int(train1.speed))
    speed_list.append(int(train3.speed))
    speed_list.append(int(train5.speed))
    speed_list.append(int(train7.speed))
    speed_list.append(int(train2.speed))
    speed_list.append(int(train4.speed))
    speed_list.append(int(train6.speed))
    angle1 = angle_list[0] + (speed_list[0])/10
    angle3 = angle_list[1] + (speed_list[1])/10
    angle5 = angle_list[2] + (speed_list[2])/10
    angle7 = angle_list[3] + (speed_list[3])/10
    angle2 = angle_list[4] + (speed_list[4])/10
    angle4 = angle_list[5] + (speed_list[5])/10
    angle6 = angle_list[6] + (speed_list[6])/10
    list1[1][2] = angle1
    list1[3][2] = angle3
    list1[7][2] = angle5
    list1[10][2] = angle7
    list11[2] = angle2
    list1[5][2] = angle4
    list1[9][2] = angle6
    alpha1 = radians(90-((180*angle1)/(3.14*315)))
    alpha2 = radians(90-((180*angle3)/(3.14*315)))
    alpha3 = radians(90-((180*angle5)/(3.14*315)))
    alpha4 = radians(90-((180*angle7)/(3.14*315)))
    alpha5 = radians(((180*angle2)/(3.14*303)))
    alpha6 = radians(((180*angle4)/(3.14*303)))
    alpha7 = radians(((180*angle6)/(3.14*303)))
    x1 = 409 + int(315*cos(alpha1)) - coords_list[0][0]
    y1 = 409 - int(315*sin(alpha1)) - coords_list[0][1]
    x3 = 409 + int(315*cos(alpha2)) - coords_list[1][0]
    y3 = 409 - int(315*sin(alpha2)) - coords_list[1][1]
    x5 = 409 + int(315*cos(alpha3)) - coords_list[2][0]
    y5 = 409 - int(315*sin(alpha3)) - coords_list[2][1]
    x7 = 409 + int(315*cos(alpha4)) - coords_list[3][0]
    y7 = 409 - int(315*sin(alpha4)) - coords_list[3][1]
    x2 = 409 + int(303*cos(alpha5)) - coords_list[4][0]
    y2 = 409 - int(303*sin(alpha5)) - coords_list[4][1]
    x4 = 409 + int(303*cos(alpha6)) - coords_list[5][0]
    y4 = 409 - int(303*sin(alpha6)) - coords_list[5][1]
    x6 = 409 + int(303*cos(alpha7)) - coords_list[6][0]
    y6 = 409 - int(303*sin(alpha7)) - coords_list[6][1]
    c.move(move_clockwise[0],x1,y1)
    c.move(move_clockwise[1],x3,y3)
    c.move(move_clockwise[2],x5,y5)
    c.move(move_clockwise[3],x7,y7)
    c.move(move_counter_clockwise[0],x2,y2)
    c.move(move_counter_clockwise[1],x4,y4)
    c.move(move_counter_clockwise[2],x6,y6)
    if a == 0:
        again()
    else:
        a = 1
        stop()
    
    

def stop():
    global a
    a = 1
    print(a)
    pass
    
def get_info(file):
    list1 = []
    f1 = open(file,'r')
    for i in f1:
        i = i.rstrip()
        list1.append(i)
    f1.close()
    list3 = []
    for i in list1:
        list3.append(i.split(' '))
    return list3

road_minutes = {3: 'Комсомольская', 6: 'Курская', 8: 'Таганская',
                11: 'Павелецкая', 13: 'Добрынинская', 14: 'Октябрьская',
                17: 'Парк культуры', 20: 'Киевская', 22: 'Краснопресненская',
                25: 'Белорусская', 27: 'Новослободская', 30: 'Проспект мира'}

root = Tk()
root.title('Moskow metro')

c = Canvas(root, width = 800, height = 750, bg = 'white')
c.pack()

btn1 = Button(text="Start", command = start)
btn1.pack()
btn2 = Button(text="Stop", command = stop)
btn2.pack()

# roads create
# 1px = 10m, 718-100 = 618px => d = 6180m. L = 19400m
# L = pi*d, 3.14*6180 = 19400m
center_road = Metro(100, 100, 718, 718, 'white', 6, 'red')
up_road = Metro(94, 94, 724, 724, 'white', 6, 'red')
down_road = Metro(106, 106, 712, 712, 'white', 6, 'red')

# stations create
# alpha = 180*l/pi*r
list1 = []
for i in sorted(road_minutes):
    l = int((i/30)*1940)
    alpha = round((180*l)/(3.14*309))
    alpha = 90 - alpha
    alpha = radians(alpha)
    x = 409 + int(309*cos(alpha))
    y = 409 - int(309*sin(alpha))
    list1.append([x,y,l])
    station = Metro(x - 10, y - 10, x + 10, y + 10, 'red', 5, 'red')
list11 = list1[3]
#trains create
trains = get_info('metro.txt')
train1 = Train(trains[0][1],trains[0][2],trains[0][3],trains[0][4],list1)
train2 = Train(trains[1][1],trains[1][2],trains[1][3],trains[1][4],list1)
train3 = Train(trains[2][1],trains[2][2],trains[2][3],trains[2][4],list1)
train4 = Train(trains[3][1],trains[3][2],trains[3][3],trains[3][4],list1)
train5 = Train(trains[4][1],trains[4][2],trains[4][3],trains[4][4],list1)
train6 = Train(trains[5][1],trains[5][2],trains[5][3],trains[5][4],list1)
train7 = Train(trains[6][1],trains[6][2],trains[6][3],trains[6][4],list1)

root.mainloop()
