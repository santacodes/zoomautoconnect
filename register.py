import pandas as pd
import csv

class Data:
    def __init__(self,meeting_id,pwd,date,time,recurring):
        self.meeting_id = meeting_id
        self.pwd = pwd
        self.date = date 
        self.time = time 
        self.recurring = recurring
        
    def input_analysis(self):
        alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 
                    'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',]
        for alphabet in alphabets:
            if (alphabet in self.meeting_id) or (alphabet.upper() in self.meeting_id):
                print('Meeting ID invalid (Contains an alphabet, should consist of only integers)')
                
        with open('meetings.csv','w') as File:
            writer = csv.writer(File, delimiter = ',',
                                quotechar = '"', quoting = csv.QUOTE_MINIMAL)
            writer.writerow()

    def ask(self): 
        id_ask = str(input('Meeting ID: '))
        pwd_ask = str(input('Password: '))
        date_ask = str(input('Date (DD/MM): '))
        time_ask = str(input('Time (hh/mm)'))
        rec_ask = str(input('If Recurring Enter "Y" or else Enter "N"'))
        #Data().input_analysis(id_ask, pwd_ask, date_ask, time_ask, rec_ask)

with open('meetings.csv','r') as file:
    reader = csv.reader(file, delimiter = ',', quotechar = '"')
    for row in reader:
        print(row)
