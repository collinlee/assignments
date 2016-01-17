# Collin Lee
# CS-7646
# Assignment 1
import math as m

# calculate the population standard deviation
def stdev_p(data):
    if not is_valid_list(data):
        raise TypeError("Invalid list - non numeric value detected")
    else:
        if len(data) == 1:
            return 0
        else:
            #calculate mean of data
            mean = average(data)
            #calculate the sum of the square of each value minus mean
            variance = calculate_variance(data, mean)
            #return the square root
            return m.sqrt(average(variance))

# calculate the sample standard deviation
def stdev_s(data):
    if not is_valid_list(data):
        raise TypeError("Invalid list - non numeric value detected")
    else:
        if len(data) == 1:
            return 0
        else:
            #calculate mean of data
            mean = average(data)
            #calculate the sum of the square of each value minus mean
            variance = calculate_variance(data, mean)
            #get average with N-1
            avg = reduce(lambda x, y: x + y, variance) / (len(data) - 1)
            #return the square root
            return m.sqrt(avg)

#get variance
def calculate_variance(data, mean):
    return map(lambda x: (x - mean)**2, data)

#average helper function
def average(data):
    return reduce(lambda x, y: x + y, data) / len(data)

#is_valid_list helper function
def is_valid_list(data):
    try:
        for key, value in enumerate(data):
            if m.isnan(value):
                return False
    except TypeError:
        return False

    return True

if __name__ == "__main__":
    test = [2.0, 4.0, 4.0, 4.0, 5.0, 5.0, 7.0, 9.0]
    print "the population stdev is", stdev_p(test)
    print "the sample stdev is", stdev_s(test)