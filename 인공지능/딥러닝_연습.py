# -*- coding: utf-8 -*-
"""딥러닝 연습

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1fSxrToJZeN8kY7kDevOLb0zMpsFU8_qk

numpy 연습
"""

import numpy as np #넘파이 import(np라는 이름으로 사용)
print(np.__version__)# 버전 확인 

np_arr = np.array([[10,20,30], [40,50,60]])# 2차원 numpy 배열 생성
print(np_arr)#출력 
#[[10 20 30]
 #[40 50 60]]<-이렇게 나옴
type(np_arr)# 배열 타입 numpy.ndarray
print(np_arr[0][2])# 요소 선택
#내장 함수
np.sum(np_arr)# 210 출

"""맷플롯립(Matplotlib)으로 그래프 그리기.
맷플롯립은 파이썬 과학 생태계의 표준 그래프 패키지를 말한다.
대부분의 그래프를 그릴 수 있다.
"""

import matplotlib.pyplot as plt# 맷플롯립 import

#선 그래프, 산점도 그리기. 두 그래프는 x축을 기준으로 y축의 변화 추이를 살펴보기 편리해 데이터 분석에 자주 사용

# 선 그래프 그리기
plt.plot([1,2,3,4,5],[1,4,9,16,25])# 첫번째 리스트는 x축, 두번째 리스트는 y축의 값이다.
plt.show()# 그래프가 그려진다.
# 산점도 그리기
# 산점도는 데이터의 x축, y축 값을 이용해 점으로 그래프를 그린 것. 
# 이 때 show()를 사용하지 않아도 자동으로 그래프가 그려지지만 show()으로 더 깔끔하고 보기 좋은 그래프를 그릴 수 있다. 
plt.scatter([1,2,3,4,5],[1,4,9,16,25])# 점 생성
plt.show()# 표

# 넘파이 배열로 선점도 그리기
# 파이썬의 과학 패키지들은 예외 없이 넘파이 배열로 데이터 주고받을 수 있게 개발되었다.

# 넘파이의 random.randn() 함수를 사용해 표준 정규 분포를 따르는 난수를 만들고 그 값을 이용해 선점도를 그려보기
x = np.random.randn(1000)# 표준 정규 분포를 따르는 난수 생성
y = np.random.randn(1000)# 난수 생성
plt.scatter(x, y)
plt.show()

# 데이터 분석과 그래프 도구는 뗄래야 뗄 수 없는 사이.
# 위와 같이 데이터를 시각화 하면 데이터의 직관성이 증가한다. 딥러닝에서 데이터 시각화는 필수.

"""머신 러닝 기초. - 수치 예측.

1. 선형 회귀\
머신 러닝 알고리즘 중 가장 간단하면서도 딥러닝의 기초가 되는 알고리즘. 선형 회귀는 간단한 1차 함수(y = ax + b)로 표현할 수 있다.\
선형회귀는 기울기와 절편을 찾는 알고리즘이라 할 수 있다.\
선형 회귀로 풀 수 있는 문제 유형\
'x가 3일 때 y는 25, x가 4일 때 y는 32, x가 5일 때 y는 39라면 기울기와 절편의 값으로 적당한 것은?'\
1) 기울기는 6, 절편은 4\
2) 기울기는 7, 절편은 5\
3) 기울기는 7, 절편은 4

선형회귀의 문제 해결 과정\
위 예제에서 보기 1번을 이용해 직선을 만들고 주어진 점 [(3,25), (4,32), (5,39)]들이 포함되었는지 확인
"""

import matplotlib.pyplot as plt

plt.axvline(x=0, color = 'r') # x
plt.axhline(y=0, color = 'r') # y축

plt.scatter([3,4,5],[25,32,39])# 점찍기

x = np.arange(0,10) 
y = 6*x + 4 #x에 대한 y값
plt.plot(x, y)#x, y값으로 직선 형성. 리스트로 만들 수 있지만 이렇게 함수를 이용해 그래프를 만들 수 있다.

plt.show()

"""위의 그래프를 보면 알 수 있듯 점이 포함되어 있지 않다. 그러니 보기 2번의 기울기, 절편을 이용해 직선을 만들어보자."""

import matplotlib.pyplot as plt

plt.axvline(x=0, color = 'r') # x
plt.axhline(y=0, color = 'r') # y축

plt.scatter([3,4,5],[25,32,39])# 점찍기

x = np.arange(0,10) 
y = 7*x + 5
plt.plot(x, y)

plt.show()

