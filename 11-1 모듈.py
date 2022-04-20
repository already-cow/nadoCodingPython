import theater_module
theater_module.price(3)
theater_module.price_morning(4)
theater_module.price_soldier(5)

import theater_module as mv # 줄여서 사용
mv.price(3)
mv.price_morning(4)
mv.price_soldier(5)

from theater_module import *
price(3)
price_morning(4)
price_soldier(5)

from theater_module import price, price_morning # 사용할 함수만 정의 (위에 것을 삭제하면 정상 작동)
price(5)
price_morning(4)
# price_soldier(1)

from theater_module import price_soldier as price # 실제 price와는 다르고 soldier 값을 받는 price로 변경
price(3)