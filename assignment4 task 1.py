try:
    with open('sample.txt', 'rt') as fh:
            content = fh.readline()
            content2 = fh.readline()
            print(f"line 1: {content}")
            print(f"line 2: {content2}")
except FileNotFoundError:
    print("The file sample.txt was not found")