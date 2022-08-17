# %%
import pandas as pd
import numpy as np
# import local funcionts
from functions import preprocessing_data, vip_criteria, last_time_vip, last_month_status

# %%
import json
with open("pur_list.json", "r") as fp:
     pur_list = json.load(fp)

# %%

# preprocessing data
df_group = preprocessing_data (pur_list)
# appliying criteria
df_group = vip_criteria(df_group)

# results
print('Last time that a user was vip')
print(last_time_vip(df_group))

print('Last month status')
print(last_month_status(df_group))

print('Users who where vip in their last month')
print(last_month_status(df_group)[last_month_status(df_group).vip==1])

# instead of these prints the code could leave the different dataframes / lists in files (csv/parquet) or upload them to a dashboard [exercise comments]


