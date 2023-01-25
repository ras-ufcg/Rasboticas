import numpy as np
matrizA = np.array([[0,0,0],[0,0,0],[0,0,0]])
for l in range(0,3):
  for c in range(0,3):
    matrizA[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))

matrizB = np.array([[0.0,0.0,0.0],[0.0,0.0,0.0],[0.0,0.0,0.0]])
for l in range(0,3):
  for c in range(0,3):
    matrizB[l][c] = np.sin(matrizA[l][c])

print()
print(matrizA,"\n")
print(matrizB)
