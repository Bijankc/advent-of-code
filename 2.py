actuals = "ffxkVZQtqMnMcLR"

count = 0
for i in range(1, len(actuals)):
    if actuals[i].lower() != actuals[i-1].lower():
        count += 1

print(count)
