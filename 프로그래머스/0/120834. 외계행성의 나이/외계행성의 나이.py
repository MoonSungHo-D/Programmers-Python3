def solution(age):
    table = str.maketrans("0123456789","abcdefghij")
    age = str(age)
    age =age.translate(table)
    return age