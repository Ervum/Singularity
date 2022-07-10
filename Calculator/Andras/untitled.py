while True:

    def calculadora():
        num1 = input('Enter the first number: ')
        pregunta = input('Do you want to subtract, add, divide or multiply? Type your answer (+,-,*,/,%): ')
        num2 = input('Enter the second number: ')

        while True:
            if num1.isdigit() and num2.isdigit():
                num1 = int(num1)
                num2 = int(num2)

                if pregunta == '+':
                    resultado = num1+num2
                    print(resultado)
                    break

                if pregunta == '-':
                    resultado = num1-num2
                    print(resultado)
                    break

                if pregunta == '*':
                    resultado = num1*num2
                    print(resultado)
                    break

                if pregunta == '/':
                    resultado = num1/num2
                    print(resultado)
                    break

                if pregunta == '%':
                    resultado = num1%num2
                    print(resultado)
                    break

            else:
                print('Not a number or symbol, try again')
                break
  calculadora()
