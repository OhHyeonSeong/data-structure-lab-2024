# 프로젝트 문제 2번
input = ")))()"

def problem2(input):
    # 이 곳에 코드를 작성하세요.
    # 입력 힌트
    if len(input) > 50 and len(input) < 1:
        return False
    stack = []
    result = 0
    for char in input:
        print(char)
        if char == '(':
            stack.append(char)
        else:
            if len(stack) != 0 and stack[-1] == '(':
                stack.pop
            else:
                result += 1
                
    return result

result = problem2(input)

assert result == 3
print("정답입니다.")
