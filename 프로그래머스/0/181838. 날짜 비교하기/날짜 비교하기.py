def solution(date1, date2):
    day1 = str(date1[0])+str(date1[1])+str(date1[2])
    day2 = str(date2[0])+str(date2[1])+str(date2[2])
    return int(int(day1) < int(day2))