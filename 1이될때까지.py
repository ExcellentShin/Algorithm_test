N, K = map(int, input().split())	#어떤 자연수, N을 나눌 수

#N을 K로 나누는 것을 우선으로 하고, 나눠지지 않으면 -1 계산
result = 0
while N != 1:
	if N % K == 0:
		result += 1
		N /= K
	else:
		result += 1
		N -= 1
	print(N)

print(result)
