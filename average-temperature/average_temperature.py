temperatures_file = 'results.txt'

def get_extremes(file):
    try:
        with open(file, 'r') as file:
            content = file.read()
            #print(content)
            #content.remove(content[0])
            info = content.split('\n')
            data_pool = []
            for line in info:
                data = line.split(' ')
                data_pool.append(data)
            #print(data_pool)
            first = data_pool[0][0]
            second = data_pool[0][1]
            third = data_pool[0][2]
            coldest_year_in_first = 0
            hottest_year_in_first = 1
            coldest_year_in_second = 2
            hottest_year_in_second = 3
            coldest_year_in_third = 4
            hottest_year_in_third = 5
            #for i in range(len(data_pool))
            res = {}
            res[first] = [coldest_year_in_first, hottest_year_in_first]
            res[second] = [coldest_year_in_second, hottest_year_in_second]
            res[third] = [coldest_year_in_third, hottest_year_in_third]

            return res

    except NameError:
        return 'Name Error'
    except FileNotFoundError:
        return 'File Not Found'
    except IOError:
        return 'IO Error'

print(get_extremes(temperatures_file))