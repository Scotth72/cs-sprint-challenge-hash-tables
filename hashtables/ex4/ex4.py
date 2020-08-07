def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # Your code here
    pos_cache = {}
    neg_cache = {}
    result = []

    for num in a:
        if num > 0 and num not in pos_cache:
            pos_cache[num] = num
        elif num < 0 and num not in neg_cache:
            neg_cache[num] = num

    for n in neg_cache:
        k = abs(int(n))
        if k in pos_cache:
            result.append(pos_cache[k])            

    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
