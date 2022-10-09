import sys

Length = int(input())
Values = []
for i in range(Length):
	Values.append(int(sys.stdin.readline()))


# https://elrion018.tistory.com/37
def counting_sort(array, maaaax):
	maaaax = max(array)

	#counting array 생성
	counting_array = [0]*(maaaax+1)

	#counting array에 input array내 원소의 빈도수 담기
	for i in array:
		counting_array[i] += 1

	#counting array 업데이트.
	for i in range(maaaax):
		counting_array[i+1] += counting_array[i]

	#output array 생성
	output_array = [-1]*len(array)

	#output array에 정렬하기(counting array를 참조)
	for i in array:
		output_array[counting_array[i] -1] = i
		counting_array[i] -= 1
	return output_array

print('\n'.join(str(s) for s in counting_sort(Values)))