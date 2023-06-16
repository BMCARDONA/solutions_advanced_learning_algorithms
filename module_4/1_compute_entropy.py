# UNQ_C1
# GRADED FUNCTION: compute_entropy

def compute_entropy(y):
    """
    Computes the entropy for 
    
    Args:
       y (ndarray): Numpy array indicating whether each example at a node is
           edible (`1`) or poisonous (`0`)
       
    Returns:
        entropy (float): Entropy at that node
        
    """
    # You need to return the following variables correctly
    entropy = 0.
    
    ### START CODE HERE ###
    if len(y) != 0:
        edible_count = 0
        for i in range(len(y)):
            if y[i] == 1:
                edible_count += 1
        p_1 = edible_count / len(y)
        if p_1 == 0 or p_1 == 1:
            return 0
        entropy = -1 * p_1 * np.log2(p_1) - (1 - p_1) * np.log2(1 - p_1)        
    ### END CODE HERE ###        
    
    return entropy