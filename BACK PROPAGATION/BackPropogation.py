import numpy as np
x=np.array(([2,9],[1,5],[3,6]),dtype=float)
y=np.array(([92],[86],[89]),dtype=float)
x=x/np.amax(x,axis=0)
y=y/100

def sigmoid(x):
    return 1/(1+np.exp(-x))

def derivaties_sigmoid(x):
    return x*(1-x)
epoch=5000
lr=0.1
inputlayer_neurons=2
hiddenlayer_neurons=3
output_neurons=1
wh=np.random.uniform(size=(inputlayer_neurons,hiddenlayer_neurons))
bh=np.random.uniform(size=(1,hiddenlayer_neurons))

wout=np.random.uniform(size=(hiddenlayer_neurons,output_neurons))

bout=np.random.uniform(size=(1,output_neurons))

for i in range(epoch):
    hinp1=np.dot(x,wh)
    hinp=hinp1+bh
    hlayer_act=sigmoid(hinp)
    outinp1=np.dot(hlayer_act,wout)
    outinp=outinp1+bout
    output=sigmoid(outinp)
    

    eo=y-output
    outgrad=derivaties_sigmoid(output)
    d_output=eo*outgrad
    eh=d_output.dot(wout.T)
    
    
    hiddengrad=derivaties_sigmoid(hlayer_act)
    d_hiddenlayer=eh*hiddengrad
    
    wout+=hlayer_act.T.dot(d_output)*lr
    wh+=x.T.dot(d_hiddenlayer)*lr
    
print("Input:\n"+str(x))
print("Actual Output :\n"+str(y))
print("Predicted Output :\n",output)
    

# OUTPUT:
# Inpput:
# [[0.66666667 1.        ]
#  [0.33333333 1.        ]
#  [1.         0.66666667]]
# Actual:
# [[0.92]
#  [0.86]
#  [0.89]]
# Predicted:
#  [[0.89155219]
#  [0.88386888]
#  [0.89127146]]                               