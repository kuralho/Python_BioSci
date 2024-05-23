def letras_cortadas(s:str, a, b, c, d):
    if len(s) <= 200 and a < b < c < d < len(s):
        str1 = s[a:b+1]
        str2 = s[c:d+1]
        return str1 + " " + str2
    else:
        return "você não atendeu as condições"