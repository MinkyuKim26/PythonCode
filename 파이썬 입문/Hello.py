"""
hello.py
Made by Minkyu Kim
Practice code 
"""
# [Do it! 점프 투 파이썬(박응용 저)]에 나온 예제 코드들을 입력한 파일이다.

#파이썬 맛보기============================================================
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
#파이썬 맛보기============================================================


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
# % 포매팅이 연산속도가 더 빠르다. format 포매팅은 전달되는 값의 타입을 추측하는 과정이 추가되기 때문.
#실은 + 연산자를 이용한 표현 방법이 제일 빠르다. 
#근데 포매팅으로 인해 연산의 부하는 없다고 한다. 파이썬은 '예쁘게 짜는 것'이란 언어적 신념을 갖고 있는 문자니
#format 포매팅을 애용하도록 하자.
#format() 함수는 표현하려는 값이 어떻던 변수명만 쓰면 되는데 %연산은 %s, %f, %d같이 표현하려는 변수의 타입을 알고있어야 한다.
# format 포매팅================================================================================================

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

#문자열 관련 함수================================================================
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
#문자열 관련 함수================================================================

#리스트========================================================================
#출력값으로 나오는 ['a', 'b', 'c', 'd']같은 애들을 '리스트'라고 부른다.
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
#리스트========================================================================

#튜플=========================================================================
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
# t1 = {1, 2, 'a','b'}
# t1[0] = 'c'#값 변경 시도 -> 에러, 튜플에서 지원하지 않는 기능이다. 
#인덱싱
# t1 = (1, 2, 'a', 'b')
# #print(t1[0])
# #print(t1[3])
# #슬라이싱
# #print(t1[1:])
# #더하기
# t2 = (3,4)
# # t3 = t1 + t2
# # print(t3)
# #곱하기
# t3 = t2 * 3
# #print(t3)
# #길이 구하기
# a = len(t1)
# print(t1)
# print(a)
#튜플=========================================================================

#딕셔너리============================================================================
#dic = {'name':'pey', 'phone':'01099993123','birth':1118}
#key:value의 쌍 여러개가 {}로 둘러싸여 있다. 여기서 key는 변하지 않는 값이며 value는 변할 수 있는 값이다. 
#딕셔너리는 연관 배열 또는 해시라 불리는 자료형의 파이썬 버전이다. 
#리스트와 튜플처럼 순차적으로 해당 요솟값을 구하지 않고 key를 통해 value를 얻을 수 있다. 
# a = {1:'hi'}#key로 1, value로 'hi'를 넣은 리스트
# b = {'b':[1,2,3]}#value로 리스트를 넣음
#딕셔너리 쌍 추가
# a = {1:'a'} #
# a[2] = 'b' # {2:'b'} 쌍 추가. 딕셔너리는 순차배열이 아니다. 그래서 a[0]부터 채워야 한다 뭐 그런거 없는듯 하다. 
# print(a)
# a['name'] = 'pey' # 'name'이라는 key에 'pey' 추가
# print(a)
# a[3] = [1,2,3]# 3이라는 key에 리스트 [1,2,3] 추가
# print(a)
#딕셔너리의 사용법
#a = {"김연아" : "피겨", "류현진", "야구", "박지성" : "축구"}
#위와 같이 각자의 특기를 표현할 수 있는 자료형을 만드는데 굉장히 편리하다. 
#사용 예
# grade = {'pey' : 10, 'julliet' : 99}
# print(grade['pey'])
# print(grade['julliet'])
#인데싱, 슬라이싱 기법을 사용해 요소값을 구하던 리스트, 튜플과는 다르게
#딕셔너리는 key를 사용해 value를 구하는 방법밖에 사용하지 못한다. 
#딕셔너리 이름[key]를 사용
# a = {1:'a', 2:'b'}
# print(a[1]) #리스트, 튜플의 a[1]과는 다르다. 여기서 1은 두번째 요소값을 가리키는게 아니라 '1'이라는 key를 가리키는 것이다. 
# print(a[2])
#뒤집어서 사용
# a = {'a':1, 'b':2}
# print(a['a'])#'a'라는 key에 해당하는 value를 출력
# print(a['b'])
#사용 예 2
# dic = {'name':'pey', 'phone':'01099993123','birth':1118}
# print(dic['name'])  #이름 출력
# print(dic['phone']) #전화번호
# print(dic['birth']) #생일
#딕셔너리 사용 주의점
#a = {1:'a', 1:'b'} #key를 중복해서 사용하면 하나 빼고 다 무시된다.
#print(a)#1:'a' 대신 1:'b'가 출력
#동일한 key가 존재 -> 어떤 value를 가져와야 할지 알 수 없음 -> 하나 빼고 다 무시당함
#그리고 key에 리스트는 사용할 수 없다. 값이 변할 수 있기 때문. 허나 값이 변하지 않는 튜플은 사용 가능하다
#a = {[1,2] : 'hi'}#type error 발생
# a = {(1,2) : "hi"}
# print(a[(1,2)])#"hi" 출력
#딕셔너리 관련 함수
# a = {'name':'pey', 'phone':'01099993123','birth':1118}
# #print(a.keys())#keys() : 딕셔너리의 key들을 모아 dict_keys 객체를 돌려줌
# #출력 결과 : dict_keys(['name', 'phone', 'birth'])
# #원래 keys()함수를 쓰면 리스트를 반환했었으나 메모리 낭비를 줄이기 위해 객체를 주는 방식으로 바뀌었다. 
# #만약 리스트를 받고 싶으면 list(a.keys())를 사용하면 된다. 
# #dict_keys객체는 리스트 고유의 append, insert, pop, remove, sort 함수를 실행할 수 없으나
# #그 외에는 리스트를 사용하는 것과 차이가 없다.
# # for k in a.keys():
# #     print(k)
# #dict_keys 객체를 list로 변환
# # list_a = list(a.keys())
# # print(list_a)
# # value리스트 만들기
# # list_a = list(a.values())#a의 value로 이루어진 dict_values를 list로 생성
# # print(list_a)
# #(key, value)쌍을 튜플로 묶은 값을 반환
# print(a.items())#튜플로 묶은 값을 dict_items객체로 돌려줌
# b = list(a.items())#dict_items객체를 list로 변환
# print(b)
# #key:value쌍 모두 제거
# a.clear()#딕셔너리 안의 모든 요소 삭제. 빈 딕셔너리는 {}로 표현
# print(a)#{}출력
#key로 value얻기
#a = {'name':'pey', 'phone':'01099993123','birth':1118}
# b = a.get('name')#key에 대응되는 value를 돌려줌. a['name']과 같은 값을 돌려받는다. 
# print(b)
# b = a.get('phone')
# print(b)
# b = a.get('nokey')#존재하지 않는 key의 value를 찾으려 하면 none을 반환. a['nokey']로 불러올 경우 에러발생
# print(b)
# #딕셔너리 안에 찾으려는 key값이 없을 경우 미리 정해준 디폴트값을 대신 가져오게 할 수 있다. 
# b = a.get('foo', 'bar')
# print(b) #'bar' 출력
# 해당 key가 딕셔러니 안에 있는지 조사
# b = 'name' in a #'name'키가 있는지 조사('키' in '딕셔너리')
# print(b)#있으니 true 출력
# b = 'email' in a
# print(b)#없으니 false 출력
# #나혼자 코딩 p96
# dic = {'name':'홍길동', 'birth':1128, 'age':30}
#딕셔너리============================================================================

#집합 자료형==========================================================================================
#집합에 관련된 것을 쉽게 처리하기 위해 만든 자료형
# s1 = set([1,2,3])#괄호 안에 리스트를 입력하여 생성
# print(s1)# {1,2,3} 출력
# s2 = set("Hello")#아니면 이렇게 문자열을 입력해 만들 수 있음
#print(s2) # {'o', 'e', 'H', 'l'} 출력
#set의 특징 : 중복이 없다. 순서가 없다(unordered)
#인덱스, 튜플은 순서가 있기 때문에(ordered) 인덱싱을 통해 요솟값을 얻을 수 있지만
#set 자료형은 순서가 없기 때문에 인덱싱으로 자료값을 얻을 수 없다. (딕셔너리처럼)
#만약 set 자료형에 저장된 값을 인덱싱으로 접근하려면 set 자료형을 list나 튜플로 만들어야한다. 
# s1 = set([1,2,3])
# l1 = list(s1)#집합을 리스트로 변환 
# print(l1)
# print(l1[0])
# t1 = tuple(s1)#집합을 튜플로 변환 
# print(t1)
# print(t1[0])
#교집합, 합집합, 차집합 구하기
# s1 = set([1,2,3,4,5,6])
# s2 = set([4,5,6,7,8,9])
# #교집합
# str_a = "교집합 : {0}".format(s1 & s2)
# print(str_a)#연산자를 사용하거나
# #혹은
# print(s1.intersection(s2))#함수를 사용
# #합집합
# str_b = "합집합 : {0}".format(s1|s2)
# print(str_b)
# #혹은
# print(s1.union(s2))#합수를 사용
# #차집합
# str_c = "차집합 : {0}".format(s1-s2)
# str_d = "차집합 : {0}".format(s2-s1)
# print(str_c)
# print(str_d)
# #혹은
# print(s1.difference(s2))#함수를 사용
# print(s2.difference(s1))#함수를 사용
#집합에 값 하나 추가(add)
# s1 = set([1,2,3])
# s1.add(4)
#print(s1)
#값 여러개 추가(update)
# s1 = set([1,2,3])
# s1.update([4,5,6])#함수에 여러개의 값을 추가
# print(s1)
#특정 값 제거하기(remove)
# s1 = set([1,2,3])
# s1.remove(2)#집합에서 2 제거
# print(s1)#{1,3} 출력
#s1.remove(2)#없는걸 제거하려고 하면 KeyError 발생
#집합 자료형==========================================================================================

#bool 자료형(참, 거짓)================================================================================
# a = True
# b = False
# print(type(a))#a의 타입을 출력. <class 'bool'>이 출력된다.
# print(type(b))#<class 'bool'> 출력
# #bool 자료형은 조건문의 반환값으로 사용된다.
# print(1==1)#조건문을 만족 -> True출력.
# print(2 > 1)#조건문 만족 -> True 출력
# print(2 < 1)#조건문 불만족 -> False 출력
#자료형에도 참, 거짓이 있다. 이는 매우 중요한 특징이며 실제로 자주 쓰인다.
#문자열, 리스트, 튜플, 딕셔너리 등의 값이 비어있으면 False 반환
#참, 거짓을 사용하는 예
# a = [1,2,3,4]
# while a:#while은 조건문이 true면 실행, false면 빠져나온다.
#     print(a.pop())
#a가 비었으면 False에 해당하기에 a가 빈 리스트가 되는 순간 while문을 빠져나온다.
#더 쉽게 이해할 수 있는 예
# if[]:#만약 조건에 해당하는 []가 참이면
#     print("참")#참 출력
# else:#참이 아니면
#     print("거짓")#거짓 출력.실제로 "거짓"이 출력된다.
# if[1,2,3]:#만약 조건에 해당하는 [1,2,3]가 참이면
#     print("참")#참 출력. 실제로 "참"이 출력
# else:#참이 아니면
#     print("거짓")#거짓 출력
#[]는 요소값이 없는 리스트기 때문에 거짓이고
#[1,2,3]은 요소값이 있는 리스트기 때문에 참이다.
#bool 연산
#bool 내장 함수를 사용하면 자료형의 참, 거짓을 식별할 수 있다
# print(bool('python'))#True출력
# print(bool(''))#False출력(빈 문자열)
# print(bool([1,2,3]))#True 출력
# print(bool([]))#False 출력(비어있는 리스트)
# print(bool(0))#False 출력(0이라 False)
# print(bool(3))#True출력
#bool 자료형(참, 거짓)================================================================================

