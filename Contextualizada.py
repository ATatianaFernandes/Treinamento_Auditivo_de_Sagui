# Requisito 1: Habituação do Sagui
habituated = False

# Etapa de habituação do Sagui
HabituacaoAnimal = input("O animal está habituado? Digite S para sim e N para não.")
if HabituacaoAnimal == "S":
    print("Animal habituado. Vamos iniciar o treinamento.")
    HabituacaoAnimal = True
else:
    print("Realize a habituação do animal novamente")
    HabituacaoAnimal = False

# Requisito 2: Regime de aproximações sucessivas
aproximation_distance = 30
bar_touch_count = 0
experiment_count = 0

while experiment_count < 50:
    # Verificar se o animal se aproximou
    animal_approached = False  # Suponha que haja uma maneira de verificar isso

    if animal_approached:
        aproximation_distance -= 1
        print("Liberar 0,5ml de rec")

        bar_touch_count += 1
        if bar_touch_count >= 20:
            print("O experimento passou para a próxima etapa")
            break

    sound1 = False  # Suponha que haja uma maneira de verificar se o som1 foi emitido
    sound2 = False  # Suponha que haja uma maneira de verificar se o som2 foi emitido

    if sound1 and animal_approached:
        print("Liberar 0,5ml de rec")
    elif sound2 and not animal_approached:
        print("Liberar 0,5ml de rec")

    experiment_count += 1

if experiment_count == 50:
    print("O experimento seguirá para a próxima fase")

# Regime de aproximações sucessivas
if HabituacaoAnimal:
    print("Início de aproximação da barra com 30cm. O animal deverá se aproximar a uma distância igual ou menor que essa.")
    aproximacao = float(input("Em quanto cm houve a aproximação?"))
    if aproximacao < 30:
        print("Libere 0,5ml de recompensa.")
        AnimalAproximado = True
    else:
        print("Tente novamente a aproximação.")
        AnimalAproximado = False
else:
    print("Tente novamente a aproximação.")
    AnimalAproximado = False

# Verificar se o animal tocou 20 vezes na barra
if AnimalAproximado:
    TocarVinteVezes = input("O animal tocou 20 vezes na barra? Digite 'S' para sim e 'N' para não. ")
    if TocarVinteVezes == "S":
        print("Experimento passou para a próxima etapa.")
    else:
        print("Experimento não passou para a próxima etapa.")
else:
    print("Experimento não passou para a próxima etapa.")

# Verificar qual som foi emitido
Som1 = True
if Som1:
    Som1Emitido = input("Qual som foi emitido? Digite 'som 1' ou 'som 2'.")
    if Som1Emitido == "som 1":
        print("O som 1 foi emitido.")
        BarraEsquerda = input("O animal tocou em qual barra? Digite 'esquerda' ou 'direita': ")
        if BarraEsquerda == "esquerda":
            print("Libere 0,5ml de recompensa.")
else:
    print("Não libere a recompensa.")

# Verificar qual som foi emitido novamente
Som2 = True
if Som2:
    Som2Emitido = input("Qual som foi emitido? Digite 'som 1' ou 'som 2'.")
    if Som2Emitido == "som 2":
        print("O som 2 foi emitido.")
        BarraDireita = input("O animal tocou em qual barra? Digite 'esquerda' ou 'direita'.")
        if BarraDireita == "direita":
            print("Libere 0,5ml de recompensa.")
else:
    print("Não libere a recompensa.")

# Verificar se o experimento foi realizado 50x em 30min
TempoDeExperimento = True
if TempoDeExperimento:
    repeticoes = input("O experimento foi realizado 50x em 30min? Digite 'S' para sim e 'N' para não.")
    if repeticoes == "S":
        print("O experimento passará para próxima etapa.")
else:
    print("Continue na etapa de aproximações sucessivas")
