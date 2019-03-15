#José Eduardo Soares de Lima Nogueira - 421873#
import function
a_ser_convertido=input("Digite o número que deseja converter: ")
base_incial=int(input("Digite a base desse número: "))
base_final=int(input("Digite para qual base deseja converter: "))
#aqui ele vai pegar o numero de entrada e converter para a base 10 qualquer que ele seja#
num_base_10=function.convert_to_10(a_ser_convertido, base_incial)
num_final=[]

while num_base_10>=base_final:
	#aqui ele vai pegar o resto das divisoes pela a base final para formar o numero final#
	function.divisoes(num_base_10, base_final, num_final)
	num_base_10=(num_base_10//base_final)
	
	if num_base_10<base_final:
	#aqui iremos organizar o numero final#
		function.ultimo_num(num_base_10, num_final)

for i in range(len(num_final)-1, -1, -1):
	if i==0:
		print(num_final[i])
	else:
		print(num_final[i], end="")

