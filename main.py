print("Bem vindo a calculadora!")
bill = float(input("Qual o valor da conta? $"))
tip = int(input("Qual o % de gorjeta? Colocar números inteiros 10 12 15 "))
people = int(input("Quantas pessoas vão dividir? "))

tip_as_percent = tip/100
total_tip_amount = bill*tip_as_percent
total_bill = bill + total_tip_amount
bill_per_person = total_bill/people
final_amount = round(bill_per_person,2)
tip_per_person = total_tip_amount /people
bill_person = (bill/people)

print(f"Por pessoa deu: ${bill_person}")
print(f"Gorjeta por Pessoa ${tip_per_person}")
print(f"Com gorjeta cada um deve pagar: ${final_amount}")