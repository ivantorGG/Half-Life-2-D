a = {
    '1': 2,
    '2': 3
}
b = {
    '1': 12,
    '2': 13
}
c = {
    '1': 22,
    '2': 32
}


def sum_player_stats(*stats):
    result = {}
    for key in stats[0]:
        result[key] = stats[0][key]
        for stat in stats[1:]:
            result[key] += stat[key]
    return result


print(sum_player_stats(a, b, c))