"""직선의 모양과 점 3개가 만드는 직선의 형태는 똑같으나 절편이 맞지 않는듯 하다. 그러니 절편만 줄여보자(보기 3의 조건으로 넘어간다.)"""

import matplotlib.pyplot as plt

plt.axvline(x=0, color = 'r') # x
plt.axhline(y=0, color = 'r') # y축

plt.scatter([3,4,5],[25,32,39])# 점찍기

x = np.arange(0,10) 
y = 7*x + 4
plt.plot(x, y)

plt.show()

"""완전히 들어맞는다.\
위 과정을 통해 만든 1차 함수들을 '선형 회귀로 만든 모델'이라고 한다. 마지막에 점 3개가 완전히 들어가는 1차 함수가 바로 최적의 선형 모델인 것이다.\
이러한 모델(최적의 선형 모델)을 통해 새로운 점에 대한 예측을 할 수 있게 된다.\
미리 준비한 입력(x : 3,4,5)과 타깃(y : 25,32,39)을 가지고 모델(y = 7x + 4)을 만든 다음 새 입력(6)에 대한 어떤 값(46)을 예상한 것.\
이것이 선형 회귀 모델을 만들어 문제를 해결하는 과정이다.

문제 해결 - 당뇨병 환자의 데이터\
당뇨병 환자의 1년 후 병의 진전된 정도를 예측하는 모델 생성
"""

# 사이킷런에서 당뇨병 환자 데이터 가져오기
# 머신러닝, 딥러닝 패키지에는 인공지능 학습을 위한 데이터 세트(dataset)가 준비되어 있다.
# 사이킷런과 케라스도 다양한 데이터 세트를 제공

from sklearn.datasets import load_diabetes # 사이킷런의 datasets 모듈에 있는 load_diabetes() 함수 임포트

# load_diabetes()로 당뇨병 데이터 준비
diabetes = load_diabetes() # diabetes에 당뇨병 데이터 저장
# diabetes 변수에 저장된 값의 자료형은 파이썬의 딕셔너리와 유사한 Bunch 클래스. 파이썬 딕셔너리라 생각해도 무방.

# 입력과 타깃 데이터의 크기 확인
# diabetes의 속성 중 data 속성과 target 속성에 입력, 타깃 데이터가 넘파이 배열로 저장되어 있다. 
# 넘파이 배열의 크기는 shape 속성에 저장되어 있다. 
# print(diabetes.data.shape, diabetes.target.shape) #(442, 10) (442, ) 출력
# data는 442*10(442개의 샘플, 10개의 샘플 특성) 크기의 2차원 배열. data의 행은 샘플(sample)이고 열은 샘플의 특성(feature)이다.
# 샘플이란 당뇨병 환자의 특성(환자의 혈압, 혈당, 몸무게 키, etc...)이고 샘플은 이에 해당하는 값(130, 27, 181,92, etc...)을 말한다. 
# 여기서 입력데이터의 특성은 속성 or 독립 변수 or 설명 변수(explanatory variable) 등으로 불린다. 

# 입력 데이터 자세히 보기
# diabetes.data[0:3]#0번 요소부터 3번 요소까지 출력(3*10 배)
# array([[ 0.03807591,  0.05068012,  0.06169621,  0.02187235, -0.0442235 ,
#        -0.03482076, -0.04340085, -0.00259226,  0.01990842, -0.01764613],
#       [-0.00188202, -0.04464164, -0.05147406, -0.02632783, -0.00844872,
#        -0.01916334,  0.07441156, -0.03949338, -0.06832974, -0.09220405],
#       [ 0.08529891,  0.05068012,  0.04445121, -0.00567061, -0.04559945,
#        -0.03419447, -0.03235593, -0.00259226,  0.00286377, -0.02593034]]) 출력

# 타깃 데이터 자세히 보기
# diabetes.target[:3] # array([151.,  75., 141.])출력
# 타깃 데이터는 샘플 1개에 대응되는 값들의 배열이다. 예를 들어 data[0] = (1*10 배열)에 해당하는 타깃 데이터는 target[0]이다. 
# 풀어서 표현하자면
# [ 0.03807591,  0.05068012,  0.06169621,  0.02187235, -0.0442235 ,
#  -0.03482076, -0.04340085, -0.00259226,  0.01990842, -0.01764613]라는 입력 데이터에 대응하는 타깃 데이터는 151.인 것이다.
# 수치의 의미는 전문가의 영역, 내가 할 일은 입력 데이터와 타깃 데이터의 수치만 보고 둘 사이의 규칙(모델)을 찾으면 된다.

