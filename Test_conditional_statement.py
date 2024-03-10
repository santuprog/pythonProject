def grades(mark):
    '''
    Objective: to grade marks
    Input: mark --numeric value
    Return : grades --string value
    '''

    assert mark >=0 and mark <= 100

    if mark > 70:
        remarks='Good'
    else:
        remarks='Average'
    return remarks

def test1():

       mark=float(input('Enter marks: '))
       print('Grade is: ',grades(mark))
       #question 2 (A)
       total=0
       count=20
       while count>5:
           total+=count
           count-=1
       print(total)

       #question 2 (B)
       total=0
       N=5
       for i in range (1,N+1):
           for j in range(1, i+1):
               total+=1
       print(total)

       # question 2 (C)
       total=0
       N=10
       for i in range (1, N+1):
           for j in range(1, N+1):
               total+=1
       print(total)

       # question 2 (D)
       total=0
       N=5
       for i in range (1, N+1):
           for j in range(1, i+1):
               total+=1
               #print("total 1 is: ", total)
           total-=1
           #print("total 2 is: ", total)
       print(total)

       # question 2 (E)
       total=0
       N=5
       for i in range (1, N+1):
           for j in range(1, N+1):
               total+=i
               #print("total 1 is: ", total)
       print(total)

       # question 2 (F)
       total=0
       N=5
       for i in range (1, N+1):
           for j in range(1, i+1):
               total+=j
               #print("total 1 is: ", total)
       print(total)

       # question 2 (G)
       total=0
       N=5
       for i in range (1, N+1):
           for j in range(1, N+1):
               total+=i+j
               #print("total 1 is: ", total)
       print(total)

       # question 2 (h)
       total=0
       N=5
       for i in range (1, N+1):
           for j in range(1, i+1):
               for k in range(1, j+1):
                   total+=1
                   #print("total 1 is: ", total)
               #print("total 2 is: ", total)
           #print("total 3 is: ", total)
       print(total)

       # question 2 (i)
       number=72958476
       a,b=0,0
       while (number>0):
           digit=number%10
           #print("digit main", digit)
           if (digit % 2!=0):
               a+=digit
               #print("digit A", a)
           else:
               b+=digit
               #print("digit B", b)
           number/=10
           #print("number",number)
       print(a,b)


def main():
    '''
    Objective: to grade marks
    Input: none
    Return : none
    '''
    marks=int(input("Enter the mark received: "))
    print("Grade received is: ", grades(marks))

    print("test 1 results: ", test1())


if __name__=='__main__':
    main()
