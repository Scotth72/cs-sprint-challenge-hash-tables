# Your code here


def finder(files, queries):
    """
    YOUR CODE HERE
    """
    # Your code here
    result = []
    cache = {}

    for path in files:
        key = path.split('/')[-1]

        if key not in cache:
            cache[key] = []

        cache[key].extend([path])

    for file in queries:
        if file in cache:
            result.extend(cache[file])

    return result


if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))
