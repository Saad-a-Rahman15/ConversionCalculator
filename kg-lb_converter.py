print('Type one of the numbers below')
print('1 = kg converted to lb')
print('2 = lb converted to kg')
choice = input('    1    2    \n')


if(choice == '1'):
        kg = input('Enter an amount of kilograms. \n')
        kg = float(kg)

        lb = ( kg / 2.2 )

        if(kg == '0' ):
            print('0.00 lb')
        else:
            print('The amount of pounds that would equal that many kilograms are:')
        lb_value = kg * 2.2
        lb_value = round(lb_value, 1)
        print(str(lb_value) + ' lb')
        print('Thank you for choosing this calculator!')
elif(choice == '2'):
        lb2 = input('Enter an amount of pounds. \n')
        lb2 = float(lb2)

        kg2 = ( lb2 * 2.2 )

        if(lb2 == '0' ):
            print('0.00 kg')
        else:
            print('The amount of kilograms that would equal that many pounds are:')
            
        kg2_value = lb2 *  0.45359237
        kg2_value = round(kg2_value, 1)
        print(str(kg2_value) + ' kg')
        print('Thank you for choosing this calculator!')
else:
    print('That cannot be done.')