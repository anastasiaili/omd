def aggregate(data, field, function):
    values = []

    for item in data:
        if item[field] is not None:
            values.append(item[field])

    return function(values)


def count_items(data):
    return len(data)


def top_n(data, n):
    return sorted(data.items(), key=lambda item: item[1], reverse=True)[:n]


def count_words(words):
    counts = {}

    for word in words:
        if word not in counts:
            counts[word] = 0

        counts[word] += 1

    return counts
