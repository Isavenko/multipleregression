from random import *
import matplotlib.pyplot as plt
import statistics
from statistics import mean
from sklearn.metrics import *
import numpy as np

## k1x1 + k2x2 = c

x = []
x1 = []
x2 = []
y = []
#randomcoefficients = [1,100,100]
randomcoefficients = sample(range(1, 101), 3)

###################################

for i in range(0,5000):
    cd1 = uniform(0,1)
    cd2 = uniform(0,1)
    cd3 = uniform(0,1)
    x.append(cd1)
    x1.append(cd2)
    x2.append(cd3)
    y.append((cd1*randomcoefficients[0])+(cd2*randomcoefficients[1])+(cd3*randomcoefficients[2]))
avgcost = mean(y)

######################################################

xs = np.array(x, dtype=np.float64)
ys = np.array(y, dtype=np.float64)

def best_fit_slope_and_intercept(xs,ys):
    m = (((mean(xs)*mean(ys)) - mean(xs*ys)) /
         ((mean(xs)*mean(xs)) - mean(xs*xs)))
    return m

print("--- C1 / Blue ---")
p1 = best_fit_slope_and_intercept(xs,ys)
print("Predicted: " + str(int(round(p1))))
a1 = randomcoefficients[0]
print("Actual: " + str(a1))
d1 = abs(p1-a1)
print("Delta: " + str(int(round(d1))))
dp1 = d1 / a1
if d1 == 0: print("Delta %: N/A\n")
else: print("Delta %: " + str(int(round(dp1 * 100))) + "\n")

######################################################

xs = np.array(x1, dtype=np.float64)
ys = np.array(y, dtype=np.float64)

print("--- C2 / Orange  ---")
p2 = best_fit_slope_and_intercept(xs,ys)
print("Predicted: " + str(int(round(p2))))
a2 = randomcoefficients[1]
print("Actual: " + str(a2))
d2 = abs(p2-a2)
print("Delta: " + str(int(round(d2))))
dp2 = d2 / a2
if d2 == 0: print("Delta %: N/A\n")
else: print("Delta %: " + str(int(round(dp2*100))) + "\n")

###

xs = np.array(x2, dtype=np.float64)
ys = np.array(y, dtype=np.float64)

print("--- C2 / Green ---")
p3 = best_fit_slope_and_intercept(xs,ys)
print("Predicted: " + str(int(round(p3))))
a3 = randomcoefficients[2]
print("Actual: " + str(a3))
d3 = abs(p3-a3)
print("Delta: " + str(int(round(d3))))
dp3 = d3 / a3
if d3 == 0: print("Delta %: N/A\n")
else: print("Delta %: " + str(int(round(dp3*100))) + "\n")




plt.style.use('Solarize_Light2')
a = plt.subplot(2, 2, 1)
plt.scatter(x, y, alpha=0.3,color=['red'])
a.set_xlabel('School Feature 1')
a.set_ylabel('Cost')
b = plt.subplot(2, 2, 2)
plt.scatter(x1, y, alpha=0.3,color=['green'])
b.set_xlabel('School Feature 2')
b.set_ylabel('Cost')
c = plt.subplot(2, 2, 3)
plt.scatter(x2, y, alpha=0.3,color=['blue'])
c.set_xlabel('School Feature 3')
c.set_ylabel('Cost')
plt.show()

##

