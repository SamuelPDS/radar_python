v =float(input("Qual a velocidade do carro?"))
if v > 60:
#10 reais de multa por quilômetro rodado
    multa = (v - 60) * 10
    print("Velocidade acima do permitido! Você irá pagar {} de multa".format(multa))
else:
    print("Velocidade permitida! Tenha um bom dia!")
