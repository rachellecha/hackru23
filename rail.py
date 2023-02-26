import pandas as pd
import numpy as np
import os
import glob
import regex

#os.chdir("/Users/rachellecha/Desktop/hackru23/rail_delay_monthly")
#extension = 'csv'
#all_filenames = [i for i in glob.glob('*.{}'.format(extension))]

#combine all files in the list
#all_2019 = pd.concat([pd.read_csv(f) for f in all_filenames ])
#export to csv
#all_2019.to_csv( "all_2019.csv", index=False, encoding='utf-8-sig')

all_2019 = pd.read_csv("rail_delay_monthly/all_2019.csv")
all_2019.dropna(inplace = True)
all_2019.drop("train_id", axis = 1, inplace = True)
all_2019.drop("date", axis = 1, inplace = True)
all_2019.drop("stop_sequence", axis = 1, inplace = True)
all_2019.drop("from_id", axis = 1, inplace = True)
all_2019.drop("to_id", axis = 1, inplace = True)
all_2019.drop("status", axis = 1, inplace = True)
all_2019.drop("type", axis = 1, inplace = True)

pattern = r'^[0-9]{4}-(?P<month>[0-9]{2})-(?P<day>[0-9]{2})\s(?P<hour>[0-9]{2}):(?P<min>[0-9]{2}):[0-9]{2}$'

all_2019[['month','day','hour','min']] = all_2019['scheduled_time'].str.extract(pattern)

all_2019.drop("scheduled_time", axis = 1, inplace = True)
all_2019.drop("actual_time", axis = 1, inplace = True)

weather = pd.read_csv('weather.csv')

all_2019[['month', 'day']] = all_2019[['month', 'day']].astype(int)

all_2019 = pd.merge(all_2019, weather,  how='left', left_on=['month','day'], right_on = ['month','day'])

all_2019[['month', 'day']] = all_2019[['month', 'day']].astype(str)

all_2019['month'] = all_2019['month'].str.zfill(2)
all_2019['day'] = all_2019['day'].str.zfill(2)

all_2019 = all_2019[['month', 'day', 'hour', 'min', 'from', 'to', 'line', 'precipitation','delay_minutes']]

#print(all_2019.head())

all_2019.to_csv("final_2019.csv", index=False)