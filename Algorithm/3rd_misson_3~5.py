import numpy as np
#
# def l1_norm(x):
#     x_norm = np.abs(x)
#     x_norm = np.sum(x_norm)
#     return x_norm
#
# def l2_norm(x):
#     x_norm = x*x
#     x_norm = np.sum(x_norm)
#     x_norm = np.sqrt(x_norm)
#     return x_norm
# def angle(x,y):
#     v = np.array(x,y) / (l2_norm(x) * l2_norm(y))
#     theta = np.arccos(v)
#     return theta

xy= np.array([[1.0,2,3,4,5,6],[10,20,30,40,50,60]],float)
## take 함수를 써먹고싶으데 어떻게 쓰는지 까먹음
x_train = xy[0,:]
y_train = xy[1,:]
print(x_train, x_train.shape)
print(y_train, y_train.shape)

beta_gd = np.random.rand(1)
bias = np.random.rand(1)
print(beta_gd,bias)

learning_rate = 0.01

