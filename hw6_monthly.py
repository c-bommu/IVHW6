import random
import math
import csv


def daily_data(a, b, c, d, e, f, g, h, i, j, k, l, m, n):
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
    return [Sleeping, Eating, Class, Homework, Hygiene, Exercise, Chores, Fun]
       
def vacation():
    day1 = daily_data(360, 650, 100, 130, 0, 0, 0, 0, 100, 140, 25, 35, 40, 150)
    day2 = daily_data(360, 650, 100, 130, 0, 0, 0, 0, 100, 140, 25, 35, 40, 150)
    day3 = daily_data(360, 650, 100, 130, 0, 0, 0, 0, 100, 140, 25, 35, 40, 150)
    day4 = daily_data(360, 650, 100, 130, 0, 0, 0, 0, 100, 140, 25, 35, 40, 150)
    day5 = daily_data(360, 650, 100, 130, 0, 0, 0, 0, 100, 140, 25, 35, 40, 150)
    day6 = daily_data(360, 650, 100, 130, 0, 0, 0, 0, 100, 140, 25, 35, 40, 150)
    day7 = daily_data(360, 650, 100, 130, 0, 0, 0, 0, 100, 140, 25, 35, 40, 150)
    week = []
    for i in range(8):
        week.append((day1[i]+day2[i]+day3[i]+day4[i]+day5[i]+day6[i]+day7[i])/7)
    return week
def spring_semester():
    #sunday
    day1 = daily_data(360, 480, 120, 150, 0, 0, 240, 300, 80, 110, 25, 35, 120, 150)
    #monday
    day2 = daily_data(240, 480, 100, 130, 80, 80, 300, 360, 90, 120, 25, 35, 40, 70)
    #tuesday
    day3 = daily_data(360, 540, 90, 110, 430, 430, 130, 180, 80, 100, 0, 0, 60, 90)
    #wednesday
    day4 = daily_data(360, 480, 120, 150, 0, 0, 300, 360, 100, 140, 35, 45, 60, 90)
    #thursday
    day5 = daily_data(240, 480, 100, 130, 80, 80, 240, 300, 90, 120, 25, 35, 40, 70)
    #friday
    day6 = daily_data(360, 650, 90, 110, 430, 430, 0, 0, 80, 100, 0, 0, 30, 60)
    #saturday
    day7 = daily_data(360, 650, 120, 150, 0, 0, 180, 240, 100, 140, 25, 35, 100, 130)
    week = []
    for i in range(8):
        week.append((day1[i]+day2[i]+day3[i]+day4[i]+day5[i]+day6[i]+day7[i])/7)
    return week
def fall_semester():
    #sunday
    day1 = daily_data(360, 480, 120, 150, 0, 0, 240, 300, 80, 110, 25, 35, 120, 150)
    #monday
    day2 = daily_data(240, 480, 100, 130, 80, 80, 300, 360, 90, 120, 25, 35, 40, 70)
    #tuesday
    day3 = daily_data(360, 540, 90, 110, 430, 430, 130, 180, 80, 100, 0, 0, 60, 90)
    #wednesday
    day4 = daily_data(360, 480, 120, 150, 0, 0, 300, 360, 100, 140, 35, 45, 60, 90)
    #thursday
    day5 = daily_data(240, 480, 100, 130, 80, 80, 240, 300, 90, 120, 25, 35, 40, 70)
    #friday
    day6 = daily_data(360, 650, 90, 110, 430, 430, 0, 0, 80, 100, 0, 0, 30, 60)
    #saturday
    day7 = daily_data(360, 650, 120, 150, 0, 0, 180, 240, 100, 140, 25, 35, 100, 130)
    week = []
    for i in range(8):
        week.append((day1[i]+day2[i]+day3[i]+day4[i]+day5[i]+day6[i]+day7[i])/7)
    return week
