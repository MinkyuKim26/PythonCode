##from game.sound.echo import echo_test 
#한 모듈에서 다른 모듈을 사용하고 싶을 때 사용 방법 : 다른 모듈을 import하면 된다.
# def render_test():
#     print("render")
#     echo_test()

#relative하게 import
# from ..sound.echo import echo_test # ..는 부모 디렉토리를 의미한다.
# #graphic과 sound 폴더는 동일한 깊이(depth)이므로 부모 디렉터리(..)를 사용하여 위와 같은 import가 가능하다.
# #..와 같은 relative한 접근자는 render.py처럼 모듈 안에서만 사용해야 한다. 파이썬 인터프리터에서 사용할 경우 오류 발생
# def render_test():
#     print("render")
#     echo_test()