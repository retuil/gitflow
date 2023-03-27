a = '7'*104
while True:
    if '33333' in a:
        a = a.replace('33333', '7', 1)
    elif '777' in a:
        a = a.replace('777', '3', 1)
    else:
        break
print(a)