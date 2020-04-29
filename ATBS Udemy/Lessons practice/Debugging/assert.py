stoplight = {'ns':'red', 'ew':'green'}

def switchlights(intersection):
    for key in intersection.keys():

        if intersection[key] == 'red':
            intersection[key] = 'green'
        elif intersection[key] == 'green':
            intersection[key] = 'yellow'
        elif intersection[key] == 'yellow':
            intersection[key] = 'red'

# The assert always holds true, if not the program should fail.

    assert 'red' in intersection.values(), 'Neither light is red ' \
    + str(intersection)

switchlights(stoplight)
