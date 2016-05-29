# This is the important information that
# needs to be at the top!

import cubelib
if __name__ == '__main__':
    print 'hello dude!'
    x = float(raw_input('%s' % "Enter number to cube: "))
    print cubelib.cube(x)