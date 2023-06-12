# UNQ_C2
# GRADED CELL: Sequential model
tf.random.set_seed(1234) # for consistent results
model = Sequential(
    [               
        ### START CODE HERE ### 
        tf.keras.Input(shape=(400,)),  
        tf.keras.layers.Dense(units=25, activation="relu", name="L1"),
        tf.keras.layers.Dense(units=15, activation="relu", name="L2"),
        tf.keras.layers.Dense(units=10, activation="linear", name="L3"),

        ### END CODE HERE ### 
    ], name = "my_model" 
)