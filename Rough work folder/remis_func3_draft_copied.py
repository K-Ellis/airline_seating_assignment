import numpy as np

# Read the Ones and Zeros matrix
initdb = np.genfromtxt('binary_db.txt')
# Result_list classifies in lists of tuples the number of consecutive available or unavailable seats.
# (0,n) indicates that n seats are available, (1,m) indicates that m seats are occupied
print(type(initdb))
for x in initdb:

    result_list = []
    current = x[0]
    count = 0
    for value in x:
        if value == current:
            count += 1
        else:
            result_list.append((int(current), count))
            current = value
            count = 1

    result_list.append((int(current), count))

    # newlist rearranges result_list so that we only keep the number of consecutive available seats

    newlist = []
    for z in result_list:

        if z[0] == 0:
            newlist.append(z[1])
    print(newlist)

print('Now Bookings')

# Read the bookings
bookings = np.genfromtxt('bookings.csv', dtype=None, delimiter=',')
for y in bookings:
    partysize = list(y)
    print(partysize)
    # for a in newlist:
    # if partysize[1]<=a: