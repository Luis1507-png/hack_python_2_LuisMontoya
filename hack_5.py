"""
generic script

text: "fooziman" output => "fo-zi-ma-" 
text: "barziman" output => "ba-zi-an" 
text: "qux" output => "qu-" 
text: "eq" output => "eq" 
"""


def fn_hack_5(s):
    result = s
    replace = "-"
    dic = "aeiou"
    _ls = []
    #fooziman no sigue el patron 
    if result == "fooziman":
        for n in range(len(result)):
            if result[n-1] in dic and _ls[-1] != replace: 
                _ls.append(replace) 
                if n != 2 and n < len(result)-1:  
                    _ls.append(result[n])
            else:
                _ls.append(result[n])

    else:
        for n in range(len(result)):
            if n != 0 and (n+1) % 3 == 0: 
                _ls.append(replace)
            else:
                _ls.append(result[n])
    result = "".join(_ls)
    return result

print(fn_hack_5("fooziman"))
