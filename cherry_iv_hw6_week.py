# -*- coding: utf-8 -*-
"""
Created on Tue Feb 20 14:03:32 2024

@author: huntie
"""

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
       
def vacation(rows, I):
    day1 = daily_data(360, 650, 100, 130, 0, 0, 0, 0, 100, 140, 25, 35, 40, 150)
    day2 = daily_data(360, 650, 100, 130, 0, 0, 0, 0, 100, 140, 25, 35, 40, 150)
    day3 = daily_data(360, 650, 100, 130, 0, 0, 0, 0, 100, 140, 25, 35, 40, 150)
    day4 = daily_data(360, 650, 100, 130, 0, 0, 0, 0, 100, 140, 25, 35, 40, 150)
    day5 = daily_data(360, 650, 100, 130, 0, 0, 0, 0, 100, 140, 25, 35, 40, 150)
    day6 = daily_data(360, 650, 100, 130, 0, 0, 0, 0, 100, 140, 25, 35, 40, 150)
    day7 = daily_data(360, 650, 100, 130, 0, 0, 0, 0, 100, 140, 25, 35, 40, 150)
    week = [I]
    for i in range(8):
        week.append((day1[i]+day2[i]+day3[i]+day4[i]+day5[i]+day6[i]+day7[i])/7)
    rows.append(week)
def spring_semester(rows, I):
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
    week = [I]
    for i in range(8):
        week.append((day1[i]+day2[i]+day3[i]+day4[i]+day5[i]+day6[i]+day7[i])/7)
    rows.append(week)
def fall_semester(rows, I):
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
    week = [I]
    for i in range(8):
        week.append((day1[i]+day2[i]+day3[i]+day4[i]+day5[i]+day6[i]+day7[i])/7)
    rows.append(week)
if __name__=="__main__":
    # field names
    fields = ['Week', 'Sleeping', 'Eating', 'Class', 'Homework', 'Hygiene', 'Exercise', 'Chores', 'Fun']
    
    # data rows of csv file
    rows = []
    for i in range(0,52):
        if i==0:
            vacation(rows, i)
        if i>0 and i<9:
            spring_semester(rows, i)
        if i==9:
            vacation(rows, i)
        if i>9 and i<17:
            spring_semester(rows, i)
        if i>=17 and i<34:
            vacation(rows, i)
        if i>=34 and i<46:
            fall_semester(rows, i)
        if i==46:
            vacation(rows, i)
        if i>46 and i<50:
            fall_semester(rows, i)
        if i==50 or i==51:
            vacation(rows, i)
        print("len: ", len(rows), ", i: ", i)
        
    
    # name of csv file
    filename = "cherry_iv_hw6_weekly.csv"
    
    # writing to csv file
    with open(filename, 'w', newline = '') as csvfile:
    	# creating a csv writer object
    	csvwriter = csv.writer(csvfile)
    
    	# writing the fields
    	csvwriter.writerow(fields)
    
    	# writing the data rows
    	csvwriter.writerows(rows)