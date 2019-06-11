from datetime import datetime, timedelta, timezone

# 获取当前时间
print(datetime.now())
print(type(datetime.now()))

# 自定义时间
dt = datetime(2015, 4, 19, 12, 20)
print(dt)

# datetime转换为timestamp
ts = dt.timestamp()
print(ts)

# timestamp转换为datetime
print(datetime.fromtimestamp(ts))
print(datetime.utcfromtimestamp(ts))  # UTC时间

# str转换为datetime
cday = datetime.strptime("2015-6-1 18:19:59", "%Y-%m-%d %H:%M:%S")
print(cday)

# datetime转换为str
now = datetime.now()
print(now.strftime("%a, %b %d %H:%M"))

# datetime加减
now = datetime.now()
print(now)
print(now + timedelta(hours=10))  # +10hours
print(now - timedelta(days=1))  # -1day
print(now + timedelta(days=2, hours=10))  # +2day10hours

# 强制设置时区
tz_utc_8 = timezone(timedelta(hours=8))  # 创建时区UTC+8:00
print(now)
dt_utc8 = now.replace(tzinfo=tz_utc_8)  # 强制设置时区
print(dt_utc8)

# 时区转换
# utcnow获取当前的UTC时间，并设置其正确的时区
utc_dt = datetime.utcnow().replace(tzinfo=timezone.utc)  # 获取UTC时间，并设置诗句为UTC+0:00
print(utc_dt)
# 使用astimezone转换为其他时区时间
bj_dt = utc_dt.astimezone(timezone(timedelta(hours=8)))
print(bj_dt)
tokyo_dt = utc_dt.astimezone(timezone(timedelta(hours=9)))
print(tokyo_dt)
tokyo_dt2 = bj_dt.astimezone(timezone(timedelta(hours=9)))
print(tokyo_dt2)


def to_timestamp(dt_str, tz_str):
    # dt_str输入时间字符串，tz_str时区信息，输出timestamp
    dt = datetime.strptime(dt_str, "%Y-%m-%d %H:%M:%S")  # str转换datetime
    import re
    tz_re = re.match(r"^UTC(\+|\-)(\d+):00", tz_str)  # 正则匹配时区信息
    # 设置一个时区
    tz_utc = timezone(timedelta(hours=int(tz_re.group(1)+tz_re.group(2))))

    dt_utc = dt.replace(tzinfo=tz_utc)  # 强制性绑定时区
    print(dt_utc.timestamp())  # 转换为timestamp


to_timestamp("2015-6-1 08:10:30", "UTC+07:00")
to_timestamp("2015-5-31 16:10:30", "UTC-09:00")
