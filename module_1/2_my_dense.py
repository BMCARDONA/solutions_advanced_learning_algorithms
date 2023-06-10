# UNQ_C2
# GRADED FUNCTION: my_dense

def my_dense(a_in, W, b, g):
    """
    Computes dense layer
    Args:
      a_in (ndarray (n, )) : Data, 1 example 
      W    (ndarray (n,j)) : Weight matrix, n features per unit, j units
      b    (ndarray (j, )) : bias vector, j units  
      g    activation function (e.g. sigmoid, relu..)
    Returns
      a_out (ndarray (j,))  : j units
    """
    units = W.shape[1]
    a_out = np.zeros(units)
### START CODE HERE ### 
    for j in range(units):          # iterate over each jth unit
        w = W[:, j]                 # assign w to the jth column of W
        z = np.dot(w, a_in) + b[j]  # take dot product of w and a_in; add to jth element of b
        a_out[j] = g(z)             # take sigmoid of result; assign resulting element of sigmoid to jth column
                                    # of a_out
### END CODE HERE ### 
    return(a_out)