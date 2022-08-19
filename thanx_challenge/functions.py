import pandas as pd
import numpy as np
import datetime

################# functions #################
# this funcionts should be in an other file and we need import them instead of having them within the main code but I left them here because for the purpose of the exercise is easier to have just one file [exercise comments]

def monthly_purchases(pur_list,threshold):
    print(str(datetime.datetime.now()) +': starting building monthly purchases' )
    # list to pandas
    df = pd.DataFrame(pur_list)

    # change column format do date
    df.date = df.date.astype('datetime64[ns]')

    # generate date_month column
    df['date_month'] = df.date.to_numpy().astype('datetime64[M]')
    
    # purchases per month
    df_group = df.groupby(['user','date_month'],as_index=False).agg(monthly_amount=('amount','sum'))

    # column amount_threshold
    df_group['amount_threshold'] = np.where(df_group.monthly_amount>=threshold,1,0)
    print(str(datetime.datetime.now()) +': monthly purchases ready' )
    return df_group

def user_check(user,df_group,user_last_month,criteria_months):
    # this list is going to be populated with 1 if the analized monthly amount is highier than the threshold
    check_list=[]
    # per user_id, analyze if the last n months the amounts were higher than the criteria
    for c in range(0,criteria_months):
        # for the current month
        if c==0:
            user_last_month
        # for the previous months     
        else:
            user_last_month = (user_last_month.replace(day=1)  - datetime.timedelta(days=1)).replace(day=1)
        # check if the amount of the analized month is higher than the threshold 
        criteria = df_group[(df_group.user==user)&(df_group.date_month==user_last_month)].amount_threshold.max()
        # append the user list
        check_list.append(criteria)
    # return true or false if the number of the last consecutive months amounts are higher than the threshold
    return sum(check_list)==criteria_months

def vip_criteria(df_group,criteria_months):
    print(str(datetime.datetime.now()) +': starting VIP criteria' )
    # it generates a list with the total number of customers that we are going to analyze 
    users_list = df_group.user.unique()
    users_status_dict = {}
    users_vip_dict = {}
    for u in users_list:
        # print('user: '+str(u))
        # it calculates the last month for the current user
        user_last_month = df_group[df_group.user == u]['date_month'].max().replace(day=1)
        # it checks if the user is vip or not and add it to the dictionary
        if user_check(u,df_group,user_last_month,criteria_months):
            # print(user_check(u,df_group,user_last_month,criteria_months))
            users_status_dict[u]=True
            users_vip_dict[u]=True
        else:
            # print(user_check(u,df_group,user_last_month,criteria_months))
            users_status_dict[u]=False
            continue
    # returns a dict with the vip users and the status of all of the users
    print(str(datetime.datetime.now()) +': VIP criteria ready' )
    return users_vip_dict, users_status_dict