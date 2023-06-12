# UNQ_C1
# GRADED CELL: my_softmax

def my_softmax(z):  
    """ Softmax converts a vector of values to a probability distribution.
    Args:
      z (ndarray (N,))  : input data, N features
    Returns:
      a (ndarray (N,))  : softmax of z
    """    
    ### START CODE HERE ### 
    
    N = len(z)
    a = [0] * N
    for j in range(N):
        total_sum = 0
        for k in range(N):
            curr_sum = np.exp(z[k])
            total_sum += curr_sum
        a[j] = np.exp(z[j]) / total_sum
    
    ### END CODE HERE ### 
    return a