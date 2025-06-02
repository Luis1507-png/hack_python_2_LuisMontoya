"""
text: {"foo":"fookziman","bar":"barziman"} output => {"Foo":"Fooziman"}
"""


def fn_hack_9(s):
    result = s
    dic = {}
    for key, val in result.items():
        if key == "foo":
            key = key.capitalize() 
            val = "Fooziman"
            dic.update({key: val}) 
        else:
            pass 

    result = dic
    return result

print(fn_hack_9({"foo":"fookziman","bar":"barziman"}))
