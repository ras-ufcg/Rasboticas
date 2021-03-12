import numpy as np

# questao 01
A = np.random.rand(4,4)
B = np.random.rand(4,4)
print("A=\n",A)
print("\nB=\n",B)
print("A + B =\n",A+B)
print("\nA - B =\n",A-B)
print("\nA .* B =\n",A*B)
print("\nA ./ B =\n",A/B)
print("\nA * B =\n",np.matmul(A,B))
print("\n[A,B] =\n",np.hstack((A,B)))

# questao 02
A = np.random.rand(3,3)
B = np.sin(A)
print("A (degrees) =\n",np.rad2deg(A))
print("\nB=\n",B)

# questao 03
valid = 1
while valid:
  str_in = input("TYPE STOP TO STOP :)\nf(x) = sin(x), for x in degrees >> x = ")
  if str_in == "STOP":
    valid = 0
  else:
    str_out = np.sin(np.deg2rad(int(str_in)))
    print("sin(",str_in,") = ",str(str_out))