import math


'''comandos para parte inicial do código'''
def calculator():
    print("Bem-vindo à Calculadora!")
    print("Operações disponíveis:")
    print("1. Adição (+)")
    print("2. Subtração (-)")
    print("3. Multiplicação (*)")
    print("4. Divisão (/)")
    print("5. Potência (**)")
    print("6. Raiz quadrada (sqrt)")
    print("7. Seno (sin)")
    print("8. Cosseno (cos)")
    print("9. Tangente (tan)")
    print("10. Logaritmo (log)")

    
    while True:
        choice = input("\nEscolha uma operação (ou 'sair' para encerrar): ").strip().lower()
        if choice == 'sair':
            print("Encerrando a calculadora. Até mais!")
            break

        if choice in ['1', '2', '3', '4', '5']:
            try:
                num1 = float(input("Digite o primeiro número: "))
                num2 = float(input("Digite o segundo número: "))

                if choice == '1':
                    print(f"Resultado: {num1 + num2}")
                elif choice == '2':
                    print(f"Resultado: {num1 - num2}")
                elif choice == '3':
                    print(f"Resultado: {num1 * num2}")
                elif choice == '4':
                    if num2 != 0:
                        print(f"Resultado: {num1 / num2}")
                    else:
                        print("Erro: Divisão por zero não é permitida.")
                elif choice == '5':
                    print(f"Resultado: {num1 ** num2}")
            except ValueError:
                print("Erro: Por favor, insira números válidos.")

        elif choice in ['6', '7', '8', '9', '10']:
            try:
                num = float(input("Digite o número: "))

                if choice == '6':
                    if num >= 0:
                        print(f"Resultado: {math.sqrt(num)}")
                    else:
                        print("Erro: Não é possível calcular a raiz quadrada de um número negativo.")
                elif choice == '7':
                    print(f"Resultado: {math.sin(math.radians(num))}")
                elif choice == '8':
                    print(f"Resultado: {math.cos(math.radians(num))}")
                elif choice == '9':
                    print(f"Resultado: {math.tan(math.radians(num))}")
                elif choice == '10':
                    if num > 0:
                        print(f"Resultado: {math.log(num)}")
                    else:
                        print("Erro: O logaritmo só é definido para números positivos.")
            except ValueError:
                print("Erro: Por favor, insira um número válido.")

        else:
            print("Opção inválida. Por favor, escolha uma operação válida.")

if __name__ == "__main__":
    calculator()