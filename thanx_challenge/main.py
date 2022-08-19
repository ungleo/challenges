# %%
import pandas as pd
import numpy as np
# import local funcionts
from parameters import threshold, criteria_months
from functions import monthly_purchases,user_check, vip_criteria
import sys, os

# %%
import json
with open(os.path.join(sys.path[0], "pur_list.json"), "r") as fp:
     pur_list = json.load(fp)

print ('checking VIP customers with the monthly threshold of '+ str(threshold) + ' in the last '+str(criteria_months)+' month/s')
# preprocessing data
monthly_purchases_df = monthly_purchases(pur_list,threshold)

# results
vip_dict, status_dict  = vip_criteria(monthly_purchases_df,criteria_months)
print(vip_dict)
print(status_dict)
