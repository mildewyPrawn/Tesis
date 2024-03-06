import Point as pt
import Circle as cr
import Delaunay as de
import Edge as ed
import math

a = pt.Point(11, 11)
b = pt.Point(13, 9)
c = pt.Point(13, 11)
d = pt.Point(12, 7)
e = pt.Point(10, 9)
f = pt.Point(15, 10)

# h1 = pt.Point(-5, 13)
# h2 = pt.Point(3, -3)
# print('{} -- {}'.format(h1, h2))
# eh1 = ed.Edge(h1, h2)
# m1, b1 = eh1.get_equation()
# print('equation: y = {}x + {} = 0'.format(m1, b1))

# c1 = cr.Circle(a=d, b=b, c=f)
# ch1, ck1, cr1 = c1.get_equation()
# print('equation: (x - {})**2 + (y - {})**2 - {}**2 = 0'.format(ch1, ck1, cr1))

l = [a,b,c,d,e,f]

# abfc = a.middle_point(b)
# print('middle between {} and {} is: {}'.format(a, b, abfc))

delaunay = de.Delaunay(l)
triangles = delaunay.get_triangulation()

voronoi = []

for t in triangles:
    # print(t)
    v = vor.Polygon(t)
    edges = v.six_edges()

    voronoi = voronoi + edges
    # voronoi.append(edges)
    # print('{}'.format(v))

for v in voronoi:
    print(v)


'''
sacar el arcotangente de un punto -> from math import atan2 atan2(x, y)
sacar el ángulo de un punto -> from math import atan2, degrees -> atan2(x, y) -> degrees(atan2(x, y))

dibujar la línea de (x,y) con ángulo [:up] y longitud r
'''

'''
Mau: mediatriz
calcular punto medio -> (x0, y0)
calcular pendiente del segmento AB -> m
calcular pendiente de la mediatriz = m' = -(1/m)

-> m'(x - x0) = y - y0
-> m'(x - x0) + y0 = y
-> y = m'(x - x0) + y0
-> = m'x + ((-m'x0) + y0)

agregar casos: if la linea es sobre el eje x -> la mediatriz es el eje
x (mediatriz de y=y es undefined).

ej.
-3*x + (-(-3)*4 + 3)
-3*x + (12 + 3)
-3*x + 15

Ahora sacar la paralela del segmento e intersectar la mediatriz con la paralela.

Para sacar la paralela sabemos: y = mx + b

Sabemos que dicha recta pasa por el origen

Además, conocemos el radio del círculo, por lo que necesitamos una paralela a distancia r de y

y = mx + b

0 = mx + b - y

mx - y + b = 0

A  = m
B  = -1
C1 = b
C2 = k

d = r

d = (|C1 - C2|) / (sqrt(A² + B²))
r = +- (|b - k|) / (sqrt(A² + B²)) # +- porque tenemos distancia pa'rriba y pa'bajo
r * (sqrt(A² + B²)) = +- (|b - k|)
(r * (sqrt(A² + B²))) - |b| = |k|

ej.
y = 0.333x + 1.666
0.333x - y + 1.666 = 0

A  = 0.333
B  = -1
C1 = 1.666 -> (distance from this line to the center = 1.006), therefor C1 = .66
C2 = k

d = r = 3.318

3.318 = (|1.666 - C2|) / (sqrt((0.333)² + (-1)²))
3.318 = +- (|.66 - k|) / (sqrt(.110 + 1))


R = -2.891, 4.104

take - away...
3.318 * sqrt(1.110) = (|.66 - k|)
3.318 * 1.053 = (|.66 - k|)
3.493 = (|.66 - k|)
3.493 - .66 = |-k|
2.833 = -k
k = -2.833

k = -1 * ((3.318 * sqrt(1.110)) - 0.66)

take + away...
3.318 * -sqrt(1.110) = (|.66 - k|)
3.318 * -1.053 = (|.66 - k|)
-3.493 = (|.66 - k|)
-3.493 - .66 = |-k|
-4.153 = k
k = 4.153

k = -1 * ((3.318 * (-1 * sqrt(1.110))) - 0.66)

'''
