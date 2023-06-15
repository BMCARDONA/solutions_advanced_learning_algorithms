# UNQ_C1
# GRADED CELL: eval_mse
def eval_mse(y, yhat):
    """ 
    Calculate the mean squared error on a data set.
    Args:
      y    : (ndarray  Shape (m,) or (m,1))  target value of each example
      yhat : (ndarray  Shape (m,) or (m,1))  predicted value of each example
    Returns:
      err: (scalar)             
    """
    m = len(y)
    err = 0.0
    for i in range(m):
        
    ### START CODE HERE ### 
        curr_err = (yhat[i] - y[i]) ** 2
        err += curr_err
    err /= 2*m
    ### END CODE HERE ### 
    
    return(err)
