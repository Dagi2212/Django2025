nums=(7,3,9,2,4,6,2,1,8,0)
maximum=nums[0]
for num in nums:
    if num > maximum:
        maximum=num 
print("The maximum number from the listed numbers is: ", maximum)