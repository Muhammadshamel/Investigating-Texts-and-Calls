"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
import numpy as np
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


"""
TASK 1:
How many different telephone numbers are there in the records?
Print a message:
"There are <count> different telephone numbers in the records."
"""
cal = np.array(calls)
txt = np.array(texts)

tot = np.append(cal[:,0:2],txt[:,0:2])

dif_telephone = np.array(np.unique(tot, return_counts=True)).T
no_dif_telephone = len(dif_telephone)


print("There are", no_dif_telephone,"different telephone numbers in the records.")
#print(dif_telephone.shape)
#print(dif_telephone)
