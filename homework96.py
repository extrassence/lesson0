def all_variants(string):
    for i in range (0, len(string)):
        for j in range (0, len(string) - i):
            yield string[j:i+j+1]

a = all_variants("Urban")
for i in a:
     print(i)