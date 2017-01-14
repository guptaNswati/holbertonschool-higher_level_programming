#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    try:
        i = 0
        while i < x:
            print("{:d}".format(my_list[i]), end="")
            i += 1
        print()
    except TypeError:
        pass
    except ValueError:
        pass
    except IndexError:
        print()
        return i
    return i
