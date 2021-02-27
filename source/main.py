import csv
import datetime

# Use pandas instead of csv
# Use settleup API - https://settleup.io/api.html

def main():
    with open('test/test_transactions.csv', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')
        next(spamreader, None)
        next(spamreader, None)
        for row in spamreader:
            # print(', '.join(row))
            # print(row[7])
            # date_time_obj = datetime.datetime.strptime(row[7], '%Y-%m-%d %H:%M:%S')
            # print('Date: ', date_time_obj.date(), " Time: ", date_time_obj.time())
            date_filter = date(spamreader, "2020-09-27")
            name_filtered = name_filter(date_filter, "Kylee")
            name_cost(name_filtered, "Kylee")


def date(reader, date):
    date_filter = []
    for row in reader:
        date_string = row[7]
        date_time_obj = datetime.datetime.strptime(date_string, '%Y-%m-%d %H:%M:%S')
        if date_time_obj.date() > datetime.datetime.strptime(date, '%Y-%m-%d').date():
            print(date_time_obj.date())
            date_filter.append(row)

    # for row in date_filter:
    #     print(row)
    return date_filter

def name_filter(reader, name):
    name_filter = []
    for row in reader:
        name_string = row[3]
        if name in name_string:
            name_filter.append(row)

    for row in name_filter:
        print(row)

    return name_filter

def name_cost(reader, name):
    name_cost_filter = []
    for row in reader:
        # Date
        date_string = row[7]
        date_time_obj = datetime.datetime.strptime(date_string, '%Y-%m-%d %H:%M:%S')

        # Description
        description = row[5]

        # Cost
        names_string = row[3]
        names = names_string.split(";")
        print(names)
        index = names.index("Kylee")
        costs_string = row[4]
        costs = costs_string.split(";")
        print(costs[index])
        print("Name: ", names[index], " Cost: ", costs[index])

#       Create table with date, name cost, blank column, and description
        name_cost_filter.append([str(date_time_obj.date()), costs[index], " ", description, row[0]])

    with open('outputs/output.csv', 'w', newline='') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=',', quotechar='"')
        for row in name_cost_filter:
            print(row)
            spamwriter.writerow(row)


if __name__ == '__main__':
    main()


