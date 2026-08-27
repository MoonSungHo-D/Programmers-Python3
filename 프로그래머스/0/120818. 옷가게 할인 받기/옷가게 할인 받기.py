def solution(price):
    if price >= 500_000:
        answer= price * 0.8
    elif price >= 300000:
        answer= price *0.9
    elif price >= 100000:
        answer= price *0.95
    else:
        answer= price
    return int(answer)