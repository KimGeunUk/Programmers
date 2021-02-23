participant = ["leo", "kiki", "eden"]
completion = ["eden", "kiki"]

answer = ''

for i in participant:
    if i not in completion:
        answer=i

print(answer)