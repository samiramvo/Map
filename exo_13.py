from operator import eq
def some_pairs(liste1,liste2):
    func=sum(map(eq,liste1,liste2))
    return func

print(some_pairs([1,2,3],[4,9,6,2]))