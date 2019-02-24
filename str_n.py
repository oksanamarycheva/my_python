s=input('Введите строку:')
n=float(input('Введите число:'))
def str_n(s,n):
    if len(s)>n:
        return s.upper()
    else:
        return s
if __name__ == '__main__':
    print(str_n(s,n))