#변수에 관하여===========================================================================================
#C, 자바와는 달리 파이썬은 변수를 선언할 때 자료형을 언급하지 않는다.
#파이썬에서 사용하는 변수는 객체를 가리키는 것
# a = [1,2,3]
# #[1,2,3]인 리스트 a를 생성할 경우 [1,2,3]의 값을 가지는 리스트 자료형(객체)이 
# #자동으로 메모리에 생성되고 a는 [1,2,3]리스트가 저장된 메모리의 주소를 가리킨다. 
# #a가 가리키는 리스트의 주소를 알아내기
# print(id(a))#140367316401216출력. 이 값은 매번 달라진다. 
#리스트의 복사에 관해
# a = [1,2,3]
# b = a#b에 a를 대입 -> 주소까지 복사한다. 
# # print(id(a))
# # print(id(b))
# #같은 주소값을 출력. [1,2,3]리스트를 가리키는 변수가 2개로 추가한 것 뿐이다. 
# #동일한 객체를 가리키고 있는지 확인 : is 사용
# print(a is b)#a와 b가 가리키는 객체는 동일한가? True 출력
# a[1] = 4# a[1]을 4로 바꿨다 
# print(a)# [1,4,3]을 출력 
# print(b)# [1,4,3]을 출력 -> 가리키는 대상이 같기 때문에 이런 결과가 나옴
# a변수의 값을 가지며 다른 주소값을 가진 b를 생성하는 방법
# a = [1,2,3]
# b = a[:]#a를 처음부터 끝까지 슬라이싱
# a[1] = 4
# print(a)#[1,4,3]출력
# print(b)#[1,2,3]출력
#copy함수를 사용할 수도 있다. 
# from copy import copy
# a = [1,2,3]
# b = copy(a)#이는 b = a[:]와 동일함
# a[1] = 4
# print(a)#[1,4,3]출력
# print(b)#[1,2,3]출력
# print(b is a)#다른 주소값을 가졌기에 False출력
#변수를 만드는 여러가지 방법
# a,b = ('python', 'life')#튜플로 a,b에 값을 대입. 
# (a,b) = 'python', 'life'#윗줄과 동일함. 'python', 'life'도 튜플. 튜플은 괄호 생략 가능
# print(a)
# print(b)
#리스트로 변수 생성
# [a,b] = ['python', 'life']
# print(a)
# print(b)
#여러개의 변수에 같은 값 대입
# a = b = 'python'
# print(a)
# print(b)
#스왑 
# a = 5
# b = 3
# print(a)
# print(b)
# a, b = b, a #스왑. C언어에서는 변수 3개에 코드 3줄인데 파이썬에서는 변수 2개에 코드 1줄이다.
# print(a)
# print(b)
#응용 p111
# a = [1,2,3] # ㅁㅁㅁㅁㅁㅁ번지에 생성된 [1,2,3]리스트를 가리키는 a
# b = [1,2,3] # ㄴㄴㄴㄴㄴㄴ번지에 생성된 [1,2,3]리스트를 가리키는 b
# print(a is b)#false 출력. 서로 다른 주소를 가리키기 때문.
#연습문제============================================================
#문제 1(평균점수 구하기)
# score = [80, 75, 55]
# num = 0
# count = 0
# while score:
#     num += score.pop()
#     count+=1
# print(num / count) #평균점수 출력
#문제 2(홀짝 구분)
# if 13%2 == 0:
#     print("짝수")
# else:
#     print("홀수") # 출력
#문제 3(문자열 슬라이싱)
# pin = "881120-1068234"
# yyyymmdd = pin[:6]
# num = pin[7:]
# print(yyyymmdd) #881120
# print(num) #1068234
#문제 4(주민등록번호에서 성별을 나타내는 숫자 출력)
# pin = "881120-1068234"
# print(pin[7])# 1 출력
#문제 5(문자열 대체)
# a = "a:b:c:d"
# b = a.replace(":", "#")
# print(b)# "a#b#c#d"출력
#문제 6(리스트 순서 변경)
# a = [1,3,5,4,2]
# a.sort()
# a.reverse()
# print(a) #[5,4,3,2,1]출력
#문제 7(리스트에 있는 문자열 모아서 한번에 출력)
# a = ["Life", "is", "very", "short"]
# result = " ".join(a)
# print(result) # Life is very short 출력
#문제 8(튜플에 값 추가)
# a = (1,2,3)
# a = a + (4, )#(4)는 튜플이 아니지만 (4, )는 튜플이다. 튜플 + 튜플 연산을 해야한다.
# print(a)
# a = dict()
# a['name'] = 'python'
# a[('a', )] = 'python'
# a[[1]] = 'python' #리스트는 변할 수 있다 -> key로 사용 불가능. key로 사용 가능한 자료형은 '변할 가능성이 없는' 자료형이다. 
# a[250] = 'python' 
#문제 10(딕셔너리에서 해당되는 값 추출)
# a = {"A":90, "B":80, "C":70}
# result = a.pop("B")#값을 추출하며 추출한 값을 반환
# print(a)
# print(result)# 80 출력
#문제 11(리스트에서 중복 숫자 제거)
# a = [1,1,1,2,2,3,3,3,4,4,5]
# aSet = set(a)
# b = list(aSet)
# print(b)# [1,2,3,4,5]출력
#문제 12(여러개의 변수 선언)
# a = b = [1,2,3]#ㅁㅁㅁㅁ주소값을 가진 [1,2,3]리스트를 a와 b가 가리킴
# a[1] = 4 #a가 가리키는 리스트의 두번째 요솟값을 4로 변경
# print(b) #a와 같은 리스트를 가리키고 있으니 [1,4,3]을 출력
#연습문제============================================================
#if문===============================================================
# money = True
# if money:#money가 True면
#     print("택시를 타고 가라")#이거 출력. money=True이므로 이 문구가 출력 된다.
# else:#False면
#     print("걸어가라")#이거 출력.
#if의 조건에 따라 수행할 문장은 들여쓰기를 해야한다. 
#들여쓰기를 하지 않을 경우 에러가 발생
#들여쓰기는 공백(space bar) 4개를 하는 것을 권장한다고 한다.
#조건문 다음에 ':'을 붙혀야한다. 이는 파이썬의 문법 구조다. 
# a = 4
# b = 2
# print(a > b)# true 출력
# 조건문 예제
# money = 2000
# if money >= 3000:# (money>=3000)이 True면
#     print("택시 타라")# 이거 출력
# else:#False면
#     print("걸어 가라")# 이거 출력. money=2000이기에 이거 출력됨.
# or연산자 사용 예제
# money = 2000
# card = True
# if money >= 3000 or card:# (money>=3000)거나 card = True일 때
#     print("택시 타라")# 이거 출력. 실제로 이거 출력
# else:#False면
#     print("걸어 가라")# 이거 출력. 
#x in s, x not in s(파이썬만 가지고 있는 조건문)
# x in 리스트, x not in 리스트
# x in 튜플, x not in 튜플
# x in 문자열, x not in 문자열
# b = 1 in [1,2,3]# [1,2,3] 안에 1이 있는가? -> True
# print(b)
# b = 1 not in [1,2,3]# [1,2,3] 안에 1이 없는가? -> False
# print(b)
# #튜플 
# c = 'a' in ('a', 'b', 'c')
# print(c)
# #문자열
# d = 'j' not in 'python'
# print(d)
# pocket = ['paper', 'cellphone', 'money']
# if 'money' in pocket:# pocket 리스트에 'money'가 있는가?
#     print("택시를 타고 가라")#있으니까 이거 출력
# else:
#     print("걸어가라")
#조건문 넘기기
# pocket = ['paper', 'cellphone', 'money']
# if 'money' in pocket:# pocket 리스트에 'money'가 있는가?
#     pass#pass가 있으면 조건이 True여도 넘어감
# else:
#     print("카드를 꺼내라")
# elif
# C, C++의 else if 역할을 한다. 
# pocket = ['paper', 'cellphone']
# card = True
# if 'money' in pocket:# 포켓에 돈이 있으면
#     print("택시를 타고 가라")# 이거 출력
# elif card:# 돈은 없는데 카드가 있다면
#     print("택시를 타고 가라") #이거 출력. 실제로 이거 출력.
# else:#둘다 없으면
#     print("걸어 가라")# 이거 출력
#조건부 표현식
score = 60
# if score >= 60:
#     message = "success"
# else:
#     message = "failure"
#위 코드를
# message = "success" if score >= 60 else "failure"
#와 같이 한 줄로 표현 가능(조건문이 참인 경우 if 조건문 else 조건문이 거짓인 경우)
#조건부 표현식은 가독성에 유리하고 한 줄로 작성할 수 있어 활용성이 좋다.
#if문===============================================================
#while문============================================================
# treeHit = 0
# while treeHit < 10:# treeHit이 10보다 작을 때까지 반복문 실행
#     treeHit = treeHit + 1
#     print("나무를 %d번 찍었다." %treeHit)
#     if treeHit == 10:
#         print("나무 넘어갑니다")
# prompt = """
# 1. Add
# 2. Del
# 3. List
# 4. Quit

# Enter number : """
# number = 0
# while(number != 4):
#     print(prompt)
#     number = int(input())# 사용자의 숫자 입력을 받아들인다.
#while문 강제 중지(break)
# coffee = 10
# money = 300
# while money:
#     print("돈을 받았으니 커피를 줍시다.")
#     coffee = coffee - 1
#     print("남은 커피의 양은 %d입니다." %coffee)
#     if(coffee == 0):
#         print("커피가 다 떨어졌습니다. 판매를 중지합니다.")
#         break
# coffee = 10
# while True:
#     money = int(input("돈을 넣어주세요: "))# 값을 입력받는 부분. 입력받은 숫자를 money에 대입
#     if money == 300:
#         print("커피를 줍니다")
#         coffee = coffee - 1
#     elif money > 300:
#         print("거스름돈 %d를 주고 커피를 줍니다." %(money - 300))
#         coffee = coffee - 1
#     else:
#         print("돈을 다시 돌려주고 커피를 주지 않습니다.")
#         print("남은 커피의 양은 %d개 입니다." %coffee)
#     if coffee == 0:
#         print("판매를 중단합니다.")
#         break;
#while문의 맨 처음으로 돌아가기
#while문을 빠져나가지 않고 맨 처음으로 다시 돌아가는 법
# a = 0
# while a<10:
#     a = a + 1
#     if a%2 == 0: continue #continue문을 사용하면 while 문의 맨 맨 처음으로 돌아간다. 
#     print(a)
#나 혼자 코딩! p136
a = 0
# while a<10:
#     a = a + 1
#     if a%3 == 0: continue #continue문을 사용하면 while 문의 맨 맨 처음으로 돌아간다. 
#     print(a)
#while문============================================================
#for문============================================================
#파이썬의 직관적 특징을 가장 잘 대변해주는 것
#전형적인 for문
# test_list = ['one', 'two', 'three']
# for i in test_list: #리스트 속 요소 중 'one'이 먼저 i에 대입
#     print(i) #one, two, three출력
#사용 예제2
# a = [(1,2), (3,4), (5,6)]
# for (first, last) in a: #a 리트의 요소값이 튜플이라 각각 요소가 자동으로 (first, last)변수에 대입
#     print(first + last)
#사용 예제3
# marks = [90, 25, 67, 45, 80]
# num  = 0
# for score in marks: 
#     num = num + 1
#     if score > 60:
#         print("%d번 학생은 합격" %num)
#     else:
#         print("%d번 학생은 불합격" %num)
#리스트의 마지막 부분까지 가리켰다는 걸 판단한다는 것이 신기하다.
#그리고 score에 mark의 요소값을 넣는다는 것도 신기하다. c, c++의 for문과는 비교도 안되는 강력함이라 생각한다. 
#continue
# marks = [90, 25, 67, 45, 80]
# num = 0
# for score in marks:
#     num = num + 1
#     if(score < 60): continue
#     else: 
#         print("%d번 학생 축하합니다. 합격입니다." %num)
#range() : 숫자 리스트를 자동으로 만들어줌
# a = list(range(10))#이렇게 리스트화 해서 사용할 수도 있다. 이렇게 사용하지 않아도 된다.
# print(a)
#사용 예제
# add = 0
# for i in range(1, 11):
#     add = add + i
# print(add)
#사용 예제 2
# marks = [90, 25, 67, 45, 80]
# for num in range(len(marks)):#range(len(marks))는 range(5)가 될 것이며 이 범위는 0~4다.
#     if(marks[num]) > 60: print("%d번 학생 축하합니다. 합격입니다." %(num + 1))
#     else: continue
#for문과 range()를 이용한 구구단
# for i in range(2, 10):
#     for j in range(1, 10):
#         print(i * j, end=" ")#end=" "는 결괏값을 출력할 때 줄바꿈 하지 말라고 넣어둔 것이다.
#     print('')
# 리스트 내포 - 리스트 안에 for문을 포함
#리스트 내포를 사용하지 않은 예
# a = [1,2,3,4]
# result = []
# for num in a:#a안에 있는 num을 하나씩 가리킨다.
#     result.append(num * 3)#num의 요솟값을 3씩 곱해 result안에 넣어줌
# print(result)#결과값 [3,6,9,12]출력
#리스트 내포를 사용한 예
# a = [1,2,3,4]
# result = [num * 3 for num in a]#리스트 내포. a 안에 있는 요소값들을 3씩 곱한걸 요소값으로 쓰겠다.
# print(result)
#리스트 요소 + 조건문
# a = [1,2,3,4]
# result = [num * 3 for num in a if num % 2 == 0]# [1,2,3,4] 중 짝수에만 3을 곱해 result에 담겠다.
# print(result)
#리스트 내포의 일반 문법 : [표현식 for 항목 in 반복 가능 객체 if 조건]
#for문을 여러개 사용할 수도 있다. 
#구구단을 리스트 안에 넣는 예
# result = [x * y for x in range(2, 10)
# for y in range(1, 10)]
# print(result)
#for문============================================================
#연습문제===========================================================
#문제 1(코드 결과값)
# a = "Life is too short, you need python"

