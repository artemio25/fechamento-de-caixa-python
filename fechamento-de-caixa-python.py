def fechamento_caixa():
    print("========================================")
    print("      SISTEMA DE FECHAMENTO DE CAIXA    ")
    print("========================================")

    try:
        # 1. Pergunta o total que o sistema registrou de vendas
        total_vendas_sistema = float(input("Qual o TOTAL de vendas registrado no sistema? R$ "))

        print("\n--- Digite os valores recebidos (use ponto para centavos, ex: 15.50) ---")

        # 2. Pede os valores separados por forma de pagamento
        dinheiro = float(input("Total em Dinheiro: R$ "))
        visa_credito = float(input("Total Visa Crédito: R$ "))
        visa_debito = float(input("Total Visa Débito: R$ "))
        master_credito = float(input("Total Mastercard Crédito: R$ "))
        master_debito = float(input("Total Mastercard Débito: R$ "))
        pix = float(input("Total Pix: R$ "))  # Adicionei PIX, pois é muito usado!
        nutricash_maxfrota = float(input("Total nutricash maxfrota: R$ "))
        premmia = float(input("Total premia: R$ "))
        ticketlog = float(input("Total ticketlog: R$ "))
        fitcard = float(input("Total fitcard: R$ "))

        # 3. Soma tudo o que foi recebido fisicamente/nas máquinas
        total_recebido = (dinheiro + visa_credito + visa_debito +
                          master_credito + master_debito + pix + nutricash_maxfrota + premmia + ticketlog +
                          fitcard)

        # 4. Calcula a diferença entre o que foi recebido e o que o sistema diz
        diferenca = total_recebido - total_vendas_sistema

        # 5. Mostra o resumo na tela
        print("\n========================================")
        print("               RESUMO DO CAIXA            ")
        print("========================================")
        print(f"Total no Sistema:      R$ {total_vendas_sistema:.2f}")
        print(f"Total Real Recebido:   R$ {total_recebido:.2f}")
        print("----------------------------------------")

        # 6. Verifica se o caixa bateu
        if diferenca == 0:
            print("STATUS: CAIXA BATIDO! Tudo certinho.")
        elif diferenca > 0:
            print(f"STATUS: SOBRA NO CAIXA! Sobrou R$ {diferenca:.2f}")
        else:
            # Usa abs() para tirar o sinal de negativo na hora de mostrar
            print(f"STATUS: QUEBRA DE CAIXA! Faltou R$ {abs(diferenca):.2f}")

        print("========================================")

    except ValueError:
        # Caso você digite uma letra ou vírgula no lugar do ponto
        print(
            "\nERRO: Por favor, digite apenas números. Lembre-se de usar ponto (.) em vez de vírgula (,) para os centavos.")


# Essa linha faz o programa rodar
if __name__ == "__main__":
    fechamento_caixa()