import matplotlib.pyplot as plt
from pylab import *


def data_parse(fname, category):
    """
    creates a list of tuples with chosen data and lung disease data

    :param category: (int) the index category to compare with disease level
    :param fname: (file) lung disease data set
    :return: (list) a list of tuples containing all necessary data
    """
    # making a new list
    new_list = []
    file = open(fname, 'r')
    # counter so that we can skip first line of file
    counter = 0
    for line in file:
        if counter > 0:
            # forming a list between each comma
            listed = line.split(',')
            # adding the data into the list (chosen data first)
            new_list.append((int(listed[category - 1]), int(listed[9])))
        counter += 1
    file.close()
    return new_list


def air_pollution_plot(data, format):
    """
    makes a plt plot comparing air pollution and lung disease data

    :param data: (list) a list returned from data_parse
    :param format: (string) type of plt plot
    :return: plt plot
    """
    # empty lists for x and y data points
    x = []
    y = []
    for sublist in data:
        # adding air pollution data into x-list and lung disease data into y-list
        x.append(sublist[0])
        y.append(sublist[1])
    # plotting x and y lists into plot
    plt.plot(x, y, format, label="(Air Pollution, Lung Disease)")
    plt.title("Correlation between Level of Air Pollution and Chronic Lung Disease")
    # adding a line of best fit to accurately visualize correlation
    plt.plot(np.unique(x), np.poly1d(np.polyfit(x, y, 1))(np.unique(x)), label="Line of Best Fit")
    plt.xlabel("Level of Air Pollution")
    plt.ylabel("Level of Lung Disease")
    plt.legend()
    plt.show()


def gender_comparison(fname, category):
    """
    returns a list of tuples that contains tuples of women's smoking and lung disease data,
    followed by men's smoking and lung disease data

    :param fname: (file) lung disease data set
    :param category: (int) the index category to compare with disease level
    :return: (list) a list of both women's and men's data
    """
    # initializing lists
    women_list = []
    men_list = []
    correlated_list = []

    file = open(fname, 'r')
    counter = 0
    for line in file:
        if counter > 0:
            # forming a list between each comma
            listed = line.split(',')
            # separating smoking and disease level data between genders
            if listed[3] == "1":
                men_list.append((int(listed[category - 1]), int(listed[9])))
            else:
                women_list.append((int(listed[category - 1]), int(listed[9])))
        counter += 1

    # appending women's data, then men's data
    correlated_list.append(women_list)
    correlated_list.append(men_list)
    file.close()
    return correlated_list


def gender_comparison_plot(data):
    """
    creates a plot that shows the correlation between smoking level
    and level of lung disease, separated by gender

    :param data: (list) the list returned from gender_comparison
    :return: a plt plot
    """
    # initializing empty lists for both men and women
    xw = []
    yw = []
    xm = []
    ym = []

    # appending all women's data into xw and yw
    for sub in data[0]:
        xw.append(sub[0])
        yw.append(sub[1])
    # plotting women's data into the graph
    plt.plot(xw, yw, "b.", label="Women")
    plt.title("Correlation between Level of Smoking and Chronic Lung Disease")
    plt.plot(np.unique(xw), np.poly1d(np.polyfit(xw, yw, 1))(np.unique(xw)), label="Line of Best Fit (Women)")

    # appending all men's data into xm and ym
    for sub in data[1]:
        xm.append(sub[0])
        ym.append(sub[1])
    # plotting men's data into graph
    plt.plot(xm, ym, "r+", label="Men")
    plt.plot(np.unique(xm), np.poly1d(np.polyfit(xm, ym, 1))(np.unique(xm)), label="Line of Best Fit (Men)")

    plt.xlabel("Level of Smoking")
    plt.ylabel("Level of Lung Disease")
    plt.legend()
    plt.show()


def age_plot(data):
    """
    plots a graph that shows the correlation between age and level of lung disease

    :param data: (list) the list returned from data_parse
    :return: a plt plot
    """
    # empty lists for x and y data points
    x = []
    y = []
    # initializing variables to zero for future use
    x1, x2, x3, x4, x5, x6, x7 = [0, 0, 0, 0, 0, 0, 0]
    count1, count2, count3, count4, count5, count6, count7 = [0, 0, 0, 0, 0, 0, 0]

    for sublist in data:
        # sorts the data into specific age group
        if sublist[0] <= 10:
            # adds together level of lung disease for each age group
            x1 += sublist[1]
            # counts the number of individuals that fall into each age group
            count1 += 1
        elif sublist[0] <= 20:
            x2 += sublist[1]
            count2 += 1
        elif sublist[0] <= 30:
            x3 += sublist[1]
            count3 += 1
        elif sublist[0] <= 40:
            x4 += sublist[1]
            count4 += 1
        elif sublist[0] <= 50:
            x5 += sublist[1]
            count5 += 1
        elif sublist[0] <= 60:
            x6 += sublist[1]
            count6 += 1
        else:
            x7 += sublist[1]
            count7 += 1
    # checks whether any count value is zero; makes it zero to avoid dividing by zero later
    # making count equal to one won't change the average if its zero anyway
    if count1 == 0:
        count1 = 1
    elif count2 == 0:
        count2 = 1
    elif count3 == 0:
        count3 = 1
    elif count4 == 0:
        count4 = 1
    elif count5 == 0:
        count5 = 1
    elif count6 == 0:
        count6 = 1
    elif count7 == 0:
        count7 = 1
    # appends into the y-list the average lung disease level for every age group
    y.append([x1/count1, x2/count2, x3/count3, x4/count4, x5/count5, x6/count6, x7/count7])
    # appending labels for the bar graph
    x.append(["0-10", "11-20", "21-30", "31-40", "41-50", "51-60", "61-70"])
    # plotting it
    plt.bar(x[0], y[0], color='green', width=0.35)

    plt.xlabel("Age")
    plt.ylabel("Average Level of Chronic Lung Disease")
    plt.title("Correlation between Age and Level of Lung Disease")
    plt.show()



def main():
    """
    plots the specified graphs into madplot

    :return: three total graphs: two plot, and one bar graph
    """
    # showing air pollution comparison plot, followed by gender comparison, and finally age
    air_pollution_plot(data_parse('cancer.csv', 5), "b.")
    gender_comparison_plot(gender_comparison('cancer.csv', 13))
    age_plot(data_parse('cancer.csv', 3))


if __name__ == '__main__':
    main()
