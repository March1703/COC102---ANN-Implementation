'''
Created on Feb 20, 2017

@author: Inthuch Therdchanakul
'''
import random
import numpy as np

class Perceptron():
    def __init__(self, n_inputs ):
        self.n_inputs = n_inputs
        self.set_weights( np.array([random.uniform(-2./n_inputs,2./n_inputs) for _ in range(0,n_inputs+1)])) # +1 for bias weight
        self.delta_weights = np.zeros(n_inputs+1)
        self.delta = None
        self.u = None

    def set_weights(self, weights ):
        self.weights = weights

    def __str__(self):
        return 'u: %s, Bias: %s, Weight: %s, Delta: %s' % ( str(self.u), str(self.weights[0]),str(self.weights[1:]), str(self.delta) )

class PerceptronLayer():
    def __init__(self, n_perceptrons, n_inputs):
            self.n_perceptrons = n_perceptrons
            self.perceptrons = np.array([Perceptron( n_inputs ) for _ in range(0,self.n_perceptrons)])

    def __str__(self):
        return 'Layer:\n\t'+'\n\t'.join([str(perceptron) for perceptron in self.perceptrons])+''

class MLP():
    def __init__(self, n_inputs, n_outputs, n_perceptrons_to_hl, n_hidden_layers):
        self.n_inputs = n_inputs
        self.n_outputs = n_outputs
        self.n_hidden_layers = n_hidden_layers
        self.n_perceptrons_to_hl = n_perceptrons_to_hl

        self.create_network()
        self._n_weights = None
        # end

    def create_network(self):
        if self.n_hidden_layers>0:
            # create the input layer
            self.layers = [PerceptronLayer( self.n_inputs,self.n_inputs )]

            # create hidden layers
            self.layers += [PerceptronLayer( self.n_perceptrons_to_hl,self.n_inputs ) for _ in range(0,self.n_hidden_layers)]

            # hidden-to-output layer
            self.layers += [PerceptronLayer( self.n_outputs,self.n_perceptrons_to_hl )]
        else:
            # If we don't require hidden layers
            self.layers = [PerceptronLayer( self.n_outputs,self.n_inputs )]
        self.layers = np.asarray(self.layers)
        
        for perceptron in self.layers[0].perceptrons:
            perceptron.set_weights(np.array([None,None]))

    def __str__(self):
        return '\n'.join([str(i+1)+' '+str(layer) for i,layer in enumerate(self.layers)])