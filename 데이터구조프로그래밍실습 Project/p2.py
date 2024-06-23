# 프로젝트 문제 2번
input = ")))()"

def problem2(input):
    # 괄호열 S의 길이 지정
    if len(input) > 50 and len(input) < 1:
        return False
    
    stack = [] #스택 생성
    result = 0
    for char in input:
        print(char)
        if char == '(': # 만약 열린 괄호인 경우
            stack.append(char) # 스택에 추가
        else: # 만약 닫힌 괄호인 경우
            if len(stack) != 0 and stack[-1] == '(': # 닫힌 괄호와 짝이 맞는 경우
                stack.pop() # 스택 안의 열린 괄호를 제거
            else: # 닫힌 괄호와 짝이 맞지 않는 경우
                result += 1 # 괄호의 최소 개수 1 증가
    result += len(stack) # 짝이 맞지 않는 열린 괄호의 개수와 닫힌 괄호의 개수를 더           
    return result

result = problem2(input)

assert result == 3
print("정답입니다.")
