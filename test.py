list_ = ['1 2 3 4'.split(),'1 2 3 4'.split(),'2 4 3 1'.split(),'3 4 2 1'.split(),'4 3 2 1'.split()]

from collections import Counter

all_fruits = set(list_[0])
to_exclude = set()
for j in range(len(list_)):
    counts = {}
    for i in list_:
        if i[j] not in to_exclude:
            print(i[j])
            if i[j] not in counts:
                counts[i[j]] = 0
            counts[i[j]] += 1

    print(counts)
    print('toexclude', min(counts, key=counts.get))
    to_exclude.add(min(counts, key=counts.get))