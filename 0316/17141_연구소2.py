'''
연구소의 특정 위치에 바이러스 m개
연구소 크기 n*n인 정사각형
바이러스는 상하좌우로 인접한 모든 빈칸으로 동시에

0 > 빈칸, 1 > 벽, 2 > 바이러스

'''

from itertools import combinations

# 1.
# bfs 함수
# 바이러스 시작 위치에서 상하좌우에 0이 있는지 탐색
def bfs(queue):
    lab_c = [lab[i][:] for i in range(n + 2)] # deepcopy
    visited = [[0] * (n + 2) for _ in range(n + 2)]

    while queue: # 큐에 존재할 때
        t = queue.pop(0)
        lab_c[t[0]][t[1]] = 1
        for di, dj in ((1, 0), (-1, 0), (0, 1), (0, -1)): # 상하좌우 탐색
            si, sj = t[0] + di, t[1] + dj
            if lab_c[si][sj] != 1 and (si, sj) not in queue:  # 1이 아니라면
                visited[si][sj] = visited[t[0]][t[1]] + 1
                lab_c[si][sj] = 1  # 1로 바꾸기
                queue.append((si, sj))

    # 1-2. return
    # 불가능 > 최댓값 return
    lab_c = sum(lab_c, [])
    if 0 in lab_c:
        return n**2
    # 가능 > max return
    visited = sum(visited, [])
    return max(visited)


# 2 초기 설정
# 2-1. input, lab은 -1로 둘러싸기
n, m = map(int, input().split()) # 연구소 크기, 바이러스 개수
lab = [[1] * (n + 2)] + [[1] + list(map(int, input().split())) + [1] for _ in range(n)] +[[1] * (n + 2)]

# 2-2. 바이러스 놓을 수 있는 칸(2) 인덱스 구하기
lab_idx = sum(lab, [])
virus = []
for i in range((n+2)**2):
    if lab_idx[i] == 2:
        virus.append(divmod(i, n+2))

# 3 result
# 3-1 m만큼의 부분집합
sub = []
sub = sub + list(combinations(virus, m))
sub = [list(sub[x]) for x in range(len(sub))]  # 튜플 리스트로 바꾸기 > for문 사용

# 3-2 계산
# 부분집합을 queue에 모두 넣고 시작 > bfs 함수
rlt = []
for i in range(len(sub)):
    rlt.append(bfs(sub[i]))

# 3-3 출력
if min(rlt) == n**2:  # 최솟값이 n**2와 같다면 불가능한 것.
    print(-1)
else:
    print(min(rlt))