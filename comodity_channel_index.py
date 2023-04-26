import numpy as np
"""
Example 


"""
def sma (array, period ):

    sma = np.empty_like(array)
    sma = np.full( sma.shape , np.nan)

    for i in range(period, len(array)+1 ):
          sma[i-1] = np.mean(array[i-period:i] , dtype=np.float32 )
    return sma 

def cci(self, period):

    typical_price = sum(high+low+close) / 3    
    typical_ma = sma( typical_price , period )
    mean_deviation = sma(   deviation( typical_price , typical_ma ) , period )
    cci = ( typical_price - typical_ma ) / 0.15 * mean_deviation
    return cci

def deviation( typical_price , typical_ma ):

    return abs(typical_price - typical_ma)
