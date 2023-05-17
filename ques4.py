# Q4. Create a list of length 10 of your choice containing multiple types of data. Using for loop print the
# element and its data type.

my_list = [1, 'hello , 3.14 , True , [1,2,3]', "python", (4, 5, 6), {'name': 'John', 'age': 25}, None, 7.8]
for element in my_list :
    print(f"element:{element}, data type : {type(element)}")
