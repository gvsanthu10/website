import numpy as np

labels = np.array(['Benign', 'Malignant'],  dtype=object)

all_features = np.array(['macro', 'micro', 'well', 'spiculations', 'Angular', 
                         'Noangular', 'Thick', 'Thin', 'taller', 'wider', 
                         'hypoechoic', 'isoechoic', 'shadowing', 'noshadowing', 
                         'Heterogeneous', 'Homogeneous', 'calcificaitons', 
                         'nocalcificaitons', 'Internal', 'Peripheral'], dtype=object)


positive = np.array([[0.95 , 0.2  ],
       [0.15 , 0.75 ],
       [0.95 , 0.5  ],
       [0.01 , 0.5  ],
       [0.05 , 0.8  ],
       [0.95 , 0.2  ],
       [0.35 , 0.6  ],
       [0.95 , 0.25 ],
       [0.1  , 0.5  ],
       [0.975, 0.5  ],
       [0.1  , 0.75 ],
       [0.95 , 0.36 ],
       [0.075, 0.6  ],
       [0.925, 0.38 ],
       [0.15 , 0.85 ],
       [0.85 , 0.15 ],
       [0.05 , 0.27 ],
       [0.95 , 0.73 ],
       [0.35 , 0.9  ],
       [0.7  , 0.075]])

negative = np.array([[0.68324936, 0.93331565],
       [0.94750336, 0.73751679],
       [0.93289474, 0.96468144],
       [0.99139236, 0.56961791],
       [0.96613791, 0.4582066 ],
       [0.68324936, 0.93331565],
       [0.98230793, 0.96967074],
       [0.75137035, 0.93457115],
       [0.96500224, 0.82501119],
       [0.92574546, 0.96192075],
       [0.95225598, 0.64191982],
       [0.85586656, 0.94538101],
       [0.96274441, 0.70195527],
       [0.87998123, 0.95069499],
       [0.94147606, 0.66836433],
       [0.66836433, 0.94147606],
       [0.98126312, 0.89882086],
       [0.98821382, 0.99094325],
       [0.94940758, 0.86990521],
       [0.62108051, 0.95940148]])


def breast_calculator(user_input, positive, negative, all_features, labels):
  postive_list = [1 if item in user_input else 0 for item in all_features]
  postive_array = np.array(postive_list).reshape(20,1)  #change the number g=here
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