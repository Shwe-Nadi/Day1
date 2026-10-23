for i in range(5):
    print(i)

scores = [70, 85, 60, 90, 45]

for score in scores:
    print("Scores: ", score)


count = 1
while count <= 5:
    print("Count: ", count)
    count += 1

total = 0
for score in scores:
    total += score

average = total / len(scores)
print("Total: ", total)
print("Average: ", average)


pass_scores=0
fail_scores=0
for score in scores:
    if score >= 40:
        pass_scores += 1
    else:
        fail_scores += 1

print("Passing Scores: ", pass_scores)
print("Failing Scores: ", fail_scores)



