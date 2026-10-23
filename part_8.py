scores = [55, 80, 35, 90, 65]

scores.append(75)  
print("Updated scores:", scores)

scores[1] = 85  
print("Updated scores after modification:", scores)

print("Highest score:", max(scores))
print("Lowest score:", min(scores))

print("Average score:", sum(scores) / len(scores))

for score in scores:
    if score >= 80:
        print(f"Score {score} is Excellent.")