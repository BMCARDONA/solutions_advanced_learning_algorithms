# UNQ_C3
# GRADED FUNCTION: compute_information_gain

def compute_information_gain(X, y, node_indices, feature):
    
    """
    Compute the information of splitting the node on a given feature
    
    Args:
        X (ndarray):            Data matrix of shape(n_samples, n_features)
        y (array like):         list or ndarray with n_samples containing the target variable
        node_indices (ndarray): List containing the active indices. I.e, the samples being considered in this step.
   
    Returns:
        cost (float):        Cost computed
    
    """    
    # Split dataset
    left_indices, right_indices = split_dataset(X, node_indices, feature)
    
    # Some useful variables
    #     X_node, y_node = X[node_indices], y[node_indices]
    #     X_left, y_left = X[left_indices], y[left_indices]
    #     X_right, y_right = X[right_indices], y[right_indices]
    
    # You need to return the following variables correctly
#     information_gain = 0
    
    ### START CODE HERE ###
    
    root_entropy = compute_entropy(y[node_indices])
    left_indices, right_indices = split_dataset(X, node_indices, feature)
    left_entropy = compute_entropy(y[left_indices])
    right_entropy = compute_entropy(y[right_indices])
    w_left = len(left_indices) / len(node_indices)
    w_right = len(right_indices) / len(node_indices)
    information_gain = root_entropy - (w_left*left_entropy + w_right*right_entropy)

    ### END CODE HERE ###  
    
    return information_gain