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

    #이동방향 지정
    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]
    
    #최단거리 구하는 함수 생성
    def bfs():
        distance = [[-1] * N for _ in range(N)] #노드의 값이 -1인 경우 지나갈 수 없음(이미 방문함)
        queue = deque([(bear_x, bear_y)]) # Deque 생
        distance[bear_x][bear_y] = 0

        while queue:
            x, y = queue.popleft()
            for d in range(4):
                nx = x + dx[d]
                ny = y + dy[d]
                #곰이 이동할 수 있는지 판별
                if nx >= 0 and nx < N and ny >= 0 and ny < N: # 노드가 범위 안에 있는 경우
                    if distance[nx][ny] == -1 and forest[nx][ny] <= bear_size: # 벌집이 곰보다 작거나 같은 경우 이동 가능함
                        distance[nx][ny] = distance[x][y] + 1
                        queue.append((nx, ny))
        return distance
    # 곰이 먹을 벌집을 탐색하는 함
    def find_honeycomb(distance):
        x, y = 0, 0
        minimal_distance = N*N # 곰이 이동하는 최소 거리의 최대치
        for i in range(N):
            for j in range(N):
                if distance[i][j] != -1 and forest[i][j] >= 1 and forest[i][j] < bear_size: # 곰이 이동할 수 있는 위치의 먹을 수 있는 벌집인 경우
                    if minimal_distance > distance[i][j]:
                        x, y = i, j
                        minimal_distance = distance[i][j]
        # 곰이 숲에 있는 모든 지점을 탐색했지만 먹을 수 있는 벌집이 없다면 종
        if minimal_distance == N*N:
            return None
        else:
            return x, y, minimal_distance

    

    result = 0
    
    while True:
        time = find_honeycomb(bfs())
        # 곰이 먹을 수 있는 벌집이 없다면
        if time == None:
            print(result) # 지금까지 이동한 시간을 리턴
            break
        else: # 곰이 먹을 수 있는 벌집이 존재하는 경우
            # 현재 위치를 벌집의 위치로 이동 후 시간을 더해주기
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
