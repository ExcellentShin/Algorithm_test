N = int(input())		#모험가 수
data = list(map(int, input().split()))		#모험가 공포도

data.sort()		#오름차순 정렬

#작은 것부터 그룹을 지음, 순차적으로 탐색하되 현재 값을 그룹에 넣었을 때 그룹 인원이 값과 동일하다면 그룹 마감
result = 0
count = 0
for num in data:
	if num == count + 1:
		count = 0
		result += 1
	else:
		count += 1

print(result)
