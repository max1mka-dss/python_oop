"""Подвиг 4. Объявите три класса геометрических фигур: Line, Rect, Ellipse.
 Должна быть возможность создавать объекты каждого класса следующими командами:

g1 = Line(a, b, c, d)
g2 = Rect(a, b, c, d)
g3 = Ellipse(a, b, c, d)


Здесь в качестве аргументов a, b, c, d передаются координаты верхнего правого и нижнего левого углов (произвольные числа).
 В каждом объекте координаты должны сохраняться в локальных свойствах sp (верхний правый угол) и ep (нижний левый)
  в виде кортежей (a, b) и (c, d) соответственно.

Сформируйте 217 объектов этих классов: для каждого текущего объекта класс выбирается случайно (или Line, или Rect, или Ellipse).
Координаты также генерируются случайным образом (числовые значения). Все объекты сохраните в списке elements.

В списке elements обнулите координаты объектов только для класса Line.

P.S. На экран в программе ничего выводить не нужно."""
import random

from sqlalchemy.sql.base import elements


class Line:
    def __init__(self,a,b,c,d):
        self.sp = (a,b)
        self.ep = (c,d)
class Rect:
    def __init__(self,a,b,c,d):
        self.sp = (a,b)
        self.ep = (c,d)
class Ellipse:
    def __init__(self,a,b,c,d):
        self.sp = (a,b)
        self.ep = (c,d)

d = Line(1,2,3,4)
elements = []
lst = [Line,Rect,Ellipse]
for x in range (1, 218,1):
    elements.append((random.choice(lst))(random.randint(-100,100),random.randint(-100,100),random.randint(-100,100),random.randint(-100,100)))


for x in elements:
    if type(x) == Line:
        x.sp = (0,0)
        x.ep = (0,0)
\

#print(type(elements[0]).__name__)

obj = Rect (4,2,7,3)
#print( type(obj).__name__)
#print(type(elements[0]).__name__)