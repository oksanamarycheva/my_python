x=['самовар','весна','лето']
import random
p=random.choice(x)
p1=list(p)
p2=random.choice(p1)

q=''.join(p1)
p4=q.find(p2)

q1=list(q)
import copy
b=copy.deepcopy(q1)
q1.remove(p2)
q1.insert(p4, "?")

q2=''.join(q1)
print(q2)

l=input('Попробуйте угадать букву! Ваш вариант:')
if l in b:
    print('Победа!')
else:
    print('Увы! Попробуйте в другой раз.')


