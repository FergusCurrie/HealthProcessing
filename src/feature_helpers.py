import datetime 
import pandas as pd 

def get_min_max_date_and_datetime_array(tmp):
    dates = []
    for i, row in tmp.iterrows():
        date = row['startDate'].split('-')
        year, month, day, hour, minute, sec = int(date[0]), int(date[1]), int(date[2].split(' ')[0]), int(date[2].split(' ')[1].split(':')[0]), int(date[2].split(' ')[1].split(':')[1]), int(date[2].split(' ')[1].split(':')[2])
        dates.append(datetime.datetime(year=year, month=month, day=day, hour=hour, minute=minute, second=sec))
    
    # find min
    min_date, max_date =  datetime.datetime.max, datetime.datetime.min
    for date in dates:
        if date < min_date:
            min_date = date
        if date > max_date:
            max_date = date
    min_date, max_date 
    
    return dates, min_date, max_date

def decompose_date(date):
    ymd, time, _ = date.split(' ')
    year, month, day = ymd.split('-')
    hours, mins, secs = time.split(':')
    return int(year), int(month), int(day), int(hours), int(mins), int(secs)

def str_to_datetime(strdate):
    year, month, day, hours, mins, secs = decompose_date(strdate)
    date = datetime.datetime(year=year, month=month, day=day, hour=hours, minute=mins, second=secs)
    return date

def get_sleep_df():
    df = pd.read_csv('../data/apple_health_export2.csv')
    df = df[df.type == "HKCategoryTypeIdentifierSleepAnalysis"]
    df = df[(df['creationDate'] > '2022-10-30')] # remove before having watch
    if 1: 
        df['creationDate'] = pd.to_datetime(df['creationDate'],yearfirst=True)
        df['startDate'] = pd.to_datetime(df['startDate'],yearfirst=True)
        df['endDate'] = pd.to_datetime(df['endDate'], yearfirst=True)
    df.reset_index(drop=True)
    df = df.reset_index(drop=True)
    return df 

def select_one_night(df, target):
    target = pd.to_datetime('2022-12-12', unit="ns", utc=True)
    day_ahead = target +  pd.Timedelta(1, "d")
    sleep_df_target = df[(df['creationDate'] > target) & (df['creationDate'] < day_ahead)]
    sleep_df_target = sleep_df_target[sleep_df_target.value != "HKCategoryValueSleepAnalysisInBed"]
    sleep_df_target = sleep_df_target.reset_index(drop=True)
    sleep_df_target



