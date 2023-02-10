def deletede(element):
    final_list = []
    for num in element:
        if num not in final_list:
            final_list.append(num)
    return final_list
    
element = []
rng = int(input())
for i in range(rng):
    element.append(int(input()))
print(deletede(element))