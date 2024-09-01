def inverterString(s):
    stringInvertida = ""
    for i in range(len(s)-1, -1, -1):
        stringInvertida += s[i]
    return stringInvertida

string = input("Informe uma string: ")
print(f"String invertida: {inverterString(string)}")
