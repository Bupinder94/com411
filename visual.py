import matplotlib.pyplot as plt

class Visualizer:
    @staticmethod
    def plot_pie_chart(data, title):
        labels, sizes = zip(*data.items())
        plt.figure(figsize=(8, 6))
        plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
        plt.title(title)
        plt.show()

    @staticmethod
    def plot_bar_chart(data, title, x_label, y_label):
        labels, values = zip(*data.items())
        plt.figure(figsize=(10, 6))
        plt.bar(labels, values)
        plt.title(title)
        plt.xlabel(x_label)
        plt.ylabel(y_label)
        plt.xticks(rotation=45)
        plt.show()