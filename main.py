def OddOdd(values):
    toggle =True
    SumToReturn =0

    for value in values:
        if(toggle == True):
            if(value %2 == 1):
                SumToReturn =SumToReturn + value
        toggle = not toggle
    return(SumToReturn)
print(OddOdd([1,2,5,6,7,8]))

    