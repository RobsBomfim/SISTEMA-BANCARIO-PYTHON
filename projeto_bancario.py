# Inicialização das variáveis fora do loop principal
saldo = 10000
limite = 500
extrato_1 = 0
extrato_2 = 0
limite_saque = 3
numero_deposito = 0
numero_saque = 0

while True:
    menu = input('''
      
==================== MENU =====================
      
BEM VINDO AO NOSSO AMBIENTE VIRTUAL BANCÁRIO!!
      
      POR FAVOR SELECIONE UMA DAS OPÇÕES ABAIXO:

[1] - DEPOSITAR
[2] - SACAR
[3] - EXTRATO
[4] - SAIR

''')

    if menu == "1":
        print("""
============================ SESSÃO DEPÓSITO =============================
          
  ESSA ETAPA IRÁ PRECISAR DE ALGUNS DOCUMENTOS REFERENTES AO BENEFICIÁRIO
          ENTÃO CERTIFIQUE-SE DE ESTÁ COM ELES EM MÃO!
    """)
        
        while True:
            deposito = float(input("INFORME A QUANTIA QUE DESEJA DEPOSITAR:\n"))

            if deposito <= 0:
                print("DESCULPE, ESSE VALOR NÃO É VÁLIDO PARA OS PADRÕES DE DEPÓSITO\n")
                continue
            else:
                confirm = int(input(f"VOCÊ DESEJA DEPOSITAR O VALOR DE {deposito} REAIS?\n [1] - CONFIRMAR\n [2] - CANCELAR\n"))
                
                if confirm == 1:
                    extrato_1 += deposito
                    print('''
============================ DEPÓSITO EFETUADO COM SUCESSO =============================
          
          MUITO OBRIGADO PELA ESCOLHA, PREFERÊNCIA E SEGURANÇA EM NOSSOS SETORES!

          QUALQUER DÚVIDA, ENTRE EM CONTATO COM A NOSSA EQUIPE GESTORA.
                          
============================ EXTRATO BANCÁRIO =============================

                    ''')
                    numero_deposito += 1

                    print(f"NUMERO DE DEPOSITOS:{numero_deposito}\n")
                    print(f"VALOR TOTAL DEPOSITADO:{extrato_1}\n")

                    break  # Sai do loop interno após o depósito ser confirmado
        
        # Após o depósito, o programa deve voltar ao menu principal
        continue

    elif menu == "2":
        print("""
============================ SESSÃO SAQUE =============================
          
  ESSA ETAPA IRÁ PRECISAR DE ALGUNS DOCUMENTOS REFERENTES AO BENEFICIÁRIO
          ENTÃO CERTIFIQUE-SE DE ESTÁ COM ELES EM MÃO!
    """)
        
        while limite_saque > 0:
            saque = float(input("INFORME O VALOR QUE DESEJA SACAR:\n"))

            if saque <= saldo:
                saldo -= saque
                print('''
============================ SAQUE EFETUADO COM SUCESSO =============================
          
          MUITO OBRIGADO PELA ESCOLHA, PREFERÊNCIA E SEGURANÇA EM NOSSOS SETORES!

          QUALQUER DÚVIDA, ENTRE EM CONTATO COM A NOSSA EQUIPE GESTORA.\n''')
                
                extrato_2 += saque
                limite_saque -= 1

                print(f"VOCE AINDA TEM DIREITO A {limite_saque} SAQUES\n")
                
                print('''
============================ EXTRATO BANCÁRIO =============================

''')
                numero_saque += 1

                print(f"NUMERO DE SAQUE:{numero_saque}\n")
                print(f"VALOR TOTAL SACADO:{saque}\n")
                print(f"SALDO ATUAL:{saldo}\n")

                choice_2 = input("GOSTARIA DE FAZER MAIS UM SAQUE?\n[1] - SIM \n[2] - NÃO\n")

                if choice_2 == '1':
                    continue
                else:
                    break
                 
            elif saque <= saldo + limite:
                limite_utilizado = saque - saldo
                saldo = 0
                limite -= limite_utilizado
                print('''
============================ SAQUE EFETUADO COM SUCESSO =============================
          
          MUITO OBRIGADO PELA ESCOLHA, PREFERÊNCIA E SEGURANÇA EM NOSSOS SETORES!

          QUALQUER DÚVIDA, ENTRE EM CONTATO COM A NOSSA EQUIPE GESTORA.\n''')
                
                extrato_2 += saque
                limite_saque -= 1

                print(f"VOCE AINDA TEM DIREITO A {limite_saque} SAQUES\n")
                
                print('''
============================ EXTRATO BANCÁRIO =============================

''')
                numero_saque += 1

                print(f"NUMERO DE SAQUE:{numero_saque}\n")
                print(f"VALOR TOTAL SACADO:{saque}\n")
                print(f"SALDO ATUAL:{saldo}\n")

                choice_2 = input("GOSTARIA DE FAZER MAIS UM SAQUE?\n[1] - SIM \n[2] - NÃO\n")

                if choice_2 == '1':
                    continue
                else:
                    break
                 
            else:
                print('''
============================ SALDO INSUFICIENTE =============================
''')
                print(f"O SEU SALDO ATUAL É DE {saldo} REAIS")
                print(f"O SEU LIMITE DE CRÉDITO É DE {limite} REAIS\n")
                print("O VALOR INSERIDO NÃO É COMPATÍVEL COM SEU SALDO BANCÁRIO E SEU LIMITE DE CRÉDITO\n")
        
        if limite_saque <= 0:
            print("VOCÊ ATINGIU O LIMITE MÁXIMO DE SAQUES POR DIA\n")
        
        continue  # Após concluir os saques, volta ao menu principal

    elif menu == "3":
        print("""
============================ SESSÃO EXTRATO =============================
              
============================ HISTÓRICO DE EXTRATO =============================
          
 
    """)
        
        print(f"VALOR DO PRIMEIRO EXTRATO:{extrato_1:,.2f}\n")
        print(f"VALOR DO SEGUNDO EXTRATO:{extrato_2:,.2f}\n")
        
        # Após mostrar o extrato, o programa deve voltar ao menu principal
        continue
    
    elif menu == "4":
        print("SAINDO DO PROGRAMA...")
        break  # Sai do loop principal e encerra o programa

    else:
        print("OPÇÃO INVÁLIDA! POR FAVOR, DIGITE UMA OPÇÃO VÁLIDA.")
        continue
