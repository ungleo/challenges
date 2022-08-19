# %%
import pandas as pd
import numpy as np
# import local funcionts
from functions import monthly_purchases,user_check, vip_criteria
import sys, os

# %%
import json
with open(os.path.join(sys.path[0], "pur_list.json"), "r") as fp:
     pur_list = json.load(fp)

# %%
threshold = 100
criteria_months = 3

# preprocessing data
monthly_purchases_df = monthly_purchases(pur_list,threshold)

# results
vip_dict, status_dict  = vip_criteria(monthly_purchases_df,criteria_months)
print(vip_dict)
print(status_dict)
