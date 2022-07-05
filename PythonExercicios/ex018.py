#Exercício Python 018: Faça um programa que leia um ângulo qualquer e
# mostre na tela o valor do seno, cosseno e tangente desse ângulo.

'''import math

ang = float(input('Digite um angulo qualquer: '))

print('O Seno do número {} é {:.2f}. '
      'O Cosseno do número {} é {:.2f}. '
      'A Tangente do número {} é {:.2f}'.format(ang, math.sin(math.radians(ang)), ang, math.cos(math.radians(ang)), ang, math.tan(math.radians(ang))))'''

from math import sin, cos, tan, radians

ang = float(input('Digite um angulo qualquer: '))

print('O Seno do ângulo {} é {:.2f}. '
      'O Cosseno do ângulo {} é {:.2f}. '
      'A Tangente do ângulo {} é {:.2f}'.format(ang, sin(radians(ang)), ang, cos(radians(ang)), ang, tan(radians(ang))))

