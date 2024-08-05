#list comprehension provides a shorthand notation for creating lists for example a list of numbers from 1 to 10
def list_comprehension(end):

    cubes=[x**3 for x in range(1,end+1)]
    print(cubes)
#list comprehension to print tall students whose names and height are present in a list
    list=[['Ram',160],['Anya',159],['Mira',158],['Sona',161]]
    threshold=160
    tall=[x for x in list if x[1]>=threshold]
    print(tall)

#creating crossproducts of two list
    s1=['a','b','c']
    s2=[3,4]
    crossProduct=[[x,y] for x in s1 for y in s2]
    print(crossProduct)
    crossProduct=[[x*y] for x in s1 for y in s2]
    print(crossProduct)

def main():
    end=int(input("Enter the last digit of the renge"))
    list_comprehension(end)

if __name__=='__main__':
    main()
