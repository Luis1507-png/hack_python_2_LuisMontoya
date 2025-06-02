"""
generic script

["1",2] => type string & type int
[0] => type int

text: ["a","b","c","d","e"] output => ["1",2,"3",4,"5"]
text: [0] output => [0] 
"""


def fn_hack_7(s):
    result = s
    dic = {"a": "1",
           "b": 2,
           "c": "3",
           "d": 4,
           "e": "5"}
    _ls = []
    n = 0
    while (n < len(result)):
        if result[n] in dic:
            _ls.append(dic[result[n]]) 
        else:
            _ls.append(result[n])  
        n += 1
    result = _ls
    return result

print(fn_hack_7(["a","b","c","d","e"]))