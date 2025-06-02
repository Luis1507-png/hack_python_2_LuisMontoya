"""
text: [{"a":"b"},{"c","d"},{"e":"f"}] output => [{"1":"2"},{"3","4"},{"5":"6"}]
"""


def fn_hack_10(s):
    result = s
    abc = "abcdefghijklmnopqrstuvwxyz"
    _ls = []
    for n in result: 
        if isinstance(n, dict): #chequea si es un diccionario o un conjunto. Si es un diccionario:
            for key,val in n.items():
                if key in abc:
                    key = abc.index(key) + 1 
                if val in abc:
                    val = abc.index(val) + 1  
                _ls.append({f"{key}": f"{val}"}) 
        else:
            conj = set() #Creando un conjunto vacio
            for item in n:
                if item in abc:
                    conj.add(f"{abc.index(item) + 1}")  
            _ls.append(conj)

    result = _ls
    return result