# if "wife" in a:print("wife")
# elif "python" in a and "you" not in a: print("python")
# elif "shirt" not in a: print("shirt")#이거 출력
# elif "need" in a: print("need")#얘도 True지만 위에서 True인 조건문이 있었기에 여기에 오질 못했다.
# else: print("none")
#문제 2(1~1000의 자연수 중 3의 배수의 합)
# result = 0
# i = 1
# while i<= 1000:
#     if i % 3 == 0:
#         result +=i
#     i += 1
# print(result)
# 문제 3(while문을 사용해 피라미드 제작)
# i = 0
# while(True):
#     i +=1
#     if(i > 5): break
#     print('*' * i)
#문제 4(for문을 사용해 1~100까지의 숫자 출력)
# for i in range(1, 101):
#     print(i)
#문제 5(평균 점수 구하기)
# A = [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]
# total = 0
# for score in A:
#     total += score
# average = total / len(A)
# print(average)
#문제 6(리스트 내포를 사용해 홀수에만 2를 곱해 저장하는 리스트 생성)
# numbers = [1,2,3,4,5]
# result = [num * 2 for num in numbers if num % 2 == 0]
# # 넣을 값 : num * 2. num은 누구? numbers의 요솟값. 넣을 조건은? num % 2 == 0 을 성립하는 num만 넣을 것
# print(result)
#연습문제===========================================================
#함수==================================================================
#파이썬 함수의 구조
# def add(a, b): #def 함수 이름(매개변수) : 수행할 문장...
#     return a+b#마지막에 리턴
# a = 3
# b = 4
# c = add(a,b)
# print(c)
# print(add(a,b))
#입력값이 없는 함수
# def say():
#     return "hi"
# a  = say()
# print(a)
#결과값이 없는 함수
# def add(a,b):
#     print("%d, %d의 합은 %d입니다."%(a,b,a+b))
# a = add(3,4)# 반환값이 없다.
# print(a)# none이 출력
# 입력값도 결과값도 없는 함수
# def say():
#     print("hi")
# say()#입력값, 반환값이 없는 say함수를 사용할 수 있는 유일한 방법
#매개변수 지정하여 호출
# def add(a,b):
#     return a+b
# # result = add(a = 3, b = 4)#a에 3, b에 4라고 지정하여 호출
# # print(result)
# #매개변수 지정의 장점 : 순서에 상관없이 사용 가능
# result = add(b = 5, a = 4)#순서 상관없다. 
# print(result)
#입력값의 갯수를 확신할 수 없을 때
# def add_many(*args):
#     result = 0
#     for i in args:
#         result +=i
#     return result

# result = add_many(1,2,3,4,5,6,7,8,9,10)#리스트가 아니라 매개변수로 하나씩 다 넣어주면 된다.
# print(result)
#예제 2
# def add_mul(choice, *args):#두가지 종류의 매개변수를 포함한 함수
#     if choice == "add":
#         result = 0
#         for i in args:
#             result +=i
#     elif choice == "mul":
#         result = 1
#         for i in args:
#             result *=i
#     return result
# result = add_mul('add', 1,2,3,4,5)
# print(result)
# result = add_mul('mul',1,2,3,4,5)
# print(result)
#키워드 파라미터
# def print_kwargs(**kwargs):#키워드 파라미터를 사용할 때는 매개변수 앞에 별 두개(**)를 붙힌다. 
#     print(kwargs)
# #딕셔너리로 만들어져 출력됨
# #**kwargs와 같은 **매개변수는 딕셔너리가 되고 모든 key=value 형태의 결과값이 저장된다.
# print_kwargs(a=1)
# print_kwargs(name = 'foo', age = 3)
# def add_and_mul(a,b):
#     return a+b, a*b
# result = add_and_mul(a=3,b=4) #결과값은 언제나 하나 -> (a+b, a*b)꼴이 튜플이 반환됨.
# print(result) #(7,12)가 출력
# #return의 또다른 쓰임새
# def say_nick(nick):
#     if nick == "바보":
#         return# 입력값으로 '바보'가 들어오면 문자열을 출력하지 않고 함수를 탈출
#     print("나의 별명은 %s입니다."%nick)
# say_nick('야호')
# say_nick('바보')
# 매개변수의 초기값 미리 정하기
# def say_myself(name, old, man=True):#매개변수에 미리 값을 넣어줌. 
#     print("나의 이름은 %s입니다." %name)
#     print("나이는 %d살입니다." %old)
#     if man:
#         print("남자입니다.")
#     else:
#         print("여자입니다.")

# say_myself('박응용', 27)
# say_myself('박응용', 27, True)#윗줄과 같은값 출력
# say_myself('박응용', 27, False)#여자라고 출력
#매개변수 위치를 바꿀 경우
# non-default argument follows default argument발생. 이는 매개변수 뒤에 초깃값을 설정해놓지 않은 매개면수는 사용할 수 없다는 뜻.
#초기화시키고 싶은 매개변수는 항상 뒤쪽에 놔둬야 한다. 
# def say_myself(name, man=True, old):#매개변수에 미리 값을 넣어줌. 
#     print("나의 이름은 %s입니다." %name)
#     print("나이는 %d살입니다." %old)
#     if man:
#         print("남자입니다.")
#     else:
#         print("여자입니다.")

# say_myself("박응용", 27)

#전역변수
# a = 1
# def vartest():
#     global a# 함수 밖의 a를 직접 사용하겠다.
#     a+=1
# vartest()
# print(a)#2출력
# lambda 사용================
# 함수를 생성할 때 사용하는 예약어. def와 동일한 역할. 함수를 한 줄로 간결하게 만들 때 사용한다. 
# def를 사용할 정도로 복잡하지 않거나 def를 사용할 수 없는 곳에서 쓰인다. 
# 사용 예제
# add = lambda a, b: a+b #lambda로 만든 함수는 return명령어가 없어도 결과값을 돌려준다.
# result = add(3,4)
# print(result)
# lambda 사용================
#사용자 입력과 출력========================================
#사용자 입력
# a = input()#사용자가 입력한 문장을 a에 대입. input()은 입력받는 모든 것은 문자열로 취급한다. 
# print(a)
#문구를 띄우며 입력 받기
# a = input("숫자를 입력하세요 : ")
# print(a)
#print에 대하여
# print("life" "is" "too short")#1
# print("life"+"is"+"too short")#2
# #1과 2는 동일한 값 출력. 따옴표로 둘러쌓인 문자열을 연속해서 쓰면 +연산을 한 것과 같다.
# #문자열 띄어쓰기
# print("life","is","too short")#콤마를 사용하면 띄어쓰기를 할 수 있다.
#결과값 출력 복습
# for i in range(10):
#     print(i, end=' ')
#파일 읽고 쓰기
#파일 쓰기
# f = open("/Users/minkyu/Documents/PythonCode/새파일.txt", 'w')#쓰기 모드로 새파일.txt를 생성. 경로를 다 써줘야한다. 
# for i in range(1, 11):
#     data = "%d번째 줄입니다.\n" % i
#     f.write(data)
# f.close()
#p172까지 함(200823)
#외부에 저장된 파일을 읽는 여러가지 방법=======================
#readline() 사용
# f = open("/Users/minkyu/Documents/PythonCode/새파일.txt", 'r')
# while True:
#     line = f.readline() #파일을 한 줄씩 읽어 들인다
#     if not line:break
#     print(line)
# f.close()
#readlines() 이용
# f = open("/Users/minkyu/Documents/PythonCode/새파일.txt", 'r')
# lines = f.readlines()#각각의 줄을 요소로 갖는 리스트를 반환
# for line in lines:
#     print(line)
# f.close()
#read() 이용
# f = open("/Users/minkyu/Documents/PythonCode/새파일.txt", 'r')
# data = f.read()#파일 전체 내용을 문자열로 돌려줌
# print(data)#파일 전체 내용을 출력
# f.close()
#파일 추가 모드('a')
# f = open("/Users/minkyu/Documents/PythonCode/새파일.txt", 'a')# 파일 추가 모드
# for i in range(11, 20):
#     data = "%d 번째 줄입니다.\n" % i
#     f.write(data)
# f.close()
#파일을 자동으로 닫아줌(with)
# with open("/Users/minkyu/Documents/PythonCode/kim.txt", 'w') as f:
#     f.write("Life is too short, you need python")
#연습문제================================================
#연습문제1(주어진 자연수의 홀, 짝 여부 판단)
# def is_odd(number):
#     if number % 2 == 0:
#         return True
#     else:
#         return False
# num = int(input())
# print(is_odd(num))
#연습문제2(입력으로 들어오는 모든 수의 평균 값을 계산해 주는 함수)
# def avg_numbers(*args):
#     result = 0
#     for i in args:
#         result+=i
#     return result / len(args)

# print(avg_numbers(1, 2))
# print(avg_numbers(1,2,3,4,5))
#연습문제3(두 개의 숫자를 입력받아 더하여 돌려주는 프로그램)
# input1 = int(input("첫번째 숫자를 입력해주세요:"))
# input2 = int(input("두번째 숫자를 입력해주세요:"))

# total = input1 + input2
# print(total)
#연습문제5(문자열 저장)
# f1 = open("test.txt", 'w')# /Users/minkyu에 저장된다.
# f1.write("Life is too short")
# f1.close()# 필수

# f2 = open("test.txt", 'r')
# print(f2.read())
# f2.close()
#연습문제6(입력을 저장)
# user_input = input("저장할 내용을 입력하세요:")
# f = open('test.txt', 'a')
# f.write(user_input)
# f.close()
#연습문제7(문자열 변경)
# f=open('test.txt', 'r')
# body = f.read()
# f.close()

# body = body.replace("java", "python")

# f = open('test.txt', 'w')
# f.write(body)
# f.close()
#연습문제================================================
#사용자 입력과 출력========================================
#클래스====================================================
# class Calculator:#클래스 선언
#     def __init__(self):
#         self.result = 0#초기값 0

#     def add(self, num):#클래스 함수
#         self.result +=num
#         return self.result
#     def sub(self, num):
#         self.result -=num
#         return self.result

# cal1 = Calculator()#객체 생성
# cal2 = Calculator()

