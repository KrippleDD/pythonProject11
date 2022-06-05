f = open('input.txt')
dict = {}
for line in f:
    a = map(str, line.split())
    a = list(a)
    for i in range(len(a)):
        if a[i] in dict:
            dict[a[i]] += 1
        else:
            dict[a[i]] = 0
        print(dict[a[i]])
