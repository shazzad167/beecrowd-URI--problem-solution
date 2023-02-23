def event_time():
    trash, day1 = input().split()
    day1 = int(day1)
    h1, trash1, m1, trash2, s1 = input().split()
    h1 = int(h1)
    m1 = int(m1)
    s1 = int(s1)
    trash, day2 = input().split()
    day2 = int(day2)
    h2, trash1, m2, trash2, s2 = input().split()
    h2 = int(h2)
    m2 = int(m2)
    s2 = int(s2)
    sd = (s1 +(m1*60) + (h1*60*60) + (day1*24*60*60))
    ed = (s2 +(m2*60) + (h2*60*60) + (day2*24*60*60))
    dur = ed - sd
    day = dur//86400
    rem1 = dur%86400
    hour = rem1//3600
    rem2 = rem1%3600
    minu = rem2//60
    second = rem2%60  
    print("{} dia(s)".format(day))
    print("{} hora(s)".format(hour))
    print("{} minuto(s)".format(minu))
    print("{} segundo(s)".format(second))

event_time()