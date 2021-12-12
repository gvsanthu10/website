import numpy as np

labels = np.array(['Benign', 'Malignant'], dtype=object)

all_features = np.array(['4', '4to15', '15', 'Smooth', 'Nodular', 'Smmothmargin', 'Spiculated'], dtype=object)

positive = np.array([[0.99, 0.01],
       [0.5 , 0.5 ],
       [0.01, 0.99],
       [0.95, 0.05],
       [0.01, 0.99],
       [0.9 , 0.1 ],
       [0.05, 0.95]])

negative = np.array([[1., 1.],
       [1., 1.],
       [1., 1.],
       [1., 1.],
       [1., 1.],
       [1., 1.],
       [1., 1.]])

def solpulnodule_calculator(user_input, positive, negative, all_features, labels):
  postive_list = [1 if item in user_input else 0 for item in all_features]
  postive_array = np.array(postive_list).reshape(7,1)  #change the number g=here
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