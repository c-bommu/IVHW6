import csv
import random

monthlySunday = [[0]*12 for _ in range(8)]
yearlySunday = [[0]*52 for _ in range(8)]
monthlyMonday = [[0]*12 for _ in range(8)]
yearlyMonday = [[0]*52 for _ in range(8)]
monthlyTuesday = [[0]*12 for _ in range(8)]
yearlyTuesday = [[0]*52 for _ in range(8)]
monthlyWednesday = [[0]*12 for _ in range(8)]
yearlyWednesday = [[0]*52 for _ in range(8)]
monthlyThursday = [[0]*12 for _ in range(8)]
yearlyThursday = [[0]*52 for _ in range(8)]
monthlyFriday = [[0]*12 for _ in range(8)]
yearlyFriday = [[0]*52 for _ in range(8)]
monthlySaturday = [[0]*12 for _ in range(8)]
yearlySaturday = [[0]*52 for _ in range(8)]

with open('yearMinutesData.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Day', 'Sleeping', 'Eating', 'Class', 'Homework', 'Hygiene', 'Exercise', 'Chores', 'Fun'])
    
    tmp_week = 0
    month = 0
    
    num_all_nighters = random.randint(0, 6)
    all_nighter_weeks = []
    for i in range(0, num_all_nighters):
        all_nighter_weeks.append(random.randint(1, 52))
    
    FourWeekSunday = [[0]*4 for _ in range(8)]
    FourWeekMonday = [[0]*4 for _ in range(8)]
    FourWeekTuesday = [[0]*4 for _ in range(8)]
    FourWeekWednesday = [[0]*4 for _ in range(8)]
    FourWeekThursday = [[0]*4 for _ in range(8)]
    FourWeekFriday = [[0]*4 for _ in range(8)]
    FourWeekSaturday = [[0]*4 for _ in range(8)]
    
    for week in range(1, 52):
        
        all_nighter_day = 0
        if (len(all_nighter_weeks) != 0 and week == all_nighter_weeks[len(all_nighter_weeks)-1]):
            all_nighter_day = random.randint(1, 8)
            all_nighter_weeks.pop()

        sleepSunday = random.randint(360, 480)
        FourWeekSunday[0][tmp_week] = sleepSunday
        yearlySunday[0][week-1] = sleepSunday
        eatSunday = random.randint(120, 150)
        FourWeekSunday[1][tmp_week] = eatSunday
        yearlySunday[1][week-1] = eatSunday
        classSunday = 0
        FourWeekSunday[2][tmp_week] = classSunday
        yearlySunday[2][week-1] = classSunday
        homeworkSunday = random.randint(240, 300)
        FourWeekSunday[3][tmp_week] = homeworkSunday
        yearlySunday[3][week-1] = homeworkSunday
        hygieneSunday = random.randint(80, 110)
        FourWeekSunday[4][tmp_week] = hygieneSunday
        yearlySunday[4][week-1] = hygieneSunday
        exerciseSunday = random.randint(25, 35)
        FourWeekSunday[5][tmp_week] = exerciseSunday
        yearlySunday[5][week-1] = exerciseSunday
        choresSunday = random.randint(120, 150)
        FourWeekSunday[6][tmp_week] = choresSunday
        yearlySunday[6][week-1] = choresSunday
        funSunday = 1440 - (sleepSunday + eatSunday + classSunday + homeworkSunday + hygieneSunday + exerciseSunday + choresSunday)
        FourWeekSunday[7][tmp_week] = funSunday
        yearlySunday[7][week-1] = funSunday
        if (all_nighter_day == 1):
            homeworkSunday += sleepSunday
            FourWeekSunday[3][tmp_week] = homeworkSunday
            yearlySunday[3][week-1] = homeworkSunday
            
            sleepSunday = 0
            FourWeekSunday[0][tmp_week] = sleepSunday
            yearlySunday[0][week-1] = sleepSunday
        writer.writerow(['Sunday', sleepSunday, eatSunday, classSunday, homeworkSunday, hygieneSunday, exerciseSunday, choresSunday, funSunday])
        
        sleepMonday = random.randint(240, 480)
        FourWeekMonday[0][tmp_week] = sleepMonday
        yearlyMonday[0][week-1] = sleepMonday
        eatMonday = random.randint(100, 130)
        FourWeekMonday[1][tmp_week] = eatMonday
        yearlyMonday[1][week-1] = eatMonday
        classMonday = 80
        FourWeekMonday[2][tmp_week] = classMonday
        yearlyMonday[2][week-1] = classMonday
        homeworkMonday = random.randint(300, 360)
        FourWeekMonday[3][tmp_week] = homeworkMonday
        yearlyMonday[3][week-1] = homeworkMonday
        hygieneMonday = random.randint(90, 120)
        FourWeekMonday[4][tmp_week] = hygieneMonday
        yearlyMonday[4][week-1] = hygieneMonday
        exerciseMonday = random.randint(25, 35)
        FourWeekMonday[5][tmp_week] = exerciseMonday
        yearlyMonday[5][week-1] = exerciseMonday
        choresMonday = random.randint(40, 70)
        FourWeekMonday[6][tmp_week] = choresMonday
        yearlyMonday[6][week-1] = choresMonday
        funMonday = 1440 - (sleepMonday + eatMonday + classMonday + homeworkMonday + hygieneMonday + exerciseMonday + choresMonday)
        FourWeekMonday[7][tmp_week] = funMonday
        yearlyMonday[7][week-1] = funMonday
        if (all_nighter_day == 2):
            homeworkMonday += sleepMonday
            FourWeekMonday[3][tmp_week] = homeworkMonday
            yearlyMonday[3][week-1] = homeworkMonday
            
            sleepMonday = 0
            FourWeekMonday[0][tmp_week] = sleepMonday
            yearlyMonday[0][week-1] = sleepMonday 
        writer.writerow(['Monday', sleepMonday, eatMonday, classMonday, homeworkMonday, hygieneMonday, exerciseMonday, choresMonday, funMonday])
        
        sleepTuesday = random.randint(360, 540)
        FourWeekTuesday[0][tmp_week] = sleepTuesday
        yearlyTuesday[0][week-1] = sleepTuesday
        eatTuesday = random.randint(90, 110)
        FourWeekTuesday[1][tmp_week] = eatTuesday
        yearlyTuesday[1][week-1] = eatTuesday
        classTuesday = 430
        FourWeekTuesday[2][tmp_week] = classTuesday
        yearlyTuesday[2][week-1] = classTuesday
        homeworkTuesday = random.randint(130, 180)
        FourWeekTuesday[3][tmp_week] = homeworkTuesday
        yearlyTuesday[3][week-1] = homeworkTuesday
        hygieneTuesday = random.randint(80, 100)
        FourWeekTuesday[4][tmp_week] = hygieneTuesday
        yearlyTuesday[4][week-1] = hygieneTuesday
        exerciseTuesday = 0
        FourWeekTuesday[5][tmp_week] = exerciseTuesday
        yearlyTuesday[5][week-1] = exerciseTuesday
        choresTuesday = random.randint(60, 90)
        FourWeekTuesday[6][tmp_week] = choresTuesday
        yearlyTuesday[6][week-1] = choresTuesday
        funTuesday = 1440 - (sleepTuesday + eatTuesday + classTuesday + homeworkTuesday + hygieneTuesday + exerciseTuesday + choresTuesday)
        FourWeekTuesday[7][tmp_week] = funTuesday
        yearlyTuesday[7][week-1] = funTuesday
        if (all_nighter_day == 3):
            homeworkTuesday += sleepTuesday
            FourWeekTuesday[3][tmp_week] = homeworkTuesday
            yearlyTuesday[3][week-1] = homeworkTuesday
            
            sleepTuesday = 0
            FourWeekTuesday[0][tmp_week] = sleepTuesday
            yearlyTuesday[0][week-1] = sleepTuesday 
        writer.writerow(['Tuesday', sleepTuesday, eatTuesday, classTuesday, homeworkTuesday, hygieneTuesday, exerciseTuesday, choresTuesday, funTuesday])
        
        sleepWednesday = random.randint(360, 480)
        FourWeekWednesday[0][tmp_week] = sleepWednesday
        yearlyWednesday[0][week-1] = sleepWednesday
        eatWednesday = random.randint(120, 150)
        FourWeekWednesday[1][tmp_week] = eatWednesday
        yearlyWednesday[1][week-1] = eatWednesday
        classWednesday = 0
        FourWeekWednesday[2][tmp_week] = classWednesday
        yearlyWednesday[2][week-1] = classWednesday
        homeworkWednesday = random.randint(300, 360)
        FourWeekWednesday[3][tmp_week] = homeworkWednesday
        yearlyWednesday[3][week-1] = homeworkWednesday
        hygieneWednesday = random.randint(100, 140)
        FourWeekWednesday[4][tmp_week] = hygieneWednesday
        yearlyWednesday[4][week-1] = hygieneWednesday
        exerciseWednesday = random.randint(35, 45)
        FourWeekWednesday[5][tmp_week] = exerciseWednesday
        yearlyWednesday[5][week-1] = exerciseWednesday
        choresWednesday = random.randint(60, 90)
        FourWeekWednesday[6][tmp_week] = choresWednesday
        yearlyWednesday[6][week-1] = choresWednesday
        funWednesday = 1440 - (sleepWednesday + eatWednesday + classWednesday + homeworkWednesday + hygieneWednesday + exerciseWednesday + choresWednesday)
        FourWeekWednesday[7][tmp_week] = funWednesday
        yearlyWednesday[7][week-1] = funWednesday
        if (all_nighter_day == 4):
            homeworkWednesday += sleepWednesday
            FourWeekWednesday[3][tmp_week] = homeworkWednesday
            yearlyWednesday[3][week-1] = homeworkWednesday
            
            sleepWednesday = 0
            FourWeekWednesday[0][tmp_week] = sleepWednesday
            yearlyWednesday[0][week-1] = sleepWednesday 
        writer.writerow(['Wednesday', sleepWednesday, eatWednesday, classWednesday, homeworkWednesday, hygieneWednesday, exerciseWednesday, choresWednesday, funWednesday])
        
        sleepThursday = random.randint(240, 480)
        FourWeekThursday[0][tmp_week] = sleepThursday
        yearlyThursday[0][week-1] = sleepThursday
        eatThursday = random.randint(100, 130)
        FourWeekThursday[1][tmp_week] = eatThursday
        yearlyThursday[1][week-1] = eatThursday
        classThursday = 80
        FourWeekThursday[2][tmp_week] = classThursday
        yearlyThursday[2][week-1] = classThursday
        homeworkThursday = random.randint(240, 300)
        FourWeekThursday[3][tmp_week] = homeworkThursday
        yearlyThursday[3][week-1] = homeworkThursday
        hygieneThursday = random.randint(90, 120)
        FourWeekThursday[4][tmp_week] = hygieneThursday
        yearlyThursday[4][week-1] = hygieneThursday
        exerciseThursday = random.randint(25, 35)
        FourWeekThursday[5][tmp_week] = exerciseThursday
        yearlyThursday[5][week-1] = exerciseThursday
        choresThursday = random.randint(40, 70)
        FourWeekThursday[6][tmp_week] = choresThursday
        yearlyThursday[6][week-1] = choresThursday
        funThursday = 1440 - (sleepThursday + eatThursday + classThursday + homeworkThursday + hygieneThursday + exerciseThursday + choresThursday)
        FourWeekThursday[7][tmp_week] = funThursday
        yearlyThursday[7][week-1] = funThursday
        if (all_nighter_day == 5):
            homeworkThursday += sleepThursday
            FourWeekThursday[3][tmp_week] = homeworkThursday
            yearlyThursday[3][week-1] = homeworkThursday
            
            sleepThursday = 0
            FourWeekThursday[0][tmp_week] = sleepThursday
            yearlyThursday[0][week-1] = sleepThursday 
        writer.writerow(['Thursday', sleepThursday, eatThursday, classThursday, homeworkThursday, hygieneThursday, exerciseThursday, choresThursday, funThursday])
        
        sleepFriday = random.randint(360, 650)
        FourWeekFriday[0][tmp_week] = sleepFriday
        yearlyFriday[0][week-1] = sleepFriday
        eatFriday = random.randint(90, 110)
        FourWeekFriday[1][tmp_week] = eatFriday
        yearlyFriday[1][week-1] = eatFriday
        classFriday = 430
        FourWeekFriday[2][tmp_week] = classFriday
        yearlyFriday[2][week-1] = classFriday
        homeworkFriday = 0
        FourWeekFriday[3][tmp_week] = homeworkFriday
        yearlyFriday[3][week-1] = homeworkFriday
        hygieneFriday = random.randint(80, 100)
        FourWeekFriday[4][tmp_week] = hygieneFriday
        yearlyFriday[4][week-1] = hygieneFriday
        exerciseFriday = 0
        FourWeekFriday[5][tmp_week] = exerciseFriday
        yearlyFriday[5][week-1] = exerciseFriday
        choresFriday = random.randint(30, 60)
        FourWeekFriday[6][tmp_week] = choresFriday
        yearlyFriday[6][week-1] = choresFriday
        funFriday = 1440 - (sleepFriday + eatFriday + classFriday + homeworkFriday + hygieneFriday + exerciseFriday + choresFriday)
        FourWeekFriday[7][tmp_week] = funFriday
        yearlyFriday[7][week-1] = funFriday
        if (all_nighter_day == 6):
            homeworkFriday += sleepFriday
            FourWeekFriday[3][tmp_week] = homeworkFriday
            yearlyFriday[3][week-1] = homeworkFriday
            
            sleepFriday = 0
            FourWeekFriday[0][tmp_week] = sleepFriday
            yearlyFriday[0][week-1] = sleepFriday 
        writer.writerow(['Friday', sleepFriday, eatFriday, classFriday, homeworkFriday, hygieneFriday, exerciseFriday, choresFriday, funFriday])
        
        sleepSaturday = random.randint(360, 650)
        FourWeekSaturday[0][tmp_week] = sleepSaturday
        yearlySaturday[0][week-1] = sleepSaturday
        eatSaturday = random.randint(120, 150)
        FourWeekSaturday[1][tmp_week] = eatSaturday
        yearlySaturday[1][week-1] = eatSaturday
        classSaturday = 0
        FourWeekSaturday[2][tmp_week] = classSaturday
        yearlySaturday[2][week-1] = classSaturday
        homeworkSaturday = random.randint(180, 240)
        FourWeekSaturday[3][tmp_week] = homeworkSaturday
        yearlySaturday[3][week-1] = homeworkSaturday
        hygieneSaturday = random.randint(100, 140)
        FourWeekSaturday[4][tmp_week] = hygieneSaturday
        yearlySaturday[4][week-1] = hygieneSaturday
        exerciseSaturday = random.randint(25, 35)
        FourWeekSaturday[5][tmp_week] = exerciseSaturday
        yearlySaturday[5][week-1] = exerciseSaturday
        choresSaturday = random.randint(100, 130)
        FourWeekSaturday[6][tmp_week] = choresSaturday
        yearlySaturday[6][week-1] = choresSaturday
        funSaturday = 1440 - (sleepSaturday + eatSaturday + classSaturday + homeworkSaturday + hygieneSaturday + exerciseSaturday + choresSaturday)
        FourWeekSaturday[7][tmp_week] = funSaturday
        yearlySaturday[7][week-1] = funSaturday
        if (all_nighter_day == 7):
            homeworkSaturday += sleepSaturday
            FourWeekSaturday[3][tmp_week] = homeworkSaturday
            yearlySaturday[3][week-1] = homeworkSaturday
            
            sleepSaturday = 0
            FourWeekSaturday[0][tmp_week] = sleepSaturday
            yearlySaturday[0][week-1] = sleepSaturday 
        writer.writerow(['Saturday', sleepSaturday, eatSaturday, classSaturday, homeworkSaturday, hygieneSaturday, exerciseSaturday, choresSaturday, funSaturday])
        
        tmp_week += 1
        
        if tmp_week == 4:
            monthlySunday[0][month] = sum(FourWeekSunday[0])/len(FourWeekSunday[0])
            monthlySunday[1][month] = sum(FourWeekSunday[1])/len(FourWeekSunday[1])
            monthlySunday[2][month] = sum(FourWeekSunday[2])/len(FourWeekSunday[2])
            monthlySunday[3][month] = sum(FourWeekSunday[3])/len(FourWeekSunday[3])
            monthlySunday[4][month] = sum(FourWeekSunday[4])/len(FourWeekSunday[4])
            monthlySunday[5][month] = sum(FourWeekSunday[5])/len(FourWeekSunday[5])
            monthlySunday[6][month] = sum(FourWeekSunday[6])/len(FourWeekSunday[6])
            monthlySunday[7][month] = sum(FourWeekSunday[7])/len(FourWeekSunday[7])
            
            monthlyMonday[0][month] = sum(FourWeekMonday[0])/len(FourWeekMonday[0])
            monthlyMonday[1][month] = sum(FourWeekMonday[1])/len(FourWeekMonday[1])
            monthlyMonday[2][month] = sum(FourWeekMonday[2])/len(FourWeekMonday[2])
            monthlyMonday[3][month] = sum(FourWeekMonday[3])/len(FourWeekMonday[3])
            monthlyMonday[4][month] = sum(FourWeekMonday[4])/len(FourWeekMonday[4])
            monthlyMonday[5][month] = sum(FourWeekMonday[5])/len(FourWeekMonday[5])
            monthlyMonday[6][month] = sum(FourWeekMonday[6])/len(FourWeekMonday[6])
            monthlyMonday[7][month] = sum(FourWeekMonday[7])/len(FourWeekMonday[7])
            
            monthlyTuesday[0][month] = sum(FourWeekTuesday[0])/len(FourWeekTuesday[0])
            monthlyTuesday[1][month] = sum(FourWeekTuesday[1])/len(FourWeekTuesday[1])
            monthlyTuesday[2][month] = sum(FourWeekTuesday[2])/len(FourWeekTuesday[2])
            monthlyTuesday[3][month] = sum(FourWeekTuesday[3])/len(FourWeekTuesday[3])
            monthlyTuesday[4][month] = sum(FourWeekTuesday[4])/len(FourWeekTuesday[4])
            monthlyTuesday[5][month] = sum(FourWeekTuesday[5])/len(FourWeekTuesday[5])
            monthlyTuesday[6][month] = sum(FourWeekTuesday[6])/len(FourWeekTuesday[6])
            monthlyTuesday[7][month] = sum(FourWeekTuesday[7])/len(FourWeekTuesday[7])
            
            monthlyWednesday[0][month] = sum(FourWeekWednesday[0])/len(FourWeekWednesday[0])
            monthlyWednesday[1][month] = sum(FourWeekWednesday[1])/len(FourWeekWednesday[1])
            monthlyWednesday[2][month] = sum(FourWeekWednesday[2])/len(FourWeekWednesday[2])
            monthlyWednesday[3][month] = sum(FourWeekWednesday[3])/len(FourWeekWednesday[3])
            monthlyWednesday[4][month] = sum(FourWeekWednesday[4])/len(FourWeekWednesday[4])
            monthlyWednesday[5][month] = sum(FourWeekWednesday[5])/len(FourWeekWednesday[5])
            monthlyWednesday[6][month] = sum(FourWeekWednesday[6])/len(FourWeekWednesday[6])
            monthlyWednesday[7][month] = sum(FourWeekWednesday[7])/len(FourWeekWednesday[7])
            
            monthlyThursday[0][month] = sum(FourWeekThursday[0])/len(FourWeekThursday[0])
            monthlyThursday[1][month] = sum(FourWeekThursday[1])/len(FourWeekThursday[1])
            monthlyThursday[2][month] = sum(FourWeekThursday[2])/len(FourWeekThursday[2])
            monthlyThursday[3][month] = sum(FourWeekThursday[3])/len(FourWeekThursday[3])
            monthlyThursday[4][month] = sum(FourWeekThursday[4])/len(FourWeekThursday[4])
            monthlyThursday[5][month] = sum(FourWeekThursday[5])/len(FourWeekThursday[5])
            monthlyThursday[6][month] = sum(FourWeekThursday[6])/len(FourWeekThursday[6])
            monthlyThursday[7][month] = sum(FourWeekThursday[7])/len(FourWeekThursday[7])
            
            monthlyFriday[0][month] = sum(FourWeekFriday[0])/len(FourWeekFriday[0])
            monthlyFriday[0][month] = sum(FourWeekFriday[0])/len(FourWeekFriday[0])
            monthlyFriday[0][month] = sum(FourWeekFriday[0])/len(FourWeekFriday[0])
            monthlyFriday[1][month] = sum(FourWeekFriday[1])/len(FourWeekFriday[1])
            monthlyFriday[2][month] = sum(FourWeekFriday[2])/len(FourWeekFriday[2])
            monthlyFriday[3][month] = sum(FourWeekFriday[3])/len(FourWeekFriday[3])
            monthlyFriday[4][month] = sum(FourWeekFriday[4])/len(FourWeekFriday[4])
            monthlyFriday[5][month] = sum(FourWeekFriday[5])/len(FourWeekFriday[5])
            monthlyFriday[6][month] = sum(FourWeekFriday[6])/len(FourWeekFriday[6])
            monthlyFriday[7][month] = sum(FourWeekFriday[7])/len(FourWeekFriday[7])
            
            monthlySaturday[0][month] = sum(FourWeekSaturday[0])/len(FourWeekSaturday[0])
            monthlySaturday[1][month] = sum(FourWeekSaturday[1])/len(FourWeekSaturday[1])
            monthlySaturday[2][month] = sum(FourWeekSaturday[2])/len(FourWeekSaturday[2])
            monthlySaturday[3][month] = sum(FourWeekSaturday[3])/len(FourWeekSaturday[3])
            monthlySaturday[4][month] = sum(FourWeekSaturday[4])/len(FourWeekSaturday[4])
            monthlySaturday[5][month] = sum(FourWeekSaturday[5])/len(FourWeekSaturday[5])
            monthlySaturday[6][month] = sum(FourWeekSaturday[6])/len(FourWeekSaturday[6])
            monthlySaturday[7][month] = sum(FourWeekSaturday[7])/len(FourWeekSaturday[7])
            
            tmp_week = 0
            month += 1

