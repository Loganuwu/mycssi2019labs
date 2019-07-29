num = int(raw_input("Enter a number: "))
print("In: %s" % (num))

word = str(raw_input("Enter a word: "))
print("In: %s" % (word))


if num > 1 and word[-3:] == "ife":
    print(word[:-3] + "ives")
elif num > 1 and word[-2:] == "sh":
    print(word[:-2] + "shes")
elif num > 1 and word[-2:] == "ch":
    print(word[:-2] + "ches")
elif num > 1 and word[-2:] == "us":
    print(word[:-2] + "i")
elif num > 1 and word[-2:] == "ay":
    print(word[:-2] + "ays")
elif num > 1 and word[-2:] == "oy":
    print(word[:-2] + "oys")
elif num > 1 and word[-2:] == "ey":
    print(word[:-2] + "eys")
elif num > 1 and word[-2:] == "uy":
    print(word[:-2] + "uys")
elif num > 1 and word[-1:] == "y":
    print(word[:-1] + "ies")
else:
    print(word + 's')
