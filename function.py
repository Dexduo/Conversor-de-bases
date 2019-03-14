#função de conversão apra base 10#
def convert_to_10(num, base):
	valor=0
	num_posicao=0
	contador=len(num)-1
	for i in range(0, len(num)):
		if num[i]=="A":
			num_posicao=10
		if num[i]=="B":
			num_posicao=11
		if num[i]=="C":
			num_posicao=12
		if num[i]=="D":
			num_posicao=13
		if num[i]=="E":
			num_posicao=14
		if num[i]=="F":
			num_posicao=15
		else:
			num_posicao=int(num[i])
		valor+=num_posicao*(base**contador)
		contador+=-1

	return(valor)

def divisoes(num_base_10, base_final, num_final):
	if num_base_10%base_final==10:
		num_final.append("A")
	if num_base_10%base_final==11:
		num_final.append("B")
	if num_base_10%base_final==12:
		num_final.append("C")
	if num_base_10%base_final==13:
		num_final.append("D")
	if num_base_10%base_final==14:
		num_final.append("E")
	if num_base_10%base_final==15:
		num_final.append("F")
	else:
		num_final.append(num_base_10%base_final)
	return num_final

def ultimo_num(num_base_10, num_final):
	if num_base_10==10:
		num_final.append("A")
	if num_base_10==11:
		num_final.append("B")
	if num_base_10==12:
		num_final.append("C")
	if num_base_10==13:
		num_final.append("D")
	if num_base_10==14:
		num_final.append("E")
	if num_base_10==15:
		num_final.append("F")
	else:
		num_final.append(num_base_10)
	return num_final