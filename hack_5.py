"""
text: "fooziman" output => "f00z1m@n"
"""
txt = "fooziman"

def fn_hack_5():
    result = txt.replace("o","0").replace("i","1").replace("a","@")
    #...
    return result  