def main(): 
    print('hello')

    print('Change counter')
    print()
    print('Please enter the count of each coin type.')
    quarters = int(input('Quarters: '))
    dimes = int(input('Dimes: '))
    nickels = int(input('Nickles: '))
    pennies = int(input('Pennies: '))
    total = .25*quarters + .10*dimes + .05*nickels + .01*pennies
    print()
    print('The total value of your change is - ', total)

if __name__ == '__main__':

    main()

    