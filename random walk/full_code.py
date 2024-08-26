import matplotlib.pyplot as plt

from random_walk import RandomWalk

while True:
    rw = RandomWalk(80000)
    rw.fill_walk()
    plt.figure(dpi=128, figsize=(10, 6))
    point_numbers = list(range(rw.num_points))
    plt.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, edgecolor='none', s=1)

    plt.gca().get_xaxis().set_visible(False)
    plt.gca().get_yaxis().set_visible(False)
    plt.show()
    keep_running = input("Make anoyher walk? (y/n): ")
    if keep_running == 'n':
        break
