import numpy as np

def calculate(list):

  try:  
    arr = np.array(list)
    a = np.reshape(arr,(3,3))
  except ValueError:
    raise ValueError("List must contain nine numbers.")
  else:
   m1 = a.mean(axis=0).tolist()
   m2 = a.mean(axis=1).tolist()
   mf = a.mean().tolist()
   v1 = a.var(axis=0).tolist()
   v2 = a.var(axis=1).tolist()
   vf = a.var().tolist()
   s1 = a.std(axis=0).tolist()
   s2 = a.std(axis=1).tolist()
   sf = a.std().tolist()
   ma1 = a.max(axis=0).tolist()
   ma2 = a.max(axis=1).tolist()
   maf = a.max().tolist()
   mi1 = a.min(axis=0).tolist()
   mi2 = a.min(axis=1).tolist()
   mif = a.min().tolist()
   su1 = a.sum(axis=0).tolist()
   su2 = a.sum(axis=1).tolist()
   suf = a.sum().tolist()
  
  calculations = {
  'mean': [m1, m2, mf],
  'variance': [v1,v2,vf],
  'standard deviation': [s1, s2, sf],
  'max': [ma1, ma2, maf],
  'min': [mi1, mi2, mif],
  'sum': [su1, su2, suf]
  }


  return calculations
