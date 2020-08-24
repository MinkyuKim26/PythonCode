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
# print(b)#'bar' 출력
#해당 key가 딕셔러니 안에 있는지 조사
# b = 'name' in a#'name'키가 있는지 조사('키' in '딕셔너리')
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
# f = open("새파일.txt", 'w')#쓰기 모드로 새파일.txt를 생성
# for i in range(1, 11):
#     data = "%d번째 줄입니다.\n" % i
#     f.write(data)
# f.close()
#p172까지 함
#사용자 입력과 출력========================================