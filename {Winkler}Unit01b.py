#Declarations for Master Transaction File Processing 
masterfile_in = ''
transfile_in = ''
newfile_Out = ''
masterRecord = []
transRecord = []
standard_Master = str()
standard_Transaction = str()
master_Eof = False
transaction_Eof = False
counted_Transaction = 0
total_Transactions = 0
credits_Counted = 0
credits_Totaled = 0
 
#The readMaster function reads the next record from the master file record and then checks for EOF 
def readMaster():
    global masterRecord
    global master_Eof
    global standard_Master
   
    masterRecord = masterfile_in.readline().rstrip('\n').split(',')
   
    if masterRecord[0] == '':
        master_Eof = True
    else:
        standard_Master = masterRecord[0]
 
#This function reads the next record from the transaction file and also checks for EOF  
def readTrans():
    
    global transRecord
    global credits_Counted
    global credits_Totaled
    global transaction_Eof
    global standard_Transaction
   
    transRecord = transfile_in.readline().rstrip('\n').split(',')
   
    if transRecord[0] == '':
        transaction_Eof = True
        
    else:
        standard_Transaction = transRecord[5]
        
 
#This function creates a handle by openeing the two text files and then allowing us to write to a new file
def houseKeeping():
    global masterfile_in
    global transfile_in
    global newfile_Out
   
    masterfile_in = open('VendorMstr.txt', 'r')
    transfile_in = open('VendorTrans.txt', 'r')
    newfile_Out = open('{Winkler}VendorReport.txt', 'w')
 
 
##This function processes the transactions and calculates a new balance
def updateRecords():
    
    global counted_Transaction
    global total_Transactions
    global credits_Counted
    global credits_Totaled
    
    readMaster()
    readTrans()
 
    while (master_Eof == False) and (transaction_Eof == False):
        
        if standard_Master == standard_Transaction:

            if transRecord[3] == 'T':
                counted_Transaction = counted_Transaction + 1
                total_Transactions = total_Transactions + float(transRecord[4])
            else:
                credits_Counted = credits_Counted + 1
                credits_Totaled = credits_Totaled + float(transRecord[4])
           
            # This gets the next Transaction
            readTrans()
           
        else:
       
            if standard_Master < standard_Transaction:
                writeUpdate()
                counted_Transaction = 0
                total_Transactions = 0
                credits_Counted = 0
                credits_Totaled = 0
 
                readMaster()
           
            else:
                errorOutput()
                
                readTrans()

                
                
           
    #This will write the last customers data into the file
    writeUpdate()
    
 
#This function allows writing the customers upgraded record to the file
def writeUpdate():  
    
    outputRec = 'User ID:' + str(masterRecord[0]) + ',' + ' ' + str(masterRecord[1]) + ',' + ' ' + 'Transaction Total:' + str(round(total_Transactions, 2)) + ',' + ' ' + 'Total amount of Transactions:' + str(counted_Transaction) + ',' + ' ' 'Total amount of credits:' + str(round(credits_Totaled, 2)) + ',' + ' ' + 'Total count of credits:' + str(credits_Counted) + '\n'
    newfile_Out.write(outputRec)
    
#This function writes an error to a error file 
def errorOutput():

    errorfile_out = open('{Winkler}ErrorFile.txt', 'w')
    outputRec = str(masterRecord[0]) + ',' + str(masterRecord[1]) + ',' + 'This is a bad transaction'
    errorfile_out.write(outputRec)    

#This finishes up the rest of the programs processing and closes all file handles
def finishUp():
    
    masterfile_in.close()
    transfile_in.close()
    newfile_Out.close()
 
 
def Main():

    houseKeeping()
    updateRecords()
    finishUp()
 
 
if __name__ == '__main__':
    Main()
 
