import math as m


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
    test2 = [2.0, 4.0, 4.0, 4.0, 5.0, 5.0, 7.0, 0.0, "foo"]
    #print "the population stdev is", stdev_p(test)
    #print "the sample stdev is", stdev_s(test)
    #print reduce(lambda x, y: x + y, test) / len(test)
    #print reduce(lambda x, y: x + y, test2) / len(test2)
    #print is_valid_list(test)
    print is_valid_list(test2)