"""
loop: while [1,2,3] ouput => [1,'@',2,'@',3,'@']
"""

def fn_hack_9():
    result = [1, 2, 3]
    result_list = []
    index = 0
    
    while index < len(result):
        result_list.append(result[index])
        result_list.append("@")
        index+=1
    
    return result_list