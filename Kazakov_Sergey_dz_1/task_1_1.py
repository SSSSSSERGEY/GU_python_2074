
def convert_time(tim_second: int) -> str:
    many_days = tim_second // 86400

    hour_s = tim_second % 86400
    hours = hour_s // 3600

    minut = hour_s % 3600
    minuts = minut // 60

    second = minut % 60

    if(many_days != 0):
        result = (F"{many_days}дн  {hours}час  {minuts}мин  {second}сек")
    elif(hours != 0):
        result = (F"{hours}час  {minuts}мин  {second}сек")
    elif(minuts != 0):
        result = (F"{minuts}мин  {second}сек")
    else:
        result = (F"{second}сек")

    return result

tim_second = 53
result = convert_time(tim_second)
print(result)