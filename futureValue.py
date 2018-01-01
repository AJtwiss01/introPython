def main():
    print('This prgram prints future values')
    print('Of ten year investments')

    principal = eval(input("enter initial value: "))
    apr = eval(input("Enter annual intrest rate: "))
    for i in range(10):
        year = i + 1
        principal = principal *(1 + apr)
        print("the value in 10 years " + str(year), principal)
if __name__ == "__main__":
    
    main()