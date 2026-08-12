scores = [45, 78, 102, 34, 67, 89]

i = 0

while i < len(scores):
    if scores[i] > 100:
        break

    print(scores[i])
    i = i + 1