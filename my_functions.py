#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 16 15:37:24 2021

@author: guillaume
"""
from datetime import timedelta

def convertTime(time) :
    """
    Parameters
    ----------
    time : int
        Time in ms to convert

    Returns 
    -------
    converted time in (min,sec)

    """
    return (time // (1000 * 60), time // 1000 % 60 )
    

def is_within_range(time1, time2, range = timedelta(minutes = 15)):
    """
    
    Parameters
    ----------
    time1 : dateTime
        first time.
    time2 : dateTime
        second time.
    range : timeDelta
        maximum range between time1 and time2.

    Returns
    -------
    Boolean. 
    True if the differance between the two times is within the given range

    """
    return time2 - time1 <= range