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