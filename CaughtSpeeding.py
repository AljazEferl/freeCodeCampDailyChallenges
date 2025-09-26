#09/26/2025

'''
Given an array of numbers representing the speed at which vehicles were observed traveling,
and a number representing the speed limit, return an array with two items,
the number of vehicles that were speeding,
followed by the average amount beyond the speed limit of those vehicles. 
'''

#-------------------------------------------------------------------------------

def speeding(speeds, limit):
    average = 0
    count = 0
    for i in speeds:
        if i  >  limit: 
            #print(i)
            count += 1
            average += i - limit

    if count != 0:
        average = average / count
    #print(average)    
    return [count , average]


'''
1. speeding([50, 60, 55], 60) should return [0, 0].
2. speeding([58, 50, 60, 55], 55) should return [2, 4].
3. speeding([61, 81, 74, 88, 65, 71, 68], 70) should return [4, 8.5].
4. speeding([100, 105, 95, 102], 100) should return [2, 3.5].
5. speeding([40, 45, 44, 50, 112, 39], 55) should return [1, 57].
'''

print(speeding([50, 60, 55], 60))
print(speeding([58, 50, 60, 55], 55))
print(speeding([61, 81, 74, 88, 65, 71, 68], 70))
print(speeding([100, 105, 95, 102], 100))
print(speeding([40, 45, 44, 50, 112, 39], 55))