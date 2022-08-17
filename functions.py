import pandas as pd
import numpy as np
import datetime

################# functions #################
# this funcionts should be in an other file and we need import them instead of having them within the main code but I left them here because for the purpose of the exercise is easier to have just one file [exercise comments]

def preprocessing_data (pur_list):
    print(str(datetime.datetime.now()) +': starting preprocessing data' )
    # list to pandas
    df = pd.DataFrame(pur_list)

    # change column format do date
    df.date = df.date.astype('datetime64[ns]')

    # generate date_month column
    #df['date_month'] = df.date.dt.to_period('M')
    df['date_month'] = df.date.to_numpy().astype('datetime64[M]')
    
    ## temporary columns
    # purchases per month
    df_group = df.groupby(['user','date_month'],as_index=False).agg(monthly_amount=('amount','sum'))

    # column amount_100
    df_group['amount_100'] = np.where(df_group.monthly_amount>=100,1,0)

    # sort df by user & date_month
    df_group = df_group.sort_values(by=['user','date_month'],ascending=True)

    # check if months are consecutive 
    df_group['last_month'] = df_group['date_month'].shift(1)

    # date_diff check (only consecutive months)
    df_group['diff_months'] = (df_group['date_month'].dt.year - df_group['last_month'].dt.year)*12 + (df_group['date_month'].dt.month - df_group['last_month'].dt.month)

    df_group['last_amount_100'] = df_group['amount_100'].shift(1)
    df_group['last_user'] = df_group['user'].shift(1)
    df_group['last_monthly_amount'] = df_group['monthly_amount'].shift(1) # this is only to be used in the last print of the function
    print(str(datetime.datetime.now()) +': data preproceded')
    return df_group

# vip criteria function
def vip_criteria(df_group):
    print(str(datetime.datetime.now()) +': starting appliying criteria')
    # vip creteria 
    criteria_user = df_group['user'].shift(1) == df_group['user'] # for the same user (instead of using the columns we use the funcionts)
    criteria_date = df_group['diff_months'] == 1 # only last month
    criteria_amount = (df_group.last_amount_100 == 1) &(df_group.amount_100 == 1)
    df_group['vip'] = np.where(criteria_user & criteria_date & criteria_amount, 1, 0)
    print(str(datetime.datetime.now()) +': criteria applied')
    return df_group
    
# output funcions
def last_time_vip(df_group):
    # last time that a user was vip
    df_last_vip_filter = df_group[df_group['vip']==1].groupby('user').agg(max_month=('date_month','max'))
    df_vips = df_group[df_group['vip']==1]
    df_last_vip = pd.merge(df_vips,
                            df_last_vip_filter,
                            how='inner',
                            left_on=['user','date_month'],
                            right_on=['user','max_month'])
    return(df_last_vip[['user','date_month','monthly_amount','last_monthly_amount','last_month','vip']])

def last_month_status(df_group):
    # last month status
    df_last_filter = df_group.groupby('user').agg(max_month=('date_month','max'))

    df_last_month = pd.merge(df_group,
                            df_last_filter,
                            how='inner',
                            left_on=['user','date_month'],
                            right_on=['user','max_month'])
    return(df_last_month[['user','date_month','monthly_amount','last_monthly_amount','last_month','vip']])