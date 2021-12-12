import numpy as np

labels = np.array(['Neuroglial cyst', 'Connatal cyst', 'Subependymal pseudocyst',
       'Cyst(s) of periventricular leukomalacia',
       'Choroidal fissure cyst', 'Intraparenchymal ependymal cyst',
       'Abscess', 'Tubercloma', 'Hydatid cyst',
       'Neurocysticercosis (NCC)', 'Toxoplasmosis',
       'Enlarged Virchow Robin space (perivascular space)',
       'Porenchyhalic cyst (if it is communicating with the ventricle)'],
      dtype=object)

all_features = np.array(['Pediatrics', 'Adult', 'Solitary', 'Multiple', 
'cystic', 'dot', 'White', 'volume', 'Caseating', 'Enhanced', 'Hemorrhage', 
'Calcification', 'Restricteddot', 'Restrictedcavity', 'frontal', 'caudothalamic', 'choroid'],
      dtype=object)

prevalence = np.array([0.13793103, 0.06896552, 0.04597701, 0.04597701, 0.09195402,
       0.04597701, 0.09195402, 0.06896552, 0.04597701, 0.06896552,
       0.05747126, 0.13793103, 0.09195402])

positive = np.array([[0.56 , 0.935, 1.01 , 1.01 , 0.36 , 0.11 , 0.41 , 0.41 , 0.16 ,
        0.16 , 0.16 , 0.26 , 0.26 ],
       [0.56 , 0.11 , 0.015, 0.01 , 0.96 , 0.91 , 0.66 , 0.76 , 0.86 ,
        0.86 , 0.86 , 0.91 , 0.81 ],
       [0.985, 0.56 , 0.91 , 0.085, 0.985, 1.01 , 0.81 , 0.56 , 0.76 ,
        0.16 , 0.56 , 0.36 , 0.91 ],
       [0.035, 0.56 , 0.16 , 0.96 , 0.06 , 0.01 , 0.16 , 0.46 , 0.31 ,
        0.91 , 0.46 , 0.81 , 0.11 ],
       [0.01 , 0.01 , 0.01 , 0.01 , 0.01 , 0.01 , 0.06 , 0.21 , 0.96 ,
        0.01 , 0.01 , 0.01 , 0.01 ],
       [0.01 , 0.01 , 0.01 , 0.01 , 0.01 , 0.01 , 0.01 , 0.41 , 0.01 ,
        1.01 , 0.21 , 0.01 , 0.01 ],
       [0.06 , 0.06 , 0.11 , 0.61 , 0.015, 0.06 , 0.985, 0.46 , 0.06 ,
        0.31 , 0.86 , 0.06 , 0.11 ],
       [0.01 , 0.01 , 0.085, 0.985, 0.01 , 0.01 , 0.01 , 0.01 , 0.01 ,
        0.01 , 0.01 , 0.02 , 0.16 ],
       [0.01 , 0.01 , 0.01 , 0.01 , 0.01 , 0.01 , 0.01 , 0.91 , 0.01 ,
        0.085, 0.06 , 0.01 , 0.01 ],
       [0.035, 0.06 , 0.02 , 0.01 , 0.01 , 0.01 , 1.01 , 1.01 , 0.11 ,
        0.91 , 1.01 , 0.01 , 0.085],
       [0.06 , 0.06 , 0.035, 0.01 , 0.01 , 0.02 , 0.01 , 0.01 , 0.16 ,
        0.085, 0.01 , 0.01 , 0.035],
       [0.01 , 0.01 , 0.01 , 0.01 , 0.01 , 0.01 , 0.01 , 0.26 , 0.16 ,
        0.21 , 0.01 , 0.01 , 0.02 ],
       [0.01 , 0.01 , 0.01 , 0.01 , 0.01 , 0.01 , 0.01 , 0.76 , 0.015,
        0.36 , 0.01 , 0.01 , 0.01 ],
       [0.015, 0.01 , 0.02 , 0.015, 0.015, 0.01 , 1.01 , 0.36 , 0.11 ,
        0.085, 0.81 , 0.01 , 0.02 ],
       [0.085, 1.01 , 0.01 , 0.11 , 0.01 , 0.01 , 0.06 , 0.06 , 0.06 ,
        0.015, 0.015, 0.015, 0.02 ],
       [0.02 , 0.01 , 0.96 , 0.11 , 0.01 , 0.01 , 0.011, 0.01 , 0.011,
        0.02 , 0.02 , 0.035, 0.02 ],
       [0.02 , 0.01 , 0.02 , 0.02 , 1.01 , 0.02 , 0.02 , 0.02 , 0.02 ,
        0.02 , 0.02 , 0.02 , 0.015]])

