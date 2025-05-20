import numpy as np
import tensorflow as tf

# npz 파일 로드
with np.load('mnist_offline/mnist.npz') as data:
    x_train, y_train = data['x_train'], data['y_train']
    x_test, y_test = data['x_test'], data['y_test']

train_ds = tf.data.Dataset.from_tensor_slices((x_train, y_train)).batch(64).shuffle(10000)
test_ds = tf.data.Dataset.from_tensor_slices((x_test, y_test)).batch(64)

# 예시 출력
print("Train shape:", x_train.shape, y_train.shape)
print("Test shape:", x_test.shape, y_test.shape)