# 당뇨병 환자의 데이터 시각화

# 맷플롯립 scatter()로 산점도 그리기
# 1개의 특성을 이용만 사용해 산점도 그리기

import matplotlib.pyplot as plt

# 다차원에서는 :를 기준으로 행, 열 분리
plt.scatter(diabetes.data[:,2], diabetes.target)# x축은 diabets의 3번째 특성(열의 인덱스가 2인 값), y축은 diabetes.target
plt.xlabel('x')
plt.ylabel('y')
plt.show()
# 그래프를 보아 입력 데이터와 타깃 데이터 사이에 정비례 관계가 있음을 알 수 있다. 

# 훈련 데이터 준비하기
# 입력 데이터의 일부를 미리 분리하여 변수 x에 저장하고 타깃 데이터는 변수 y에 저장.
x = diabetes.data[:, 2]
y = diabetes.target

# 경사 하강법
# 앞서 그린 산점도에 가장 잘 맞는 직선을 그리려먼 어떻게 해야할까?
# 가장 잘맞는 직선 -> 데이터를 표현하는 점들의 가운데 지점을 가로지르는 직선
# 특성 n개의 특성으로 그린 그래프 -> (n+1)차원 그래프. 너무 높은 차원의 그래프는 그리기 어렵다. 
# 그래서 특성 1, 2개만 사용해 2, 3차원 그래프로 그리는 경우가 많다. 이러한 그래프는 알고리즘에 대한 직관을 쉽게 얻을 수 있다.
# 항상 그런건 아니지만 낮은 차원에서(적은 특성으로) 얻은 직관(그래프)는 높은 차원(고차원 그래프)로 확장될 수 있으니 데이터의 특성 1개를 골라 시각화 하는 경우가 많다. 

# 선형 회귀와 경사 하강법
# 선형 회귀의 목표 : 입력 데이터(x)와 타깃 데이터(y)를 통해 기울기(a)와 절편(b)를 찾는 것 -> 산점도 그래프를 잘 표현하는 직선의 방정식을 찾는 것
# 경사 하강법(gradient descent) : 선형 회귀 알고리즘의 목표를 달성할 수 있는 방법 중 하나.
# 경사 하강법은 모델이 데이터를 잘 표현할 수 있더록 기울기(변화율)를 사용하여 모델을 조금씩 조정하는 최적화 알고리즘.
# 경사 하강법은 많은 양의 데이터에 사용하기 좋은 알고리즘.
# 경사 하강법 외에도 정규 방정식, 결정 트리, 서포트 벡터 머신 등 회귀 문제를 푸는 알고리즘은 아주 많다. 

# 경사 하강법 구현. 딥러닝 분야에선 기울기 a를 가중치를 의미하는 w나 계수를 의미하는 세타로 표기한다.
# 그리고 y대신 ŷ(y축 성분 표현할 때 쓰던거)을 사용한다. 고로 앞으로 모델을 y=ax+b 대신 ŷ=wx+b로 이해하도록 하자. 
# ŷ=wx+b에서 가중치 w와 절편 b는 알고리즘이 찾은 규칙을 의미하고 ŷ는 우리가 예측한 값(예측값)을 의미한다. 

# 예측값이란?
# 우리는 입력과 출력 데이터(x,y)를 이용해 규칙(a,b)을 발견하면 모델을 만들 수 있다. 
# 이 모델에 새로운 입력값을 넣으면 어떤 출력값이 나올 것이다. 이 때 출력값을 '모델을 통해 예측한 값'이라고 한다. 
# 예를 들어 y=7x+4에 입력값(x)으로 7을 넣으면 53이 나오는데 이 값(53)이 모델을 통해 예측한 값이다.
# 그렇기에 타깃 데이터를 표현한 y와 구분하기 위해 예측값을 ŷ라고 표현한다.(y와 ŷ가 어떤 결과라는 점은 동일하다.)
# ŷ을 적용하여 바꾼 식은 위에서 표현했듯 ŷ=wx+b이다. 

# 예측값으로 올바른 모델 찾기
# w와 b를 찾기 위한 방법
# 1. 무작위로 w와 b를 정한다(무작위로 모델 생성)
# 2. x에서 샘플 하나를 선택하여 ŷ를 계산(무작위로 모델 예측)
# 3. ŷ과 선택한 샘플의 진짜 y를 비교합니다.(예측값과 진짜 정답 비교)
# 4. ŷ와 y이 가까워지도록 w, b를 조정(모델 조정)
# 5. 모든 샘플을 처리할 때까지 다시 2~4 항목을 반복

