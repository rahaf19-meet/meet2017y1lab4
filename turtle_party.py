strawberries=39
is_weekend=True
weekday=strawberries>39 and strawberries< 61
weekend= strawberries>39
if is_weekend==True:
    if strawberries<39:
        print('Not Fun!')
    else:
        print('Fun!')
else:
    if strawberries<39 and strawberries>61:
        print('Not Fun!')
    else:
        print('Fun')
        
