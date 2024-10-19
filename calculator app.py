def choice_input_1() :
    print("Choose Input 1")
    global x 
    x = int(input())
    choice_input_2()
    return()
    

def choice_input_2() :
    print("Choose Input 2")
    global y 
    y = int(input())
    choice_operator()
    return()


def continue_or_end() :
    print("Would you like to\n1)continue with this output for the next calculation?\n2)start new operation?\n3)end?")
    try:
        global t
        t = int(input())
    except ValueError:
        print("That's not a valid integer!")
    if t == 1 :
        update()
        choice_input_2()
    if t == 2 :
        choice_input_1()
    if t == 3 :
        return()
    else :
        print("Choose from 1 to 3!")
        continue_or_end()
    return()


def choice_operator() :
    print("Choose Operator\n 1) Addition\n 2) Subtraction\n 3) Multiplication\n 4) Division")
    try:
        global z
        z = int(input())
    except ValueError:
        print("That's not a valid integer!")
    global output 
    if z == 1 :
        output = x + y
        print(x , " + " , y , " = " , output)
        continue_or_end()
        return()
    if z == 2 :
        output = x - y 
        print(x , " - " , y , " = " , output)
        continue_or_end()
        return()
    if z == 3 :
        output =  x * y 
        print(x , " * " , y , " = " , output)
        continue_or_end()
        return()
    if z == 4 :
        output =  x / y
        if x % y == 0 :
            print(x , " / " , y , " = " , int(output)) 
        else :
            print(x , " / " , y , " = " , output) 
        continue_or_end()
        return()
    else :
        print("Choose from 1 to 4!")
        choice_operator()
        return()


def update() : 
    global x
    global output
    x = output
    return()


print("Calculator App:\n-->Choose Input 1 and then 2\n-->Choose Operator\n-->Recieve Output...")


choice_input_1()



