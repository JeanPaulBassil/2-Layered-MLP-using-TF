import tensorflow as tf
import time

input = [
    [0, 0],
    [0, 1],
    [1 ,0],
    [1 ,1]
]

output = [[0], [1], [1], [0]]

model = tf.keras.Sequential()

model.add(tf.keras.layers.Dense(2, input_dim=2, activation='sigmoid'))

model.add(tf.keras.layers.Dense(1, activation='sigmoid'))

model.compile(loss='binary_crossentropy',
              optimizer='adam',
              metrics=['binary_accuracy'])

start = time.time()
model.fit(input, output, epochs=1500, verbose=1)
end = time.time()


print("\nModel Evaluation:")
trainingTime = end - start
loss, accuracy = model.evaluate(input, output)
print(f"Loss: {loss}, Accuracy: {accuracy}, time: {round(trainingTime, 2)}s")

print("\nPrediction:")
predictions = model.predict(input)
print(predictions.round())