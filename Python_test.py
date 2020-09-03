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
# input_file = open("/Users/minkyu/Documents/PythonCode/sample.txt", 'r')
# nums = []
# while True:
#     num_str = input_file.readline()
#     if not num_str : break
#     nums.append(int(num_str))
# count = 0
# sum = 0
# for num in nums:
#     sum += num
#     count +=1
# avr = sum / count
# print(avr)
#문제10(사칙연산 계산기 클래스) -> 클래스 선언법 복습하기
# class Calculator:
#     def __init__(self, list_num):
#         self.list_num = list_num# 초기화 함수에서 .사용으로 자연스럽게 클래스 변수 선언 + 초기화
#     def sum(self):
#         val = 0
#         for num in self.list_num:
#             val += num
#         return val

#     def avg(self):
#         val = 0
#         count = 0
#         for num in self.list_num:
#             val += num
#             count +=1
#         avg = val / count
#         return avg

# cal1 = Calculator([1,2,3,4,5])
# print(cal1.sum())
# print(cal1.avg())

# cal2 = Calculator([6,7,8,9,10])
# print(cal2.sum())
# print(cal2.avg())

#문제11(모듈 사용 방법)
#import mymod를 터미널에서 열어사용할 수 있는 방법
#1. mymod.py파일 생성 -> 환경변수 path에 mymod.py가 존재하는 경로 추가
#1밖에 생각이 안나는데...

#문제12(오류와 예외 처리) -> 복습하기
# result = 0
# try:
#     [1,2,3][3]
#     "a" + 1
#     4 / 0
# except TypeError:
#     result+=1
# except ZeroDivisionError:
#     result+=2
# except IndexError:
#     result+=3
# finally:#예외 발생 여부에 상관없이 실행 -> 복습
#     result+=4
# print(result)# 3 + 4 = 7

# 문제13(DashInsert함수) -> 무수히 많은 변수 선언이 필요했다. 분명 변수 선언을 적게 하고도 문제를 푸는 방법이 있지 않을까 싶다.
# 숫자로 구성된 문자열을 입력받은 뒤 문자열 안에서 홀수가 연속되면 두 수 사이에 - 추가, 짝수가 연속되면 *를 추가.
# def DashInsert(num):
#     num_str = str(num)
#     last_char = ''
#     result_str = ""
#     count = 0
#     for chr in num_str:
#         if(count != 0):
#             num_last_char = int(last_char)
#             num_chr = int(chr)

#             if( num_last_char % 2 == 0 and num_chr % 2 == 0):# 둘다 짝수
#                 plus_chr = '*'+chr
#                 result_str +=plus_chr
#             elif( num_last_char % 2 == 1 and num_chr % 2 == 1 ):#둘다 홀수
#                 plus_chr = '-'+chr
#                 result_str += plus_chr
#             else:
#                 result_str +=chr#아무것도 아님
#         else:
#             result_str = chr
#         last_char = chr
#         count+=1
#     return result_str

# print(DashInsert(4546793))
#문제14(문자열 압축) -> 복습


                


