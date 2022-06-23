import numpy as np

x = np.array([1,2,3])
print(x.__class__) #クラス名を表示
print(x.shape)  #ベクトルの形を出力
print(x.ndim) #ベクトルの次元数（？）を表示、次元数であれば、この場合3の気がする…

W = np.array([[1,2,3],[4,5,6]])
print(W.shape)  #テンソルの形を出力
print(W.ndim) #テンソルの次元数（？）を表示

# 多分、数学的な次元ではなくて、プログラム的な配列の次元なんだと思う

# 1.1.2
# 多次元配列中の要素ごと、つまり各要素で独立して演算が行われる。
W = np.array([[1,2,3],[4,5,6]])
X = np.array([[0,1,2],[3,4,5]])

print(W+X)
print(W*X)

# 1.1.3 ブロードキャスト

# 以下の場合は線形代数の行列で言うスカラー倍
A = np.array([[1,2],[3,4]])
print(A*10)

# 以下の場合は、多分、数学上、見ない展開
b = np.array([10,20])
print(A*b)

# 1.1.4 ベクトルの内積と行列の積
# ベクトルの内積
a = np.array([1,2,3])
b = np.array([4,5,6])
print(np.dot(a,b))

# 行列の積
A = np.array([[1,2],[3,4]])
B = np.array([[5,6],[7,8]])
print(np.dot(A,B))
