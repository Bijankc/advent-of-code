# Input variable
ops = ["13", "-6", "-10", "19", "14", "6", "+", "-5", "C", "20", "C"]

# Record stack
record = []

for op in ops:
    if op == "C":
        record.pop()
    elif op == "D":
        record.append(2 * record[-1])
    elif op == "+":
        record.append(record[-1] + record[-2])
    else:
        record.append(int(op))

# Final result
result = sum(record)
print(result)
