import numpy as np
import matplotlib.pyplot as plt
plt.style.use("seaborn-poster")

n = 10
h = (5-0)/n

A = np.zeros((n+1, n+1))
A[0,0] = 1
A[n,n] = 1
for i in range (1,n):
    A[i,i-1] = 1
    A[i,i] =-2
    A[i,i+1] = 1
print("Matriks A=",A)

B = np.zeros(n+1)
B[1:-1] = -9.8*h**2
B[-1] =50
print("Matriks B=",B)

#Menghitung persamaan linear
y = np.linalg.solve(A, B)
t = np.linspace(0,5,11)

#Membuat plot gambar
plt.figure(figsize=(10,8))
plt.plot(t,y)
plt.plot([0,0.5,1,1.5],[0,16.025,29.6,40.725],"ro")
plt.plot([2,2.5,3,3.5],[49.4,55.625,59.4,60.725],"ro")
plt.plot([4,4.5,5],[59.6,56.025,50],"ro")
plt.xlabel("time (s)")
plt.ylabel("altitude (m)")
plt.show()

#Mencari Kecepatan Awal
y_n1 = -9.8*h**2 + 2*y[0] - y[1]
Solusi = (y[1] - y_n1) / (2*h)

print ("Kecepatan Awal dari proses peluncuran adalah",Solusi)