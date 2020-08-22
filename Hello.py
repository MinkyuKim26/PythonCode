"""
hello.py
Made by Minkyu Kim
Practice code 
"""
# print('=' * 50)
# head = "\npython is"
# tail = " very easy language\n"
# all_sentence = head + tail
# print(all_sentence * 2)
# print('=' * 50)

# a = len(head + tail)
# print(a)
# print("\n" + all_sentence[0:4]) #0번부터 3번까지(n<4)
# print("\n" + all_sentence[4:]) #4번부터 끝까지(n>=4)
# print("\n" + all_sentence[:10])#0번부터 10번까지
# print("\n" + all_sentence[14:-8])#14번부터 -9번 앞까지(뒤에서 9번째 문자 앞까지)

# a = "20200820Sunny"
# date = a[:8]#0번부터 8번 앞까지(0 <= n < 8)
# weather = a[8:]#8번부터 끝까지 (8 <= n  <=끝)
# print(date)#문자열 출력하고 알아서 엔터 치는듯?
# #print("\n")
# print(weather)

# head = "min"
# tail = "yu"
# all_sen = head + 'k' + tail#원래 문자열의 요소값은 바꿀 수 없으나 이런식으로는 할 수 있다. 뒷장을 보니 바꿀 수 있는듯?
# print(all_sen)

# number = 10
# day = "two"

# %포매팅================================================================================================
# test = "I ate %d apples. so I was sick for %s days." %(number, day) #문자열 생성

# print(test)
# #%s에는 어떤 형태의 값이든 넣을 수 있다. 
# test_2 = "I have %s apples" %3
# print(test_2)
# test_3 = "rate is %s" %3.234
# print(test_3)
# #%와 숫자는 이렇게 표기할 수 있다
# test_4 = "Error is %d%%" %98
# print(test_4)

# #문자열 오른쪽 정렬
# test_5 = "%10s" %"hi"
# print(test_5)

# #문자열 왼쪽으로 정렬
# test_6 = "%-10s" %"hi"
# print(test_6)

# #소숫점 포현 + 오른쪽 정렬
# test_7 = "%10.4f" %3.1234567
# print(test_7)

# %포매팅================================================================================================

# format 포매팅================================================================================================
# #format()함수 사용. .format()이라고 써야한다. (not format())
# test_8 = "I eat {0} apples".format(3)
# print(test_8)

# #format()함수에 변수를 대입할 수도 있다. 
# num = 10
# test_9 = "I eat {0} apples".format(num)
# print(test_9)

#format()함수에 2개 이상 변수 대입
# number = 10
# day = "three"
# str = "I ate {0} apples. so I was sick for {1} days".format(number, day)
# print(str)

#{0}, {1}...대신 이름으로 넣기. 이런 형태일 경우 각 변수(number, day)에 값을 넣어줘야함
# str = "I ate {number} apples. so I was sick for {day} days".format(number = 10, day = 3)
# print(str)

#인덱스와 이름 혼용
# str = "I ate {0} apples. so I was sick for {day} days".format(10, day = 3)
# print(str)

# :<10 표현식. 치환되는 문자열을 왼쪽으로 정렬하고 문자열의 총 자릿수를 10으로 맞춘다.
# str = "{0:<10}".format("hi")
# print(str)

#오른쪽 정렬
# str = "{0:>10}".format("hi")
# print(str)

#가운데 정렬
# str = "{0:^10}".format("hi")
# print(str)

#공백 채우기
# str = "{0:=^10}".format("hi")
# print(str)
# str = "{0:=>10}".format("hi")
# print(str)
# str = "{0:=<10}".format("hi")
# print(str)

# str = "{0:!^10}".format("hi")
# print(str)
# str = "{0:!>10}".format("hi")
# print(str)
# str = "{0:!<10}".format("hi")
# print(str)

#.4f를 다르게 표시
# y = 3.42134234
# str = "{0:0.4f}".format(y)
# print(str)

#10.4f를 다르게 표시. {0}에다 y를 대입할건데 이 때 조건이 자릿수 10에 소숫점은 4번째 자리까지만 표편하겠다는 뜻인듯.
# y = 3.42134234
# str = "{0:10.4f}".format(y)
# print(str)

#{ 또는 } 표시. 아무것도 표시하지 않을 때는 format()만 쓰면 되는듯 하다.
# str = "{{ and }}".format()
# print(str)
# format 포매팅================================================================================================
# % 포매팅이 연산속도가 더 빠르다. format 포매팅은 전달되는 값의 타입을 추측하는 과정이 추가되기 때문.
#실은 + 연산자를 이용한 표현 방법이 제일 빠르다. 
#근데 포매팅으로 인해 연산의 부하는 없다고 한다. 파이썬은 '예쁘게 짜는 것'이란 언어적 신념을 갖고 있는 문자니
#format 포매팅을 애용하도록 하자.
#format() 함수는 표현하려는 값이 어떻던 변수명만 쓰면 되는데 %연산은 %s, %f, %d같이 표현하려는 변수의 타입을 알고있어야 한다.


