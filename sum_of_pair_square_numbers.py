import math
import itertools as it

global_result = False

def get_nearest_square(n):
    m = math.sqrt(n)
    m = str(m).split('.')[0]
    return int(m)

def list_of_squers(n):
    return [i**2 for i in range(1,n+1)]

def get_pairs_of_sum(num,n):
    res = []
    res1 = []
    for i in range(1,(num//2)+1):
        ln = num - i
        if ln > n:
            continue
        rn = i
        if ln > rn :
            res.append((ln,rn))
            res1.extend((ln,rn))
    return (res , res1 )

def get_singles(d = {}):
    singles = []
    for k,v in d.items():
        if len(v) == 1:
            singles.append(k)
    return singles

def find_graph(pairs , n):
    res2 = {}
    for p in pairs:
        n1 = p[0]
        n2 = p[1]
        res2.setdefault(n1 , list()).append(n2)
        res2.setdefault(n2 , list()).append(n1)
    return res2

def hamiltonians(G, vis = []):
    dests = (not vis and G.keys()) or (set(G[vis[-1]]) - set(vis))
    if not dests and len(vis) == len(G):
        yield vis
    for n in dests:
        for p in hamiltonians(G, vis + [n]):
            yield p

def main():
    #n = int(input('Enter a number : '))
    n = 15
    lowest_square = get_nearest_square(2*n-1)
    squres_list = list_of_squers(lowest_square)
    pairs = []
    counts = []    
    for sqr in squres_list:
        res = get_pairs_of_sum(sqr,n)
        if res[0] != []:
            pairs +=  res[0] 
            counts += res[1]
    
    res2 = find_graph(pairs,n)
    print(res2)
    results = list(hamiltonians(res2))
    if results == []:
        print(results)
        print(False)
    else:
        print(results)
        print(True)

main()