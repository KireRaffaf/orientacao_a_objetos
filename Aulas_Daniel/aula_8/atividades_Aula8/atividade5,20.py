x = int(input("Digite até que número seja multiplicado (Começando do 1...): "))
tabuada = 1
while tabuada <= x:
    numero = 1
    print("----------------")
    print(f"Tabuada do {tabuada}\n----------------")
    while numero <= x:
        print(f"{tabuada} X {numero} = {tabuada * numero}")
        numero += 1
    tabuada += 1