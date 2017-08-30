def cosineSimilarity(A, B):
    import math
    product = 0
    quadratic_sum_of_A = 0
    quadratic_sum_of_B = 0
    new_A = [i for i in A if i != 0]
    new_B = [i for i in B if i != 0]
    if new_A == [] and new_B == []:
        return 2.000
    for i in range(len(A)):
        product += A[i] * B[i]
        quadratic_sum_of_A += A[i] ** 2
        quadratic_sum_of_B += B[i] ** 2
    result = product / (math.sqrt(quadratic_sum_of_A) * math.sqrt(quadratic_sum_of_B))
    return result