# UNQ_C4
# GRADED FUNCTION: get_best_split

def get_best_split(X, y, node_indices):   
    """
    Returns the optimal feature and threshold value
    to split the node data 
    
    Args:
        X (ndarray):            Data matrix of shape(n_samples, n_features)
        y (array like):         list or ndarray with n_samples containing the target variable
        node_indices (ndarray): List containing the active indices. I.e, the samples being considered in this step.

    Returns:
        best_feature (int):     The index of the best feature to split
    """    
    
    # Some useful variables
    num_features = X.shape[1]
    
    # You need to return the following variables correctly
    best_feature = -1
    
    ### START CODE HERE ###
    highest_information_gain = 0
    for i in range(num_features):
        curr_information_gain = compute_information_gain(X, y, node_indices, i)
        if curr_information_gain > highest_information_gain:
            highest_information_gain = curr_information_gain
            best_feature = i
            
    ### END CODE HERE ##    
   
    return best_feature