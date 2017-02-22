def mk_cities():
    arr = []
    with open('cities.txt', 'r') as f:
        for i in f:
            arr.append(i.rstrip('\n'))
    return arr

if __name__ == '__main__':
    print(len(mk_cities()))