def simple(x):
    """
    if x simple then return True
    :param x:
    :return:
    """
    div = 2
    while div < x:
        if x%div == 0:
            return False
        div += 1
    return True

    simple(109)