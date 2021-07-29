password = 'a123456'
i = 3 
while i > 0:
    trying = input('請輸入密碼: ')
    i = i - 1
    if trying == password:
        print('密碼正確!')
        break
    else:
        print('密碼錯誤')
        if i > 0:  
            print('剩下', i, '次機會')
        else:
            print('沒機會了')
            
        
