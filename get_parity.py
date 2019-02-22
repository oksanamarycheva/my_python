x=int(input('Напишите целое число:'))
def get_parity(x):
    if x/2==x//2:
        return('Четное')
    else:
        return('Нечетное')
print(get_parity(x))
