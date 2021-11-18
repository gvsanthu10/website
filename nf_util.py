import numpy as np

all_features = ['Target', 'Fascicular', 'rim', 'enhancement', 'diffuse']       

positive = np.array([[0.79, 0.21],
       [0.4 , 0.6 ],
       [0.12, 0.88],
       [0.9 , 0.1 ],
       [0.16, 0.84]])

negative = np.array([[0.8, 1. ],
       [1. , 0.6],
       [1. , 0.7],
       [0.8, 1. ],
       [1. , 0.8]])

labels = np.array(['Neurofibroma', 'Neurilemmoma'])

def nf_calculator(user_input, positive, negative, all_features, labels):
  postive_list = [1 if item in user_input else 0 for item in all_features]
  postive_array = np.array(postive_list).reshape(5,1)  #change the number g=here
  neg_array = 1- postive_array
  
  pos_multi = np.multiply(positive,postive_array)
  neg_multi = np.multiply(negative,neg_array)
  
  total_sum = pos_multi + neg_multi
  
  pre_normalize = np.prod(total_sum, axis=0)
  
  normalized = pre_normalize/pre_normalize.sum()
  
  tuple_list = list(zip(normalized, labels))
  
  result = {}
  for i in range(2):
    result[tuple_list[i][1]] = tuple_list[i][0]
  
  return result