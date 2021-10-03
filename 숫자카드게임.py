N, M = map(int, input().split())		#행, 열 갯수

#각 행에서 가장 작은 수를 찾은 후 그 중에 가장 큰 수 출력
result = 0;
for i in range(N):
	row = list(map(int, input().split()))
	result = max(min(row), result)

print(result)
