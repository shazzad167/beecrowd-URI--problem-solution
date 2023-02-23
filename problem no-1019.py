A = int(input())

hours = A//3600
rem_1 = A%3600

minutes = rem_1//60
rem_2 = rem_1%60
seconds = rem_2
print("{}:{}:{}".format(hours,minutes,seconds))