negative = np.array([[0.9476929 , 0.91266582, 0.9056604 , 0.9056604 , 0.96637401,
        0.98972539, 0.96170373, 0.96170373, 0.98505511, 0.98505511,
        0.98505511, 0.97571456, 0.97571456],
       [0.95250845, 0.9906713 , 0.9987279 , 0.99915194, 0.91858592,
        0.92282623, 0.94402782, 0.93554718, 0.92706655, 0.92706655,
        0.92706655, 0.92282623, 0.93130687],
       [0.95094886, 0.97211306, 0.95468372, 0.99576716, 0.95094886,
        0.94970391, 0.95966353, 0.97211306, 0.96215343, 0.9920323 ,
        0.97211306, 0.98207268, 0.95468372],
       [0.99477107, 0.91633716, 0.97609633, 0.85657798, 0.99103612,
        0.99850602, 0.97609633, 0.93127695, 0.95368664, 0.86404788,
        0.93127695, 0.87898767, 0.98356623],
       [0.99403235, 0.99403235, 0.99403235, 0.99403235, 0.99403235,
        0.99403235, 0.96419411, 0.87467939, 0.42710579, 0.99403235,
        0.99403235, 0.99403235, 0.99403235],
       [0.9947147 , 0.9947147 , 0.9947147 , 0.9947147 , 0.9947147 ,
        0.9947147 , 0.9947147 , 0.7833026 , 0.9947147 , 0.46618446,
        0.88900865, 0.9947147 , 0.9947147 ],
       [0.98690232, 0.98690232, 0.9759876 , 0.8668403 , 0.99672558,
        0.98690232, 0.78497983, 0.89958449, 0.98690232, 0.93232868,
        0.81226666, 0.98690232, 0.9759876 ],
       [0.99408076, 0.99408076, 0.94968648, 0.41695508, 0.99408076,
        0.99408076, 0.99408076, 0.99408076, 0.99408076, 0.99408076,
        0.99408076, 0.98816152, 0.9052922 ],
       [0.99368322, 0.99368322, 0.99368322, 0.99368322, 0.99368322,
        0.99368322, 0.99368322, 0.42517322, 0.99368322, 0.94630739,
        0.96209933, 0.99368322, 0.99368322],
       [0.98823306, 0.97982811, 0.99327604, 0.99663802, 0.99663802,
        0.99663802, 0.66043985, 0.66043985, 0.9630182 , 0.69405967,
        0.66043985, 0.99663802, 0.97142316],
       [0.9894118 , 0.9894118 , 0.99382355, 0.9982353 , 0.9982353 ,
        0.9964706 , 0.9982353 , 0.9982353 , 0.97176479, 0.98500005,
        0.9982353 , 0.9982353 , 0.99382355],
       [0.99653878, 0.99653878, 0.99653878, 0.99653878, 0.99653878,
        0.99653878, 0.99653878, 0.9100082 , 0.94462043, 0.92731432,
        0.99653878, 0.99653878, 0.99307755],
       [0.99429522, 0.99429522, 0.99429522, 0.99429522, 0.99429522,
        0.99429522, 0.99429522, 0.56643684, 0.99144283, 0.79462798,
        0.99429522, 0.99429522, 0.99429522],
       [0.99377461, 0.99584974, 0.99169948, 0.99377461, 0.99377461,
        0.99584974, 0.5808236 , 0.85059059, 0.95434712, 0.96472278,
        0.66382883, 0.99584974, 0.99169948],
       [0.95831264, 0.50465609, 0.9950956 , 0.94605165, 0.9950956 ,
        0.9950956 , 0.97057363, 0.97057363, 0.97057363, 0.99264341,
        0.99264341, 0.99264341, 0.99019121],
       [0.98794763, 0.99397381, 0.42148605, 0.93371194, 0.99397381,
        0.99397381, 0.99337119, 0.99397381, 0.99337119, 0.98794763,
        0.98794763, 0.97890835, 0.98794763],
       [0.98721102, 0.99360551, 0.98721102, 0.98721102, 0.35415629,
        0.98721102, 0.98721102, 0.98721102, 0.98721102, 0.98721102,
        0.98721102, 0.98721102, 0.99040826]])

def neurocystic_calculator(user_input, positive, negative, all_features, labels,prevalence):
  postive_list = [1 if item in user_input else 0 for item in all_features]
  postive_array = np.array(postive_list).reshape(17,1)  #change the number g=here
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