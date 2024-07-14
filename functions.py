import math

def mean(values:list):
    num = sum(values)
    den = len(values)

    return num/den

def median(values:list):
    sort_values = sorted(values)
    num_values = len(values)

    center_pos = int((num_values + 1) / 2) - 1 # -1 pois o index começa a contar de 0

    is_even = num_values % 2 == 0 #se par
    if is_even:
        center_values = [sort_values[center_pos], sort_values[center_pos + 1]]
        center_mean = mean(center_values) 
        return center_mean
    
    return sort_values[center_pos]

def mode(values:list):
    most_commons = []

    for value in values:
        freq = values.count(value)
        tup = (value, freq)

        most_commons.append(tup)

    biggest_value = max(most_commons, key=lambda x: x[1])[1]
    most_freqs = [v[0] for v in most_commons if v[1] == biggest_value]

    return set(most_freqs)


def quartil(values:list, percentil):
    num_values = len(values)
    center_pos = int((num_values + 1) / 2) 

    if percentil == 0.5:
        return median(values)
    elif percentil == 0.25:
        values_quantil = values[:center_pos]
        return median(values_quantil)
    elif percentil == 0.75:
        values_quantil = values[center_pos:]
        return median(values_quantil)
    else:
        print('Insira um quartil válido - 0.25, 0.5, 0.75')

def amplitude(values:list):
    max_v = max(values)
    min_v = min(values)
    range_v = max_v - min_v
    return range_v

def iqr(values:list):
    result = quartil(values, 0.75) - quartil(values, 0.25)
    return result

def variance(values:list, is_population = False):
    mean_value = mean(values)

    num = sum([(value - mean_value)**2 for value in values])
    den = len(values) - 1

    if is_population:
        den = den + 1
        
    return (num/den)

def std(values:list, is_population = False ):
    return math.sqrt(variance(values, is_population))

def cv(values:list, **kwargs):
    return std(values, kwargs) / mean(values)

def corr(values1:list, values2:list):
    x_mean = mean(values1)
    y_mean = mean(values2)

    num_items = len(values1)

    if num_items != len(values2):
        raise print('Conjuntos de tamanhos diferentes')

    num = 0
    den_x = 0
    den_y = 0
    for v_index in range(num_items):
        dist_x = values1[v_index] - x_mean
        dist_y = values2[v_index] - y_mean

        num_n = dist_x * dist_y

        dist_square_x = dist_x ** 2
        dist_square_y = dist_y ** 2

        den_x += dist_square_x
        den_y += dist_square_y

        num += num_n

    den = math.sqrt((den_x * den_y))
    corr = num / den

    return corr

        