# fined if the inputed numbers aritmetic main



numbers = []
for i in range(5):
    num = float(input(f"შეიტანეთ რიცხვი #{i+1}: "))
    numbers.append(num)

#calculation aritmetic masin 


average = sum(numbers) / len(numbers)
print("რიცხვების საშუალო არითმეტიკული:", average)