# #클래스 함수 호출
# print(cal1.add(3))
# print(cal1.add(4))
# print(cal2.add(3))
# print(cal2.add(7))
#사칙연산 클래스 생성
# class FourCal: #클래스 선언
#     def __init__(self, first, second):
#         self.first = first
#         self.second = second
#     def setdata(self, first, second): #초기화 함수에서 클래스에 속하는 변수를 만드는듯? 매개변수로(객체 본인, 인자1, 인자2, ...)이렇게 받는듯.
#         self.first = first #함수 호출시 함수를 호출한 객체가 자동으로 첫번째 인수로 
#         self.second = second
#     def add(self):
#         return (self.first + self.second)
#     def sub(self):
#         return (self.first - self.second)
#     def div(self):
#         return (self.first / self.second)
#     def mul(self):
#         return (self.first * self.second)

# a = FourCal(2,4) #생성자가 정의되었으면 생성자 __init__호출
# print(type(a))#객체 타입을 출력. Fourcal()의 인스턴스임을 확인할 수 있음 
# FourCal.setdata(a, 3, 4)#이렇게도 호출 가능
# print(a.first)
# print(a.second)
# a.first = 5
# a.second = 6
# print(a.first)
# print(a.second)
# print(a.add())
# print(a.sub())
# print(a.mul())
# print(a.div())
#인자를 초기화하지 않고 사용할 경우 에러 발생
#클래스 상속=========================
# class MoreFourCal(FourCal):# 상속 클래스 이름(부모 클래스 이름)
#     def pow(self): # 제곱 함수
#         result = self.first ** self.second#  **가 제곱 연산
#         return result
# a = MoreFourCal(2,4)
# print(a.pow())
#상속받은 클래스 함수 모두 사용 가능
# class safeFourcal(FourCal):
#     def div(self):# 메서드 오버라이딩
#         if self.second == 0 :
#             return 0
#         else:
#             return (self.first / self.second)
# a = safeFourcal(4,0)
# print(a.div())# 0을 반환
#클래스 변수
# class Family:
#     lastname = "박" # 클래스 변수. 클래스의 모든 객체에 공유되는 변수
# print(Family.lastname)# 클래스 변수 출력. "박"
# a = Family()
# b = Family()
# Family.lastname = "김"# 클래스 변수는 바꿀 수 있다. 바꾼 값도 모든 객체가 공유한다.
# a.lastname = "성"#객체의 클래스 변수 == 일반변수다.
# print(a.lastname)# "성"
# print(b.lastname)# "김"
#클래스====================================================
#모듈=====================================================
#모듈 : 함수, 변수, 클래스를 모아놓은 파일
#C언어의 헤더파일 불러오듯 불러오는건가 싶다. 굳이 따지자면 .cpp나 .c를 불러온다고 생각하면 된다. 
# #inlcude "asdfasfd.h"꼴과 같다고 생각하자. 
#형식 : import 모듈 이름(이미 만들어놓은 파이썬 모듈을 사용할 수 있게 해주는 명령어라 .py는 입력하지 않는다.)
#모듈 이름 없이 함수 이름만 쓰고 싶을 때(== using namespace)
# from 모듈 이름 import 모듈 함수 형식으로 쓰도록 한다. 
# 예제
# from mod1 import add
# add(3,4) #7을 출력. mod1.add(3,4)과 같이 쓰지 않아도 된다.
#함수를 여러개 가져오기
# from mod1 import add, sub #함수 이름 2개 입력
# from mod1 import * # *는 '모든 것'이라는 뜻
#if __name__ == "__main__"의 의미 : 직접 실행되었을 때만 아래 코드를 실행한다는 뜻(mod1.py를 참조)
#__name__ 변수 : 파이썬이 내부적으로 사용하는 특별한 변수 이름. 실행된 .py파일의 이름이 들어간다. 여기 경우엔 Hello가 __name__에 들어간다. 
#클래스나 변수 등을 포함한 모듈(mod2)
#import mod2
#a = mod2.Math()#모듈 안에 있는 클래스 사용 -> '.'사용
#print(a.solv(2))
#print(mod2.add(mod2.PI, 4.4))
#다른 파일에서 모듈 불러오기(modtest.py)
#모듈=====================================================
#패키지=====================================================
#도트를 사용하여 파이썬 모듈을 계층적으로 관리할 수 있게 해준다.
#예 : A패키지에 있는 모듈 B : A.B
#패키지 예제는 다른 파일에서
#결론 : 라이브러리 만드는거 같은 기분이 들었다. 나중에 필요할 때 책 보면서 복습해야지.
#패키지=====================================================
#200826 : 클래스, 모듈, 패키지에 대해 배움. 클래스는 뭐 내가 알던 그거고 모듈은 C언어의 .h파일을 include하는 느낌 들게 하는 친구고
#패키지는 라이브러리 제작하는 것 같은 기분이 들었다. 했던거라 어렵지는 않은데 이걸 몸에 체득해서 쓰기에는 시간이 좀 걸리지 않을까 싶다. 
#예외 처리=====================================================
#try.except문
#try 블록 수행 중 오류가 발생시 except 블록이 수행.
#try 블록 수행 중 오류가 발생하지 않으면 except 블록 수행 X
#1. try, except만 표기
#try:
#   4 / 0
#except: #오류 종류에 상관없이 오류가 발생하면 except블록을 수행
#   print("에러")
#2. 발생 오류만 포함한 except문
# try:
#     4 / 0
# except ZeroDivisionError: # except문에 미리 정해 놓은 오류 이름과 일치할 때만 except 블록을 수행
#     print("에러")
#3. 발생 오류와 오류 메세지 변수까지 포함한 except문
# try:
#     4/0
# except ZeroDivisionError as e:#오류 메세지의 내용까지 알고 싶을 때 사용하는 방법
#     print(e)#e에 오류 메세지가 담긴다.
#indexError
# try:
#     a = [1,2,3]
#     print(a[4])
# except IndexError as e:
#     print(e)#list index out of range 출력
#finally문
#try문 수행 도중 예외 발생 여부에 상관없이 항상 수행된다. 
#사용한 리소스를 close해야할 때 많이 사용
# f = open('foo.txt', 'w')
# try:
#     f.write("hi")
# finally:# try문을 수행한 뒤 예외 발생 여부와 상관없이 수행된다.
#     f.close()
#여러 개의 오류 처리
# try:
#     a = [1,2]
#     print(a[3])
#     4/0
# except ZeroDivisionError:# 인덱싱 오류가 먼저 발생했기에 이 문은 시행되지 않는다. 
#     print("0으로 나눌 수 없습니다.")
# except IndexError:# 인덱싱 오류가 먼저 발생 -> 이 문으로 먼저 넘어옴.
#     print("인덱싱할 수 없습니다.")
#+오류 메세지 출력
# try:
#     a = [1,2]
#     print(a[3])
#     4/0
# except ZeroDivisionError as e:# 인덱싱 오류가 먼저 발생했기에 이 문은 시행되지 않는다. 
#     print(e)
# except IndexError as e:# 인덱싱 오류가 먼저 발생 -> 이 문으로 먼저 넘어옴.
#     print(e)# list index out of range 출력
#오류 회피하기
# try:
#     f = open('없는파일.txt', 'r')
# except FileNotFoundError:
#     pass# 파일이 없더라도 오류를 발생시키지 않고 통과
#오류 일부러 발생시키기
# class Bird:
#     def fly(self):
#         raise NotImplementedError # 자식 클래스는 반드시 fly라는 함수를 구현하도록 만들고 싶을 때 이렇게 일부러 에러를 발생
    #에러를 발생시키니 자식 클래스는 반드시 fly함수를 오버라이딩 해야한다.
# class Eagle(Bird):
#     pass
# eagle = Eagle()
# eagle.fly()# NotImplementedError 발생
# 에러가 발생하지 않게 하려면
# class Eagle(Bird):
#     def fly(self):# 함수 재정의
#         print("very fast")

# eagle = Eagle()
# eagle.fly()
#예외 만들기
#특수한 경우에만 예외 처리를 하기 위해 예외를 만들어서 사용
#파이썬 내장 클래스인 Exception 클래스를 상속하여 만들 수 있다. 
# class MyError(Exception):
#     def __str__(self):
#         return "허용되지 않는 별명입니다." # 얘가 e에 들어간다. 

# def say_nick(nick):
#     if nick == "바보":
#         raise MyError()
#     print(nick)

# # say_nick("천사")
# # say_nick("바보")# '천사'가 한 번 출력된 후 MyError 발생
# try:
#     say_nick("천사")
#     say_nick("바보")# MyError 발생
# # except MyError:
# #     print("허용되지 않는 별명입니다.")# 천사를 출력 후 여기로 온다.
# # 오류 메세지를 사용하고 싶을 때
# except MyError as e:
#     print(e) # __str__메서드를 구현해야 e에 값이 담김
#예외 처리=====================================================
#내장 함수=====================================================
#내장 함수는 import 없이 바로 사용할 수 있다(예 : print 등)
#abs(절대값)
# print(abs(-3))
# print(abs(-1.2))
#all(반복 가능한 자료형 x를 입력 인수로 받음. x가 모두 참이면 True, 거짓이 하나라도 있으면 False 반환)
#반복 가능한 자료형은 리스트, 튜플, 문자열, 딕셔너리, 집합이 있다. 
# print(all([1,2,3]))# 요소가 모두 참 -> True 반환
# print(all([1,2,3,0]))# 요소 중 0이 포함 -> False 반환
#any(x중 하나라도 참이 있으면 True, 모두 거짓이면 False)
# print(any([1,2,3,0]))# True 반환
# print(any([0,""]))# 모두 거짓 -> False 반환
#chr(아스키코드 값을 입력받아 해당하는 문자를 출력)
# print(chr(97))# 'a'
# print(chr(48))# 0
# dir(객체가 자체적으로 가지고 있는 변수나 함수를 보여준다)
# c = dir([1,2,3]) # 리스트 '객체' -> 리스트가 가지고 있는 함수 목록
# print(c)
# d = dir({'1' : 'a'})# 딕셔너리 '객체' -> 딕셔너리가 가지고 있는 함수 목록
# print(d)
#divmod(a를 b로 나눈 몫과 나머지를 튜플 형태로 돌려줌)
# print(divmod(7,3))# (2,1)출력
#enumerate(순서가 있는 자료형을 입력 받아 인덱스 값을 포함하는 enumerate 객체로 돌려줌)
# for i, name in enumerate(['body', 'foo', 'bar']):#i와 name을 enumerate(['body', 'foo', 'bar'])에서 받는다.
#     print(i, name)
    #0 body
    #1 foo
    #2 bar 출력
# eval(expression, 실행 가능한 문자열을 입력 받아 문자열을 실행한 결과값을 돌려줌)
# print(eval('1+2'))# 3 출력
# print(eval("'hi' + 'a'"))# hia 출력
# print(eval('divmod(4,3)'))# (1,1) 출력
# eval 함수는 입력받은 문자열로 파이썬 함수나 클래스를 동적으로 실행하고 싶을 때 사용
# filter(함수 이름과 인수를 자료형으로 받아 인수에 함수를 넣었을 때 True를 반환하는 것만 골라내서 돌려줌)
#filter를 쓰지 않을 경우
# def positive(l):
#     result= []#반환값이 참인 것만 골라내서 저장할 변수
#     for i in l:
#         if i > 0:
#             result.append(i)
#     return result
# print(positive([1,-3,2,0,-5,6]))#[1,2,6] 출력
# filter를 사용할 경우
# def positive(x):
#     return x > 0
#                   # 함수이름, 들어갈 인수(목록)
# print(list(filter(positive, [1,-3,2,0,-5,6])))# [1,2,6] 출력
#lambda를 사용해 더 간편하게
# print(list(filter(lambda x: x>0, [1,-3,2,0,-5,6])))#[1,2,6] 출력
#hex(정수를 16진수로 변경)
# print(hex(234))# 0x3a
# print(hex(3))# 0x3
#id(객체를 입력받아 객체의 고유 주소 값을 반환)
# a = 3
# print(id(a))#a가 가리키는 메모리 주소를 반환
# print(id(3))#같은 주소값 반환
# b = a
# print(id(b))#같은 주소값 반환 -> 모두 같은 객체를 가리킴
# print(id(4))#다른 객체 -> 다른 주소값 반환
#input(사용자 입력을 받는 함수)
# a = input()
# print(a)
# b = input("Enter : ")
# print(b)
# int(문자열 형태의 숫자나 소숫점이 있는 숫자 등을 정수 형태로 반환)
# print(int('3'))# 3
# print(int(3.4))# 3
# int(x, radix)는 radix 진수로 표현된 문자열 x를 10진수로 변환하여 돌려줌
# print(int('11', 2))# 2진수로 표현된 '11'을 10진수로 변환
# print(int('1A', 16))# 16진수로 표현된 '1A'을 10진수로 변환
# isinstance(첫 번째 인수로 인스턴스, 두 번째 인수로 클래스 이름을 받음. 인스턴스가 그 클래스의 인스턴스가 맞으면 True, 아니면 False 반환)
# class person: pass
# a = person()
# b = 3
# print(isinstance(a, person))# 인스턴스 맞는지 여부 판단. True 반환
# print(isinstance(b, person))# False 반환. 왜냐하면 b는 person 클래스의 인스턴스가 아니니까.
# len(입력값의 길이(요소의 전체 개수)를 반환)
# print(len("python"))# 6
# print(len([1,2,3]))# 3
# print(len((1, 'a')))# 2
#list(반복 가능한 자료형을 리스트로 만들어서 반환)
# print(list("python"))# ['p', 'y', 't', 'h', 'o', 'n']
# print(list((1,2,3)))# [1, 2, 3]
#리스트를 넣으면 리스트를 반환
#map(함수와 반복 가능한 자료형을 입력받아 함수가 수생한 결과를 반환)
#map을 쓰지 않을 경우
# def two_times(numberList):
#     result = []
#     for number in numberList:
#         result.append(number * 2)
#     return result

