from BMICal_Classes import*

User_name = name()
W_H= BMIResult()
i=r=0
#print(type(W_H))

print('\t\t\t\t Welcome to BMI calculator Version 0.0.3')
while i==0:
    print('\n\t\t\t\t  Type "e" to enter, or type "x" to exit\n')
    enter_exit = input('--> ')
    if enter_exit == 'e' or enter_exit =='E':
        #program begins
        User_name.in_name = str(input('Insert your name--> '))
        while r==0:
            try:                                                                                                    #Check if it's a correct value
                W_H.height= float(input('Insert your height(In meters)--> '))
                W_H.weight= float(input('Insert your weight(In kilograms)--> '))
            except ValueError as e:                                                                                 #When input 'String', it will show error
                print('No words allowed:', e)
                continue
            else:
                if (W_H.height <0.3 or W_H.height > 2.4) or (W_H.weight < 20 or W_H.weight > 300):
                    print('Please insert the correct information (No negative number or unrealistic number)\n')
                    continue
                else:
                    print('\nYour name is:',User_name.in_name)
                    W_H.calBMI_Value()
                    W_H.dispBMIResult()
                break
    elif enter_exit == 'x' or enter_exit =='X':
        print('You exit the program')
        break
    else:
        print('Please try again')
        continue
