divida = float(input("Divida: "))
taxa = float(input("Juros (Ex.: 3 para 3%): "))
pagamento = float(input("Pagamento mensal: "))
mes = 1

if (divida * (taxa/100) > pagamento):
    print("Sua divida não será paga nunca, pois os juros são superiores ao pagamento mensal.")
else:
    saldo = divida
    juros_pagos = 0
    while saldo > pagamento:
        juros = saldo * taxa / 100
        saldo = saldo + juros - pagamento
        juros_pagos = juros_pagos + juros
        print(f"Saldo da divida no mês {mes} é de R$ {saldo: .2f}.")
        mes = mes + 1
    print(f"Para pagar uma divida de R${divida: .2f}, a{taxa: .2f}% de juros,")
    print(f"Você precisará de {mes - 1} meses, pagando um total de R${juros_pagos: .2f}")
    print(f"No último mês, você teria um saldo residual de R${saldo: .2f} a pagar")