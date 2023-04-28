import numpy as np
"""
Example 


"""
close = np.array( np.round(bar.Close , 2) , dtype=np.float32 )
close = np.nan_to_num(close, nan=0)

high =   np.array( np.round(bar.High , 2) , dtype=np.float32)
high = np.nan_to_num(high, nan=0)

low =  np.array( np.round(bar.Low , 2 ) , dtype=np.float32 )
low = np.nan_to_num(low, nan=0)

def sma (array, period ):
  import numpy as np
  sma = np.empty_like(array , dtype =np.float32 )
  sma = np.full( sma.shape , np.nan)

  for i in range(period, len(array)+1 ):
        sma[i-1] = np.mean(array[i-period:i]) 
  return sma 

def deviation(typical_price , typical_ma ):
     
    return abs(typical_price - typical_ma)
    

def cci( period ):

    typical_price = np.mean((np.hstack((high , low , close)).reshape(-1,3) ), axis=1 )
    # mean(typical)
    typical_ma = sma( typical_price , period )
    typical_ma[:period-1] = (typical_price[:period-1] * 1/period) + typical_price[:period-1]
    dev = deviation( typical_price , typical_ma ) 
    mean_deviation = sma( dev  , period) 
    mean_deviation[:period-1] =  (dev[:period-1] * 1/period) + dev[:period-1]

    cci = ( typical_price - typical_ma ) / ( 0.015 * mean_deviation ) 
    
    return  cci


