import datetime


def data_plot(data):
    from matplotlib import pyplot as plt
    x, height = [item[0].strftime('%m%d') for item in data], [item[1] for item in data]
    plt.figure(dpi=200)
    plt.bar(x, height, width=0.35)
    plt.title("Bar")
    plt.xlabel("month")
    plt.ylabel("month count")
    plt.tick_params(axis='x', labelsize=9, rotation=50)
    plt.show()


if __name__ == '__main__':
    import read_excel

    file = '/Users/admin/PycharmProjects/learn-python/python_coder_share/数据来源.xlsx'
    # excel 数据
    data = read_excel.read_excel(file, sheet='Sheet1')
    print(data)
    # data = [[datetime.datetime(2018, 12, 1, 0, 0), 227526, 16251], [datetime.datetime(2019, 1, 1, 0, 0), 263218, 22689],
    #         [datetime.datetime(2019, 2, 1, 0, 0), 189339, 9585], [datetime.datetime(2019, 3, 1, 0, 0), 116730, 9425],
    #         [datetime.datetime(2019, 4, 1, 0, 0), 383429, 21349], [datetime.datetime(2019, 5, 1, 0, 0), 247331, 12531],
    #         [datetime.datetime(2019, 6, 1, 0, 0), 181440, 14579], [datetime.datetime(2019, 7, 1, 0, 0), 236901, 16256],
    #         [datetime.datetime(2019, 8, 1, 0, 0), 200990, 15150]]
    # print(data)
    # x = [item[0].strftime('%m%d') for item in data]
    # y = [item[1] for item in data]
    # print(x, y)
    data_plot(data)
    pass
