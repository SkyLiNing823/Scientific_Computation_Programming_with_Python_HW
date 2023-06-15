class SortKey:
    def __init__(self, index=0) -> None:
        self.index = index

    def __call__(self, x):
        return x.scores[self.index]


class student:
    def __init__(self, id='', name='', age=18, scores=[0.0, 0.0, 0.0]):
        self.id = id
        self.name = name
        self.age = age
        self.scores = list(scores)

    def __str__(self):
        return self.name

    def __repr__(self) -> str:
        return self.__str__()


Mary = student('A000', 'Mary', 20, [90, 80, 75])
James = student('A010', 'James', 20, [82, 60, 91])
Ann = student('A008', 'Ann', 19, [95, 92, 100])
Tim = student('A208', 'Tim', 21, [56, 72, 50])
L = [Mary, James, Ann, Tim]
print(L)
L.sort(key=SortKey())
print(L)
L.sort(key=SortKey(1))
print(L)
L.sort(key=SortKey(2))
print(L)
