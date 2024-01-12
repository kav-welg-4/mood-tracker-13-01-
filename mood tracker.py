"""
This program is a mood tracker, which can: 
1) Take in your mood at given time in the day. 
2) Then, after the day has passed, we average the mood to calculate the daily mood. 
3) This average daily mood will be used to plot weekly, monthly, and yearly mood data. 

Process: 
1) First generate an array for the entire year. 
2) def ask_for_mood(): Will ask for your mood. 
3)def daily_mood(): Will store an array for the daily mood. Will return the array of all moods for that day. 
4) def plot_daily_mood(): From this daily array, we can calculate the average daily mood. Will return the average daily mood. 
5) def append_daily_mood(): Now that we have the average daily mood, we can append it to the array for the entire year.
6) Then we can press a button to generate graphs based on the week, month or year.

"""


import numpy as np 
import datetime as dt
import matplotlib.pyplot as plt
import tkinter as tk 
import pandas as pd
from tkinter import simpledialog, messagebox
from datetime import datetime

print("test")
