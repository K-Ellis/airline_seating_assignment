import numpy as np
def func_3():
    
    from operator import itemgetter
#Read the Ones and Zeros matrix 
    initdb = np.genfromtxt('txt_airline_seating.txt')
    reshapedplane=initdb.reshape((1,60))
#Result_list classifies in lists of tuples the number of consecutive available or unavailable seats. 
#(0,n) indicates that n seats are available, (1,m) indicates that m seats are occupied
    result_list=[]
    for x in initdb:
    
        current=x[0]
        count=0
        for value in x:
            if value==current:
                count+=1
            else:
                result_list.append((int(current), count))
                current = value
                count = 1

        result_list.append((int(current), count))

        #Read the bookings

    bookings=np.genfromtxt('bookings.csv', dtype=None, delimiter=',')
    next_new_booking=[]
    for y in bookings:



        try:
            partysize=list(y)
    #We identify the position of consecutive seats available that match the partysize required
            b=next(x for x in result_list if x[0]==0 and x[1]>=partysize[1])
            b_position=result_list.index(b)
            b_sum_position=sum([x[1] for x in result_list[:b_position]])


            print('We attribute the seats ',b_sum_position+1,'to',b_sum_position+partysize[1], 'to ',partysize[0],'who booked ',partysize[1],'seat(s)')

            for k,l in enumerate(range(partysize[1])):
                next_new_booking.append([b_sum_position+(k+1),partysize[0]])

            reshapedplane[0,b_sum_position:(b_sum_position+partysize[1])]=1


    #The result_list which classifies in lists of tuples the number of consecutive available or unavailable seats has to be updated. 

            result_list=[]
            reshapedplane=reshapedplane.reshape((15,4))
            for x in reshapedplane:


                current=x[0]
                count=0
                for value in x:
                    if value==current:
                        count+=1
                    else:
                        result_list.append((int(current), count))
                        current = value
                        count = 1

                result_list.append((int(current), count))
                reshapedplane=reshapedplane.reshape((1,60))
    #We sort the new_booking list by the number of seat
            next_new_booking=sorted(next_new_booking, key=itemgetter(0))
    #We print out a preview of the plane seating assigment
            print(reshapedplane.reshape(15,4))

        except StopIteration:
            print(y,"wasn't succesful")
    return next_new_booking
