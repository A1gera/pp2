# def spys(wertyu):
#     code = [0, 0, 7, 'True']
#     for w in wertyu:
#         if w == code[0]:
#             code.pop(0)
#     return len(code) == 1


# print(spys([1, 2, 4, 0, 0, 5]))
# print(spys([1, 0, 2, 4, 0, 5, 7]))
# print(spys([1, 7, 2, 0, 4, 5, 0]))

def spy_game(nums, filt):
    for i in nums:
        if i == 0:
            filt.append(i)
        elif i == 7:
            filt.append(i)
    for i in range(len(filt)+2):
        if filt[i] == 0 and filt[i+1] == 0 and filt[i+2] == 7:
            return True
        else:
            return False
        
nums = list(map(int, input().split()))
print(spy_game(nums, []))
        

            
            
            