#f문자열 포매팅====================================================================================================
# name = '김민규'
# age = 23
# str = f'나의 이름은 {name}입니다. 나이는 {age}입니다.'
# print(str)
#정렬
# str = f'{"hi":<10}' # "hi"라는 문자열에 대해 10칸으로 설정해놓은 구간에서 왼쪽 정렬을 하겠다.
# print(str)
# str = f'{"hi":>10}' # "hi"라는 문자열에 대해 10칸으로 설정해놓은 구간에서 오른쪽 정렬을 하겠다.
# print(str)
# str = f'{"hi":^10}' # "hi"라는 문자열에 대해 10칸으로 설정해놓은 구간에서 가운데 정렬을 하겠다.
# print(str)
#공백 채우기
# str = f'{"hi":=<10}' # 왼쪽 정렬 후 빈공간을 =로 채우겠다
# print(str)
# str = f'{"hi":!>10}' # 오른쪽 정렬 후 빈공간을 !로 채우겠다. 
# print(str)
# str = f'{"hi":~^10}' # 가운데 정렬 후 빈공간을 ~로 채우겠다. 
# print(str)
#소수점 표현
# y = 3.124123
# str = f'{y:0.4f}'
# print(str)
# y = 3.124123
# str = f'{y:10.4f}'
# print(str)
#!!!python!!!표현
# str_0 = f'{"python":!^12}'
# print(str_0)
# #format 포매팅으로 표현
# str_1 = "{0:!^12}".format('python') #이게 더 보기에 예쁘다.
# print(str_1)
#f문자열 포매팅====================================================================================================

#문자열 관련 함수
# a = "hobby"
# print(a.count('b'))#a라는 문자열에 들어있는 'b'의 갯수를 반환
# a = "Python is the best choice"
# print(a.find('b'))#a문자열에 'b'가 들어있는 위치 반환
# print(a.find('k'))#찾을 수 없으면 -1을 반환
# print(a.index('t'))#a문자열에 'b'가 들어있는 위치 반환
# print(a.index('k'))#찾을 수 없으면 오류 발생

#문자열 삽입
# str = ",".join('abcd') # 'abcd' 사이에 , 삽입
# print(str)
#join함수는 리스트, 튜플도 입력으로 사용 가능
#리스트 사용 예
# str = ",".join(['a','b','c','d'])
# print(str)
#소문자->대문자
# a = "hi"
# str = a.upper()
# print(str)
#대문자 -> 소문자
# a = "HI"
# str = a.lower()
# print(str)
#문자열 공백 지우기
# a = " hi"
# str = a.lstrip()#왼쪽 공백을 지워준다. 
# print(str)
# a = "hi "
# str = a.rstrip()#오른쪽 공백을 지워준다. 
# print(str)
# a = "hi "
# str = a.strip()#양쪽 공백을 지워준다. 
# print(str)
#문자열 바꾸기
# a = "Life is too short"
# str = a.replace("Life", "Your leg")#Life를 Your leg로
# print(str)
#문자열 나누기
# a = "Life is too short"
# str = a.split()#공백을 기준으로 문자열 나눔
# print(str)
# a = "a:b:c:d"
# str = a.split(':')#기호를 기준으로 문자열 나눔
# print(str)
#출력값으로 나오는 ['a', 'b', 'c', 'd']같은 애들을 '리스트'라고 부른다.
# 
# 배열에 해당하는 list에 대해 알아보기
# odd = [1, 3, 5, 7, 9]#리스트명 = [요소1, 요소2, 요소3, ...] 
# a = []#빈 리스트
# b = [1, 2, 3]#숫자를 요소값으로 가진 리스트
# c = ['Life', 'is', 'too', 'short']#문자열을 요소값으로 가진 리스트
# d = [1, 2, 'Life', 'is']#숫자와 문자열을 함께 문자열로 가진 리스트
# e = [1, 2, ['Life', 'is']]#리스트 자체를 요소값으로 가진 리스트. ['Life', 'is']라는 리스트를 요솟값으로 가지고 있다. 
#->리스트 안에는 어떠한 자료형도 포함시킬 수 있다. 

