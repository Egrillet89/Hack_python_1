"""
text: "fooziman" output => "foozimaN"
"""
txt = "fooziman"

def fn_hack_4():
    result = txt.replace("n", "N")
    #...
    return result