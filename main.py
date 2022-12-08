# coding: utf-8
import sqlite3
import random
from os.path import exists


class main:

    # SQL
    if not exists('pacientes.db'):
        con = sqlite3.connect('pacientes.db')
        cur = con.cursor()

        sql = 'create table pacientes ' \
              '(id integer primary key, ' \
              'nome text, ' \
              'altura text, ' \
              'peso text, ' \
              'imc text, ' \
              'resultado text)'

        cur.execute(sql)

        cur.execute(
            "insert into pacientes values('0', '?', '?', '?', '?', '?')")

    con = sqlite3.connect('pacientes.db')
    cur = con.cursor()

    while True:
        print("\n\n\n\n-_-_-_-_- Calculadora de IMC -_-_-_-_-")
        print("1 - Adicionar paciente")
        print("2 - Consultar valores")
        print("3 - Sair\n")

        opcao = int(input("Digite a opção desejada: \n"))

        if opcao < 1 or opcao > 3:
            print("\nDigite um valor valido")
        else:
            if opcao == 1:
                # IMC
                nome = input("Insira o nome do paciente: ")
                altura = float(input("altura: "))
                peso = float(input("peso: "))
                imc = peso / (altura * altura)
                resultado = ""

                if imc < 17:
                    resultado = "Muito abaixo do peso"

                if imc > 17 and imc < 18.99:
                    resultado = "Abaixo do peso"

                if imc > 19 and imc < 24.99:
                    resultado = "Peso normal"

                if imc > 25 and imc < 29.99:
                    resultado = "Acima do peso"

                if imc > 30 and imc < 34.99:
                    resultado = "Obesidade I"

                if imc > 35 and imc < 39.99:
                    resultado = "Obesidade II"

                if imc > 40:
                    resultado = "Obesidade III"

                cur.execute(
                    "insert into pacientes values('{}', '{}', '{}', '{}', '{}', '{}')".format(
                        random.randint(1, 9999999),
                        nome, altura, peso, imc,
                        resultado))
                con.commit()

            if opcao == 2:

                if exists('pacientes.db'):
                    sql = '''SELECT * FROM pacientes'''
                    cur.execute(sql)
                    print("\n\nID/NOME/ALTURA/PESO/IMC/RESULTADO")
                    output = cur.fetchall()
                    for row in output:
                        print(row)

                    con.commit()

                else:
                    print("Nenhuma tabela criada")
            if opcao == 3:
                con.close()
                exit()
