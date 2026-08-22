def solution(num_list):
    j = 0
    for i in range(len(num_list)):
        if int(num_list[i])%2==1:
            j +=1
    return [len(num_list)-j, j]
        