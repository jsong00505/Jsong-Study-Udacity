def clique(n):
    print "in a clique..."
    for j in range(n):
        for i in range(j):
            print i, "is friends with", j

def count(n):
    result = 1 + 1 + n + n*(n-1)/2
    return result

clique(4)
print count(4)