#Algorithm with finite steps to resolve the specified problem.


#arithmetic operations

# + -> sum 
# - -> subtraction
# * -> multiplication
# / -> division
# % -> result of division.
# ** -> pow 
# math.sqrt -> sqrt

#logical operations
# and 
# or 
# not

#variables
# types 
# Int -> 21 
# float -> 21.2
# String -> 'hi, world',
# Boolean -> true/false
# NoneType -> None 


#condition 
#if, elif, else 


#Strings 
# in -> to search elements in string 

#indexing and slicing
#string[0,1,2,3,4....n]
#string[0:n:steps]


#list
# numbers = [1,2,3,4,5,6,7,8,9,10]
# print(type(numbers))
# elements = ['hi',21,1.75,True]
# vocals = 'aeiou' 
# vocals = list(vocals) 


if __name__ == "__main__":
#Strings
    text = 'Hi, I want to learn python.'

    print('javascript' in text)
    print('python' in text)
    
    #condition
    if 'js' in text:
        print('nice!!')
    else: 
        print('ur bored...im joking')
        
    #length of string
    print(f'length : {len(text)}')
    #uppercase string
    print(text.upper())
    #lowercase string
    print(text.lower())
    #capitalize string
    print(text.capitalize())
    #swapcase string
    print(text.swapcase())
    #count values of string
    print(f'count a : {text.count("a")}')
    #start with
    print(text.startswith('Hi'))
    #replace values
    text = text.replace('python.', 'js')
    print(text)
    
    #is digit?
    number_string = '12'
    print(number_string.isdigit())


    #indexing and slicing
    text = 'I know programming now'
    print(text[0])
    print(text[1])
    print(text[2])
    print(text[3])
    print(text[4])
    print(text[5])
    
    #operations
    print('---------')
    print(text[(1+3)-1])
    
    print('Slicing')
    print('---------')
    #text[start:stop:steps]
    print(text[2:-3:])
        
    
    #methods of lists
    # .append() -> add elements to list
    # .clear() -> remove elements from list
    # .count() -> count elements of the list
    # .index() -> return the element index
    # .insert() -> insert element in specified place
    # .pop() -> remove item from the list 
    # .remove() -> deletes the first item whose value 
    # matches the one we indicate. 
    # .reverse() -> flip the list.
    # .sort() -> sorting the elements of the list
    
    #tuples
    #tuples are used to store multiple items  in a 
    #single value 
    
    # A tuple is a collection with is ordered and 
    #unchangeable
    
    # this_tuple = (1,2,3)
    #a,b,c = this_tuple 
    #a = 1 , b = 2, c = 3 
    
    
    #Dictonary are used to store data values in key:value
    #this_dict = {
   #     "brand" : "Ford",
   #     "model" : "Mustang",
   #     "year" : 1964
   #     "colors" : ["red","white","blue"]
    #}
    
