import tensorflow as tf
def activation_summary(W): 
  ''' shamelessly stolen from CIFAR 10 in TF tutorial  :) ''' 

  tf.summary.histogram(W.op.name + '/activations', W)
  tf.summary.scalar(W.op.name + '/sparsity', tf.nn.zero_fraction(W))