# result = two_times([1,2,3,4])
# print(result)# [2,4,6,8] 반환
# map을 사용
# def two_times(x) : return x*2
# print(list(map(two_times, [1,2,3,4])))# [1,2,3,4]의 요솟값을 차례대로 two_times에 넣고 반환된 값을 차레대로 list에 담아 list 생성
# max(반복 가능한 자료형을 입력받아 최댓값 반환)
# print(max([1,2,3]))# 3 반환
# print(max("python"))# y 반환
# min(max와 반대)
# print(min([1,2,3]))# 1 반환
# print(min("python"))# h 반환
# oct(정수 형태의 숫자를 8진수 문자열로 바꾸어 반환)
# print(oct(34))# 0o42
# print(oct(12345))# 0o30071
# open(파일 이름과 읽기 방법을 입력받아 파일 객체를 돌려주는 함수)
# f = open("binary_file", "rb")#바이너리 읽기 모드(바이너리 모드는 기존 키워드에 b를 추가)
# f = open("binary_file", "rw")#바이너리 쓰기 모드
# fread1 = open("read_mode.txt", 'r')
# fread2 = open("read_mode.txt")# fread1과 fread2는 동일한 방법
#->모드 부분을 생락하면 기본값으로 읽기 모드(r)를 갖게 된다.
# fappend = open("append_mode.txt", 'a')# 추가 모드로 파일을 여는 예
# ord(문자의 아스키 코드 값을 반환)
# print(ord('a'))# 97
# print(ord('0'))# 48
# chr함수(int -> char)와 반대다(ord 함수는 char -> int)
# pow(제곱 반환)
# print(pow(2,4))# 2의 4제곱 반환
# print(pow(3,3))# 3의 3제곱 반환
# range(입력받은 숫자에 해당하는 범위 값을 반복 가능한 객체로 반환)
# 인수가 하나일 경우
# print(list(range(5)))# [0,1,2,3,4] 출력
#인수가 2개일 경우(시작, 끝)
#끝 숫자는 해당값에 포함되지 않는다.
# print(list(range(5,10)))# [5,6,7,8,9] 출력
# range()의 반환값이 list가 아니다. 그러니 list로 쓰려면 list()를 이용하도록 하자.
#인수가 3개일 경우(세 번째 인수는 숫자 사이의 거리)
# print(list(range(1,10,2)))# [1,3,5,7,9]. 1부터 9까지, 숫자 사이의 거리는 2
# print(list(range(0,-10,-1)))# [0, -1, -2, -3, -4, -5, -6, -7, -8, -9]. 0부터 -9까지, 숫자 사이의 거리는 -1
# round(반올림)
# print(round(4.6))# 5
# print(round(4.2))# 4
# 표시 소숫점 따로 표기
# print(round(5.678, 2))# 소수점 2자리까지만 반올림. 5.68
# sorted(입력값을 정렬, 리스트로 반환)
# print(sorted([1,3,2]))# [1, 2, 3]
# print(sorted(['a','c','b']))# ['a', 'b', 'c']
# print(sorted("zero"))# ['e', 'o', 'r', 'z']
# print(sorted((3,2,1)))# [1, 2, 3]
#list의 함수로 sort가 있으나 이는 리스트 객체를 정렬할 뿐, 그 결과를 반환하지 않는다. 
# str(문자열로 만들어서 반환)
# print(str(3))# 3
# print(str('hi'))# hi
# print(str('hi'.upper()))# HI. 'hi'.upper()를 문자열로 만들어 돌려줌.
# sum(입력받은 리스트나 튜플의 모든 요소값의 합을 반환)
# print(sum([1,2,3]))# 6
# print(sum((4,5,6)))# 15
# tuple(반복 가능한 자료형을 입력받아 튜플로 반환. 튜플이 입력되었으면 그대로 반환)
# print(tuple("abc"))# ('a', 'b', 'c')
# print(tuple([1,2,3]))# (1, 2, 3)
# print(tuple((1,2,3)))# (1, 2, 3)
# type(입력된 값의 자료형 반환)
# print(type("abc")) # <class 'str'>
# print(type([])) # <class 'list'>
# print(type(open("test", 'w'))) # <class '_io.TextIOWrapper'>
# zip('동일한' 개수로 이루어진 자료형을 묶어줌)
# a = list(zip([1,2,3], [4,5,6]))
# print(a)# [(1, 4), (2, 5), (3, 6)]. 각 리스트에서 [0]인 것끼리, [1]인 것끼리 묶어서 반환
# a = list(zip([1,2,3], [4,5,6], [7,8,9]))
# print(a)# [(1, 4, 7), (2, 5, 8), (3, 6, 9)]
# a = list(zip("abc", "def"))
# print(a)# [('a', 'd'), ('b', 'e'), ('c', 'f')]
#내장 함수=====================================================
#외장 함수=====================================================
#자주 사용되는 라이브러리
#sys : 파이썬 인터프리터가 제공하는 변수와 함수를 직접 제어할 수 있게 해주는 모듈
#argv_test에 
# import sts
# print(sys.argv)
# 를 입력후 터미널에
# python argv_test.py you need python # 이렇게 치니까
# ['argv_test.py', 'you', 'need', 'python'] # 이렇게 나왔다. 
#python 명령어 뒤 모든 것들이 공백을 기준으로 나뉘어 sys.argv 리스트의 요소가 된다.
# 강제로 스크립트 종료 - sys.exit
# 대화형 인터프리터를 종료하는 것과 같은 기능을 한다. 프로그램 파일 안에서 사용하면 프로그램을 종료시킨다. 
# C의 exit() 같은 거라고 생각하면 될듯
# 자신이 만든 모듈을 불러와 사용하기 - sys.path
# 파이썬 모듈이 저장된 위치를 나타낸다. sys.path를 실행하면 나오는 위치에 있는 파이썬 모듈은 경로에 상관없이 어디에서나 불러올 수 있다. 
# 터미널을 통해 실행시키니
# ['', '/System/Library/Frameworks/Python.framework/Versions/2.7/lib/python27.zip', 
# '/System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7', 
# '/System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/plat-darwin', 
# '/System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/plat-mac', 
# '/System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/plat-mac/lib-scriptpackages', 
# '/System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/lib-tk', 
# '/System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/lib-old', 
# '/System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/lib-dynload', 
# '/Users/minkyu/Library/Python/2.7/lib/python/site-packages', 
# '/Library/Python/2.7/site-packages', 
# '/System/Library/Frameworks/Python.framework/Versions/2.7/Extras/lib/python', 
# '/System/Library/Frameworks/Python.framework/Versions/2.7/Extras/lib/python/PyObjC', 
# '/Library/Python/2.7/site-packages/pip-20.2b1-py2.7.egg'] 이렇게 나온다. ㄷㄷ
# 여기서 ''는 현재 디렉터리를 말한다. 
# sys.path.append("경로")로 경로 이름을 추가할 수 있다. 
# pickle : 객체의 형태를 그대로 유지하면서 파일에 저장하고 불러올 수 있게 하는 모듈
# import pickle
# f = open("test.txt", 'wb')
# data1 = {1:'python', 2:'you need'}
# pickle.dump(data1,f)#dump()를 이용해 딕셔너리 객체 data를 그대로 파일에 저장. 게임 데이터 저장할 때 사용할 수 있을거 같다. 
# f.close()

# f = open("test.txt", 'rb')
# data2 = pickle.load(f)#load를 이용해 객체 그대로 불러온다.
# print(data2)# {1:'python', 2:'you need'} 출력
# OS : 환경 변수, 디렉터리, 파일 등의 OS자원을 제어할 수 있께 해주는 모듈
# os.environ - 현재 시스템의 환경 변수값을 보여준다. 
# import os
# print(os.environ)# 환경 변수에 대한 정볼르 딕셔너리 객체로 돌려준다.
# environ({'TERM_PROGRAM': 'vscode', 
# 'TERM': 'xterm-256color', 
# 'SHELL': '/bin/bash'...출력(엄청 많다)
#각 환경변수를 따로 출력할 수 있다. 왜냐하면 딕셔너리니까
# print(os.environ['PATH'])
# /Library/Frameworks/Python.framework/Versions/3.7/bin:
# /Library/Frameworks/Python.framework/Versions/3.8/bin: 등등...(아주 많다)
# os.chdir - 현재 디렉터리 위치 변경
# os.getcwd - 현재 디렉터리 위치 반환
# print(os.getcwd())# /Users/minkyu/com.minkyu/unity_GOMap 반환
# os.system - 시스템 명령어 호출
# 시스템 자체의 프로그램이나 기타 명령어를 호출
# os.system("dir")
# os.popen - 실행한 시스템 명령어의 결과값 돌려받기
# 시스템 명령어를 실행한 결과값을 읽기 모드 형태의 파일 객체로 돌려받음
# f = os.popen("dir")
# print(f.read())# 읽어들인 파일 객체의 내용을 출력
# 기타 os 관련 함수
# os.mkdir(디렉터리) - 디렉터리 생성
# os.rmdir(디렉터리) - 디렉터리 삭제. 디렉터리가 비어있어야 삭제 가능
# os.unlink(파일 이름) - 파일을 지운다
# os.rename(src, dst) - src라는 이름의 파일을 dst라는 이름으로 바꾼다. 
# shutil - 파일을 북사해줌
# import shutil
# shutil.copy('src.txt', "dsc.txt") # src.txt 파일과 동등한 내용의 파일이 dst.txt로 복사된다.
# glob - 특정 디렉터리에 있는 파일 이름을 모두 알려준다.
# glob(pathname) - 디렉터리에 있는 파일들을 읽은 뒤 리스트로 만들어 반환
# import glob
# a = glob.glob("/Users/minkyu/Documents/PythonCode/doit/Mymod/*")# *는 모든 파일 반환. 만약 mark*라고 적혀있으면 'mark~'꼴의 이름으로 된 파일만 반환
# print(a)
# tempfile - 파일을 임시로 만들어서 사용할 때 유용하다
# tempfile.mktemp()는 중복되지 않는 임시 파일의 이름을 무작위로 만든 뒤 반환
# import tempfile
# filename = tempfile.mktemp()
# print(filename)# /var/folders/j4/cjh0qv9j7_d9pcjff5ddgyn80000gn/T/tmprk_2_fzm이 반환
# # tempfile.TemporaryFile() - 임시 저장 공간으로 사용할 파일 객체 반환.
# # 반환한 파일은 기본적으로 바이너리 쓰기 모드(wb)를 가진다. f.close()가 사용되면 자동으로 사라진다.
# f = tempfile.TemporaryFile()
# f.close() # 생성한 임시 파일이 자동으로 삭제
# time - 시간과 관련된 모듈
# time.time - UTC 기준 현재 시간을 실수 형태로 반환
# import time 
#print(time.time())
# time.localtime(time.time()) - time.time()의 반환값을 사용해 연도, 월, 일, 시, 분, 초...등등의 형태로 바꾼뒤 반환
# print(time.localtime()) # time.struct_time(tm_year=2020, tm_mon=8, tm_mday=29, tm_hour=15, tm_min=3, tm_sec=48, tm_wday=5, tm_yday=242, tm_isdst=0)
# time.asctime() - time.localtime()에 의해 반환된 튜플 형태의 값을 인수로 받아 날짜와 시간을 알아보기 쉬운 형태로 돌려주는 함수
# print(time.asctime(time.localtime(time.time()))# Sat Aug 29 15:05:42 2020
# time.ctime() - time.asctime(time.localtime(time.time())을 간단하게 표시하는 방법
# print(time.ctime()) # 근데 time.asctime()도 인수 없이 출력해도 같은값이 나온다. 뭐지
# time.strftime() - 시간에 관계된 것을 세밀하게 표현하는 여러 가지 포맷 코드를 제공
# print(time.strftime('%x', time.localtime()))# 08/29/20
# print(time.strftime('%c', time.localtime()))# Sat Aug 29 15:09:00 2020
# 포맷 코드가 엄청 많다. 나중에 구글링으로 찾아보며 사용할 것
# time.sleep() - 일정 시간 간격을 두고 루프 실행
# for i in range(10):
#     print(i)
#    time.sleep(1) # 1초 지연
# calender - 달력 관련 모듈
# import calendar
# print(calendar.calendar(2020))
#  2020
#       January                   February                   March
# Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su
#        1  2  3  4  5                      1  2                         1
#  6  7  8  9 10 11 12       3  4  5  6  7  8  9       2  3  4  5  6  7  8
# 13 14 15 16 17 18 19      10 11 12 13 14 15 16       9 10 11 12 13 14 15
# 20 21 22 23 24 25 26      17 18 19 20 21 22 23      16 17 18 19 20 21 22
# 27 28 29 30 31            24 25 26 27 28 29         23 24 25 26 27 28 29
#                                                     30 31

