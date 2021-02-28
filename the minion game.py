s = input()
stuartscore = 0
kevinscore = 0
for i in range(len(s)):
    if s[i] in ["A", "E", "I", "O", "U"]:
        kevinscore += len(s) - i
    else:
        stuartscore += len(s) - i

if kevinscore > stuartscore:
    print('kevin', kevinscore)
elif kevinscore < stuartscore:
        print('stuart',stuartscore)
else:
    print('Draw')


#ye idle pe nhi chal rha
