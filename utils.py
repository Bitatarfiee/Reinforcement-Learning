
import numpy as np
from matplotlib import pyplot as plt


def getpolicy(Q):
    """ 
    Get best policy matrix from the Q-matrix.

    """

    P = np.argmax(Q, axis = 2)

    return P


def getvalue(Q):
    """ 
    Get best value matrix from the Q-matrix.
 
    """
    
    V = np.max(Q, axis = 2)

    return V

