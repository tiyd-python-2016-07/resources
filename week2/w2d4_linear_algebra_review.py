class ShapeError(Exception):
    print("can't put a square peg in a round hole.")


def shape(vector):
    return (len(vector),)


def prod(vector):
    """multiply all the elements of a vector together and return as a scalar"""
    if len(vector) == 0:
        return 1
    return vector[0] * prod(vector[1:])

def verify_same_shape(*vectors):
    if len({ shape(vector) for vector in vectors }) != 1:
        raise ShapeError


def vector_negate(vector):
    return [-x for x in vector]


def vector_sub(lhs, rhs):
    return vector_add(lhs, vector_negate(rhs))


def vector_sum(*vectors):
    verify_same_shape(*vectors)
    return [sum(zipper) for zipper in zip(*vectors)]


def vector_add(lhs, rhs):
    return vector_sum(lhs, rhs)


def dot(lhs, rhs):
    verify_same_shape(lhs, rhs)
    return sum([prod(zipper) for zipper in zip(lhs, rhs)])


def vector_multiply(vector, scalar):
    return [element*scalar for element in vector]


def mean(vector):
    return sum(vector)/len(vector)


def vector_mean(*vectors):
    return [mean(zipper) for zipper in zip(*vectors)]


def magnitude(vector):
    return sum([element**2 for element in vector])**.5
