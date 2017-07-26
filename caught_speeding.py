speed=40
no_ticket= speed<31
small_ticket=speed>30 and speed <51
big_ticket= speed>50

is_birthday= False
if is_birthday==True:
    if speed <36:
        print('no ticket')
    elif speed>35 and speed <56:
        print('small ticket')
    else:
        print('big ticket')
else:
    if speed < 31:
        print('no ticket')
    elif speed>30 and speed<51:
        print('small ticket')
    else:
        print('big ticket')
