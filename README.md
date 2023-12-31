# CG

Task 1 - алгоритм Брезенхема для построения прямой \
Task 2 - поворот прямой \
Task 3 - алгоритм Брезенхема для построения окружности \
Task 4 - кратчайший путь\
Task 5 - фильтр Собеля\
Task 6 - фильтр Гаусса\
Task 7 - алгоритм Цируса-Бека\
Task 8 - Алгоритм отсечения невидимых граней с использованием Z-буфера\
Task 9 - Алгоритм Роджерса\
Task 10 - transform 3d\
Task 11 - transform 2d\
Task 12 - заполнение\
Task 13 - освещенность

Bresenham's algorithm - a fundamental method in Computer Graphics - is a clever way of approximating a continuous straight line with discrete pixels, ensuring that the line appears straight and smooth on a pixel-based display.

'Aлгоритмические основы компьютерной графики' Hью Pоджерс\
'Математические основы компьютерной графики' Hью Pоджерс

Cравниваем две окружности, проходящие через две точки растра

Rd - диагональ\
Rs - shift

**Rs - R < R - Rd** - смещение вверх            <=>  **Rs - 2R + Rd < 0**    по вертикали\
**Rs - R >= R - Rd** - смещение по диагонали    <=>  **Rs - 2R + Rd >= 0** по диагонали

**(Rs - R)^2 < (R - Rd)^2** - вверх\
**(Rs - R)^2 >= (R - Rd)^2** - по диагонали

**Rs = (xs^2 +ys^2)^(1/2)** примерно равно R^2                     

=> **Rs - 2R + Rd ? 0** => (xd^2 +yd^2 - R^2) + (xs^2 +ys^2 - R^2) ? 0

**Rd = (xd^2 +yd^2)^(1/2)** примерно равно 2*R*(xd^2 +yd^2)^(1/2)  

**F = (xd^2 +yd^2 - R^2) + (xs^2 +ys^2 - R^2) ? 0**

При движении вверх посчитаем dF:

dFs = (x^2 + (y+2)^2 + (x+1)^2 +(y+2)^2 - 2*R) - (x^2 + (y+1)^2 + (x+1)^2 +(y+1)^2 - 2 * R) = 4*y + 6
// по вертикали **(1)**

dFd = (x+1)^2 + (y+2)^2 + (x+2)^2 + (y+2)^2 - 2*R^2 - (x^2 + (y+1)^2 + (x+1)^2 + (y+1)^2 - 2*R) = 4*x + 4*y + 10 // по диагонали **(2)**


F0 = R^2 + (1)^2 + (R-1)^2 + (R-1)^2 + (1)^2 - 2*R^2 = 3 - 2*R **(3)**
к текущему F прибавляем то F, которое получилось при смещении



```
  x    y     F
-10   0   -17 вверх   => (1) вместро R пожставляем x
-10   1   -11 вверх
-10    2   -1  вверх
-10    3    13  диаг
-9     4   -18 вверх
-9     5    4 диаг
-8     6   -2 вверх
-8     7    32 диаг
-7     8
```

Aлгортм построения эллипса
a*x^2 + b*y^2 = R^2
