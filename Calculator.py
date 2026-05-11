def calculator():
    while True:
        print("\n" + "="*30)
        print("   0YKON'S CALCULATOR")
        print("="*30)
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")
        print("5. Exit")
        
        choice = input("\nOption chunein (1-5): ")

        if choice == '5':
            print("\nCalculator band ho gya fir se suru krne ke liye file ko dubara run kijiye. Alvida!")
            break

        if choice in ('1', '2', '3', '4'):
            try:
                num1 = float(input("Pehla number: "))
                num2 = float(input("Dusra number: "))
            except ValueError:
                print("\nError: Sirf numbers likhein!")
                continue

            if choice == '1':
                print(f"\nRESULT: {num1} + {num2} = {num1 + num2}")
            elif choice == '2':
                print(f"\nRESULT: {num1} - {num2} = {num1 - num2}")
            elif choice == '3':
                print(f"\nRESULT: {num1} * {num2} = {num1 * num2}")
            elif choice == '4':
                if num2 == 0:
                    print("\nError: Zero se divide nahi kar sakte!")
                else:
                    print(f"\nRESULT: {num1} / {num2} = {num1 / num2}")
            
            print("\n" + "-"*30)
        else:
            print("\nGalat option! Kripya 1 se 5 tak hi chunein.")

calculator()
