import numpy as np

labels = np.array(['Benign', 'Malignant'],  dtype=object)

all_features = np.array(['4', '4to7', '8to20', '20', 'Nocal', 'Diffuse', 
                         'Central', 'Ring', 'Concentric', 'Popcorn', 
                         'Strippled', 'Eccentric', 'fatpresent', 'fatabsent', 
                         'Smmothmargin', 'Lobulated', 'Spiculated', 
                         'airpresent', 'airabsent', 'Solid', 'onglygg', 
                         'partsolid'], dtype=object)


positive = np.array([[0.99 , 0.01 ],
       [0.925, 0.075],
       [0.7  , 0.3  ],
       [0.2  , 0.8  ],
       [0.5  , 0.5  ],
       [0.95 , 0.05 ],
       [0.95 , 0.05 ],
       [0.925, 0.075],
       [0.9  , 0.1  ],
       [0.95 , 0.05 ],
       [0.075, 0.925],
       [0.05 , 0.95 ],
       [0.99 , 0.01 ],
       [0.5  , 0.5  ],
       [0.95 , 0.05 ],
       [0.5  , 0.5  ],
       [0.075, 0.925],
       [0.1  , 0.9  ],
       [0.5  , 0.5  ],
       [0.5  , 0.5  ],
       [0.82 , 0.18 ],
       [0.35 , 0.65 ]])

negative = np.array([[1., 1.],
       [1., 1.],
       [1., 1.],
       [1., 1.],
       [1., 1.],
       [1., 1.],
       [1., 1.],
       [1., 1.],
       [1., 1.],
       [1., 1.],
       [1., 1.],
       [1., 1.],
       [1., 1.],
       [1., 1.],
       [1., 1.],
       [1., 1.],
       [1., 1.],
       [1., 1.],
       [1., 1.],
       [1., 1.],
       [1., 1.],
       [1., 1.]])

def solpulnodule1_calculator(user_input, positive, negative, all_features, labels):
  postive_list = [1 if item in user_input else 0 for item in all_features]
  postive_array = np.array(postive_list).reshape(22,1)  #change the number g=here
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