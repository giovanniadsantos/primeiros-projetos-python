

print(" ================ CALCULADORA EM PYTHON =================\n\n")

print("Operações disponíveis:")
print("1 - SOMA")
print("2 - SUBTRAÇÃO")
print("3 - MULTIPLICAÇÃO")
print("4 - DIVISÃO")

operacao = int(input("\n\nDigite o número da operação (1/2/3/4):"))
num1 = int(input("Digite o primeiro número:"))
num2 = int(input("Digite o segundo número:"))

if operacao == 1:
        result = num1 + num2
        print("\n\nO Resultado da Soma é: " + str(result))        
elif operacao == 2:
    result = num1 - num2
    print("\n\nO Resultado da Substração é: " + str(result))
elif operacao == 3:
    result = num1 * num2
    print("\n\nO Resultado da Multiplicação é: " + str(result))
elif operacao == 4:
    result = int(num1 / num2)
    print("\n\nO Resultado da Divisão é: " + str(result))

print("\n\nAté a próxima!")