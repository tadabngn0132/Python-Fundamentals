english = int(input('Enter Engling grade: '))
math = int(input('Enter Math grade: '))
literature = int(input('Enter Literature grade: '))

average = ((english + math + literature) / 3)
    
if 0.0 <= english <= 10.0 and 0.0 <= math <= 10.0 and 0.0 <= literature <= 10.0:
    if 4.0 > average:
        print('failed')
    elif 4.0 <= average <= 6.5:
        print('pass') 
    elif 6.5 < average < 8.0:
        print('merit') 
    else:
        print('distinction') 
else:
        print('invalid grade') 
