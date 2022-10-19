from multipledispatch import dispatch

@dispatch(int , int)
def add(First,Second):
    result=First+Second
    print("addition of two integer value : ",result)


@dispatch(float , float)
def add(First,Second):
    result=First+Second
    print("Addition of two float value : ",result)

@dispatch(int , int , int)
def add(First,Second,Third):
    result=First+Second+Third
    print("Addition of three integer value : ",result)
    
@dispatch (float , int)
def add(First,Second):
    result=First+Second
    print("Addition of two different data : ",result)


add(10,20)
add(2.1,3.4)
add(10,20,30)
add(3.2,10)
