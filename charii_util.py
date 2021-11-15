import numpy as np

labels = np.array(['Chiari Malformation Type-I',	
                   'Idiopathic Intracranial Hypertension', 	
                   'Intracranial Hypotension'], dtype=object)

all_features = np.array(['ectopia', 'Pointed', 'optic', 'tortous', 'Flattening', 
                         'empty', 'Meckel', 'Pachymeningeal', 'Venous', 
                         'pituitary', 'penis', 'mammilopontine', 
                         'Interpeduncular'], dtype=object)

positive = np.array([[1.   , 0.925, 0.925],
       [0.95 , 0.2  , 0.05 ],
       [0.2  , 0.55 , 0.05 ],
       [0.1  , 0.45 , 0.05 ],
       [0.08 , 0.9  , 0.05 ],
       [0.5  , 0.72 , 0.05 ],
       [0.25 , 0.75 , 0.05 ],
       [0.05 , 0.05 , 0.975],
       [0.05 , 0.05 , 0.9  ],
       [0.05 , 0.05 , 0.75 ],
       [0.05 , 0.05 , 0.8  ],
       [0.05 , 0.05 , 0.925],
       [0.05 , 0.05 , 0.9  ]])

negative = np.array([[0.99937496, 0.99942184, 0.99942184],
       [0.58266385, 0.91213976, 0.97803494],
       [0.94153531, 0.83922209, 0.98538383],
       [0.96567045, 0.84551705, 0.98283523],
       [0.95373116, 0.47947559, 0.97108198],
       [0.87141867, 0.81484289, 0.98714187],
       [0.91543629, 0.74630887, 0.98308726],
       [0.96701948, 0.96701948, 0.35687977],
       [0.96794981, 0.96794981, 0.42309662],
       [0.97019626, 0.97019626, 0.55294397],
       [0.9693812 , 0.9693812 , 0.51009917],
       [0.96762745, 0.96762745, 0.40110787],
       [0.96794981, 0.96794981, 0.42309662]])

def charii_calculator(user_input, positive, negative, all_features, labels):
  postive_list = [1 if item in user_input else 0 for item in all_features]
  postive_array = np.array(postive_list).reshape(13,1)  #change the number g=here
  neg_array = 1- postive_array
  
  pos_multi = np.multiply(positive,postive_array)
  neg_multi = np.multiply(negative,neg_array)
  
  total_sum = pos_multi + neg_multi
  
  row_wise_sum = np.prod(total_sum, axis=0)
  
  #pre_normalize = np.multiply(row_wise_sum, prevalence)
  pre_normalize= row_wise_sum
  normalized = pre_normalize/pre_normalize.sum()
  
  list1, list2 = (list(t) for t in zip(*sorted(zip(normalized, labels))))
  
  result = {}
  for i in range(3):
    result[str(list2[::-1][i])] = round(list1[::-1][i],5)
  
  return result