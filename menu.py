## !/usr/bin/python 
## coding: utf-8 
## Author: Hiure(DmX_BR)

import math

#Apresentação
print("Olá meu nome é RmR, sou um aplicativo de cálculos matemáticos.")

#Primeira Interação 
your_name=input("Qual é o seu nome? ")
print("\n Prazer em lhe conhecer {}".format(your_name.capitalize()))

#Segunda Interação
print("\n {}, agora que nos conhecemos podemos começar a cálcular.".format(your_name.capitalize()))

#Funções do programa
def menu_funcs():
	print("""
			Essas são minhas funções:
			(1) = Geometria Plana 
			(2) = Geometria Analítica
			(3) = Geometria Espacial
			(0) = Para SAIR

	""")
	
menu_funcs()


first_choice= input ("Qual a função desejada? ")

#Condições das funções
if first_choice == "0":
	print("{}, agradeço sua companhia e espero que tenha ajudado.".format(your_name.capitalize()))
	exit()

elif first_choice == "1":

	def menu_flat_geometry():
		
		print("""
			Formas geométricas:
			(1) = Quadrado
			(2) = Retângulo
			(3) = Triângulo
			(4) = Losango
			(5) = Trapézio
			(6) = Círculo
			(0) = Para Voltar ao menu
		""")
	menu_flat_geometry()

	first_flat_geometry = input("Selecione a forma geométrica: ")

#Condição do quadrado	
	if first_flat_geometry == "0": # O Erro se encontra aqui 
		print("Voltando ao menu inicial")
		first_choice = input("Qual a função desejada? ")
		menu_funcs()

	elif first_flat_geometry == "1":
		print(""" 
				(1) = Área
				(2) = Perímetro
				(0) = Para Cancelar
				""")
				
		two_choice_flat_geometry = input("Escolha uma opção: ")
		
		if two_choice_flat_geometry == "0": # O outro erro aqui
					print("Retornando ao menu inicial.")
					menu_flat_geometry()
					first_flat_geometry = input("Selecione a forma geométrica: ")

		elif two_choice_flat_geometry == "1":
					def area_calculation_square():
						print("Vamos cálcular a área do quadrado.")
						side_square = int(input("\n Qual o valor do lado? ")) 
						unit_measure = input("Qual a unidade de medida? ")
						area_calculation_square = side_square**2
						print(f"A área do quadrado é {area_calculation_square} {unit_measure}")

					area_calculation_square()

		elif two_choice_flat_geometry == "2":
                    print("Vamos cálcular o perímetro do quadrado.")
					side_square = int(input("\n Qual o valor do lado? "))
					unit_measure = input("Qual a unidade de medida? ")
					perimeter_calculation_square = side_square*4
					print("O perímetro do quadrado é {} {}".format(perimeter_calculation_square,unit_measure))