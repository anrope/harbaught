import pybrain.structure

nn = pybrain.structure.FeedForwardNetwork()

in_layer = pybrain.structure.LinearLayer(4, name='in')
hidden_layer = pybrain.structure.SigmoidLayer(7, name='hidden')
out_layer = pybrain.structure.LinearLayer(10, name='out')

nn.addInputModule(in_layer)
nn.addModule(hidden_layer)
nn.AddOutputModule(out_layer)

in_to_hidden = pybrain.structure.FullConnection(in_layer, hidden_layer)
hidden_to_out = pybrain.structure.FullConnection(hidden_layer, out_layer)

n.addConnection(in_to_hidden)
n.addConnection(hidden_to_out)

n.sortModules()