with open('monthMinutesData.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Day', 'Sleeping', 'Eating', 'Class', 'Homework', 'Hygiene', 'Exercise', 'Chores', 'Fun'])
    for i in range(0, 12):
        writer.writerow(['Sunday', monthlySunday[0][i], monthlySunday[1][i], monthlySunday[2][i], monthlySunday[3][i], monthlySunday[4][i], monthlySunday[5][i], monthlySunday[6][i], monthlySunday[7][i]])
        writer.writerow(['Monday', monthlyMonday[0][i], monthlyMonday[1][i], monthlyMonday[2][i], monthlyMonday[3][i], monthlyMonday[4][i], monthlyMonday[5][i], monthlyMonday[6][i], monthlyMonday[7][i]])
        writer.writerow(['Tuesday', monthlyTuesday[0][i], monthlyTuesday[1][i], monthlyTuesday[2][i], monthlyTuesday[3][i], monthlyTuesday[4][i], monthlyTuesday[5][i], monthlyTuesday[6][i], monthlyTuesday[7][i]])
        writer.writerow(['Wednesday', monthlyWednesday[0][i], monthlyWednesday[1][i], monthlyWednesday[2][i], monthlyWednesday[3][i], monthlyWednesday[4][i], monthlyWednesday[5][i], monthlyWednesday[6][i], monthlyWednesday[7][i]])
        writer.writerow(['Thursday', monthlyThursday[0][i], monthlyThursday[1][i], monthlyThursday[2][i], monthlyThursday[3][i], monthlyThursday[4][i], monthlyThursday[5][i], monthlyThursday[6][i], monthlyThursday[7][i]])
        writer.writerow(['Friday', monthlyFriday[0][i], monthlyFriday[1][i], monthlyFriday[2][i], monthlyFriday[3][i], monthlyFriday[4][i], monthlyFriday[5][i], monthlyFriday[6][i], monthlyFriday[7][i]])
        writer.writerow(['Saturday', monthlySaturday[0][i], monthlySaturday[1][i], monthlySaturday[2][i], monthlySaturday[3][i], monthlySaturday[4][i], monthlySaturday[5][i], monthlySaturday[6][i], monthlySaturday[7][i]])
    
    
