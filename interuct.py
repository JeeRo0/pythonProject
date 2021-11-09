while True:
    reply = input('Введите текст:')
    if reply == 'стоп': break
    try:
        num = int(reply)
    except:
        print('bad'*8)
    else:
        print(num**2)
print('bye')