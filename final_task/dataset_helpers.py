def group_by_attributes(data, attributes):
    result = {}

    for item in data:
        key = tuple(item[attribute] for attribute in attributes)

        if key not in result:
            result[key] = []

        result[key].append(item)

    return result


def count_missing(data, fields):
    missing = {}
    missing_share = {}

    for field in fields:
        count = 0

        for item in data:
            if item.get(field) is None:
                count += 1

        missing[field] = count
        missing_share[field] = round(count / len(data) * 100, 2)

    return missing, missing_share


def get_decade(year):
    return year // 10 * 10


def split_into_words(motivation):
    text = motivation.lower()

    for symbol in '.,;:!?()[]"/-':
        text = text.replace(symbol, ' ')

    return text.split()
