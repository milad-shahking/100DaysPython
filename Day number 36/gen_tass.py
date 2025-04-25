import random
import pickle



data = []
for i in range(10000):
    this_one = (random.randint(1,6), random.randint(1,6))
    data.append(this_one)


tass_out = open('mosabeghhe.taas', 'wb')
pickle.dump(data, tass_out)
tass_out.close()


