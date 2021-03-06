import numpy as np

labels = np.array(['Acoustic schwannoma (vestibular schwannoma)', 'Meningioma',
       'atypical meningioma', 'Metastasis', 'arachnoid cyst',
       'epidermoid cyst', 'glomus jugulare paraganglioma',
       'jugular schwannoma ', 'lipoma', 'Trigeminal schwannoma '],
      dtype=object)

all_features = np.array(['Icecream', 'Solid', 'Cystic', 'Crossing', 'Homogenous', 
'Heterogeneous', 'Diffusion', 'Calcification', 'Fat', 'Hemorrhagic', 
'tail', 'Leptomeningeal', 'Bilateral', 'jugular', 'Signal'], dtype=object)

prevalence = np.array([0.17333333, 0.16      , 0.08      , 0.08      , 0.08666667,
       0.10666667, 0.12      , 0.06666667, 0.04      , 0.08666667])

positive = np.array([[0.81 , 0.36 , 0.21 , 0.085, 0.01 , 0.035, 0.01 , 0.01 , 0.06 ,
        0.01 ],
       [1.01 , 1.01 , 1.01 , 1.01 , 0.01 , 0.01 , 1.01 , 1.01 , 1.01 ,
        1.01 ],
       [0.06 , 0.06 , 0.06 , 0.11 , 1.01 , 1.01 , 0.01 , 0.035, 0.01 ,
        0.035],
       [0.01 , 0.01 , 0.01 , 0.085, 0.06 , 0.085, 0.01 , 0.01 , 0.01 ,
        1.01 ],
       [0.66 , 0.91 , 0.36 , 0.56 , 0.01 , 0.01 , 0.46 , 0.51 , 0.01 ,
        0.56 ],
       [0.56 , 0.16 , 0.76 , 0.46 , 0.01 , 0.01 , 0.66 , 0.56 , 0.01 ,
        0.46 ],
       [0.02 , 0.085, 0.81 , 0.11 , 0.01 , 0.96 , 0.01 , 0.01 , 0.01 ,
        0.02 ],
       [0.015, 0.21 , 0.21 , 0.06 , 0.01 , 0.01 , 0.135, 0.085, 0.06 ,
        0.035],
       [0.01 , 0.01 , 0.01 , 0.01 , 0.01 , 0.01 , 0.01 , 0.01 , 1.01 ,
        0.01 ],
       [0.06 , 0.06 , 0.16 , 0.16 , 0.02 , 0.02 , 0.085, 0.085, 0.01 ,
        0.06 ],
       [0.16 , 0.86 , 0.86 , 0.06 , 0.01 , 0.01 , 0.01 , 0.01 , 0.06 ,
        0.085],
       [0.01 , 0.01 , 0.01 , 1.01 , 0.01 , 0.06 , 0.01 , 0.01 , 0.06 ,
        0.01 ],
       [0.085, 0.085, 0.035, 0.21 , 0.02 , 0.02 , 0.01 , 0.01 , 0.01 ,
        0.085],
       [0.01 , 0.01 , 0.01 , 0.085, 0.01 , 0.02 , 1.01 , 1.01 , 0.01 ,
        0.01 ],
       [0.06 , 0.06 , 0.06 , 0.11 , 0.01 , 0.015, 0.76 , 0.01 , 0.01 ,
        0.06 ]])

negative = np.array([[0.69530704, 0.86458091, 0.92100553, 0.96802605, 0.99623836,
        0.98683425, 0.99623836, 0.99623836, 0.97743015, 0.99623836],
       [0.90824768, 0.90824768, 0.90824768, 0.90824768, 0.99909156,
        0.99909156, 0.90824768, 0.90824768, 0.90824768, 0.90824768],
       [0.97428011, 0.97428011, 0.97428011, 0.95284687, 0.56704854,
        0.56704854, 0.99571335, 0.98499673, 0.99571335, 0.98499673],
       [0.99399347, 0.99399347, 0.99399347, 0.94894445, 0.96396079,
        0.94894445, 0.99399347, 0.99399347, 0.99399347, 0.39333999],
       [0.89778804, 0.85907139, 0.94424802, 0.9132747 , 0.99845133,
        0.99845133, 0.92876136, 0.92101803, 0.99845133, 0.9132747 ],
       [0.90669617, 0.97334176, 0.87337337, 0.92335757, 0.99833386,
        0.99833386, 0.89003477, 0.90669617, 0.99833386, 0.92335757],
       [0.99047477, 0.95951778, 0.61422822, 0.94761124, 0.99523739,
        0.54278901, 0.99523739, 0.99523739, 0.99523739, 0.99047477],
       [0.99748574, 0.96480041, 0.96480041, 0.98994297, 0.99832383,
        0.99832383, 0.97737169, 0.98575255, 0.98994297, 0.9941334 ],
       [0.99201132, 0.99201132, 0.99201132, 0.99201132, 0.99201132,
        0.99201132, 0.99201132, 0.99201132, 0.19314289, 0.99201132],
       [0.99348972, 0.99348972, 0.98263926, 0.98263926, 0.99782991,
        0.99782991, 0.99077711, 0.99077711, 0.99891495, 0.99348972],
       [0.93437239, 0.64725158, 0.64725158, 0.97538964, 0.99589827,
        0.99589827, 0.99589827, 0.99589827, 0.97538964, 0.96513533],
       [0.9931446 , 0.9931446 , 0.9931446 , 0.30760467, 0.9931446 ,
        0.9588676 , 0.9931446 , 0.9931446 , 0.9588676 , 0.9931446 ],
       [0.98167603, 0.98167603, 0.99245483, 0.95472901, 0.99784424,
        0.99568848, 0.99784424, 0.99784424, 0.99784424, 0.98167603],
       [0.99447644, 0.99447644, 0.99447644, 0.95304973, 0.99447644,
        0.98895288, 0.44212033, 0.44212033, 0.99447644, 0.99447644],
       [0.97371279, 0.97371279, 0.97371279, 0.95180678, 0.9956188 ,
        0.9934282 , 0.66702864, 0.9956188 , 0.9956188 , 0.97371279]])

def cpa_calculator(user_input, positive, negative, all_features, labels,prevalence):
  postive_list = [1 if item in user_input else 0 for item in all_features]
  postive_array = np.array(postive_list).reshape(15,1)  #change the number g=here
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