from datetime import datetime

def time_this(num=10):
    def wrapper(f):
        i = 0
        time_list = []
        while i <= num:
            start = datetime.now()
            result = f()
            finish = datetime.now()
            timedelta = finish-start
            time_list.append(timedelta.total_seconds())    
            i += 1
        avg_time = sum(time_list) / len(time_list)
        #print(avg_time)
        return avg_time
    return wrapper

@time_this(10)
def f():
    for j in range(1000):
        pass
