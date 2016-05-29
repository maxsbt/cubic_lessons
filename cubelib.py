def cube(x):
    return x * x * x

if __name__ == '__main__':
    print 'testing out cube'
    print cube(3)
    assert cube(3) == 27