with open('dayMinutesData.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Day', 'Sleeping', 'Eating', 'Class', 'Homework', 'Hygiene', 'Exercise', 'Chores', 'Fun'])
    writer.writerow(['Sunday', sum(yearlySunday[0])/len(yearlySunday[0]), sum(yearlySunday[1])/len(yearlySunday[1]),
                    sum(yearlySunday[2])/len(yearlySunday[2]), sum(yearlySunday[3])/len(yearlySunday[3]), 
                    sum(yearlySunday[4])/len(yearlySunday[4]), sum(yearlySunday[5])/len(yearlySunday[5]), 
                    sum(yearlySunday[6])/len(yearlySunday[6]), sum(yearlySunday[7])/len(yearlySunday[7])])
    writer.writerow(['Monday', sum(yearlyMonday[0])/len(yearlyMonday[0]), sum(yearlyMonday[1])/len(yearlyMonday[1]),
                    sum(yearlyMonday[2])/len(yearlyMonday[2]), sum(yearlyMonday[3])/len(yearlyMonday[3]), 
                    sum(yearlyMonday[4])/len(yearlyMonday[4]), sum(yearlyMonday[5])/len(yearlyMonday[5]), 
                    sum(yearlyMonday[6])/len(yearlyMonday[6]), sum(yearlyMonday[7])/len(yearlyMonday[7])])
    writer.writerow(['Tuesday', sum(yearlyTuesday[0])/len(yearlyTuesday[0]), sum(yearlyTuesday[1])/len(yearlyTuesday[1]),
                    sum(yearlyTuesday[2])/len(yearlyTuesday[2]), sum(yearlyTuesday[3])/len(yearlyTuesday[3]), 
                    sum(yearlyTuesday[4])/len(yearlyTuesday[4]), sum(yearlyTuesday[5])/len(yearlyTuesday[5]), 
                    sum(yearlyTuesday[6])/len(yearlyTuesday[6]), sum(yearlyTuesday[7])/len(yearlyTuesday[7])])
    writer.writerow(['Wednesday', sum(yearlyWednesday[0])/len(yearlyWednesday[0]), sum(yearlyWednesday[1])/len(yearlyWednesday[1]),
                    sum(yearlyWednesday[2])/len(yearlyWednesday[2]), sum(yearlyWednesday[3])/len(yearlyWednesday[3]), 
                    sum(yearlyWednesday[4])/len(yearlyWednesday[4]), sum(yearlyWednesday[5])/len(yearlyWednesday[5]), 
                    sum(yearlyWednesday[6])/len(yearlyWednesday[6]), sum(yearlyWednesday[7])/len(yearlyWednesday[7])])
    writer.writerow(['Thursday', sum(yearlyThursday[0])/len(yearlyThursday[0]), sum(yearlyThursday[1])/len(yearlyThursday[1]),
                    sum(yearlyThursday[2])/len(yearlyThursday[2]), sum(yearlyThursday[3])/len(yearlyThursday[3]), 
                    sum(yearlyThursday[4])/len(yearlyThursday[4]), sum(yearlyThursday[5])/len(yearlyThursday[5]), 
                    sum(yearlyThursday[6])/len(yearlyThursday[6]), sum(yearlyThursday[7])/len(yearlyThursday[7])])
    writer.writerow(['Friday', sum(yearlyFriday[0])/len(yearlyFriday[0]), sum(yearlyFriday[1])/len(yearlyFriday[1]),
                    sum(yearlyFriday[2])/len(yearlyFriday[2]), sum(yearlyFriday[3])/len(yearlyFriday[3]), 
                    sum(yearlyFriday[4])/len(yearlyFriday[4]), sum(yearlyFriday[5])/len(yearlyFriday[5]), 
                    sum(yearlyFriday[6])/len(yearlyFriday[6]), sum(yearlyFriday[7])/len(yearlyFriday[7])])
    writer.writerow(['Saturday', sum(yearlySaturday[0])/len(yearlySaturday[0]), sum(yearlySaturday[1])/len(yearlySaturday[1]),
                    sum(yearlySaturday[2])/len(yearlySaturday[2]), sum(yearlySaturday[3])/len(yearlySaturday[3]), 
                    sum(yearlySaturday[4])/len(yearlySaturday[4]), sum(yearlySaturday[5])/len(yearlySaturday[5]), 
                    sum(yearlySaturday[6])/len(yearlySaturday[6]), sum(yearlySaturday[7])/len(yearlySaturday[7])])