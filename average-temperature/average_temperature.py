temperatures_file = 'results.txt'

def get_extremes(file):
    try:
        with open(file, 'r') as file:
            content = file.read()
            info = content.split('\n')
            data_pool = []
            for line in info:
                data = line.split(' ')
                data_pool.append(data)
            first = data_pool[0][0]
            second = data_pool[0][1]
            third = data_pool[0][2]
            coldest_years = [data_pool[1][3], data_pool[1][3], data_pool[1][3]]
            hottest_years = [data_pool[1][3], data_pool[1][3], data_pool[1][3]]
            coldest_values = [data_pool[1][0], data_pool[1][1], data_pool[1][2]]
            hottest_values = [data_pool[1][0], data_pool[1][1], data_pool[1][2]]
            for i in range(3):
                for j in range(1, len(data_pool)):
                    if data_pool[j][i] < coldest_values[i]:
                        coldest_years[i] = data_pool[j][3]
                        coldest_values[i] = data_pool[j][i]
                    if data_pool[j][i] > hottest_values[i]:
                        hottest_years[i] = data_pool[j][3]
                        hottest_values[i] = data_pool[j][i]
            res = {}
            res[first] = [coldest_years[0], hottest_years[0]]
            res[second] = [coldest_years[1], hottest_years[1]]
            res[third] = [coldest_years[2], hottest_years[2]]
            return res
    except NameError:
        return 'Name Error'
    except FileNotFoundError:
        return 'File Not Found'
    except IOError:
        return 'IO Error'

for k, v in (get_extremes(temperatures_file)).items():
    value = ''
    for element in v:
        value += element
        if v.index(element) < len(v) - 1:
            value += ', '
    print(str(k) + ' => ' + str(value))