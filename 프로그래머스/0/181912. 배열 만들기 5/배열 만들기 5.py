def solution(intStrs, k, s, l):
    result = []
    for nums in intStrs:
        if int(nums[s:s+l]) >k:
            result.append(int(nums[s:s+l]))
    return result