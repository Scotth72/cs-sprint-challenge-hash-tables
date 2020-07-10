def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # need to store weights in cache
    # loop through the list of weights

    weight_cache = {weights[i]: i for i in range(len(weights))}

    for w in range(length):
        missing_weight = limit - weights[w]

        if missing_weight in weight_cache:
            h_index = max(w, weight_cache[missing_weight])
            l_index = min(w, weight_cache[missing_weight])

            return (h_index, l_index)

    return None
