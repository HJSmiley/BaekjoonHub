import datetime

dt_kst = datetime.datetime.now()
dt_utc = str(dt_kst - datetime.timedelta(hours=9))

print(dt_utc[:4], dt_utc[5:7], dt_utc[8:10], sep='\n')