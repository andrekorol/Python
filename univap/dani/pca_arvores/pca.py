series_out = open('SeriesPFSemTend.dat', 'w')
mean_radius_file = open('mean.dat', 'w+')
series_in = open('SeriesPFComTend.dat')
header = series_in.readline()
mean_radius_file.write('Tempo\tMedia\n')
for line in series_in:
    year = line.split('\t')[0]
    year_radius_data = line.split('\t')[1:]
    year_radius_data = [r for r in year_radius_data if r not in ('', '\n')]
    year_radius_sum = round(sum(float(x) for x in year_radius_data), 5)
    number_of_radius = len(year_radius_data)
    year_mean_radius = round(year_radius_sum / number_of_radius, 5)
    mean_radius_file.write(f'{year}\t{year_mean_radius}\n')

series_out.write(header)

series_in.seek(0)
next(series_in)

mean_radius_file.seek(0)
next(mean_radius_file)

for mean_radius_file_line, series_in_line in zip(mean_radius_file.readlines(), series_in.readlines()):
    year = series_in_line.split('\t')[0]
    series_out.write(year)
    mean_radius = float(mean_radius_file_line.split('\t')[1])
    radius_list = [r for r in series_in_line.split('\t')[1:] if r not in ('', '\n')]
    for radius in radius_list:
        no_tend_radius = round(float(radius) - mean_radius, 5)
        series_out.write(f'\t{no_tend_radius}')
    series_out.write('\n')

series_out.close()
mean_radius_file.close()
series_in.close()