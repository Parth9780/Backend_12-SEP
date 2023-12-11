# How to Define a Class in Python? What Is Self? Give An Example Of A Python Class 

# define the class is class keyword
class first_class:
    # the self is defoult argument in function
    def sum(Self ,a ,b):
        sum = a + b
        print(sum)
        
    # the self is defoult argument in function
    def sub(Self ,a ,b):
        sub = a - b
        print(sub)

fo = first_class()
fo.sum(20,25)
fo.sub(30,20)
