#Declaring my Variables to use in Merge Program below

cins_File = ''
pbis_File = ''
merged_File = ''
pbis_Record = []
cins_Record = []
bothFilesEnd = 'N'
last_name = 'ZZZZZ'
stu_Cins_Count = 0
stu_Pbis_Count = 0
tot_Rec_Count = 0
gpa_For_Cins = float()
gpa_For_Pbis = float()
cins_Average = float()
pbis_Average = float()


#Below is a program that is merging two different .txt files, while getting GPA averages and different counts for students
#in each major as well as a total of students in all majors.
open_CINS = open('CINSMajors.txt','r')

for line in open_CINS:
        record_C_GPA = (line.rstrip('\n').split(','))
        cins_Line_Count = 0
        cins_Line_Count += 1
        gpa_For_Cins = gpa_For_Cins + float(record_C_GPA[3])
cins_Average = gpa_For_Cins / cins_Line_Count



open_PBIS = open('PBISMajors.txt','r')

for line in open_PBIS:
    record_P_GPA = (line.rstrip('\n').split(','))
    pbis_Line_Count = 0
    pbis_Line_Count += 1
    gpa_For_Pbis = gpa_For_Pbis + float(record_P_GPA[3])
pbis_Average = gpa_For_Pbis / pbis_Line_Count 
add_Total_GPAs = gpa_For_Cins + gpa_For_Pbis

#The ReadCins function is reading the first .txt file given to us
def ReadCins(cins_File):
    cins_Record = (cins_File.readline().rstrip('\n').split(','))
    if cins_Record[0] == '':
        cins_Record[0] = last_name

    return cins_Record

#The ReadPbis function does the same as the ReadCins but is reading the second .txt file instead of the first
def ReadPbis(pbis_File):
    pbis_Record = (pbis_File.readline().rstrip('\n').split(','))
    if pbis_Record[0]== '':
        pbis_Record[0] = last_name

    return pbis_Record

#The CheckEnd function is used to see if either file is at the end of the data written in the .txt files
def CheckEnd(cins_Record, pbis_Record):
    if cins_Record[0] == last_name:
        if pbis_Record[0] == last_name:
            return True

    return False

#The GetReady function below is reading each file as stated below. After it has read the .txt files the variable
#merged_File is used to write(create) a file named DeptStudentMerge. 
def GetReady():
    cins_File = open('CINSMajors.txt','r')
    pbis_File = open('PBISMajors.txt','r')
    merged_File = open('DeptStudentMerge.txt','w')

    return cins_File, pbis_File, merged_File

#The MergedRecords function merges both .txt files according the lowest studentID number. A while loop is used to compare each
#individual record and put the lesser number next into the newly created merge file. We input a counter inside the function
#to count the number of records and the average .
def MergedRecords(cins_File, pbis_File, merged_File):
    global stu_Pbis_Count
    global stu_Cins_Count
    global tot_Rec_Count
    global avg_GPAs
    outputLine = str()
    cins_Record = ReadCins(cins_File)
    pbis_Record = ReadPbis(pbis_File)
    bothFilesEnd = CheckEnd(cins_Record, pbis_Record)

    while bothFilesEnd == False:
        if cins_Record[0] < pbis_Record[0]:
            outputLine = cins_Record[0] + ',' + str(cins_Record[1]) + ',' + str(cins_Record[2]) + ',' + str(cins_Record[3]) + '\n'
            cins_Record = ReadCins(cins_File)
            stu_Cins_Count = stu_Cins_Count + 1
        else:
            outputLine = pbis_Record[0] + ',' + str(pbis_Record[1]) + ',' + str(pbis_Record[2]) + ',' + str(pbis_Record[3]) + '\n'
            pbis_Record = ReadPbis(pbis_File)
            stu_Pbis_Count = stu_Pbis_Count + 1
 
        tot_Rec_Count = tot_Rec_Count + 1
        avg_GPAs = add_Total_GPAs / tot_Rec_Count
        merged_File.write(outputLine)
        bothFilesEnd = CheckEnd(cins_Record, pbis_Record)

    

#FinishUp function closes the files 
def FinishUp(cins_File, pbis_File, merged_File):
    cins_File.close()
    pbis_File.close()
    merged_File.close()


#The OutputData Funcion prints all of the things we are trying to find in the directions for this program. I used append to
#add to the DeptStudentMerge.txt file
def OutputData():
    merged_File = open('DeptStudentMerge.txt','a+')
    merged_File.write('\n')
    merged_File.write(str(stu_Cins_Count) + " " + "students are currently CINS Majors" + '\n')
    merged_File.write(str(stu_Pbis_Count) + " " + "students are currently PBIS Majors" + '\n')
    merged_File.write(str(tot_Rec_Count) + " " + " is the total amount of students that are in both of the majors" + '\n')
    merged_File.write((str(round(cins_Average,2))) + '\n')
    merged_File.write((str(pbis_Average)) + '\n')
    merged_File.write(str(round(avg_GPAs,2))) 
    

#Here we are defining the MainLine Logic of the program and inside is other functions we definied so when the program
#is ran it runs in the order i want it to.
def Main(): 
    cins_File, pbis_File, merged_File = GetReady()
    MergedRecords(cins_File, pbis_File, merged_File)
    FinishUp(cins_File, pbis_File, merged_File)

    OutputData()
if __name__== '__main__':
    Main()

