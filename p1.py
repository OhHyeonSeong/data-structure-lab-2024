# 프로젝트 문제 1번
input = [10, 40, 30, 60, 30]

def problem1(input):
    mean = 0
    median = 0
    result = [0,0]

    if len(input) == 5:
        for n in input:
            if n % 10 != 0 :
                return false
            else:
                #리스트 크기 순으로 정렬하기
                for pass_num in range(len(input) - 1, 0, -1):
                    for i in range(pass_num):
                        if input[i] > input[i + 1]:
                            temp = input[i]
                            input[i] = input[i + 1]
                            input[i + 1] = temp
                if input[4] < 100:
                    # 평균값 구하기
                    sum = 0
                    for i in input:
                        sum = sum + i
                        mean = int(sum / len(input))
                    #중간값 구하기
                    median = input[2]
      
    
    result[0] = mean
    result[1] = median
    return result

result = problem1(input)

assert result == [34, 30]
print("정답입니다.")
