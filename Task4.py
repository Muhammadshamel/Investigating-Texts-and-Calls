"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""
def getSalesPhone(calllist, textlist):


    call_out_list = []
    except_list = []
    result_list = []
    for callline in calllist:
        call_out_list.append(callline[0])
        except_list.append(callline[1])

    for textline in textlist:
        except_list.append(textline[0])
        except_list.append(textline[1])

    for call_num in call_out_list:
        if call_num not in except_list:
            result_list.append(call_num)

    return result_list


result_list = list(set(getSalesPhone(calls, texts)))
result_list.sort()
print('These numbers could be telemarketers:')
for result in result_list:
    print(result)
