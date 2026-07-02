import matplotlib.pyplot as plt


def plot_bar(data, title):

    data.plot(
        kind="bar",
        figsize=(10,5)
    )

    plt.title(title)

    plt.tight_layout()

    plt.show()
