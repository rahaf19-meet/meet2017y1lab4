for i in range(100):
    count=i+1
    if count%15==0:
        print('fizzbuzz')
    
    else :
        if count%3==0:
            print('fizz')
        elif count%5==0:
            print('buzz')
        else:
            print(count)
    
