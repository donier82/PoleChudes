from ran_help import ran_word
word=ran_word()
#print(word)

q=len(word)
s=6
k=''
print('''угадайте слова по буквом. у вас 7 попыток при ошибке.''')
while s>-1:
    
    l=input('введите букву: ')
    if l in word:
        print('угадали')
        print(f'буква: {l}')
        k=k+l
        print(k)
        m=len(k)
        if m==q:
            print(f'вы выиграли. слова {word}')
            break
    
    else:
        print('не угадали')
        print(f'у вас осталось {s} попыток')
        s=s-1



    
       
    
    
            
