print('Type one of of the numbers below')
print('1 = celcius converted to farenheit')
print('2 = farenheit converted to celcius')
choice = input('    1    2    \n')


if(choice == '1'):
        celcius = input('Enter an amount of degrees in celcius. \n')
        celcius = float(celcius)

        farenheit = ( celcius * 1.8 + 32 )

        if(celcius == '0' ):
            print('0.00 degrees farenheit')
        else:
            print('The amount of degrees farenheit that would equal that many degrees celcius is:')
        farenheit = round(farenheit, 2)
        print(str(farenheit) + ' degrees farenheit')
        print('Thank you for choosing this calculator!')
elif(choice == '2'):
        farenheit2 = input('Enter an amount of degrees in farenheit. \n')
        farenheit2 = float(farenheit2)

        celcius2 = ( farenheit2 - 32 * 0.5556 )

        if(farenheit2 == '0' ):
            print('0.00 degrees celcius')
        else:
            print('The amount of degrees celcius that would equal that many degrees farenheit is:')
            
        celcius2 = round(celcius2, 2)
        print(str(celcius2) + ' degrees celcius')
        print('Thank you for choosing this calculator!')
else:
    print('That cannot be done.')