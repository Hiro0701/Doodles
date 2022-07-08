import numpy as np
import matplotlib.pyplot as plt

file = input("파일 위치: ")
iteration = input("반복 횟수: ")
theta = input("초기 세타값 (띄어쓰기로 입력): ")
alpha = input("알파값: ")
theta = theta.split()
theta = np.array(theta, dtype=float)
iteration = int(iteration)
alpha = float(alpha)
ts = open(file, 'r')

data = []
for row in ts:
    data.append([float(x) for x in row.split()])
data = np.asarray(data)
n = data.shape[1]

X = data[:,0:n-1]
y = data[:,n-1]
y = y.reshape(-1,1)
m = len(y)
n = len(theta)

X = np.append(np.ones(m, dtype=int).reshape(-1,1), X, axis=1)
J = np.zeros(m)
temp = np.zeros(n)
temp1 = np.zeros(X.shape)
J_iter = np.zeros(iteration)
theta_iter = np.zeros((iteration,n))

for k in range(iteration):
    for i in range(m):
        for j in range(n):
            temp[j] = theta[j]*X[i,j]
            temp1[i,j] = theta[j]*X[i,j]
        sum = np.sum(temp)
        J[i] = (sum - y[i]) ** 2
    J_iter[k] = 1/(2*m)*(np.sum(J))
    for i in range(n):
        theta[i] = theta[i] - alpha*(1/m)*(np.sum(np.multiply(temp1[i,:] - y, X[i,:])))
    theta_iter[k] = theta

plt.figure(1)
plt.title('J cost of each iteration')
plt.plot(range(iteration), J_iter, '-b')
plt.text(J_iter.argmin(), J_iter.min(), round(J_iter.min(),5), horizontalalignment='center', verticalalignment='top')
plt.xlabel("Iteration")
plt.ylabel("J function")
plt.ylim([0, 100])
plt.show()

if n < 3:
    plt.figure(2)
    plt.title('Prediction with the optimal theta values')
    plt.plot(X[:, 1], y, 'ro', X[:,1], np.matmul(X, theta_iter[J_iter.argmin()]), '-')
    plt.xlabel("Training set")
    plt.ylabel("Result")
    plt.show()
    print("The minimum J cost is: ", J_iter.min())
    print("The optimal theta is ", theta_iter[J_iter.argmin()])
else:
    print("The minimum J cost is: ", J_iter.min())
    print("The optimal theta is ", theta_iter[J_iter.argmin()])