#        April                      May                       June
# Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su
#        1  2  3  4  5                   1  2  3       1  2  3  4  5  6  7
#  6  7  8  9 10 11 12       4  5  6  7  8  9 10       8  9 10 11 12 13 14
# 13 14 15 16 17 18 19      11 12 13 14 15 16 17      15 16 17 18 19 20 21
# 20 21 22 23 24 25 26      18 19 20 21 22 23 24      22 23 24 25 26 27 28
# 27 28 29 30               25 26 27 28 29 30 31      29 30

#         July                     August                  September
# Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su
#        1  2  3  4  5                      1  2          1  2  3  4  5  6
#  6  7  8  9 10 11 12       3  4  5  6  7  8  9       7  8  9 10 11 12 13
# 13 14 15 16 17 18 19      10 11 12 13 14 15 16      14 15 16 17 18 19 20
# 20 21 22 23 24 25 26      17 18 19 20 21 22 23      21 22 23 24 25 26 27
# 27 28 29 30 31            24 25 26 27 28 29 30      28 29 30
#                           31

#       October                   November                  December
# Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su
#           1  2  3  4                         1          1  2  3  4  5  6
#  5  6  7  8  9 10 11       2  3  4  5  6  7  8       7  8  9 10 11 12 13
# 12 13 14 15 16 17 18       9 10 11 12 13 14 15      14 15 16 17 18 19 20
# 19 20 21 22 23 24 25      16 17 18 19 20 21 22      21 22 23 24 25 26 27
# 26 27 28 29 30 31         23 24 25 26 27 28 29      28 29 30 31
#                           30
#calender.calender()의 결과. calender.prcal(연도)를 사용해도 같은 결과 출력
#한 달만 출력
# print(calendar.prmonth(2020, 8))
#     August 2020
# Mo Tu We Th Fr Sa Su
#                 1  2
#  3  4  5  6  7  8  9
# 10 11 12 13 14 15 16
# 17 18 19 20 21 22 23
# 24 25 26 27 28 29 30
# 31
# 출력 결과
# calender.weekady() - 그 날짜에 해당하는 요일 정보 반환
# 월요일은 0, 화요일은 1,...,일요일은 6
# print(calendar.weekday(2020,12,31))# 3(목요일) 반환
# calendar.monthrange(연도, 월) - 입력받은 달의 1일이 무슨 요일인지, 그 달이 며칠까지 있는지 튜플 형태로 반환
# print(calendar.monthrange(2015,12))# (1,31) 반환 -> 2015년 12월은 화요일, 12월은 31일까지 존재.
#날짜와 관련된 프로그램을 할 때 매우 유용하게 사용됨
# random - 난수 발생 모듈
# import random
# print(random.random())# 0.0~1.0사이 실수 중 난수 반환
# print(random.randint(1, 10))# 1~10사이 정수 중 난수 반환
#사용 예
# def random_pop(data):#리스트의 요소 중 무작위로 하나 선택해 빼내는 함수
#     number = random.randint(0, len(data) - 1)
#     return data.pop(number)
# data = [1,2,3,4,5]
# while data: print(random_pop(data))
# random.shuffle - 리스트의 항목으로 무작위로 섞음
# data = [1,2,3,4,5]
# random.shuffle(data)#리스트의 항목을 무작위로 섞음
# print(data)# [5, 2, 1, 3, 4], [1, 5, 2, 4, 3] 등 출력
# webbrowser - 자신의 시스템에서 사용하는 기본 웹 브라우저를 자동으로 실행
# import webbrowser
# webbrowser.open("http://google.com")# 구글 실행
# webbrowser.open_new("http://google.com")# 새 창에서 구글 실행
# threading - 스레드를 다룸
# 스레드를 사용해 한 프로세스 안에서 n가지 일을 동시에 수행
# import time
# import threading

# def long_task():
#     for i in range(5):
#         time.sleep(1)
#         print("working : %s\n" %i)
# print("Start")

# threads = []
# for i in range(5):
#     t = threading.Thread(target=long_task)# 스레드의 객체가 동시 작업을 가능하게 해줌
#     threads.append(t)

# for t in threads:
#     t.start()

# print("End")
# 원래 5초짜리 일을 5번 반복 - 25초가 걸리지만
# 한 번에 5번 실행함으로써 5초밖에 걸리지 않는다. 
# 허나 위의 코드를 돌리면 start와 end가 출력이 안됨.
# start와 end가 나오게 하기
# import time
# import threading

# def long_task():
#     for i in range(5):
#         time.sleep(1)
#         print("working:%s\n" % i)

# print("start")

# threads = []
# for i in range(5):
#     t = threading.Thread(target=long_task)# threading.Thread로 만든 객체가 동시 작업을 가능하게 해줌
#     threads.append(t)
# for t in threads:
#     t.start()
# for t in threads:
#     t.join() # 스레드가 종료될 때까지 기다림

# print("End")

#start, end가 같이 나옴

#연습 문제================================================
#문제 1(자식 객체 생성)
# class Calculator:
#     def __init__(self):
#         self.value = 0
    
#     def add(self, val):
#         self.value += val

# class UpgradeCalculator(Calculator):
#     def minus(self, val):
#         self.value -= val

# cal = UpgradeCalculator()
# cal.add(10)
# cal.minus(7)
# # print(cal.value)# 10 - 7 = 3출력
# #문제 2(값을 제한하는 MaxLimitCalculator 클래스)
# class MaxLimitCalculator(Calculator):
#     def add(self, val):
#         self.value +=val
#         if self.value > 100 : self.value = 100

# cal = MaxLimitCalculator()
# cal.add(50)
# cal.add(60) # 110이지만 조건문에 의해 100이 된다.
# print(cal.value)# 100 출력
# 문제3(내장 함수)
# print(all([1,2,abs(-3)-3]))# false
# b = chr(ord('a')) == 'a'
# print(b)# true
# 문제4(내장 함수)
# a = list(filter(lambda x: x>0, [1,-2,3,-5,8,-3]))#filter + lambda로 리스트 생성
# print(a)# [1,3,8]
# 문제5(진수 문제)
# print(int(0xea))# 문자열로 넣지 말기
# 문제6(map, lambda사용)
# def mul(a):
#     return a*3
# b = list(map(mul,[1,2,3,4]))# list함수 사용하기
# print(b)# [3,6,9,12]
# 문제7(최댓값, 최솟값의 합)
# a = [-8,2,7,5,-3,5,0,1]
# b = max(a) + min(a)# 7 + (-8) = -1
# print(b)
# 문제 8
# c = round(17 / 3, 4)
# print(c)
# 문제 9(스크립트 생성)
# import sys

# num = 0
# for i in sys.argv:
#     num += int(i)
# 문제 10(os모듈 사용)
# import os
# print(dir(os.chdir("/Users/minkyu/Documents/PythonCode/doit")))
#['__bool__', '__class__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__'] 출력
#dir : 객체가 자체적으로 가지고 있는 변수나 함수를 보여준다
#  문제 11(glob 모듈 사용) - 특정 폴더에 있는 파일 이름 알려줌
# import glob
# print(glob.glob("/Users/minkyu/Documents/PythonCode/doit/Mymod/*.py"))# 해당 경로에 ~.py만 출력
# ['/Users/minkyu/Documents/PythonCode/doit/Mymod/argv_test.py']가 출력
# 문제12(time 모듈 사용)
# import time
# print(time.strftime('%x %H:%M:%S', time.localtime()))# 08/29/20 16:57:51
# 문제13(random 모듈 사용 - 로또 프로그램 실행)
# import random
# def lotto(data):#45개 숫자 중 6개 출력-data가 1~45값을 갖고있는 리스트
#     number = random.randint(0, len(data) - 1)
#     print(number)
#     return data.pop(number)
# count = 0
# data = []
# b = []
# for i in range(1,46):
#     data.append(i)
# # print(data)
# while count < 6:
#     b.append(lotto(data))
#     count+=1
        
# print(b)
#외장 함수==============================================================
# 파이썬으로 프로그램 만들어보기=============================================
#구구단 프로그램
# def Gugu(n):
#     ggdan = []
#     count = 1
#     while count < 10:
#         ggdan.append(n * count)
#         count+=1
#     return ggdan

# print(Gugu(2))
# print(Gugu(3))
# print(Gugu(4))
# print(Gugu(5))
# print(Gugu(6))
# print(Gugu(7))
# print(Gugu(8))
# print(Gugu(9))
# 3과 5의 배수 합하기
# def Plus_3_5():
#     count = 1
#     sum = 0
#     while count < 1001 :
#         if(count % 3 == 0 | count % 5 == 0): sum +=count
#         count+=1
#     return sum

# print(Plus_3_5())
#게시판 페이징하기
# def show_page(paper_num, show_oneTime):
#     page_num = int(paper_num / show_oneTime)
#     if (paper_num % show_oneTime) != 0 : page_num+=1
#     return page_num

# print(show_page(5, 10))
# print(show_page(15, 10))
# print(show_page(25, 10))
# print(show_page(30, 10))
#간단한 메모장 만들기
#입력 부분
# import sys

# option = sys.argv[1]
# memo = sys.argv[2]

# print(option)
# print(memo)

#추가 입력, 출력 부분
# import sys

# option = sys.argv[1]
# if option == '-a':
#     memo = sys.argv[2]
#     f = open('memo.txt' 'a')
#     f.write(memo)
#     f.write('\n')
#     f.close()
# if option == '-v':
#     f = open('memo.txt' 'r')
#     print(f.read())
#     f.close()
# 탭을 4개의 공백으로 바꾸기
# import sys

# file_input = open(sys.argv[1], 'r')
# text_input = file_input.read()
# file_input.close()
# text_input.replace("\t", ""*4)# 탭 공백을 스페이스바 4개 공백으로

# file_output = open(sys.argv[2], 'w')
# file_output.write(text_input)
# file_output.close()

#하위 디렉터리 검색하기
# import os

