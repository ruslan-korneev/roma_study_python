from typing import Optional, Union


def summa(a: Optional[int], b: int) -> Union[int, str]:
    """ This function summ `a` and `b` and return number """
    if not a:
        return "Cool!"
    return a + b

a = 5
b = 10

c = summa(10, b)
print(c)
c = summa(4, summa(a, b))
print(c)


# 1. когда ты видишь, что ты несколько раз пишешь одно и тоже, создай функцию
# 2. пиши документации к функцие
# 3. пиши аннотации к функцие
