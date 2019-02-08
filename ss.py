

with open('data.txt','r') as textfile:
    test = textfile.read()
    test = test.split("\n\n")
    test = [x for x in test if len(x) > 100]
    for i in test:
        print("\n----------------------\n", i)
