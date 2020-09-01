# 문제1(split과 join을 이용해 문자열 완성)
# s = "a:b:c:d"
# b = s.split(":")
# str = ""
# for c in b:
#     str+=c
# str = '#'.join(str)
# print(str)
# 문제2(딕셔너리 값 추출 예외처리)
# a = {'A':90, 'B':80}
# isC = a.get('C', 70)
# print(isC)
# 문제3(리스트의 더하기와 extend)
# a = [1,2,3]
# a = a + [4,5]
# print(a)
# a = [1,2,3]
# a.extend([4,5])
# print(a)
# 둘이 차이? 뭐지...모르겠다. 
#문제4(리스트 총합 구하기)
# A = [20, 55, 67, 82, 45, 33, 90, 87, 100, 25]
# sum_over50 = 0

# for a in A:
#     if a > 50:
#         sum_over50 += a
# print(sum_over50)
#문제5(피보나치 수열)
# a = [0,1]
# n = int(input())
# now_count = 1
# while(a[now_count] + a[now_count - 1] <= n):
#     pibo = a[now_count] + a[now_count - 1]
#     a += [pibo]
#     now_count+=1
# print(a)
#문제6(숫자의 총합 구하기)
# s = input()
# nums = s.split(',')
# sum = 0
# for num in nums:
#     num_d = int(num)
#     sum += num_d
# print(sum)
#문제7(한 줄 구구단)
# num = int(input("구구단을 입력할 숫자를 입력하세요(2~9):"))
# count = 1
# str = ""
# while(count < 10):
#     val = num * count
#     str += "%d " % val
#     count +=1
# print(str)
# 문제8(역순 저장, 파일 입출력)
# input = open("/Users/minkyu/Documents/PythonCode/abc.txt", 'r')
# input_read=input.readlines()
# input.close()
# print(input_read)
# str = ""
# count = 0
# while(input_read):
#     str += input_read.pop()
#     if count == 0:
#         str +="\n"
#         count+=1
# print(str)
#문제9(평균값 구하기)
input_file = open("/Users/minkyu/Documents/PythonCode/sample.txt", 'r')
nums = []
while True:
    num_str = input_file.readline()
    if not num_str : break
    nums.append(int(num_str))
count = 0
sum = 0
for num in nums:
    sum += num
    count +=1
avr = sum / count
print(avr)
#문제10(사칙연산 계산기)