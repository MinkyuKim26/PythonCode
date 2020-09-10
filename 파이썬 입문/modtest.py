#modtest.py와 mod2.py가 같은 폴더 안에 있어야 아래 코드가 정상적으로 작동
import mod2
result = mod2.add(3,4)
print(result)
#파이썬 라이브러리가 설치된 폴더에 모듈이 들어있다면 그 모듈은 같은 디렉토리가 아니여도 바로 불러서 사용할 수 있다. 
#PYTHONPATH 환경변수에 모듈의 경로를 추가해도 바로 사용 가능하다.