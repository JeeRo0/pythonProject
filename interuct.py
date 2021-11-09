while True:
    reply = input('Введите текст:')
    if reply == 'стоп': break
    try:
        print(int(reply)**2)
    except:
        print('bad'*8)
print('bye')
