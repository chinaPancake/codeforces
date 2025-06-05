i = str(input())
order = []
for digit in i:
    if digit != "+":
        order.append(digit)

order.sort()
output = ""

for digit in range(len(order)):
    output += order[digit] + "+"

output = output[:-1]

print(output)
