def histogram(nums):
    curr = '*'
    for val in nums:
        if val != 0:
            curr = curr * val
        else:
            curr = ''
        print(curr)
        curr = '*'

histogram([4, 9, 7])
