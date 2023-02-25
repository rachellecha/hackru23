import pandas as pd
import numpy as np
import os
import glob

#os.chdir("/Users/rachellecha/Desktop/hackru23/rail_delay_monthly")
#extension = 'csv'
#all_filenames = [i for i in glob.glob('*.{}'.format(extension))]

#combine all files in the list
#all_2019 = pd.concat([pd.read_csv(f) for f in all_filenames ])
#export to csv
#all_2019.to_csv( "all_2019.csv", index=False, encoding='utf-8-sig')

all_2019 = pd.read_csv("rail_delay_monthly/all_2019.csv")
all_2019["type"] = all_2019.type.apply(lambda x: None if "Amtrak" in x else x)
all_2019.dropna(inplace = True)
all_2019["delay_change"] = all_2019.delay_minutes.diff()
all_2019.loc[all_2019["stop_sequence"] == 1.0, 'delay_change'] = 0
all_2019.drop("delay_minutes", axis = 1, inplace = True)

all_2019.to_csv("final_2019.csv")