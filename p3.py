# 프로젝트 문제 3번
from collections import deque
input = [[4, 3, 2, 1],
         [0, 0, 0, 0],
         [0, 0, 9, 0],
         [1, 2, 3, 4]]
N = 4

forest = []

def problem3(input):
    bear_size = 2
    honeycomb_count = 0
    time = 0
    bear_x, bear_y = 0, 0


    forest = [row[:] for row in input]
    
    # 곰의 초기 위치 찾기
    for i in range(N):
        for j in range(N):
            if forest[i][j] == 9:
                bear_x, bear_y = i, j
                forest[i][j] = 0
    print("곰의 초기 위치 x : {0}, y : {1}".format(bear_x, bear_y))

    #여기에서부터 코드를 작성하세요.
    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]
    def bfs():
        distance = [[-1] * N for _ in range(N)]
        queue = deque([(bear_x, bear_y)])
        distance[bear_x][bear_y] = 0

        while queue:
            x, y = queue.popleft()
            for d in range(4):
                nx = x + dx[d]
                ny = y + dy[d]
                if nx >= 0 and nx < N and ny >= 0 and ny < N:
                    if distance[nx][ny] == -1 and forest[nx][ny] <= bear_size:
                        distance[nx][ny] = distance[x][y] + 1
                        queue.append((nx, ny))
        return distance
   
    def find_honeycomb(distance):
        x, y = 0, 0
        minimal_distance = N*N
        for i in range(N):
            for j in range(N):
                if distance[i][j] != -1 and forest[i][j] >= 1 and forest[i][j] < bear_size:
                    if minimal_distance > distance[i][j]:
                        x, y = i, j
                        minimal_distance = distance[i][j]
        if minimal_distance == N*N:
            return None
        else:
            return x, y, minimal_distance

    

    result = 0
    
    while True:
        time = find_honeycomb(bfs())
        if time == None:
            print(result)
            break
        else:
            bear_x, bear_y = time[0], time[1]
            result += time[2]
            forest[bear_x][bear_y] = 0
            honeycomb_count += 1
            if honeycomb_count >= bear_size:
                bear_size += 1
                honeycomb_count = 0

    return result


result = problem3(input)

assert result == 14
print("정답입니다.")