# def search(dirname):
#     filenames = os.listdir(dirname)# os.listdir를 사용해 해당 디렉토리에 있는 파일들의 리스트를 구할 수 있다.
#     for filename in filenames:#하나씩 체크
#         full_filename = os.path.join(dirname, filename)
#         if os.path.isdir(full_filename):# 하위 폴더가 있으면 
#             search(full_filename)# 함수 다시 실행(재귀호출)
#         else:
#             ext = os.path.splitext(full_filename)[-1]# 파일 확장명만 따로 추출(splitext : 파일 이름을 확장자 기준으로 둘로 나눔)
#             if ext == '.py':
#                 print(full_filename)

# search("c:/")
# 파이썬으로 프로그램 만들어보기=============================================
#정규 표현식============================================================
#정규 표현식을 사용하면 간편하고 편하게 코드를 짤 수 있다.
# import re #정규 표현식을 사용하기 위한 모듈
# 메타 문자(원래 의미가 아닌 특별한 용도로 사용하는 문자) : . ^ $ * + ? {} [] \ | ()
# 문자 클래스(character class) []
# 문자 클래스로 만들어진 정규식은 '[] 사이의 문자들과 매치'라는 의미를 갖는다
# 예 : [abc]는 'a,b,c 중 한 개의 문자와 매치'를 뜻한다
# "a"랑 "before"은 a,b,c 중 한 개 이상의 문자를 갖고 있기 때문에 [abc]와 "일치"한다고 본다.
# 허나 "dude"는 a,b,c 중 어느 하나도 갖고 있지 않기 때문에 [abc]와 "불일치"한다고 본다.
# []안의 두 문자 사이에 하이픈(-)을 넣으면 두 문자 사이의 범위(From - To)를 의미한다.
# 예를 들어 [a-c]는 [abc]를 뜻하고 [0-5]는 [012345]라는 뜻이다.
# 이를 활용한 얘 : [a-zA-Z] : 알파벳 모두, [0-9] : 숫자
# 문자 클래스 안에 ^메타문자를 사용할 경우에는 반대(not)라는 의미를 갖는다.
# 예를 들어 [^0-9]라는 정규 표현식은 숫자가 아닌 문자만 매치된다.
# 자주 사용하는 정규식은 별도의 표기법으로 표기할 수 있다. 기억하는게 좋다.
# \d(숫자, [0-9]와 매치)
# \D(숫자가 아닌 것, [^0-9]와 매치)
# \s(공백을 표현하는 문자(space나 tab), [ \t\n\r\f\v]와 매치. 맨 앞의 빈칸은 공백 문자(space)를 의미)
# \S(공백이 아닌 것. [^ \t\n\r\f\v]와 매치)
# \w(문자+숫자, [a-zA-Z0-9_]와 매치)
# \W(문자+숫자가 아닌 것, [^a-zA-Z0-9_]와 동일한 표현식)
# -> 대문자로 사용한 것은 소문자의 반대
# Dot(.) 메타 문자 : 줄바꿈 문자인 \n을 제외한 모든 문자와 매치
# 예 : a.b는 a와 b 사이에 \n을 제외한 어떤 문자가 들어가도 모두 매치( = a + 모든 문자 + b)
# aab는 a와 b사이에 있는 a가 .와 일치하므로 정규식과 매치
# a0b도 a와 b사이에 있는 0이 .와 일치하므로 정규식과 매치
# abc는 a와 b사이에 있는게 아닌 b의 오른쪽에 문자가 있응니 정규식과 일치하지 않음
# a[.]b는 a와 b 사이에 Dot(.) 문자가 있으면 매치한다는 뜻으로 a.b와 매치되지만 a0b와는 매치되지 않는다. 
# 반복(*)
# ca*t는 *바로 앞에 있는 a가 0번 이상 반복되면 매치된다는 뜻이다. 
# ct, cat, caaat모두 a가 0번 이상(0 포함) 반복 되었기에 ca*t와 매치된다.
# 반복(+)
# 반복을 나타내는 또다른 메타 문자. 최소 1번 이상 반복될 때 사용
# ca+t에 대하여
# ct는 a가 0번 반복되기 때문에 정규식과 일치하지 않고
# cat, caaat는 a가 1번 이상 반복되기 때문에 ca+t와 매치된다.
# {{m,n},?} 반복 횟수 m부터 n까지 매치.
# 만약 [3,]이면 반복 횟수가 3 이상이고 {,3}이면 반복횟수가 3이하를 의미. 생략된 m은 0과 동일, 생략된 n은 무한대(2억개 미만)의 의미를 가짐
# 사용 예
# 1.{m} : ca{2}t -> a가 2번 반복되면 매치. cat는 매치X, caat는 매치O
# 2.{m,n} : ca{2,5}t -> a가 2~5번 반복되면 매치. caat, caaaaat는 매치O지만 cat는 매치X
# 3.? : ab?c -> ?는 {0,1}을 의미. ac, abc 모두 매치O
# *, +, ?메타 문자 모두 {m,n}형태로 고쳐 쓸 수 있지만 가급적 이해하기 쉽고 표현도 간결한 *, +, ?메타문자를 사용하도록 하자
# 파이썬에서 정규 표현식을 사용하는 예
# import re # 장규 표현식을 제공하는 모듈을 import
# p = re.compile('ab*')# 정규 표햔식 컴파일
# 정규식을 사용한 문자열 검색
# 캄파일된 패턴 객체를 사용해 문자열 검색을 수행
# match() : 문자열의 처음부터 정규식과 매치되는지 조사. 매치되면 match 객체를, 아니면 none 반환
# search() : 문자열 전체를 검색해 정규식과 매치되는지 조사
# findall() : 정규식과 매치되는 모든 문자열(substring)을 리스트로 반환
# finditer() : 정규식과 매치되는 모든 문자열(substring)을 반복 가능한 객체로 반환
# 사용 예
# import re
# p = re.compile('[a-z]+')
#match()==================
# m = p.match("python") # "python"은 정규식 '[a-z]+'에 부합. match객체 반환
# print(m) # <re.Match object; span=(0, 6), match='python'>
# m = p.match("3 python") # '[a-z]+'에 부합하지 않으니 None 반환
# print(m) # <re.Match object; span=(0, 6), match='python'>
# match()의 결과로 match객체 또는 none을 반환하기 때문에 파이썬 정규식 프로그램은 
# p = re.compile(정규 표현식)
# m = p.match("조사할 문자열")
# if m:
#   print('Match fround : ', m.group())
# else:
#   print('No match')
# 이렇게 쓴다. match의 결과값이 있어야 그다음 작업을 수행하겠다는 뜻. 
#match()==================
#search()=================
# import re
# p = re.compile('[a-z]+')
# m = p.search("python")# <re.Match object; span=(0, 6), match='python'> 출력.
# print(m)
# m = p.search("3 python")# <re.Match object; span=(2, 8), match='python'> 출력. 첫번째 문자는 3이지만 search는 문자열의 처음부터 검색하는 것이 아니라 문자열 전체를 검색하는 것이기에 3 이후의 "python" 문자열과 매치된다. 
# print(m)
#search()=================
#findall()================
# import re
# p = re.compile('[a-z]+')
# result = p.findall("life is too short")
# print(result) # ['life', 'is', 'too', 'short']. 각 단어를 [a-z]+ 정규식과 매치해서 리스트로 반환
#findall()================
#finditer()===============
# import re
# p = re.compile('[a-z]+')
# result = p.finditer("life is too short") # finditer()는 findall과 동일하지만 그 결과로 반복 가능한 객체(iterator object)를 돌려준다.
# print(result) # <callable_iterator object at 0x7f88a800c310>
# for r in result:
#     print(r)
# <re.Match object; span=(0, 4), match='life'> # 반복 가능한 객체가 포함하는 각각의 요소는 match 객체.
# <re.Match object; span=(5, 7), match='is'>
# <re.Match object; span=(8, 11), match='too'>
# <re.Match object; span=(12, 17), match='short'>
#finditer()===============
# match 객체의 메서드
# group() : 매치된 문자열 반환
# start() : 매치된 문자열의 시작 위치 반환
# end() : 매치된 문자열의 끝 위치 반환
# span() : 매치된 문자열의 (시작, 끝)에 해당하는 튜플을 반환
# 예제
# import re
# p = re.compile('[a-z]+')
# m = p.match("python")
# print(m.group())# 'python'
# print(m.start())# 0(시작 위치 : 0)
# print(m.end())# 6(끝나는 위치 : 6)
# print(m.span())# (0,6) - 시작 위치 0, 끝나는 위치 6
# search 메서드 사용
# import re
# p = re.compile('[a-z]+')
# m = p.search("3 python")
# print(m.group())# 'python'
# print(m.start())# 2(시작 위치 : 2)
# print(m.end())# 8(끝나는 위치 : 8)
# print(m.span())# (2,8) - 시작 위치 2, 끝나는 위치 8
# 모듈 단위로 수행하기
# p = re.compile('[a-z]+')
# m = p.match("python") 대신
# m = re.match('[a-z]+', "python")으로 간략하게 사용 가능
# 컴파일 옵션
# DOTALL(약어 : S), dot(.)이 줄바꿈 문자를 포함해 모든 문자와 매치
# IGNORECASE(약어 : I), 대소문자에 관계 없이 매치
# MULTILINE(약어 : M), 여러 줄과 매치(^, $메타 문자의 사용과 관계가 있는 옵션)
# VERBOSE(약어 : X), verbose 모드를 사용(정규식을 보기 편하게 만들 수도 있고 주석 등을 사용할 수 있다.)
# re.DOTALL 혹은 re.S로도 사용 가능
# DOTALL, S
# 기존의 메타문자는 줄바꿈 문자(\n)을 제외한 모든 문자와 매치된다느 규칙이 있었다.
# 허나 re.DOTALL 또는 re.S 옵션을 사용할 경우 \n도 포함하여 매치 가능하다.
# 예시
# import re
# p = re.compile('a.b')
# m = p.match('a\nb')
# print(m)# none 출력. \n은 메타 문자 .와 매치 X
# \n도 매치
# import re
# p = re.compile('a.b', re.DOTALL)
# m = p.match('a\nb')
# print(m)# <re.Match object; span=(0, 3), match='a\nb'>
# re.DOTALL 옵션은 여러 줄로 이루어진 문자열에서 \n에 상관없이 검색할 때 많이 사용한다.
# IGNORECASE, I
# 대, 소문자 구별 없이 매치를 수행할 때 사용하는 옵션
# import re
# p = re.compile('[a-z]', re.I)# 영어만 들어갔는지 검사. 
# print(p.match('python'))# <re.Match object; span=(0, 1), match='p'>
# print(p.match('Python'))# <re.Match object; span=(0, 1), match='P'>
# print(p.match('PYTHON'))# <re.Match object; span=(0, 1), match='P'>
# 대, 소문자에 관계없이 매치된다.
# MULTILINE, M
# 메타 문자 ^, $와 연관된 옵션. ^는 문자열의 처음, $는 문자열의 마지막을 의미. 
# 예를 들어 '^python'인 경우 문자열의 처음은 항상 python으로 시작해야 매치, 'python$'인 경우 문자열의 마지막은 항상 python으로 끝나야 매치
# 예시
# import re
# p = re.compile("^python\s\w+")# python으로 시작, 그 뒤에 whitespace(스페이스 공백), 그 뒤에 단어가 와야 한다는 의미
# data = """python one
# life is too short
# python two
# you need python
# python three"""
# print(p.findall(data))# 정규식과 매치되는 모든 문자열(substring)을 리스트로 반환
# ['python one'] 출력. ^메타문자(처음에 python으로 시작하는 문자열만 매치)로 인해 python one만 출력
# ^메타 문자를 각 라인의 처음으로 인식시키고 싶을 때 re.MULTILNE 또는 re.M 사용.
# import re
# p = re.compile("^python\s\w+", re.MULTILINE)# python으로 시작, 그 뒤에 whitespace(스페이스 공백), 그 뒤에 단어가 와야 한다는 의미
# data = """python one
# life is too short
# python two
# you need python
# python three"""
# print(p.findall(data))# ['python one', 'python two', 'python three'] 출력
# VERBOSE, X
# 정규식을 주석 또는 줄 단위로 구분할 때 사용
# import re
# charref = re.compile(r'&[#](0[0-7]+|[0-9]+|x[0-9a-fA-F]+);')
# 얘는 이해하기 어렵다.
# charref = re.compile(r"""
# &[#]
# (
#     0[0-7]+     # Octal form
#     | [0-9]+    # Decimal form
#     | x[0-9a-fA-F]  #Hexadecimal form
# )
# ;
# """, re.VERBOSE)
# 정규식이 복잡할 경우 주석을 적고 여러 줄로 표현하는 것이 가독성이 좋다. 
# re.VERBOSE 옵션을 사용하면 문자열에 사용된 whitespace는 컴파일할 때 제거된다.([]안에 쓰인 whitespace는 제거되지 않는다.)
# 그리고 줄단위로 주석을 달 수 있다.
# 백슬래시 문제
# 'section' 문자열을 찾기 위한 정규식 만들기
# \section이라고만 치면 \s가 whitespace로 인식되어 의도한 대로 매치가 이루어지지 않는다. 
# 그래서 \\section과 같이 쳐야한다. \문자가 문자열 자체임을 알려주기 위해 백슬래시 2개를 사용.
# import re
# p = re.compile('\\section')# 이렇게 쳐야한다.
# 허나 이렇게 하면 파이썬 정규식 엔진에는 \\ -> \이 되어 \section이 전달된다.
# 그래서 \\\\section으로 해야하지만 이는 복잡하다. 
# 이러한 문제를 해결하기 위해 Raw String 규칙이 생겨났고 이는
# import re
# p = re.compile(r'\\section')# 이렇게 앞에 r을 치면 된다. Raw String 규칙에 의해 백슬래시를 1개만 써도 2개를 쓴 것과 동일한 의미를 가진다.
# 문자열을 소비시키지 않는 메타 문자(zero-width assertions 메타 문자)
# 1. | : or과 동일한 의미
# import re
# p = re.compile('Crow|Servo')
# m = p.match('CrowHello')
# print(m)# <re.Match object; span=(0, 4), match='Crow'> 출력
# 2. ^ : 문자열의 맨처음
# import re
# print(re.search('^Life', "Life is too short"))# <re.Match object; span=(0, 4), match='Life'>
# print(re.search('^Life', 'My Life'))# None 출력. Life가 처음에 오는 경우가 아니면 None을 반환
# 3. $ : 문자열의 맨끝
# import re
# print(re.search('short$', 'Life is too short'))# None
# print(re.search('short$', 'Life is too short, you need python'))# <re.Match object; span=(12, 17), match='short'>
# short로 끝난 경우에만 매치
# ^와 $를 문자 그자체로 매치하고 싶은 경우에는 [^], [$] 또는 \^, \$로 사용하면 된다.
# 4. \A : 문자열의 처음과 매치. ^ 메타문자는 re.MULTILINE을 사용할 경우 각 줄의 문자열의 처음과 매치되지만 \A는 줄과 상관없이 전체 문자열의 처음하고만 매치
# 5. \Z : 문자열의 끝과 매치. $ 메타문자는 re.MULTILINE을 사용할 경우 각 줄의 문자열의 끝과 매치되지만 \Z는 줄과 상관업이 전체 문자열의 끝하고만 매치
# 6. \b : 단어 구분자(Word boundary). 보통 단어는 whitespace에 의해 구분
# import re
# p = re.compile(r'\bclass\b')
# print(p.search('no class at all'))# <re.Match object; span=(3, 8), match='class'>
#'\bclass\b' 정규식은 앞뒤가 whitespace로 구분된 class라는 단어와 매치
# import re
# p = re.compile(r'\bclass\b')
# print(p.search('the declassified algorithm'))# None출력. 안에 class문자열이 있지만 양 옆에 공백이 없으므로 매치 X
# 7. \B. \b와 반대의 경우. whitespace로 구분된 단어가 아닌 경우에만 매치
# import re
# p = re.compile(r'\Bclass\B')
# print(p.search('no class at all'))# None
# print(p.search('the declassified algorithm'))# <re.Match object; span=(6, 11), match='class'>
# print(p.search('our subclass is'))# None. class의 뒤에 공백이 있어서 매치X
# 그루핑
# import re
# p = re.compile(r"(\w+)\s+\d+[-]\d+[-]\d+")# 이름 부분만 출력. \w+ 부분을 (\w+)로 만들면 구르핑된 부분의 문자열만 출력
# m = p.search("park 010-1234-1234")
# print(m.group(1))# park 출력
# group(0) : 매치된 전체 문자열
# group(1) : 첫번째 그룹에 해당하는 문자열
# group(2) : 두번째 그룹에 해당하는 문자열
# group(3) : 세번째 그룹에 해당하는 문자열
# import re
# p = re.compile(r"(\w+)\s+(\d+[-]\d+[-]\d+)")# \d+[-]\d+[-]\d+ 그루핑
# m = p.search("park 010-1234-1234")
# print(m.group(2))# 010-1234-1234 출력.
#국번만 출력
# import re
# p = re.compile(r"(\w+)\s+((\d+)[-]\d+[-]\d+)") # \d+[-]\d+[-]\d+ 속에 \d+을 또 그루핑.
# m = p.search("park 010-1234-1234")
# print(m.group(3))# 010 출력
# 그루핑된 문자열 재참조
# import re
# p = re.compile(r'(\b\w+)\s+\1')# \1 : 재참조 메타 문자. 정규식의 그룹 중 첫 번째 그룹을 가리킴. 즉, '(\b\w+)\s+\(\b\w+)'과 같다고 본다.
# print(p.search('Paris in the the spring').group())# 'the the' 출력
# 그루핑된 문자열에 이름 붙히기
# import re
# p = re.compile(r"(?P<name>\w+)\s+((\d+)[-]\d+[-]\d+)")# (\w+) 그룹에 name이란 이름을 붙힘. 여기서 ?... 표현식은 정규 표현식의 확장 구문이며 이는 강력한 힘을 갖고있다. 
# m = p.search("park 010-1234-1234") # 이름 작성의 확장 구문 : (?P<그룹 이름>...)
# print(m.group("name"))# park 출력
# 정규식 안에서 재참조
# import re
# p = re.compile(r'(?P<word>\b\w+)\s+(?P=word)')# 재참조를 할 때 (?P=그룹 이름)이라는 확장 구문 사용
# print(p.search('paris in the the spring').group())# the the 출력
# 전방 탐색(Lookahead Assertions)
# import re
# p = re.compile(".+:")#:로 끝나는 모든 것
# m = p.search("http://google.com")
# print(m.group())# http: 출력
# 여기서 'http'만 출력하려면? -> 이럴때 사용하는 것이 바로 전방 탐색
# 전방 탐색==============================================
# 긍정과 부정의 2종류가 있다. 
# (?=...) : 긍정형 전방 탐색(...에 해당하는 정규식과 매치되어야 하며 조건이 통과되어도 문자열이 소비되지 않는다.)
# (?!...) : 부정형 전방 탐색(...에 해당하는 정규식과 매치되지 않아야 하며 조건이 통과 되어도 문자열이 소비되지 않는다.)
# 긍정형 전방 탐색
# 예시
# import re
# p = re.compile(".+(?=:)")#:에 해당하는 부분에 긍정형 전방 탐색 기법 적용. :에 해당하는 문자열이 정규식 엔진에 의해 소비되지 않아(검색에는 포함, 검색 결과에는 제외) :이 제거된 값을 반환
# m = p.search("http://google.com")
# print(m.group())# http출력
# .*[.].*$ : '파일이름 + . + 확장자'를 나타내는 정규식. foo.bar, autoexec.bat, sendmail.cf같은 형식의 파일과 매치
# .*[.][^b].*$ : 확장자가 b라는 문자로 시작하면 안된다는 의미. 이 정규식은 foo.bar과 같은 파일도 걸러낸다. 이는
# .*[.]([^b]..|.[^a].|..[^t])$ : 첫번째 문자가 b가 아니거나 두번째 문자가 a가 아니거나 세번째 문자가 t가 아닌 경우. 이 경우 foo.bar는 제외. 허나 이런 경우에 sendmai.cf같이 확장자의 문자 개수가 2개인 케이스를 포함하지 못하는 오작동을 한다. 그렇기에
# .*[.]([^b].?.?|.[^a]?.?|..?[^t]?)$ : 확장자의 문자 개수가 2개여도 통과되는 정규식. 허나 갈수록 복잡해짐. 
# 이러한 경우를 간단하게 해결하기 위해 있는게 바로 부정형 전방 탐색. 위 예를 부정형 전방 탐색을 이용해
# .*[.](?!bat$).*$ 와 같이 간단하게 표현할 수 있다. 이는 확장자가 bat이 아닌 경우에만 통과 시킨다는 의미다. 
# exe도 제외하라는 조건을 추가하면 .*[.](?!bat$|exe$).*$ 와 같이 된다.
# 긍정, 부정형 전방 탐색====================================
# 문자열 바꾸기============================================
# import re
# p = re.compile('(blue|white|red)')
# print(p.sub('colour', 'blue socks and red shoes', count=1))# colour socks and red shoe 출력
# sub(바꿀 문자열, 대상 문자열, 바꾸기 횟수) <-바꾸기 횟수는 넣어도 되고 안넣어도 됨
# '대상 문자열'에 정규식에 매치되는 문자열을 '바꿀 문자열'로 바꾼다.
# subn 메서드 : sub와 동일한 기능을 하지만 튜플로 반환한다. (변경된 문자열, 바꾸기가 발생한 횟수)
# 예제
# import re
# p = re.compile('(blue|white|red)')
# print(p.subn('colour', 'blue socks and red shoes'))# ('colour socks and colour shoes', 2) 출력
# sub 매서드를 사용할 때 참조 구문 사용하기
# '이름 + 전화번호'를 '전화번호 + 이름'으로 바꾸는 예.'\g<그룹 이름>'을 사용하면 정규식의 그룹 이름을 참조할 수 있게 된다.
# import re
# p = re.compile(r"(?P<name>\w+)\s+(?P<phone>(\d+)[-]\d+[-]\d+)")
# print(p.sub("\g<phone> \g<name>", "park 010-1234-1234"))
# 그룹 이름 대신 참조 번호를 사용해도 같은 결과 반환
# import re
# p = re.compile(r"(?P<name>\w+)\s+(?P<phone>(\d+)[-]\d+[-]\d+)")
# print(p.sub("\g<2> \g<1>", "park 010-1234-1234"))#<name> <phone> 구조에 매치되는 문자열을 <phone> <name>으로 바꿔줌. 010-1234-1234 park 출력
# sub 매서드의 매개변수로 함수 넣기
# import re
# def hexrepl(match):
#     value = int(match.group())
#     return hex(value)
# p = re.compile(r'\d+')
# print(p.sub(hexrepl, 'Call 65490 for printing, 49152 for user code'))# Call 0xffd2 for printing, 0xc000 for user code 출력
# Call...문자열에 p에 매치되는 문자열을 hexrepl(match)에 match로 넣은 뒤 반환된 값을 match로 들어간 문자열과 교체
# 문자열 바꾸기============================================
# Greedy vs Non-Greedy==================================
# import re
# s = '<html><head><title><Title></title>'
# print(re.match('<.*>', s).span())# (0, 34), span() : 매치된 문자열의 (시작, 끝)에 해당하는 튜플을 반환
# print(re.match('<.*>', s).group())# <html><head><title><Title></title>. 반환할 수 있는 최대 문자열 반환.
# non-greedy 문자 ?를 사용하면 모든 값이 반환되는 걸 막을 수 있다. 
# import re
# s = '<html><head><title><Title></title>'
# print(re.match('<.*?>', s).group())# <html>
# non-greedy 문자인 ?는 *? +? ?? {m,n}?와 같이 사용할 수 있다. 가장 최소한의 반복을 수행하도록 도와주는 역할을 한다. 
# Greedy vs Non-Greedy==================================
# 정규 표현식============================================================
# 코딩 면허 시험==========================================================
    
