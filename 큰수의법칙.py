N, M, K = map(int, input().split())		#배열의 크기, 숫자가 총 더해지는 횟수, 중복된 값이 더해지는 제한 횟수
array = list(map(int, input().split()))	#배열 원소 입력

#내림차순 정렬
array.sort(reverse= True)

#맨 앞 인덱스의 값을 두 번 더하고 두 번째 인덱스의 값을 한 번 더하는 식으로 진행
result = 0
for i in range(1, M + 1):
	if i % (K + 1) == 0:
		result += array[1]
	else:
		result += array[0]

print(result)
