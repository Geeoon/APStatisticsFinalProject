import matplotlib.pyplot as plt

if __name__ == '__main__':
    anonymous = [40, 43, 45, 45, 45, 45, 50, 50, 50, 55]
    not_anonymous = [35, 35, 40, 40, 42, 45, 50, 50, 50, 60]
    data = [anonymous, not_anonymous]
    colors = ['#94bdff', '#85ffa7']
    bp = plt.boxplot(data, vert=0, patch_artist=True, labels=['Anonymous', 'Not Anonymous'])
    for patch, color in zip(bp['boxes'], colors):
        patch.set_facecolor(color)
    plt.savefig('boxplots.png', bbox_inches="tight")
    plt.show()