# 과정 4(ŷ와 y이 가까워지도록 w, b를 조정) -> 모델이 복잡해질수록 체계적인 방법이 필요 

# 훈련 데이터에 맞는 w와 b 찾아보기
# w와 b가 바뀌었을 때 ŷ이 어떻게 변하는지 알아내는 가장 간단한 방법 : 실제로 계산을 해보는 것

# 1. w와 b 초기화하기
# w와 b를 무작위로 초기화(이번에는 1.0으로 초기화)
w = 1.0
b = 1.0

# 2. 훈련 데이터의 첫 번째 샘플 데이터로 ŷ얻기
# 훈련 데이터의 첫 번째 샘플 x[0]에 대한 ŷ을 계산. 예측값 ŷ는 y_hat에 저장
y_hat = x[0] * w + b
# print(y_hat) # 1.0616962065186886 출력

# 3. 타깃과 예측 데이터 비교
# 첫 번째 샘플 x[0]에 대응하는 타깃값 y[0]을 출력, y_hat과 비교
# print(y[0])# 151.0 출력 -> 예측값 1.0616962065186886과 차이가 크다.

# 4. w값 조절해 예측값 바꾸기
# y_hat이 y[0]에 가까워지도록 w, b를 바꾸는 방법 -> w,b를 조금씩 변경해 y_hat이 증가하는지 또는 감소하는지 관찰
# 우선 w를 0.1 증가
w_inc = w + 0.1
y_hat_inc = x[0] * w_inc + b
# print(y_hat_inc)# 1.0678658271705574출력. 값이 증가

# 5. w값 조정 후 예측값 증가 정도 확인
w_rate = (y_hat_inc - y_hat) / (w_inc - w)
# print(w_rate)# 0.061696206518688734 출력. 이 값을 첫번 째 훈련 데이터 x[0]에 대한 w의 변화율이라고 한다. 
# 근데 w_rate 식을 정리해보면 x[0]과 같다는 사실을 알 수 있다. 
# 변화율이 양수일 때 w를 증가시키면 y_hat이 증가하고 변화율이 음수일 때 w를 감소시키면 y_hat이 증가한다. 
# 허나 이 방법은 변화율의 부호에 따라 구분해야 하므로 번거롭다. 

# 변화율로 가중치 업데이트
# 위에서 알아낸 번거로움을 해결할 수 있는 방법.
# 선형 회귀의 목표 : y에 가까운 ŷ을 출력하는 모델(w와 b)를 찾아내는 것

# w의 업데이트 방법
# 1. 변화율이 양수일 때 업데이트 : 변화율이 양수이니 변화율에 w를 더하는 방법으로 w 증가
# 2. 변화율이 음수일 때 : w가 증가하면 y_hat이 감소 -> w가 감소하면 y_hat이 증가. 
# 즉, w에 변화율을 더하면 w가 감소 -> y_hat이 증가
# 결론, w에 w_rate를 더하기만 하면 된다.
w_new = w + w_rate # 가중치 업데이트
#  print(w_new)

# 절편 업데이트
# b의 변화율을 구한 다음 변화율로 b 업데이트. b를 0.1만큼 증가시킨 후 y_hat이 얼마나 증가했는지 계산하고 변화율도 계산
b_inc = b + 0.1
y_hat_inc = x[0] * w + b_inc
print(y_hat_inc)# 1.1616962065186887

b_rate = (y_hat_inc - y_hat) / (b_inc - b)
print(b_rate) # 1.0, 변화율이 1(b가 1만큼 증가하면 y_hat도 1만큼 증가)
# b 업데이트 -> b + (b의 변화율)
b_new = b + 1
print(b_new)# 2.0

# 위에서 구현한 w, b 업데이트 방법은 다소 수동적이다. 
# 왜냐하면 이 방법이 
# 1) y_hat이 y에 한참 미치치 못하는 경우, w와 b를 더 큰 폭으로 수정할 수 없다. (변화율만큼 수정했지만 특별한 기준을 정하기가 어렵다.)
# 2) y_hat이 y보다 커지면 y_hat을 감소시키지 못한다.(변화율의 음, 양수에 관계없이 무조건 y_hat은 커지니까)

# 오차 역전파(backpropagation) : w와 b를 능동적으로 업데이트 하는 방법
# 오차 역전파는 y와 y_hat의 차이를 이용해 w, b를 업데이트 하는 방법이다. 
# 이 방법은 오차가 연이어 전파되는 방법으로 수행된다.