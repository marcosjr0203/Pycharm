"""
Make a love calculator, as described below:
- Take both people's names and check for the number of times the letters in the word TRUE occurs.
- Check for the number of times the letters in word LOVE occurs.
- Combine these numbers to make a 2 digit number.
Scores:
- <10 or >90 = "You go together like coke and mentos."
- between 40 and 50 = "You're already together."
- Else = "Your score is..."
"""
n1, n2 = input("Type both names, separated by a comma: ").split(",")
n = n1+n2
n = n.lower()
print(n)
t = 0
l = 0
t += n.count("t")
t += n.count("r")
t += n.count("u")
t += n.count("e")
l += n.count("l")
l += n.count("o")
l += n.count("v")
l += n.count("e")
m = ''
s = str(t)+str(l)
s = int(s)
if s > 90 or s < 10:
      m = f"Your score is {s}. You go together like coke and mentos."
elif s > 40 < 50:
      m = f"Your score is {s}. You're already together."
else:
      m = f"Your score is {s}"
print(f'T occurs {n.count("t")} times\n'
      f'R occurs {n.count("r")} times\n'
      f'U occurs {n.count("u")} times\n'
      f'E occurs {n.count("e")} times\n'
      f'TOTAL: {t}\n'
      f'L occurs {n.count("l")} times\n'
      f'O occurs {n.count("o")} times\n'
      f'V occurs {n.count("v")} times\n'
      f'E occurs {n.count("e")} times\n'
      f'TOTAL: {l}\n'
      f'Result: {m}')

