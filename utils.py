def binom(n, k): 
    """
    Computes the binomial coefficient C(n, k), the number of combinations of n
    things taken k at a time.

    Parameters
    ----------
    n : int
        Number of total elements.
    k : int
        Cardinality of the groups.

    Returns
    -------
    int
        Binomial coefficient C(n, k).

    """
    if not 0 <= k <= n:
        return 0
    
    b=1
    for t in range(min(k, n-k)):
        b *= n
        b /= t+1
        n -= 1

    return int(b)