#리스트의 인덱싱과 슬라이싱
# a = [1, 2, 3]
# print(a[0])#1
# print(a[0] + a[2])#1 + 3
# #마지막 요솟값 출력
# print(a[-1])
#숫자와 리스트가 포함된 리스트 
# a = [1, 2, 3, ['a', 'b', 'c']]
# print(a[0])
# print(a[-1])#마지막 요솟값 ['a', 'b', 'c']출력
# print(a[3])#a[-1]과 같은값 출력
# #리스트 속 리스트의 요솟값 출력
# print(a[3][0])#리스트 속 리스트 ['a', 'b', 'c']의 첫번째 요솟값 'a'가 나온다.
# print(a[3][1])#b
# print(a[3][2])#c 출력
#리스트의 슬라이싱(나누기)
# a = [1,2,3,4,5]
# print(a[0:2])#(0 <= n < 2)에 해당하는 a[n] 출력
# b = a[:2]#처음부터 a[1]까지
# c = a[2:]#a[2]부터 끝까지
# print(b)
# print(c)
# d = a[1:3]
# print(d)
#중첩된 리스트에서 슬라이싱
# a = [1,2,3,['a','b','c'],4,5]
# print(a[2:5])#a[2]부터 a[4]까지. 
# print(a[3][:2])#a[3]에 있는 리스트에서 0번 요소부터 1번 요소까지 출력
#리스트 연산
# a = [1,2,3]
# b = [4,5,6]
# print(a + b)#리스트의 +연산 : 2개의 리스트를 합치는 기능 
# print(a * 3)#리스트의 *연산 : 리스트를 n번 반복
# #리스트 길이
# print(len(a))
# print( str(a[:2]) + "hi") #a[:2] + "hi"는 (정수 + 문자열) 연산이라 에러가 나온다. 그래서 정수를 문자열로 바꿔준 다음 더해서 출력한다. 
#리스트의 수정과 삭제
#리스트 값 수정
# a = [1,2,3]
# a[2] = 4 #a[2]에 4 대입
# print(a) #[1,2,3]이 아닌 [1,2,4]가 나온다.
#리스트 요소 삭제
# a = [1,2,3]
# del a[1]
# print(a)#a[1]에 해당하던 2가 사라지로 [1,3]만 출력된다.
#슬라이싱 기법으로 리스트의 요소 여러개를 한꺼번에 삭제
# a = [1,2,3,4,5]
# del a[2:]#a[2]부터 뒤에 있던 요소들이 다 삭제
# print(a)#a[0]과 a[1]만 출력
#리스트 관련 함수
#요소 추가(append)
# a = [1,2,3]
# a.append(4)#a뒤에 4 추가 - push_back의 기능을 하는 함수인듯
# print(a)
# #리스트 안에는 어떠한 자료형도 추가 가능
# a.append([5,6])#5,6이 아닌 [5,6]이라는 리스트가 추가
# print(a)
#정렬
# a = [1,4,3,2]
# a.sort()#[1,4,3,2]를 [1,2,3,4]로 정리
# print(a)
#알파벳도 순서대로 정리 가능
# a = ['a', 'c', 'b']
# a.sort()#알파벳 순서대로 정리
# print(a)
#위치 반환(index)
# a = [1,2,3]
# print(a.index(3))#3을 찾아서 그 위치를 반환
# print(a.index(1))#1을 찾아서 그 위치를 반환
#찾으려는 값이 리스트 안에 없으면 오류 발생
#리스트에 요소 삽입(insert)
# a = [1,2,3]
# a.insert(0, 4)#0번 자리에 4 삽입
# print(a)
# a.insert(3,5)#3번 자리에 5 삽입
# print(a)
#리스트 요소 제거(remove)
# a = [1,2,3,1,2,3]
# a.remove(3)#a 안에서 가장 먼저 발견되는 3 제거
# print(a)
# a.remove(3)
# print(a)
#리스트의 맨 마지막 요소 반환, 그 요소는 리스트 내에서 삭제
# a = [1,2,3]
# print (a.pop())#마지막 요소 3 반환
# print(a)#3이 지워진 리스트 출력
#리스트에 포함된 특정 요솟값의 개수 세기(count)
# a = [1,2,3,1]
# print(a.count(1))#1이 들어있는 갯수를 카운트해서 반환
#리스트 확장
# a = [1,2,3]
# a.extend([4,5])#[1,2,3]에 [4,5]리스트를 추가
# print(a)#[1,2,3,4,5]가 출력
# b = [6,7]
# a.extend(b)#[1,2,3,4,5]에 리스트 b를 추가
# print(a)#추가된 리스트 [1,2,3,4,5,6,7]이 출력
#a.extend([4,5])는 a+=[4,5]와 동일하다.

#튜플
#리스트와 거의 비슷하다.
# t1 = ()
# t2 = (1, )#1개 요소만을 가질 때는 뒤에 콤마 붙혀야 한다. 
# t3 = (1,2,3)
# t4 = 1,2,3#괄호는 생략해도 괜찮다.
# t5 = ('a', 'b', ('ab','cd'))
#튜플과 리스트의 차이점
#리스트는 요소값을 바꿀 수 있으나
#튜플은 요소값을 바꿀 수 없다. 
#프로그램을 실행하는 동안 그 값을 상수로만 쓸거면 튜플을 쓰고
#수시로 값을 바꿔줘야 할 경우에는 리스트를 쓴다. 
#값이 바뀌지 않는 튜플의 에제
t1 = {1, 2, 'a','b'}
t1[0] = 'c'#값 변경 시도 -> 에러, 튜플에서 지원하지 않는 기능이다. 
