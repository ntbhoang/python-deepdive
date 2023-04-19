import random


# print(f"1st random number= {random.random()}")
#
# for _ in range(10):
#     print(random.randint(10, 20), random.random())

# Use random seeds
# random.seed(0)
#
# for _ in range(10):
#     print(random.randint(10, 20), random.random())


def generate_random_stuff(seed=None):
    random.seed(seed)
    results = []

    for _ in range(5):
        results.append(random.randint(0, 5))

    characters = list("abc")
    random.shuffle(characters)
    results.append(characters)

    for _ in range(5):
        results.append(random.gauss(0, 1))

    return results


lst = [random.randint(0, 10) for _ in range(15)]
print(lst)


def freq_analysis(items: list):
    return {k: items.count(k) for k in set(items)}


print(freq_analysis(lst))
