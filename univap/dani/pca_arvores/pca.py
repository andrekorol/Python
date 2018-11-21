with open('/home/andre/src/repos/github/Python/univap/dani/pca_arvores/SeriesPFComTend.dat') as data:
    next(data)
    for line in data:
        year = line.split('\t')[0]
        year_radius_data = line.split('\t')[1:]
        year_radius_data = [r for r in year_radius_data if r not in ('', '\n')]
        # print(year_radius_data)
        year_radius_sum = round(sum(float(x) for x in year_radius_data), 5)
        print(year_radius_sum)
        number_of_radius = len(year_radius_data)
        print(number_of_radius)