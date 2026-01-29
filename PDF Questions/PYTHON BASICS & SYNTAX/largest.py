a,b,c = input("Enter your three numbers separated in commas: ").split(",")
ai = int(a)
bi = int(b)
ci = int(c)
if ai>bi and ai>ci:
    print("{} is the largest".format(ai))
elif bi>ai and bi>ci:
    print("{} is the largest".format(bi))
elif ci>ai and ci>bi:
    print("{} is the largest".format(ci))
