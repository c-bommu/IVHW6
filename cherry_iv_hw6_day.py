import random
import math
import csv

def add_row(I, rows, a, b, c, d, e, f, g, h, i, j, k, l, m, n):
    Sleeping=random.randrange(a, b)
    Eating=random.randrange(c, d)
    if e!=f:
        Class=random.randrange(e, f)
    else:
        Class=e
    if g!=h:
        Homework=random.randrange(g, h)
    else:
        Homework=g
    Hygiene=random.randrange(i, j)
    if k!=l:
        Exercise=random.randrange(k, l)
    else:
        Exercise=k
    Chores=random.randrange(m, n)
    Fun=1440-Sleeping-Eating-Class-Homework-Hygiene-Exercise-Chores
    if Fun<0:
        Sleeping-=math.ceil(Fun/2)
        Hygiene-=math.floor(Fun/2)
        Fun=0
    rows.append([I, Sleeping, Eating, Class, Homework, Hygiene, Exercise, Chores, Fun])
    
def vacation(rows, I):
    for i in range(7):
        add_row(I+i, rows, 360, 650, 100, 130, 0, 0, 0, 0, 100, 140, 25, 35, 40, 150)

def spring_semester(rows, I):
    #sunday
    add_row(I, rows, 360, 480, 120, 150, 0, 0, 240, 300, 80, 110, 25, 35, 120, 150)
    #monday
    add_row(I+1, rows, 240, 480, 100, 130, 80, 80, 300, 360, 90, 120, 25, 35, 40, 70)
    #tuesday
    add_row(I+2, rows, 360, 540, 90, 110, 430, 430, 130, 180, 80, 100, 0, 0, 60, 90)
    #wednesday
    add_row(I+3, rows, 360, 480, 120, 150, 0, 0, 300, 360, 100, 140, 35, 45, 60, 90)
    #thursday
    add_row(I+4, rows, 240, 480, 100, 130, 80, 80, 240, 300, 90, 120, 25, 35, 40, 70)
    #friday
    add_row(I+5, rows, 360, 650, 90, 110, 430, 430, 0, 0, 80, 100, 0, 0, 30, 60)
    #saturday
    add_row(I+6, rows, 360, 650, 120, 150, 0, 0, 180, 240, 100, 140, 25, 35, 100, 130)

def fall_semester(rows, I):
    #sunday
    add_row(I, rows, 360, 480, 120, 150, 0, 0, 240, 300, 80, 110, 25, 30, 120, 150)
    #monday
    add_row(I+1, rows, 240, 480, 100, 130, 80, 80, 300, 360, 90, 120, 25, 35, 40, 70)
    #tuesday
    add_row(I+2, rows, 360, 540, 90, 110, 430, 430, 130, 180, 80, 100, 0, 0, 60, 90)
    #wednesday
    add_row(I+3, rows, 360, 480, 120, 150, 0, 0, 300, 360, 100, 140, 35, 45, 60, 90)
    #thursday
    add_row(I+4, rows, 240, 480, 100, 130, 80, 80, 240, 300, 90, 120, 25, 35, 40, 70)
    #friday
    add_row(I+5, rows, 360, 650, 90, 110, 430, 430, 0, 0, 80, 100, 0, 0, 30, 60)
    #saturday
    add_row(I+6, rows, 360, 650, 120, 150, 0, 0, 180, 240, 100, 140, 25, 35, 100, 130)
    
if __name__=="__main__":
    # field names
    fields = ['Day', 'Sleeping', 'Eating', 'Class', 'Homework', 'Hygiene', 'Exercise', 'Chores', 'Fun']
    
    # data rows of csv file
    rows = []
    for i in range(0,52):
        if i==0:
            vacation(rows, i*7)
        if i>0 and i<9:
            spring_semester(rows, i*7)
        if i==9:
            vacation(rows, i*7)
        if i>9 and i<17:
            spring_semester(rows, i*7)
        if i>=17 and i<34:
            vacation(rows, i*7)
        if i>=34 and i<46:
            fall_semester(rows, i*7)
        if i==46:
            vacation(rows, i*7)
        if i>46 and i<50:
            fall_semester(rows, i*7)
        if i==50 or i==51:
            vacation(rows, i*7)
        print("len: ", len(rows), ", i: ", i)
        
    
    # name of csv file
    filename = "cherry_iv_hw6.csv"
    
    # writing to csv file
    with open(filename, 'w', newline = '') as csvfile:
    	# creating a csv writer object
    	csvwriter = csv.writer(csvfile)
    
    	# writing the fields
    	csvwriter.writerow(fields)
    
    	# writing the data rows
    	csvwriter.writerows(rows)