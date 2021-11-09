while True:
    reply = input('Введите текст:')
    if reply == 'стоп':
        break
    elif not reply.isdigit():
        print('bad'*8)
    else:
        print(int(reply)**2)
print('bye')