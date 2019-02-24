s='У лукоморья 123 дуб зеленый 456'
print(s.index('я'))
print(s.count('у'))
if s.isalpha() == False:
    print(s.upper())
p=len(s)
if p>4:
    print(s.lower())
print(s.replace("У", 'O'))
      
