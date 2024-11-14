import math
angulo = float(input('Digite o angulo que voce deseja: '))
sen = math.sin(math.radians(angulo))
print('o angulo 'f"{angulo:.2f}", 'tem seno ' f"{sen:.2f}")
cos = math.cos(math.radians(angulo))
print('o angulo ' f"{angulo:.2f}", 'tem cosseno ' f"{cos:.2f}")
tan = math.tan(math.radians(angulo))
print('o angulo ' f"{angulo:.2f}", 'tem tangente ' f"{tan:.2f}")