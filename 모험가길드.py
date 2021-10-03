N = int(input())		#모험가 수
data = list(map(int, input().split()))		#모험가 공포도

data.sort()		#오름차순 정렬

#작은 것부터 그룹을 지음
result = 0;
