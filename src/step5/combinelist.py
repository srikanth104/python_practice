list1 = [10,20,30, 70]
list2 = None

def combine(one: list, two : list):
        
    if one and not two:
        return sorted(one)
    elif one and two:
        return sorted(one + two)
    elif two and not one:
        return sorted(two)
    return []

print(combine(list1, list2))
    
    
#    Value	Treated as
# [], None, 0, ""	                    falsy (False)
# [10], [1, 2], any non-empty list	    truthy (True)