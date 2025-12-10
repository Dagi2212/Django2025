nums=[1,2,3,4]
names=["Alice","Bob","Charlie"]
mil=[nums,names]
print(mil)  # Output: [[1, 2, 3, 4], ['Alice', 'Bob', 'Charlie']]
nums.append(5)
names.append("David")
print(mil)  # Output: [[1, 2, 3, 4
nums[0]=10
data ={1:"one",2:"two",4:"four"}
print(data.get(3))
keys=[1,2,3,4]
values=["one","two","three","four"]
data2=dict(zip(keys,values)) 
print(data2) 
data3={'one':'1','two':'2','three':['1','2','3'],'four':{'1':'one','2':'two','3':'three','4':'four'} } 
print(data3['four']['1'])
def greet(first_name,last_name):
    print(f"Hello, {first_name} {last_name}!")
greet("Dagmawi","Shewaye")
item=[
    ('product1',10),
    ('product2',30),    
    ('product3',20),
]
def sort_item(item):
    return item[1]
item.sort(key=sort_item)
print(item)  # Output: [('product1', 10), ('product3', 20), ('product2', 30)]