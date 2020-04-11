# More efficient sampled softmax for TensorFlow

This code is simplifies and improves the existing implementation of sampled softmax loss in TensorFlow.
It is based on a simplified graph for forward and backward passes.
When tested on Google Colab hardware a speedup of about 2x is observed.
