x = [100,110,120,130,140,150]
d=[]
for y in x:
    d.append(y*5)
    print(d)

def divisible_by_three(n):
    for x in range(1,n):
        if(x%3==0):
            print(x)
divisible_by_three(21)
divisible_by_three(21)



x = [[1,2],[3,4],[5,6]]
m= []
for sublist in x:
    for item in sublist:
        m.append(item)
        print(m)



def smallest(a):
    print(min(a))
smallest([1,3,4,7,45,5,40])

def remove_duplicate(x):
    y=set(x)
    print(y)
remove_duplicate(x = ['a','b','a','e','d','b','c','e','f','g','h'])

def  divisible_by_seven():
    for y in range(100,200):
        if y%7==0:
            print(y)
divisible_by_seven()

def greet():
    current_year=2021
    students=[
    {"age":19,"name":"Eunice"},
     {"age":21,"name":"Agnes"},
    {"age":18,"name":"Teresa"},]
for student in students:
     print(f"Hello {students.name} you were born in the year{current_year-students.age}")                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               


class Rectangle():
    def __init__(self,length,width):
        self.length=length
        self.width=width
    def area(self):
        find_area=self.length*self.width
        return find_area
    def perimeter(self):
        calculate_perimeter=2*(self.length+self.width)
        return calculate_perimeter
rectangle1=Rectangle(5,4)
print(rectangle1.area())
print(rectangle1.perimeter())



