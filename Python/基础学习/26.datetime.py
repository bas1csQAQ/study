# 内置模块
# datetime是处理时间和日期的标准库
from datetime import datetime
# 获取当前时间和日期
now = datetime.now()
print(now)

# 使用datetime制定创造时间
# 按照年月日时分的顺序给参数 会返回一个对应的时间
dt = datetime(2015, 4, 19, 12, 30)
print(dt)

# 时间戳
# 使用 timestap()方法将一个datetime转为timestap类型
print(dt.timestamp())
# python 中的时间戳是一个浮点数  如果有小数位 小数位表示的是毫秒数
# 某些编程语言（如Java和JavaScript）的timestamp使用整数表示毫秒数，这种情况下只需要把timestamp除以1000就得到Python的浮点表示方法。

# 使用fromtimestap()方法将时间戳转换成datetime类型
t = 1429417200.0
print(datetime.fromtimestamp(t))
# 需要注意的是 时间戳没有时区的概念 但是datetime类型有
# fromtimestamp()方法是让时间戳和本地时间进行转换
# 本地时间指的是当前操作系统所设定的时区 比如说北京 就是东8区的时间 实际上也就是 utc+8:00时区的时间
# 标准utc时间指的是 utc+0:00时区的时间
# 时间戳也可以直接转换成utc标准时区的时间
print(datetime.utcfromtimestamp(t))


# 使用datetime.strptime()将字符串转为时间 需要传入一个时间格式化字符串
cday = datetime.strptime('2015-6-1 18:19:59', '%Y-%m-%d %H:%M:%S')
print(cday)

# 使用strftime()方法将时间转换成字符串  同样需要传入一个时间格式化字符串
print(now.strftime('%a, %b %d %H:^%M'))


# datetime的加减
# 时间类型的加减实际上就是将datatime往前或往后进行计算 得到新的datetime 可以直接使用+ -
# 需要导入 timedelta类
from datetime import timedelta
print('now：', now)
print(now + timedelta(hours=10))
print(now - timedelta(days=1))
# 通过使用timedelta可以很容易的算出任意时间的时刻


# 时区转换
from datetime import timezone
# 1. 拿到utc时间 并强制设置时区为utc+0:00
utc_dt = datetime.utcnow().replace(tzinfo=timezone.utc)
print(utc_dt)
# 2. 使用astimezone()转换时区
bj_dt = utc_dt.astimezone(timezone(timedelta(hours=8)))
print(bj_dt)

# 当然也可以使用这个方法转换成其他时区的时间
# 使用utc_dt转换成东9区的时间
tokyo_dt = utc_dt.astimezone(timezone(timedelta(hours=9)))
print(tokyo_dt)

# 当然 也不是必须从 utc+0:00时区转换到其他时区 任何带有时区的datetime都可以正确转换
# 东八区转换到东九区
tokyo_dt2 = bj_dt.astimezone(timezone(timedelta(hours=9)))
print(tokyo_dt2)



# 假设获取了时间日期如2015-1-21 9:01:30 以及一个时区信息UTC+5:00 都是str 编写一个函数 让这个时间转换成时间戳
import re
def to_timestamp(dt_str, tz_str):
    dt = datetime.strptime(dt_str, '%Y-%m-%d %H:%M:%S')
    tz = re.match(r'^UTC([\+|\-].*\d)\:00$', tz_str).groups(1)
    # print(dt )
    tz_utc = timezone(timedelta(hours=int(tz[0])))
    # print(tz_utc)
    dt = dt.replace(tzinfo=tz_utc)
    # print(dt)
    return dt.timestamp()


print(to_timestamp('2015-6-1 08:10:30', 'UTC+7:00')) # 1433121030.0
print(to_timestamp('2015-5-31 16:10:30', 'UTC-09:00')) # 1433121030.0