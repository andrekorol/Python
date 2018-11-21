series_out = open('SeriesPFSemTend.dat', 'w')
mean_radius_file = open('mean.dat', 'r+')
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


series_in.seek(0)
series_out.write(header)
next(series_in)
next(mean_radius_file)

for mean_radius_file_line, series_out_line in zip(mean_radius_file.readlines(), series_in.readlines()):
    print(mean_radius_file_line)
    print(series_out_line)

series_out.close()
mean_radius_file.close()
series_in.close()