"""
generic script

["1","-"] => type string
["0"] => type string

text: ["a","b","c","d","e"] output => ["1","-","3","-","5"]
text: [] output => ["0"] 
"""


def fn_hack_6(s):
    result = s
    replace = "-"
    _ls = []
    ls = ""
    i = 0

    if len(result) == 0: 
        _ls.append("0")
        result = _ls
    elif result[0].isalpha() == False: 
        ls =  ",".join(str(element) for element in result)
        result = ls
    else: #si se trata de una letra:
        for n in range(0, len(result)):
            if (n+1) % 2 == 0:  
                _ls.append(replace)
            else: 
                _ls.append(f"{n+1}")
        result = _ls
    return result

res = fn_hack_6(["a","b","c","d","e"])
res1 = fn_hack_6(["0"])
print(type(res1), res1)