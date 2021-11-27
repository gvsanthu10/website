import numpy as np

labels = np.array(['Chronic prostatitis', 'Granulomatous prostatitis',
       'Glandular hyperplastic nodule', 'Stromal hyperplastic nodule ',
       'Displaced normal central zone into the Transitional zone',
       'Hypertrophy of the anterior fibromuscular stroma',
       'Prostate Cancer', 'Hemorrhage (post-biopsy)'], dtype=object)

all_features = np.array(['Mass', 'illmargins', 'Amorphous', 'fibromuscular', 
                         'opposite', 'antfibromuscular', 'central', 'T2', 
                         'highT2', 'Diffusion', 'Enhancement', 
                         'Minimal', 'blood'], dtype=object)

prevalence = np.array([0.11111111, 0.09259259, 0.18518519, 0.18518519, 0.11111111,
       0.11111111, 0.11111111, 0.09259259])

positive = np.array([[0.085, 0.26 , 0.26 , 0.26 , 0.01 , 0.01 , 0.76 , 0.06 ],
       [0.26 , 0.26 , 0.11 , 0.11 , 0.11 , 0.01 , 0.81 , 0.06 ],
       [0.91 , 0.86 , 0.16 , 0.16 , 0.01 , 0.01 , 0.91 , 0.11 ],
       [0.02 , 0.31 , 0.02 , 0.02 , 0.01 , 0.01 , 0.46 , 0.01 ],
       [0.01 , 0.21 , 0.06 , 0.06 , 0.01 , 0.01 , 0.21 , 0.06 ],
       [0.06 , 0.02 , 0.02 , 0.02 , 0.01 , 1.01 , 0.02 , 0.02 ],
       [0.06 , 0.06 , 0.06 , 0.06 , 1.01 , 0.01 , 0.06 , 0.01 ],
       [0.86 , 0.76 , 0.21 , 0.86 , 1.01 , 1.01 , 0.96 , 0.96 ],
       [0.01 , 0.01 , 0.91 , 0.41 , 0.01 , 0.01 , 0.085, 0.06 ],
       [0.31 , 0.31 , 0.16 , 0.31 , 0.31 , 0.26 , 0.985, 0.96 ],
       [0.01 , 0.06 , 0.11 , 0.11 , 0.01 , 0.01 , 0.96 , 0.02 ],
       [0.71 , 0.36 , 0.76 , 0.76 , 0.085, 0.085, 0.01 , 0.31 ],
       [0.01 , 0.02 , 0.02 , 0.02 , 0.01 , 0.01 , 0.06 , 1.01 ]])

negative = np.array([[0.97828009, 0.93356264, 0.93356264, 0.93356264, 0.99744472,
        0.99744472, 0.80579849, 0.9846683 ],
       [0.93967012, 0.93967012, 0.97447582, 0.97447582, 0.97447582,
        0.99767962, 0.81204922, 0.98607772],
       [0.7602913 , 0.77346211, 0.95785342, 0.95785342, 0.99736584,
        0.99736584, 0.7602913 , 0.97102422],
       [0.99077497, 0.85701202, 0.99077497, 0.99077497, 0.99538748,
        0.99538748, 0.78782429, 0.99538748],
       [0.99770176, 0.95173691, 0.98621055, 0.98621055, 0.99770176,
        0.99770176, 0.95173691, 0.98621055],
       [0.9593502 , 0.98645007, 0.98645007, 0.98645007, 0.99322503,
        0.31572842, 0.98645007, 0.98645007],
       [0.96831995, 0.96831995, 0.96831995, 0.96831995, 0.46671923,
        0.99471999, 0.96831995, 0.99471999],
       [0.9755915 , 0.9784297 , 0.99403978, 0.9755915 , 0.9713342 ,
        0.9713342 , 0.9727533 , 0.9727533 ],
       [0.9952058 , 0.9952058 , 0.56372794, 0.80343786, 0.9952058 ,
        0.9952058 , 0.95924931, 0.97123481],
       [0.97006914, 0.97006914, 0.98455181, 0.97006914, 0.97006914,
        0.97489669, 0.90489709, 0.90731087],
       [0.99461701, 0.96770204, 0.94078708, 0.94078708, 0.99461701,
        0.99461701, 0.48323271, 0.98923401],
       [0.87988016, 0.93909417, 0.87142102, 0.87142102, 0.98561946,
        0.98561946, 0.99830817, 0.94755331],
       [0.99291782, 0.98583565, 0.98583565, 0.98583565, 0.99291782,
        0.99291782, 0.95750694, 0.2847002 ]])


def prostate_calculator(user_input, positive, negative, all_features, labels,prevalence):
  postive_list = [1 if item in user_input else 0 for item in all_features]
  postive_array = np.array(postive_list).reshape(13,1)  #change the number g=here
  neg_array = 1- postive_array
  
  pos_multi = np.multiply(positive,postive_array)
  neg_multi = np.multiply(negative,neg_array)
  
  total_sum = pos_multi + neg_multi
  
  row_wise_sum = np.prod(total_sum, axis=0)
  
  pre_normalize = np.multiply(row_wise_sum, prevalence)
  pre_normalize= row_wise_sum
  normalized = pre_normalize/pre_normalize.sum()
  
  list1, list2 = (list(t) for t in zip(*sorted(zip(normalized, labels))))
  
  result = {}
  for i in range(5):
    result[str(list2[::-1][i])] = round(list1[::-1][i],5)
  
  return result