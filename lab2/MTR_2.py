#Variant 7

import math

p1 = 0.5
p2 = 0.5
p3 = 0.99
p4 = 0.01

inc1 = 3000
inc2 = 2000
inc3 = 2510
inc4 = 1510

M_1 = p1*inc1 + p2*inc2
M_2 = p3*inc3 + p4*inc4

print(M_1, " ", M_2)

V_1 = (inc1-M_1)**2 * p1 + (inc2-M_1)**2 * p2
V_2 = (inc3-M_2)**2 * p3 + (inc4-M_2)**2 * p4

CV_1 = math.sqrt(V_1) / M_1
CV_2 = math.sqrt(V_2) / M_2

print(CV_1, " ", CV_2)
