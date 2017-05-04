

#=======================================Data Rows=================================================
# Name
# Registration time
# Triage Start time
# Consult start time
# Consult End Time
# Visit Type
# AH Diagnosis
# Disposition Type
# Admission Time
# Discharge Time
# Discharge Completion
# Number of nights
#=================================================================================================

import random
import csv

Title = ['Name', 'Date', 'Hour', 'Registration Time', 'Triage Start Time', 'Consult Start Time', 'Consult End Time', 'Visit Type', 'Diagonsis', 'Disposition type', 'Admission Time', 'Discharge Time', 'Discharge Completion', 'number of nights']

def writeDay(number, date):
    patientID = 0
    oneDayData = []
    oneDayData.append(Title)
    hourlyNumber = []
    hourlyPercentage = [2.5, 1.8, 1.2,1,1,0.8,1,2.2,4,5.6,7.4,9,8,7,6.5,6.2,5.8,5.5,5,4.5,4.2,3.8,3.5,2.5]
    disChargePercentage = [3.8,3.5,2.5, 2.5, 1.8, 1.2,1,1,0.8,1,2.2,4,5.6,7.4,9,8,7,6.5,6.2,5.8,5.5,5,4.5,4.2]
    hour = 0;
    waitPercentage = [0.01, 0.0, 0.00, 0.0, 0.0, 0.01, 0.01, 0.01, 0.02, 0.03, 0.08, 0.1, 0.18, 0.25, 0.1, 0.03, 0.1, 0.01, 0.02, 0.01, 0.00, 0.01, 0.01, 0.01]
    largerThanSixPercentage = [0.04,0.04,0.04,0.04,0.04,0.09,0.20,0.35,0.38,0.30,0.18,0.12,0.08,0.08,0.07,0.06,0.04,0.04,0.03,0.03,0.03,0.04,0.03]
    currentIndex = 0
    waitNumber = []
    nightsOfStayPercentage = [0.03,0.2,0.23, 0.15, 0.1, 0.07, 0.05, 0.04, 0.03, 0.02, 0.018, 0.017, 0.016, 0.015, 0.014]
    nOfStay = []
    filled = [0]*24
    nOfStayIndex = 0
    nOfStayCount = 0
    for i in range(23):
        percentage=float((random.randint((hourlyPercentage[i]*10-2), (hourlyPercentage[i]*10+2))))/1000
        hourlyNumber.append(int(number*percentage))
        waitNumber.append(int((number-25)*waitPercentage[i]))

    for i in range(len(nightsOfStayPercentage)):
        nOfStay.append(int(number*nightsOfStayPercentage[i]))

    nofStayCount = nOfStay[nOfStayIndex]
    filled[0] = 0
    for index, population in enumerate(hourlyNumber):
        for number in range(population):
            name = "Patient" + str(patientID)
            patientID+=1
            time = random.randint(0,59)
            triageRand = random.randint(0,3)
            consultRand = random.randint(2,8)
            consultEnd = random.randint(15, 60)
            if (i % 13 == 0):
                consultEnd = consultEnd + 60
            largerThanSix = probability(largerThanSixPercentage[hour])
            if (largerThanSix == 0):
                admissionTime = random.randint(6,8)*60
            else:
                if (hour <= 2 and hour >= 0):
                    admissionTime = random.randint(1,2)*60
                elif(hour <= 6 and hour > 2):
                    admissionTime = random.randint(1,2)*60
                elif (hour == 7):
                    admissionTime = random.randint(3,4)*60
                elif (hour == 8):
                    admissionTime = random.randint(3,5)*60
                elif (hour == 9):
                    admissionTime = random.randint(4,5)*60
                elif (hour == 10):
                    admissionTime = random.randint(5,6)*60
                elif (hour == 11):
                    admissionTime = random.randint(4,6)*60
                elif (hour == 12):
                    admissionTime = random.randint(4,6)*60
                elif (hour == 13):
                    admissionTime = random.randint(3,4)*60
                elif (hour >= 14 and hour <= 24):
                    admissionTime = random.randint(1,3)*60

            if currentIndex <= 23:
                # print("Current Number: ", filled[currentIndex], "FUll: ", waitNumber[currentIndex])
                if (filled[currentIndex] == waitNumber[currentIndex]):
                    currentIndex+=1
                else:
                    filled[currentIndex]+=1
            print(currentIndex)
            if (currentIndex == 10):
                dischargeTime = random.randint(3, 5)
            elif (currentIndex == 11):
                dischargeTime = random.randint(5,8)
            elif (currentIndex == 12):
                dischargeTime = random.randint(8,11)
            elif (currentIndex == 13):
                dischargeTime = random.randint(11,15)
            elif (currentIndex == 14):
                dischargeTime = random.randint(15,25)
            elif (currentIndex == 15):
                dischargeTime = random.randint(13,18)
            elif (currentIndex == 16):
                dischargeTime = random.randint(10,12)
            elif (currentIndex == 17):
                dischargeTime = random.randint(4,7)
            elif (currentIndex == 18):
                dischargeTime = random.randint(3,5)
            else:
                dischargeTime = random.randint(1,2)

            if nOfStayIndex < len(nOfStay):
                if nOfStayCount > 0:
                    nOfStayCount-=1
                else:
                    nOfStayIndex+=1
                    nOfStayCount = nOfStay[nOfStayIndex]

            dataRow = [name, date, hour, time, time+triageRand, time+consultRand, time+consultRand+consultEnd, "Vist data", "Diagnostic data", "Data", time+consultRand+consultEnd+admissionTime, currentIndex, dischargeTime, nOfStayIndex]
            oneDayData.append(dataRow)
        hour+=1

    writeFile = open('./data.csv', 'wb')
    writer = csv.writer(writeFile)

    for i in oneDayData:
        writer.writerow(i)
    writeFile.close()

def probability(p):
    i = random.random()
    if i < p:
        return 0
    else:
        return 1

writeDay(400, '04/24/2017')