if __name__=="__main__":
    # field names
    fields = ['Month', 'Sleeping', 'Eating', 'Class', 'Homework', 'Hygiene', 'Exercise', 'Chores', 'Fun']
    
    # data rows of csv file
    rows = []
    month = []
    for i in range(0,52):
        if i==0:
            month = vacation()
        if i>0 and i<4:
            week = spring_semester()
            for j in range(len(month)):
                month[j]+=week[j]
            if i==3:
                for j in range(len(month)):
                    month[j]/=4
                month.insert(0, 0)
                rows.append(month)
                month=[]
        if i==4:
            month = spring_semester()
        if i>4 and i<8:
            week = spring_semester()
            for j in range(len(month)):
                month[j]+=week[j]
            if i==7:
                for j in range(len(month)):
                    month[j]/=4
                month.insert(0, 1)
                rows.append(month)
                month=[]
        if i==8:
            month=vacation()
        if i>8 and i<12:
            week = spring_semester()
            for j in range(len(month)):
                month[j]+=week[j]
            if i==11:
                for j in range(len(month)):
                    month[j]/=4
                month.insert(0, 2)
                rows.append(month)
                month=[]
        if i==12:
            month = spring_semester()
        if i>12 and i<16:
            week = spring_semester()
            for j in range(len(month)):
                month[j]+=week[j]
            if i==15:
                for j in range(len(month)):
                    month[j]/=4
                month.insert(0, 3)
                rows.append(month)
                month=[]
        if i==16:
            month = spring_semester()
        if i>16 and i<20:
            week = vacation()
            for j in range(len(month)):
                month[j]+=week[j]
            if i==19:
                for j in range(len(month)):
                    month[j]/=4
                month.insert(0, 4)
                rows.append(month)
                month=[]
        if i==20:
            month = vacation()
        if i>20 and i<25:
            week = vacation()
            for j in range(len(month)):
                month[j]+=week[j]
            if i==24:
                for j in range(len(month)):
                    month[j]/=5
                month.insert(0, 5)
                rows.append(month)
                month=[]
        if i==25:
            month = vacation()
        if i>25 and i<30:
            week = vacation()
            for j in range(len(month)):
                month[j]+=week[j]
            if i==29:
                for j in range(len(month)):
                    month[j]/=5
                month.insert(0, 6)
                rows.append(month)
                month=[]
        if i==30:
            month = fall_semester()
        if i==31:
            week = fall_semester()
            for j in range(len(month)):
                month[j]+=week[j]
        if i>31 and i<35:
            week = vacation()
            for j in range(len(month)):
                month[j]+=week[j]
            if i==34:
                for j in range(len(month)):
                    month[j]/=5
                month.insert(0, 7)
                rows.append(month)
                month=[]
        if i==35:
            month = fall_semester()
        if i>35 and i<40:
            week = fall_semester()
            for j in range(len(month)):
                month[j]+=week[j]
            if i==39:
                for j in range(len(month)):
                    month[j]/=5
                month.insert(0, 8)
                rows.append(month)
                month=[]
        if i==40:
            month = fall_semester()
        if i>40 and i<44:
            week = fall_semester()
            for j in range(len(month)):
                month[j]+=week[j]
            if i==43:
                for j in range(len(month)):
                    month[j]/=4
                month.insert(0, 9)
                rows.append(month)
                month=[]
        if i==44:
            month = vacation()
        if i>44 and i<48:
            week = fall_semester()
            for j in range(len(month)):
                month[j]+=week[j]
            if i==47:
                for j in range(len(month)):
                    month[j]/=4
                month.insert(0, 10)
                rows.append(month)
                month=[]
        if i==48:
            month = fall_semester()
        if i==49:
            week = fall_semester()
            for j in range(len(month)):
                month[j]+=week[j]
        if i>49 and i<52:
            week = vacation()
            for j in range(len(month)):
                month[j]+=week[j]
            if i==51:
                for j in range(len(month)):
                    month[j]/=4
                month.insert(0, 11)
                rows.append(month)
                month=[]
        print("len: ", len(rows), ", i: ", i)
        
    
    # name of csv file
    filename = "cherry_iv_hw6_monthly.csv"
    
    # writing to csv file
    with open(filename, 'w', newline = '') as csvfile:
    	# creating a csv writer object
    	csvwriter = csv.writer(csvfile)
    
    	# writing the fields
    	csvwriter.writerow(fields)
    
    	# writing the data rows
    	csvwriter.writerows(rows)