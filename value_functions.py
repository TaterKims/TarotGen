# File for where number shit and stuff happens

import json
import random
import datetime

def random_value():
    ''' Returns an int between 1 to 78 for card value '''
    
    return random.randint(0, 78)

def date():
    ''' Returns current date as yyyy-mm-dd '''
    
    today = datetime.datetime.now()
    return today.strftime('%Y-%m-%d')

def time():
    ''' Returns current time in hour:minutes '''
    
    now = datetime.datetime.now()
    return now.strftime("%I:%M:%S %p")

def value_log(date, time, value):
    ''' Records the value to values_log.json. The top level object MUST be a list and not a dictionary'''
    
    with open('value_log.json', 'r') as log_file:
        logs = json.load(log_file)
        
    with open('value_log.json', 'w') as log:
        entry = {"date" : date, "time" : time, "value" : value}
        logs.append(entry)
        json.dump(logs, log, indent=4)
    
    return

def compare_previous(value):
    ''' Compare a value to values stored in a json log. If value is identical, returns True '''
    
    log = open('value_log.json')
    l = json.load(log)
    
    # This was a pain
    entries = [entry.items() for entry in l] # Gets a list of tuples
    itm = [tuple(items[1] for items in entry) for entry in entries[:]] # Gets the 2nd element of every tuple
    items = [itms[2] for itms in itm] # Gets the 3rd element of every 2nd item in every tuple
    
    for item in items:
        if item == value:
            result = True
        else:
            result = False
    
    return result
