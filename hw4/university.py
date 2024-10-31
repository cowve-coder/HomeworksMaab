import statistics
universities = [
    ['California Institute of Technology', 2175, 37704],
    ['Harvard', 19627, 39849],
    ['Massachusetts Institute of Technology', 10566, 40732],
    ['Princeton', 7802, 37000],
    ['Rice', 5879, 35551],
    ['Stanford', 19535, 40569],
    ['Yale', 11701, 40500]
]
def enrollment_stats(l: list) -> tuple[list, list]:
    l1, l2 = [], []
    for i in l:
        l1.append(i[1])
    for i in l:
        l2.append(i[2])
    return l1, l2
enrollment_stats(universities)
lis1, lis2 = [], []
lis1, lis2 = enrollment_stats(universities)
def mean(l: list) -> float:
    return statistics.mean(l)
def median(l:list) -> float:
    return statistics.median(l)
print('*************************\n')
print('Total students: ', round(len(universities) * mean(lis1), 2), '\n')
print('Total tuition: $', round(len(universities) * mean(lis2), 2), '\n\n')
print('Student mean: ', round(mean(lis1), 2), '\n')
print('Student median: ', round(median(lis1), 2), '\n\n')
print('Tuition mean: $', round(mean(lis2), 2), '\n')
print('Tuition median: $', round(median(lis2), 2), '\n')
print('*************************\n')