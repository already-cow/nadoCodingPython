# 모듈을 모아놓은 집합 = 패키지

import travel.thailand # 맨 마지막은 모듈, 패키지만 가능 / 클래스, 함수 직접 import 불가능
trip_to = travel.thailand.ThailandPackage()
trip_to.detail()

from travel.thailand import ThailandPackage # from import 구문은 클래스, 함수 가능
trip_to = ThailandPackage()
trip_to.detail()

from travel import vietnam
trip_to = vietnam.VietnamPackage()
trip_to.detail()