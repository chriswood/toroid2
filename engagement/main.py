#!/usr/bin/env python
# encoding: utf-8
"""
main.py

Created by Chris Wood on 2010-08-15.
Copyright (c) 2010 __MyCompanyName__. All rights reserved.
"""

import sys
import os
import string
from engagement import CriteriaBuild
import django

def main():
    criteria = {
        'opens' : 2,
        'clicks' : 30,
        'shares' : 10,
    }
    response = CriteriaBuild(criteria)
    print(response.data)
    #So at this point I have my criteria (pre-defined) with corresponding 
    #weights as applied by the CriteriaBuild class
    #The next step is to apply these to users and the desired events
    events = get_event_list(5)
    users = get_user_list(5)
    
    #So for each event, each user has 3 criteria represented
    #from the example in README
    #I'll represent each event response with a 1,0
    user_data = get_user_data(events, users)
    
    #I have each user's response data, and I want to apply the weight function to each
    for user in user_data:
        print('user\'s score is %s' %(response.generate_score(user)))
        
def get_user_data(events, users):
    '''
        Stubbed in function to represent the returned data for a set of events.
        Given a set of events, and a set of users, this should return
        a matrix of dimension (len(events), len(users)) implemented via a list
        of tuples. So we can add a user/event, but not alter an element
    '''
    response_data = [
        [(1,1,1), (1,1,1), (1,1,1), (1,1,1), (1,1,1)],
        [(0,0,0), (1,0,0), (0,0,0), (0,0,0), (0,0,0)],
        [(1,1,0), (1,0,1), (1,1,1), (0,0,0), (0,0,0)],
        [(1,0,0), (1,0,0), (1,0,0), (1,0,0), (1,0,0)],
        [(0,0,0), (0,0,0), (0,0,0), (1,1,1), (1,1,1)],
    ]
    return(response_data)

def get_event_list(event_count):
    '''
        stubbed in to provide a list of events to include in engagement
        calculation
    '''
    return(string.ascii_uppercase[:event_count + 1])
        
def get_user_list(event_count):
    '''
        stubbed in to set up users whose response data we want
    '''
    return(['user%s' %(str(x)) for x in range(1, event_count + 1)])

if __name__ == '__main__':
    main()

