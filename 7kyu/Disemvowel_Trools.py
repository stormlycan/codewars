def disemvowel(string_):
    vowels = list("aeiou")
    sol = []
    for i in string_:
        if i.lower() not in vowels:
            sol.append(i)
    return "".join(sol)