import random
x=random.randint(1,4)
a=int(input('Какое число я загадал?'))
if x==a:
    print("Победа!")
elif x>a:
    print('Ваше число меньше загаданного. Повторите еще раз!')
elif x<a:
    print('Ваше число больше загаданного. Повторите еще раз!')

