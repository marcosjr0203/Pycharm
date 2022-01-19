import random
# # random.randrage(start, stop, step): Returns a randomly selected integer from 0 to 100, with step 2.
# # Value Error if start > stop.
# print(random.randrange(0, 100, 2))
# # random.randint(a, b): Returns a random integer between "a" and "b", both included.
# # Value Error if a > b.
# print(random.randint(1, 5))
# # random.random(): Returns the next random floating point between 0.0 to 1.0 (1.0 not included).
# print(random.random())
# # random.uniform(a, b): Returns a random floating point between "a" and "b", such that:
# # a <= N <=b,
# # if a <= b,
# # and b <= N <= a,
# # if b < a
# print(random.uniform(0, 5))
# #random.expovariate(lambda): returns a number corresponding to an exponential distribution
# print(random.expovariate(lambd=0.0001)) #e.g.: 8794.6477906032324052
# print(random.expovariate(lambd=0.001)) #e.g.: 149.739417848663638435
# print(random.expovariate(lambd=0.01)) #e.g.: 96.25444207977454364181
# print(random.expovariate(lambd=0.1)) #e.g.: 4.2217959577088484527465
# print(random.expovariate(lambd=1)) #e.g.: 0.216645660575210842304164
# print(random.expovariate(lambd=10)) #e.g.: 0.01382669281903017341864
# print(random.expovariate(lambd=100)) #e.g.: 0.0091105961195040454128
# print(random.expovariate(lambd=1000)) #e.g.: 0.002110185520901729779
# print(random.expovariate(lambd=10000)) #e.g.: 0.00018711952487905666
# random.seed(): generate a random number attached to a seed number
# random.seed(1515103)
# print(random.randint(1, 10))  # it returns always the same number, attached to the seed.
# #random.choice() = choose one item from a list. e.g.: random.choice(list)
