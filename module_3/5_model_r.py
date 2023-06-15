# UNQ_C5
# GRADED CELL: model_r

tf.random.set_seed(1234)
model_r = Sequential(
    [
        
        ### START CODE HERE ### 
        Dense(units=120, activation="relu", kernel_regularizer=tf.keras.regularizers.l2(0.1)),
        Dense(units=40, activation="relu", kernel_regularizer=tf.keras.regularizers.l2(0.1)),
        Dense(units=6, activation="linear")
        ### START CODE HERE ### 
        
    ], name= None
)
model_r.compile(
    
    ### START CODE HERE ### 
    loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
    optimizer=tf.keras.optimizers.Adam(learning_rate=0.01),
    ### START CODE HERE ### 
    
)
