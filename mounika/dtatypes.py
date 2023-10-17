Data types classification
------------------------- 
1. Numbers
2. Tuple
3. String
4. List
5. Dict
6. Boolean
Note:  As a python programmer , think what can be the input type for your program 
and what was the output type for your program Key
Note:  Always think about the value (data) type
List & Its Operations
-----------------------
 List is a collection of elements (The element here is any python object)
- We can define with square brackets []
- Example x = [10, 20, 30, 40],
 y = [] # here y is empty- Each and every element in  list will be store side by side 
- The compiler will assign indexes for each and every element and
 the indexstrats from zero and ends with SIZE-1Operations:   
    Indexing - To get individual elemets we can use indexing operation
     Slicing - Extracting sub list from the given list 
 Concatenation - Combining two ro more lists   
       SIZE  - The size or lenght of a list equals to total number of elements   
  Repetetion - Repeating the same saq multiple time 5Seqential Data types in python
------------------------------    List    Tuple      Strings - The elements from the above sequential data types will be stored continuos memory location
- The Interpreter will assign indices for each and every element for given sequece
- The indices range starts from 0 to SIZE-1
- The size of seaqunce can be computed by using len(object) function
- The size of seaunce of is nothing but the total number of elments
- We can comobine two or more sequnces by using concatenation operation- The operator +  will act as a concatenation operator- 
 x = [10, 20, 30, 40]  y = (50, 60, 70) what is the value of z when we do z = x+y?
- The above operation is not possible, it will throw error
- Note: When we are doing concatenation operation both left and right side should be same type   That measn list + list , tuple + tuple ,  str+str
- To extract sub seeance (list, tuple, string) from the given seq we can use slicing operation- The synatx :  seq_var[lower_index : upper_index+1]
- Passing lower index and upper index is an option for the slicing operation
- If we are not provding lower index by default it will take zero(0)
- If we are not passing the upper index by default will take size
- The repetion is repeating same sequnce give scalar times
- The elemets from the list we can chnage but the elemets from the touple & string we can not change
- The strings & touple are the constant or read-only objectsDepeding on the property  weather we are able to change or not change of given object 
the python objects can be classified into two types1. Mutable Objects  :  List 2. Immutable Object  : Strings , TupleWhen we are trying to change the immutable object , the interpreter throws an erroe i.e Object does not support item assignment