import numpy as np

labels = np.array(['Low grade glioma (or diffuse astrocytoma)',
       'Pilocytic astrocytoma', 'Anaplastic astrocytoma',
       'GBM (glioblastoma)', 'Metastasis', 'Gliosarcoma',
       'Gliomatosis cerebri ', 'PXA (pleomorphic xanthoastrocytoma)',
       'Oligodendroglioma ', 'Anaplastic oligodendroglioma',
       'Intraparenchymal ependymoma',
       'DNET (Dysembryoplastic neuroepithelial tumour)',
       'Hemanagioblastoma (Supratentorial)',
       'Lymphoma in immunocompromised or treated patients', 'Lymphoma ',
       'Oligoastrocytoma',
       'Radiation necrosis (if history of radiotherapy exists)',
       'Abscess', 'Cavernoma (or cavernoma complicated with hemorrhage)',
       'Lipoma', 'Extraventricular Neurocytoma', 'Haemorrhage (hematoma)',
       'Meningioangiomatosis',
       'Granulocytic sarcoma\Granulocytic sarcoma',
       'Angiocentric glioma', 'Tubercloma ', 'Septic emboli',
       'Aspergillus infection', 'Kaposi sarcoma',
       'Cerebral amyloid angiopathy', 'Toxoplasmosis (acquired)',
       'Astroblastoma', 'Ganglioglioma',
       'Dysmoplastic infantile ganglioglioma',
       'Supratentorial PNET (Primitive neuroectodermal tumour)',
       'AT/RTs (atypical  teratoid-rhabdoid tumor)', 'Teratoma',
       'Gangliocytoma',
       'Focal areas of signal intensity (unidentified bright objects)',
       'TS (Tuberous Sclerosis)',
       'Tumefactive demylinating lesion (monofocal acute inflammatory demyelination (MAID)) ',
       'Tumefactive multiple sclerosis',
       'Hemophagocytic Lymphohistiocytosis (LHL)',
       'NCC (neurocysticercosis)'], dtype=object)

all_features = np.array(['Child', 'Adult', 'solitary ', 'multiple',
       'pleomorphic',
       'same_area',
       'solid',
       'solid_necrosis',
       'Small',
       'cystic',
       'cortical_based',
       'More_then_one_lobe',
       'cc',
       'symmetrical',
       'asymmetrical',
       'complete_enhance',
       'Enhanced_wall',
       'hemorrhage',
       'popcorn', 'calcification',
       'calcification_coarse', 'fat',
       'restriction_solid',
       'restriction_cystuc',
       'caseating',
       'Serpentine',
       'White_matter_edema', 'dural',
       'remodeling',
       'calvarial_erosion',
       'subependymal_calcific',
       'subependymal_spread ', 'tubers',
       'cortical_dysplasia'])

prevalence = np.array([1.2 , 1.  , 0.9 , 1.5 , 1.5 , 0.6 , 0.75, 1.  , 1.  , 0.7 , 0.5 ,
       0.7 , 0.4 , 1.  , 1.  , 0.7 , 0.4 , 0.8 , 1.  , 0.7 , 0.7 , 0.8 ,
       0.6 , 0.8 , 0.7 , 0.5 , 1.  , 1.  , 0.5 , 1.  , 1.  , 0.9 , 1.  ,
       0.5 , 1.  , 1.  , 1.  , 0.8 , 0.8 , 0.8 , 0.4 , 1.  , 0.3 , 0.9 ])


positive = np.array([[0.825 , 0.9   , 0.06  , 0.11  , 0.16  , 0.11  , 0.085 , 0.16  ,
        0.08  , 0.06  , 0.26  , 0.66  , 0.16  , 0.26  , 0.26  , 0.06  ,
        0.11  , 0.3   , 0.3   , 0.41  , 0.085 , 0.06  , 0.26  , 0.71  ,
        0.66  , 0.61  , 0.21  , 0.11  , 0.085 , 0.01  , 0.26  , 0.61  ,
        0.96  , 1.    , 0.975 , 0.975 , 0.975 , 0.96  , 0.96  , 1.    ,
        0.05  , 0.02  , 0.67  , 0.125 ],
       [0.95  , 0.51  , 0.96  , 0.96  , 0.96  , 0.96  , 0.96  , 0.91  ,
        0.985 , 0.985 , 0.86  , 0.66  , 0.91  , 0.925 , 0.925 , 0.985 ,
        0.925 , 0.85  , 0.91  , 0.66  , 0.86  , 0.96  , 0.86  , 0.31  ,
        0.41  , 0.85  , 0.935 , 0.86  , 0.96  , 1.    , 0.86  , 0.46  ,
        0.06  , 0.05  , 0.06  , 0.075 , 0.06  , 0.06  , 0.085 , 0.01  ,
        0.95  , 1.    , 0.4   , 0.91  ],
       [1.    , 1.    , 1.    , 0.95  , 0.11  , 0.96  , 1.    , 1.    ,
        1.    , 1.    , 0.91  , 1.    , 0.96  , 0.46  , 0.86  , 1.    ,
        0.96  , 0.96  , 0.95  , 1.    , 1.    , 1.    , 0.46  , 0.86  ,
        1.    , 0.76  , 0.06  , 0.26  , 0.06  , 0.01  , 0.11  , 1.    ,
        1.    , 1.    , 1.    , 1.    , 1.    , 1.    , 0.06  , 0.06  ,
        0.96  , 0.085 , 0.02  , 0.035 ],
       [0.085 , 0.085 , 0.035 , 0.26  , 0.8   , 0.01  , 0.035 , 0.035 ,
        0.06  , 0.01  , 0.11  , 0.01  , 0.11  , 0.56  , 0.26  , 0.01  ,
        0.16  , 0.16  , 0.085 , 0.01  , 0.01  , 0.01  , 0.56  , 0.11  ,
        0.01  , 0.66  , 0.985 , 0.76  , 0.96  , 1.    , 0.91  , 0.01  ,
        0.06  , 0.01  , 0.01  , 0.035 , 0.01  , 0.06  , 0.96  , 1.    ,
        0.085 , 0.985 , 0.985 , 0.985 ],
       [0.06  , 0.06  , 0.01  , 0.4   , 0.3   , 0.26  , 0.01  , 0.01  ,
        0.01  , 0.01  , 0.085 , 0.01  , 0.11  , 0.46  , 0.46  , 0.01  ,
        0.01  , 0.01  , 0.06  , 0.01  , 0.01  , 0.01  , 0.51  , 0.085 ,
        0.01  , 0.41  , 0.36  , 0.31  , 0.91  , 0.01  , 0.86  , 0.01  ,
        0.21  , 0.01  , 0.01  , 0.01  , 0.01  , 0.06  , 0.21  , 0.01  ,
        0.06  , 0.76  , 0.86  , 0.11  ],
       [0.06  , 0.06  , 0.01  , 0.7   , 0.1   , 0.01  , 0.36  , 0.01  ,
        0.01  , 0.01  , 0.06  , 0.01  , 0.01  , 0.56  , 0.31  , 0.01  ,
        0.01  , 0.01  , 0.01  , 0.01  , 0.01  , 0.01  , 0.01  , 0.06  ,
        0.01  , 0.01  , 0.11  , 0.31  , 0.11  , 0.01  , 0.41  , 0.01  ,
        0.01  , 0.01  , 0.01  , 0.01  , 0.01  , 0.01  , 0.085 , 0.01  ,
        0.06  , 0.06  , 0.51  , 0.06  ],
       [0.975 , 0.085 , 0.76  , 0.13  , 0.45  , 0.31  , 0.96  , 0.085 ,
        0.36  , 0.36  , 0.36  , 0.975 , 0.085 , 0.31  , 0.85  , 0.36  ,
        0.26  , 0.01  , 0.95  , 1.    , 0.26  , 1.    , 1.    , 0.86  ,
        0.96  , 0.46  , 0.02  , 0.01  , 0.96  , 1.    , 0.01  , 0.11  ,
        0.76  , 0.06  , 0.11  , 0.11  , 0.11  , 0.31  , 1.    , 0.1075,
        0.86  , 0.71  , 0.085 , 0.01  ],
       [0.085 , 0.985 , 0.66  , 0.975 , 0.76  , 0.81  , 0.26  , 1.    ,
        0.96  , 0.96  , 0.7   , 0.06  , 1.    , 0.76  , 0.36  , 0.96  ,
        0.91  , 0.01  , 0.06  , 0.01  , 0.76  , 0.36  , 0.21  , 0.36  ,
        0.11  , 0.76  , 0.21  , 0.31  , 0.66  , 0.01  , 0.16  , 0.86  ,
        0.51  , 1.    , 0.86  , 0.91  , 0.96  , 0.76  , 0.16  , 0.01  ,
        0.31  , 0.31  , 0.96  , 0.085 ],
       [0.4   , 0.36  , 0.6   , 0.55  , 0.885 , 0.86  , 0.01  , 0.46  ,
        0.16  , 0.16  , 0.46  , 0.96  , 0.8   , 0.36  , 0.36  , 0.16  ,
        0.31  , 0.56  , 0.9   , 0.86  , 0.36  , 0.46  , 0.96  , 0.56  ,
        0.76  , 0.76  , 0.91  , 0.36  , 0.21  , 1.    , 0.36  , 0.91  ,
        0.91  , 0.01  , 0.035 , 0.035 , 0.11  , 0.91  , 0.96  , 0.46  ,
        0.085 , 0.21  , 0.21  , 1.    ],
       [0.01  , 0.45  , 0.01  , 0.08  , 0.16  , 0.11  , 0.01  , 0.11  ,
        0.01  , 0.01  , 0.06  , 0.01  , 0.31  , 0.06  , 0.06  , 0.01  ,
        0.11  , 1.    , 0.01  , 0.01  , 0.085 , 0.36  , 0.01  , 0.16  ,
        0.01  , 0.66  , 0.985 , 0.76  , 0.01  , 0.01  , 0.96  , 0.01  ,
        0.16  , 0.085 , 0.085 , 0.01  , 0.06  , 0.26  , 0.01  , 0.01  ,
        0.01  , 0.01  , 0.21  , 0.96  ],
       [0.4   , 0.4   , 0.11  , 0.2   , 0.66  , 0.86  , 0.86  , 0.975 ,
        1.    , 1.    , 0.36  , 0.86  , 0.41  , 0.31  , 0.31  , 0.86  ,
        0.26  , 0.26  , 0.36  , 0.01  , 0.26  , 0.66  , 1.    , 0.56  ,
        1.    , 0.31  , 0.46  , 0.21  , 0.31  , 0.01  , 0.11  , 0.96  ,
        1.    , 1.    , 0.31  , 0.01  , 0.36  , 1.    , 0.01  , 1.    ,
        0.96  , 0.96  , 0.86  , 0.11  ],
       [0.06  , 0.06  , 0.01  , 0.06  , 0.02  , 0.01  , 0.985 , 0.01  ,
        0.01  , 0.01  , 0.01  , 0.01  , 0.01  , 0.01  , 0.01  , 0.01  ,
        0.01  , 0.01  , 0.01  , 0.01  , 0.01  , 0.01  , 0.01  , 0.01  ,
        0.01  , 0.01  , 0.01  , 0.01  , 0.11  , 0.01  , 0.01  , 0.01  ,
        0.01  , 0.01  , 0.01  , 0.01  , 0.01  , 0.01  , 0.01  , 0.01  ,
        0.06  , 0.06  , 0.21  , 0.085 ],
       [0.15  , 0.1   , 0.31  , 0.35  , 0.06  , 0.01  , 0.46  , 0.01  ,
        0.085 , 0.085 , 0.06  , 0.085 , 0.019 , 0.56  , 0.56  , 0.135 ,
        0.26  , 0.01  , 0.26  , 1.    , 0.085 , 0.085 , 0.01  , 0.26  ,
        0.01  , 0.085 , 0.11  , 0.01  , 0.085 , 0.01  , 0.085 , 0.085 ,
        0.06  , 0.01  , 0.085 , 0.01  , 0.16  , 0.06  , 0.01  , 0.01  ,
        0.035 , 0.035 , 0.035 , 0.085 ],
       [0.15  , 0.06  , 0.035 , 0.035 , 0.03  , 0.01  , 0.01  , 0.01  ,
        0.01  , 0.01  , 0.06  , 0.085 , 0.01  , 0.06  , 0.06  , 0.01  ,
        0.01  , 0.01  , 0.16  , 0.01  , 0.01  , 0.01  , 0.01  , 0.01  ,
        0.01  , 0.11  , 0.085 , 0.01  , 0.06  , 0.01  , 0.11  , 0.01  ,
        0.01  , 0.01  , 0.01  , 0.01  , 0.16  , 0.01  , 0.36  , 0.01  ,
        0.01  , 0.01  , 0.1   , 0.035 ],
       [0.16  , 0.05  , 0.21  , 0.085 , 0.16  , 0.01  , 0.26  , 0.065 ,
        0.01  , 0.01  , 0.01  , 0.085 , 0.175 , 0.46  , 0.46  , 0.01  ,
        0.01  , 0.21  , 0.08  , 0.01  , 0.085 , 0.01  , 0.01  , 0.01  ,
        0.01  , 0.31  , 0.21  , 0.01  , 0.085 , 0.01  , 0.75  , 0.01  ,
        0.01  , 0.01  , 0.11  , 0.11  , 0.035 , 0.01  , 1.    , 0.01  ,
        0.015 , 0.01  , 0.09  , 0.15  ],
       [0.1   , 0.985 , 0.66  , 1.    , 0.91  , 0.96  , 0.36  , 1.    ,
        0.66  , 0.86  , 0.96  , 0.36  , 1.    , 1.    , 1.    , 0.16  ,
        0.96  , 0.01  , 0.15  , 0.01  , 0.86  , 0.085 , 0.11  , 1.    ,
        0.06  , 0.86  , 0.21  , 0.01  , 0.96  , 0.01  , 0.11  , 0.91  ,
        0.56  , 1.    , 1.    , 1.    , 0.96  , 0.56  , 0.01  , 0.21  ,
        0.51  , 0.51  , 0.76  , 0.26  ],
       [0.01  , 0.51  , 0.01  , 0.085 , 0.36  , 0.01  , 0.01  , 0.01  ,
        0.01  , 0.01  , 0.01  , 0.01  , 0.61  , 0.01  , 0.01  , 0.01  ,
        1.    , 1.    , 0.15  , 0.01  , 0.01  , 0.16  , 0.01  , 0.01  ,
        0.01  , 0.86  , 0.985 , 0.01  , 0.01  , 0.01  , 0.96  , 0.01  ,
        0.41  , 0.11  , 0.085 , 0.01  , 0.06  , 0.41  , 0.01  , 0.01  ,
        0.01  , 0.015 , 0.16  , 0.96  ],
       [0.06  , 0.06  , 0.085 , 0.17  , 0.25  , 0.55  , 0.01  , 0.21  ,
        0.21  , 0.21  , 0.26  , 0.01  , 0.21  , 0.085 , 0.085 , 0.085 ,
        0.06  , 0.085 , 0.935 , 0.01  , 0.01  , 1.    , 1.    , 0.01  ,
        0.01  , 0.11  , 0.085 , 0.41  , 0.46  , 1.    , 0.06  , 0.21  ,
        0.01  , 0.085 , 0.11  , 0.16  , 0.085 , 0.01  , 0.01  , 0.01  ,
        0.01  , 0.01  , 0.06  , 0.01  ],
       [0.01  , 0.011 , 0.01  , 0.075 , 0.01  , 0.01  , 0.01  , 0.01  ,
        0.01  , 0.01  , 0.01  , 0.01  , 0.085 , 0.01  , 0.01  , 0.01  ,
        0.01  , 0.01  , 0.96  , 0.01  , 0.01  , 0.01  , 0.01  , 0.01  ,
        0.01  , 0.01  , 0.01  , 0.21  , 0.01  , 0.085 , 0.01  , 0.01  ,
        0.01  , 0.01  , 0.01  , 0.01  , 0.01  , 0.01  , 0.01  , 0.01  ,
        0.01  , 0.01  , 0.01  , 0.01  ],
       [0.11  , 0.26  , 0.035 , 0.11  , 0.085 , 0.01  , 0.01  , 0.085 ,
        0.81  , 0.61  , 0.51  , 0.36  , 0.03  , 0.21  , 0.21  , 0.21  ,
        0.035 , 0.01  , 0.11  , 0.01  , 0.16  , 0.01  , 0.11  , 0.01  ,
        0.01  , 0.36  , 0.01  , 0.01  , 0.01  , 0.01  , 0.01  , 0.96  ,
        0.41  , 0.035 , 0.76  , 0.56  , 0.66  , 0.26  , 0.01  , 0.66  ,
        0.01  , 0.01  , 0.51  , 0.26  ],
       [0.06  , 0.01  , 0.01  , 0.06  , 0.01  , 0.01  , 0.01  , 0.01  ,
        0.81  , 0.61  , 0.61  , 0.06  , 0.03  , 0.06  , 0.01  , 0.21  ,
        0.01  , 0.01  , 0.06  , 0.01  , 0.16  , 0.01  , 0.01  , 0.01  ,
        0.01  , 0.21  , 0.01  , 0.01  , 0.01  , 0.01  , 0.01  , 0.16  ,
        0.36  , 0.01  , 0.36  , 0.36  , 0.46  , 0.11  , 0.085 , 0.36  ,
        0.01  , 0.01  , 0.31  , 0.06  ],
       [0.01  , 0.01  , 0.01  , 0.01  , 0.01  , 0.01  , 0.01  , 0.01  ,
        0.01  , 0.01  , 0.01  , 0.01  , 0.01  , 0.0125, 0.0125, 0.01  ,
        0.01  , 0.01  , 0.01  , 1.    , 0.01  , 0.01  , 0.01  , 0.01  ,
        0.01  , 0.01  , 0.01  , 0.01  , 0.01  , 0.01  , 0.01  , 0.01  ,
        0.01  , 0.01  , 0.01  , 0.01  , 0.56  , 0.01  , 0.01  , 0.01  ,
        0.01  , 0.01  , 0.01  , 0.01  ],
       [0.01  , 0.06  , 0.06  , 0.25  , 0.16  , 0.01  , 0.01  , 0.16  ,
        0.16  , 0.16  , 0.16  , 0.01  , 0.085 , 0.96  , 0.96  , 0.085 ,
        0.0195, 0.035 , 0.31  , 0.01  , 0.01  , 0.56  , 0.01  , 0.76  ,
        0.01  , 0.76  , 0.085 , 0.21  , 0.31  , 0.31  , 0.035 , 0.16  ,
        0.01  , 0.06  , 0.96  , 0.16  , 0.11  , 0.01  , 0.0125, 0.01  ,
        0.02  , 0.01  , 0.01  , 0.36  ],
       [0.01  , 0.03  , 0.01  , 0.11  , 0.055 , 0.01  , 0.01  , 0.01  ,
        0.01  , 0.01  , 0.01  , 0.01  , 0.01  , 0.035 , 0.01  , 0.01  ,
        0.02  , 1.    , 0.01  , 0.01  , 0.01  , 0.01  , 0.01  , 0.01  ,
        0.01  , 0.76  , 0.86  , 0.76  , 0.11  , 0.01  , 0.86  , 0.01  ,
        0.01  , 0.01  , 0.06  , 0.01  , 0.01  , 0.01  , 0.01  , 0.01  ,
        0.01  , 0.01  , 0.01  , 0.06  ],
       [0.01  , 0.01  , 0.01  , 0.01  , 0.035 , 0.01  , 0.01  , 0.01  ,
        0.01  , 0.01  , 0.01  , 0.01  , 0.01  , 0.035 , 0.035 , 0.01  ,
        0.01  , 0.11  , 0.01  , 0.01  , 0.01  , 0.01  , 0.01  , 0.01  ,
        0.01  , 0.96  , 0.11  , 0.085 , 0.01  , 0.01  , 0.085 , 0.01  ,
        0.01  , 0.01  , 0.01  , 0.01  , 0.01  , 0.01  , 0.01  , 0.01  ,
        0.01  , 0.01  , 0.035 , 0.035 ],
       [0.01  , 0.01  , 0.01  , 0.01  , 0.01  , 0.01  , 0.01  , 0.01  ,
        0.01  , 0.01  , 0.01  , 0.01  , 0.95  , 0.01  , 0.01  , 0.01  ,
        0.01  , 0.01  , 0.08  , 0.01  , 0.01  , 0.01  , 0.01  , 0.01  ,
        0.01  , 0.01  , 0.01  , 0.01  , 0.01  , 0.01  , 0.01  , 0.01  ,
        0.01  , 0.01  , 0.01  , 0.01  , 0.01  , 0.01  , 0.01  , 0.01  ,
        0.01  , 0.01  , 0.01  , 0.01  ],
       [0.11  , 0.11  , 0.66  , 0.8   , 0.91  , 0.86  , 0.81  , 0.085 ,
        0.56  , 0.56  , 0.56  , 0.1   , 0.46  , 0.7   , 0.56  , 0.71  ,
        0.66  , 1.    , 0.11  , 0.01  , 0.76  , 0.76  , 0.01  , 0.51  ,
        0.01  , 0.36  , 0.61  , 0.81  , 0.11  , 0.085 , 1.    , 0.01  ,
        0.085 , 0.41  , 0.76  , 0.76  , 0.76  , 0.11  , 0.015 , 0.01  ,
        0.035 , 0.035 , 0.01  , 0.26  ],
       [0.01  , 0.01  , 0.01  , 0.035 , 0.085 , 0.01  , 0.01  , 0.71  ,
        0.085 , 0.085 , 0.01  , 0.01  , 0.035 , 0.01  , 0.01  , 0.085 ,
        0.01  , 0.11  , 0.01  , 0.01  , 0.01  , 0.01  , 1.    , 0.085 ,
        0.01  , 0.085 , 0.21  , 0.01  , 0.06  , 0.01  , 0.01  , 0.06  ,
        0.11  , 0.56  , 0.31  , 0.01  , 0.01  , 0.11  , 0.01  , 0.01  ,
        0.01  , 0.01  , 0.085 , 0.01  ],
       [0.01  , 0.01  , 0.01  , 0.01  , 0.01  , 0.01  , 0.01  , 0.36  ,
        0.01  , 0.01  , 0.01  , 0.76  , 0.085 , 0.01  , 0.01  , 0.01  ,
        0.01  , 0.01  , 0.01  , 0.01  , 0.01  , 0.01  , 0.06  , 0.01  ,
        0.01  , 0.01  , 0.01  , 0.01  , 0.01  , 0.01  , 0.01  , 0.06  ,
        0.26  , 0.26  , 0.085 , 0.01  , 0.01  , 0.26  , 0.01  , 0.01  ,
        0.01  , 0.01  , 0.015 , 0.01  ],
       [0.01  , 0.01  , 0.01  , 0.01  , 0.065 , 0.01  , 0.01  , 0.01  ,
        0.11  , 0.11  , 0.01  , 0.01  , 0.01  , 0.01  , 0.01  , 0.06  ,
        0.01  , 0.01  , 0.01  , 0.01  , 0.01  , 0.01  , 0.01  , 0.21  ,
        0.01  , 0.01  , 0.01  , 0.01  , 0.01  , 0.01  , 0.01  , 0.01  ,
        0.01  , 0.01  , 0.16  , 0.01  , 0.01  , 0.01  , 0.01  , 0.01  ,
        0.01  , 0.01  , 0.01  , 0.01  ],
       [0.01  , 0.01  , 0.01  , 0.01  , 0.01  , 0.01  , 0.01  , 0.01  ,
        0.01  , 0.01  , 0.01  , 0.01  , 0.01  , 0.01  , 0.01  , 0.01  ,
        0.01  , 0.01  , 0.01  , 0.01  , 0.01  , 0.01  , 0.01  , 0.01  ,
        0.01  , 0.01  , 0.01  , 0.01  , 0.01  , 0.01  , 0.01  , 0.01  ,
        0.01  , 0.01  , 0.01  , 0.01  , 0.01  , 0.01  , 0.01  , 1.    ,
        0.01  , 0.01  , 0.015 , 0.01  ],
       [0.01  , 0.01  , 0.01  , 0.12  , 0.11  , 0.01  , 0.01  , 0.01  ,
        0.01  , 0.01  , 0.01  , 0.01  , 0.01  , 0.21  , 0.21  , 0.01  ,
        0.01  , 0.01  , 0.01  , 0.01  , 0.01  , 0.01  , 0.01  , 0.01  ,
        0.01  , 0.01  , 0.01  , 0.01  , 0.01  , 0.01  , 0.01  , 0.01  ,
        0.01  , 0.01  , 0.085 , 0.01  , 0.01  , 0.01  , 0.01  , 0.06  ,
        0.01  , 0.01  , 0.01  , 0.035 ],
       [0.01  , 0.01  , 0.01  , 0.01  , 0.01  , 0.01  , 0.01  , 0.01  ,
        0.01  , 0.01  , 0.01  , 0.01  , 0.01  , 0.01  , 0.01  , 0.01  ,
        0.01  , 0.01  , 0.01  , 0.01  , 0.01  , 0.01  , 0.01  , 0.01  ,
        0.01  , 0.01  , 0.01  , 0.01  , 0.01  , 0.01  , 0.01  , 0.01  ,
        0.01  , 0.01  , 0.01  , 0.01  , 0.01  , 0.01  , 0.01  , 1.    ,
        0.03  , 0.03  , 0.01  , 0.01  ],
       [0.01  , 0.01  , 0.01  , 0.01  , 0.01  , 0.01  , 0.01  , 0.01  ,
        0.01  , 0.01  , 0.01  , 0.21  , 0.01  , 0.01  , 0.01  , 0.01  ,
        0.01  , 0.01  , 0.01  , 0.01  , 0.01  , 0.01  , 0.01  , 0.01  ,
        0.01  , 0.01  , 0.01  , 0.01  , 0.01  , 0.01  , 0.01  , 0.01  ,
        0.26  , 0.01  , 0.01  , 0.01  , 0.01  , 0.25  , 0.01  , 0.11  ,
        0.01  , 0.01  , 0.01  , 0.01  ]])

negative = np.array([[0.91418979, 0.90638886, 0.99375926, 0.98855864, 0.98335802,
        0.98855864, 0.99115895, 0.98335802, 0.99167901, 0.99375926,
        0.97295678, 0.93135183, 0.98335802, 0.97295678, 0.97295678,
        0.99375926, 0.98855864, 0.96879629, 0.96879629, 0.95735493,
        0.99115895, 0.99375926, 0.97295678, 0.92615122, 0.93135183,
        0.93655245, 0.9781574 , 0.98855864, 0.99115895, 0.99895988,
        0.97295678, 0.93655245, 0.90014812, 0.89598763, 0.89858794,
        0.89858794, 0.89858794, 0.90014812, 0.90014812, 0.89598763,
        0.99479938, 0.99791975, 0.93031171, 0.98699845],
       [0.95592981, 0.97634127, 0.95546592, 0.95546592, 0.95546592,
        0.95546592, 0.95546592, 0.9577854 , 0.95430618, 0.95430618,
        0.96010488, 0.96938282, 0.9577854 , 0.95708956, 0.95708956,
        0.95430618, 0.95708956, 0.96056878, 0.9577854 , 0.96938282,
        0.96010488, 0.95546592, 0.96010488, 0.9856192 , 0.98098024,
        0.96056878, 0.95662566, 0.96010488, 0.95546592, 0.95361033,
        0.96010488, 0.97866075, 0.99721662, 0.99768052, 0.99721662,
        0.99652077, 0.99721662, 0.99721662, 0.99605688, 0.9995361 ,
        0.95592981, 0.95361033, 0.98144413, 0.9577854 ],
       [0.94406297, 0.94406297, 0.94406297, 0.94685982, 0.99384693,
        0.94630045, 0.94406297, 0.94406297, 0.94406297, 0.94406297,
        0.9490973 , 0.94406297, 0.94630045, 0.97426896, 0.95189415,
        0.94406297, 0.94630045, 0.94630045, 0.94685982, 0.94406297,
        0.94406297, 0.94406297, 0.97426896, 0.95189415, 0.94406297,
        0.95748785, 0.99664378, 0.98545637, 0.99664378, 0.99944063,
        0.99384693, 0.94406297, 0.94406297, 0.94406297, 0.94406297,
        0.94406297, 0.94406297, 0.94406297, 0.99664378, 0.99664378,
        0.94630045, 0.99524535, 0.99888126, 0.9980422 ],
       [0.98382594, 0.98382594, 0.99334009, 0.95052639, 0.84777351,
        0.99809717, 0.99334009, 0.99334009, 0.98858301, 0.99809717,
        0.97906886, 0.99809717, 0.97906886, 0.89344146, 0.95052639,
        0.99809717, 0.9695547 , 0.9695547 , 0.98382594, 0.99809717,
        0.99809717, 0.99809717, 0.89344146, 0.97906886, 0.99809717,
        0.87441314, 0.81257113, 0.85538483, 0.81732821, 0.80971688,
        0.82684236, 0.99809717, 0.98858301, 0.99809717, 0.99809717,
        0.99334009, 0.99809717, 0.98858301, 0.81732821, 0.80971688,
        0.98382594, 0.81257113, 0.81257113, 0.81257113],
       [0.98710447, 0.98710447, 0.99785075, 0.9140298 , 0.93552235,
        0.94411937, 0.99785075, 0.99785075, 0.99785075, 0.99785075,
        0.98173133, 0.99785075, 0.9763582 , 0.90113427, 0.90113427,
        0.99785075, 0.99785075, 0.99785075, 0.98710447, 0.99785075,
        0.99785075, 0.99785075, 0.890388  , 0.98173133, 0.99785075,
        0.91188055, 0.92262682, 0.9333731 , 0.8044178 , 0.99785075,
        0.81516407, 0.99785075, 0.95486565, 0.99785075, 0.99785075,
        0.99785075, 0.99785075, 0.98710447, 0.95486565, 0.99785075,
        0.98710447, 0.83665662, 0.81516407, 0.9763582 ],
       [0.98414425, 0.98414425, 0.99735738, 0.81501628, 0.97357375,
        0.99735738, 0.90486552, 0.99735738, 0.99735738, 0.99735738,
        0.98414425, 0.99735738, 0.99735738, 0.85201302, 0.91807864,
        0.99735738, 0.99735738, 0.99735738, 0.99735738, 0.99735738,
        0.99735738, 0.99735738, 0.99735738, 0.98414425, 0.99735738,
        0.99735738, 0.97093113, 0.91807864, 0.97093113, 0.99735738,
        0.89165239, 0.99735738, 0.99735738, 0.99735738, 0.99735738,
        0.99735738, 0.99735738, 0.99735738, 0.97753769, 0.99735738,
        0.98414425, 0.98414425, 0.86522615, 0.98414425],
       [0.90385205, 0.99161787, 0.92505391, 0.98718027, 0.95562402,
        0.96942988, 0.90533125, 0.99161787, 0.96449922, 0.96449922,
        0.96449922, 0.90385205, 0.99161787, 0.96942988, 0.91617871,
        0.96449922, 0.97436055, 0.99901387, 0.90631739, 0.90138672,
        0.97436055, 0.90138672, 0.90138672, 0.91519258, 0.90533125,
        0.95463789, 0.99802773, 0.99901387, 0.90533125, 0.90138672,
        0.99901387, 0.98915254, 0.92505391, 0.9940832 , 0.98915254,
        0.98915254, 0.98915254, 0.96942988, 0.90138672, 0.98939907,
        0.91519258, 0.92998457, 0.99161787, 0.99901387],
       [0.99379431, 0.92808701, 0.95181465, 0.92881709, 0.94451384,
        0.94086343, 0.98101789, 0.92699189, 0.92991222, 0.92991222,
        0.94889432, 0.99561951, 0.92699189, 0.94451384, 0.97371708,
        0.92991222, 0.93356262, 0.99926992, 0.99561951, 0.99926992,
        0.94451384, 0.97371708, 0.9846683 , 0.97371708, 0.99196911,
        0.94451384, 0.9846683 , 0.97736749, 0.95181465, 0.99926992,
        0.9883187 , 0.93721303, 0.96276586, 0.92699189, 0.93721303,
        0.93356262, 0.92991222, 0.94451384, 0.9883187 , 0.99926992,
        0.97736749, 0.97736749, 0.92991222, 0.99379431],
       [0.97577972, 0.97820175, 0.96366958, 0.96669711, 0.94641263,
        0.94792639, 0.99939449, 0.97214668, 0.99031189, 0.99031189,
        0.97214668, 0.94187132, 0.95155944, 0.97820175, 0.97820175,
        0.99031189, 0.98122928, 0.96609161, 0.94550437, 0.94792639,
        0.97820175, 0.97214668, 0.94187132, 0.96609161, 0.95398147,
        0.95398147, 0.94489886, 0.97820175, 0.98728435, 0.9394493 ,
        0.97820175, 0.94489886, 0.94489886, 0.99939449, 0.99788073,
        0.99788073, 0.99333942, 0.94489886, 0.94187132, 0.97214668,
        0.99485319, 0.98728435, 0.98728435, 0.9394493 ],
       [0.99762341, 0.89305337, 0.99762341, 0.98098727, 0.96197453,
        0.97385749, 0.99762341, 0.97385749, 0.99762341, 0.99762341,
        0.98574045, 0.99762341, 0.92632565, 0.98574045, 0.98574045,
        0.99762341, 0.97385749, 0.76234081, 0.99762341, 0.99762341,
        0.97979897, 0.91444269, 0.99762341, 0.96197453, 0.99762341,
        0.84314494, 0.7659057 , 0.81937902, 0.99762341, 0.99762341,
        0.77184718, 0.99762341, 0.96197453, 0.97979897, 0.97979897,
        0.99762341, 0.98574045, 0.93820861, 0.99762341, 0.99762341,
        0.99762341, 0.99762341, 0.95009157, 0.77184718],
       [0.97373701, 0.97373701, 0.99277768, 0.98686851, 0.95666607,
        0.94353458, 0.94353458, 0.93598397, 0.93434253, 0.93434253,
        0.97636331, 0.94353458, 0.97308044, 0.97964619, 0.97964619,
        0.94353458, 0.98292906, 0.98292906, 0.97636331, 0.99934343,
        0.98292906, 0.95666607, 0.93434253, 0.96323182, 0.93434253,
        0.97964619, 0.96979757, 0.98621193, 0.97964619, 0.99934343,
        0.99277768, 0.93696883, 0.93434253, 0.93434253, 0.97964619,
        0.99934343, 0.97636331, 0.93434253, 0.99934343, 0.93434253,
        0.93696883, 0.93696883, 0.94353458, 0.99277768],
       [0.97677341, 0.97677341, 0.9961289 , 0.97677341, 0.9922578 ,
        0.9961289 , 0.61869685, 0.9961289 , 0.9961289 , 0.9961289 ,
        0.9961289 , 0.9961289 , 0.9961289 , 0.9961289 , 0.9961289 ,
        0.9961289 , 0.9961289 , 0.9961289 , 0.9961289 , 0.9961289 ,
        0.9961289 , 0.9961289 , 0.9961289 , 0.9961289 , 0.9961289 ,
        0.9961289 , 0.9961289 , 0.9961289 , 0.95741792, 0.9961289 ,
        0.9961289 , 0.9961289 , 0.9961289 , 0.9961289 , 0.9961289 ,
        0.9961289 , 0.9961289 , 0.9961289 , 0.9961289 , 0.9961289 ,
        0.97677341, 0.97677341, 0.91870694, 0.96709567],
       [0.97384531, 0.98256354, 0.94594697, 0.93897239, 0.98953812,
        0.99825635, 0.91979228, 0.99825635, 0.98517901, 0.98517901,
        0.98953812, 0.98517901, 0.99668707, 0.90235582, 0.90235582,
        0.97646078, 0.9546652 , 0.99825635, 0.9546652 , 0.82563539,
        0.98517901, 0.98517901, 0.99825635, 0.9546652 , 0.99825635,
        0.98517901, 0.98081989, 0.99825635, 0.98517901, 0.99825635,
        0.98517901, 0.98517901, 0.98953812, 0.99825635, 0.98517901,
        0.99825635, 0.97210166, 0.98953812, 0.99825635, 0.99825635,
        0.99389724, 0.99389724, 0.99389724, 0.98517901],
       [0.97361795, 0.98944718, 0.99384419, 0.99384419, 0.99472359,
        0.9982412 , 0.9982412 , 0.9982412 , 0.9982412 , 0.9982412 ,
        0.98944718, 0.98505017, 0.9982412 , 0.98944718, 0.98944718,
        0.9982412 , 0.9982412 , 0.9982412 , 0.97185915, 0.9982412 ,
        0.9982412 , 0.9982412 , 0.9982412 , 0.9982412 , 0.9982412 ,
        0.98065317, 0.98505017, 0.9982412 , 0.98944718, 0.9982412 ,
        0.98065317, 0.9982412 , 0.9982412 , 0.9982412 , 0.9982412 ,
        0.9982412 , 0.97185915, 0.9982412 , 0.93668309, 0.9982412 ,
        0.9982412 , 0.9982412 , 0.98241197, 0.99384419],
       [0.96514826, 0.98910883, 0.95425709, 0.98148501, 0.96514826,
        0.99782177, 0.94336592, 0.98584148, 0.99782177, 0.99782177,
        0.99782177, 0.98148501, 0.9618809 , 0.89980123, 0.89980123,
        0.99782177, 0.99782177, 0.95425709, 0.98257413, 0.99782177,
        0.98148501, 0.99782177, 0.99782177, 0.99782177, 0.99782177,
        0.93247474, 0.95425709, 0.99782177, 0.98148501, 0.99782177,
        0.83663245, 0.99782177, 0.99782177, 0.99782177, 0.97603943,
        0.97603943, 0.99237618, 0.99782177, 0.7821766 , 0.99782177,
        0.99673265, 0.99782177, 0.98039589, 0.96732649],
       [0.99242931, 0.92542868, 0.95003343, 0.92429308, 0.9311067 ,
        0.92732135, 0.97274551, 0.92429308, 0.95003343, 0.93489205,
        0.92732135, 0.97274551, 0.92429308, 0.92429308, 0.92429308,
        0.98788689, 0.92732135, 0.99924293, 0.98864396, 0.99924293,
        0.93489205, 0.99356491, 0.99167224, 0.92429308, 0.99545758,
        0.93489205, 0.98410155, 0.99924293, 0.92732135, 0.99924293,
        0.99167224, 0.9311067 , 0.95760412, 0.92429308, 0.92429308,
        0.92429308, 0.92732135, 0.95760412, 0.99924293, 0.98410155,
        0.96138947, 0.96138947, 0.94246274, 0.9803162 ],
       [0.99725883, 0.86020035, 0.99725883, 0.97670006, 0.9013179 ,
        0.99725883, 0.99725883, 0.99725883, 0.99725883, 0.99725883,
        0.99725883, 0.99725883, 0.83278866, 0.99725883, 0.99725883,
        0.99725883, 0.72588304, 0.72588304, 0.95888246, 0.99725883,
        0.99725883, 0.95614129, 0.99725883, 0.99725883, 0.99725883,
        0.76425942, 0.7299948 , 0.99725883, 0.99725883, 0.99725883,
        0.73684772, 0.99725883, 0.88761205, 0.96984713, 0.97670006,
        0.99725883, 0.98355298, 0.88761205, 0.99725883, 0.99725883,
        0.99725883, 0.99588825, 0.95614129, 0.73684772],
       [0.98821406, 0.98821406, 0.98330326, 0.96660651, 0.95089193,
        0.89196225, 0.99803568, 0.95874922, 0.95874922, 0.95874922,
        0.94892761, 0.99803568, 0.95874922, 0.98330326, 0.98330326,
        0.98330326, 0.98821406, 0.98330326, 0.81633582, 0.99803568,
        0.99803568, 0.80356772, 0.80356772, 0.99803568, 0.99803568,
        0.97839245, 0.98330326, 0.91946277, 0.90964115, 0.80356772,
        0.98821406, 0.95874922, 0.99803568, 0.98330326, 0.97839245,
        0.96857084, 0.98330326, 0.99803568, 0.99803568, 0.99803568,
        0.99803568, 0.99803568, 0.98821406, 0.99803568],
       [0.99562957, 0.99519253, 0.99562957, 0.96722179, 0.99562957,
        0.99562957, 0.99562957, 0.99562957, 0.99562957, 0.99562957,
        0.99562957, 0.99562957, 0.96285137, 0.99562957, 0.99562957,
        0.99562957, 0.99562957, 0.99562957, 0.58043897, 0.99562957,
        0.99562957, 0.99562957, 0.99562957, 0.99562957, 0.99562957,
        0.99562957, 0.99562957, 0.90822103, 0.99562957, 0.96285137,
        0.99562957, 0.99562957, 0.99562957, 0.99562957, 0.99562957,
        0.99562957, 0.99562957, 0.99562957, 0.99562957, 0.99562957,
        0.99562957, 0.99562957, 0.99562957, 0.99562957],
       [0.98073064, 0.95445424, 0.99386884, 0.98073064, 0.98511004,
        0.99824824, 0.99824824, 0.98511004, 0.85810745, 0.89314265,
        0.91066024, 0.93693664, 0.99474472, 0.96321304, 0.96321304,
        0.96321304, 0.99386884, 0.99824824, 0.98073064, 0.99824824,
        0.97197184, 0.99824824, 0.98073064, 0.99824824, 0.99824824,
        0.93693664, 0.99824824, 0.99824824, 0.99824824, 0.99824824,
        0.99824824, 0.83183105, 0.92817784, 0.99386884, 0.86686625,
        0.90190145, 0.88438385, 0.95445424, 0.99824824, 0.88438385,
        0.99824824, 0.99824824, 0.91066024, 0.95445424],
       [0.98644204, 0.99774034, 0.99774034, 0.98644204, 0.99774034,
        0.99774034, 0.99774034, 0.99774034, 0.81696758, 0.86216077,
        0.86216077, 0.98644204, 0.99322102, 0.98644204, 0.99774034,
        0.95254715, 0.99774034, 0.99774034, 0.98644204, 0.99774034,
        0.96384545, 0.99774034, 0.99774034, 0.99774034, 0.99774034,
        0.95254715, 0.99774034, 0.99774034, 0.99774034, 0.99774034,
        0.99774034, 0.96384545, 0.91865226, 0.99774034, 0.91865226,
        0.91865226, 0.89605566, 0.97514375, 0.98079289, 0.91865226,
        0.99774034, 0.99774034, 0.92995055, 0.98644204],
       [0.99484219, 0.99484219, 0.99484219, 0.99484219, 0.99484219,
        0.99484219, 0.99484219, 0.99484219, 0.99484219, 0.99484219,
        0.99484219, 0.99484219, 0.99484219, 0.99355274, 0.99355274,
        0.99484219, 0.99484219, 0.99484219, 0.99484219, 0.48421943,
        0.99484219, 0.99484219, 0.99484219, 0.99484219, 0.99484219,
        0.99484219, 0.99484219, 0.99484219, 0.99484219, 0.99484219,
        0.99484219, 0.99484219, 0.99484219, 0.99484219, 0.99484219,
        0.99484219, 0.71116288, 0.99484219, 0.99484219, 0.99484219,
        0.99484219, 0.99484219, 0.99484219, 0.99484219],
       [0.99798085, 0.98788511, 0.98788511, 0.94952129, 0.96769362,
        0.99798085, 0.99798085, 0.96769362, 0.96769362, 0.96769362,
        0.96769362, 0.99798085, 0.98283724, 0.80616174, 0.80616174,
        0.98283724, 0.99606266, 0.99293298, 0.93740639, 0.99798085,
        0.99798085, 0.88692768, 0.99798085, 0.84654471, 0.99798085,
        0.84654471, 0.98283724, 0.95759788, 0.93740639, 0.93740639,
        0.99293298, 0.96769362, 0.99798085, 0.98788511, 0.80616174,
        0.96769362, 0.97778937, 0.99798085, 0.99747606, 0.99798085,
        0.9959617 , 0.99798085, 0.99798085, 0.92731065],
       [0.99604862, 0.98814586, 0.99604862, 0.95653482, 0.97826741,
        0.99604862, 0.99604862, 0.99604862, 0.99604862, 0.99604862,
        0.99604862, 0.99604862, 0.99604862, 0.98617017, 0.99604862,
        0.99604862, 0.99209724, 0.60486196, 0.99604862, 0.99604862,
        0.99604862, 0.99604862, 0.99604862, 0.99604862, 0.99604862,
        0.69969509, 0.66018128, 0.69969509, 0.95653482, 0.99604862,
        0.66018128, 0.99604862, 0.99604862, 0.99604862, 0.97629172,
        0.99604862, 0.99604862, 0.99604862, 0.99604862, 0.99604862,
        0.99604862, 0.99604862, 0.99604862, 0.97629172],
       [0.99603423, 0.99603423, 0.99603423, 0.99603423, 0.98611982,
        0.99603423, 0.99603423, 0.99603423, 0.99603423, 0.99603423,
        0.99603423, 0.99603423, 0.99603423, 0.98611982, 0.98611982,
        0.99603423, 0.99603423, 0.95637656, 0.99603423, 0.99603423,
        0.99603423, 0.99603423, 0.99603423, 0.99603423, 0.99603423,
        0.61928638, 0.95637656, 0.96629098, 0.99603423, 0.99603423,
        0.96629098, 0.99603423, 0.99603423, 0.99603423, 0.99603423,
        0.99603423, 0.99603423, 0.99603423, 0.99603423, 0.99603423,
        0.99603423, 0.99603423, 0.98611982, 0.98611982],
       [0.99496389, 0.99496389, 0.99496389, 0.99496389, 0.99496389,
        0.99496389, 0.99496389, 0.99496389, 0.99496389, 0.99496389,
        0.99496389, 0.99496389, 0.52156988, 0.99496389, 0.99496389,
        0.99496389, 0.99496389, 0.99496389, 0.95971115, 0.99496389,
        0.99496389, 0.99496389, 0.99496389, 0.99496389, 0.99496389,
        0.99496389, 0.99496389, 0.99496389, 0.99496389, 0.99496389,
        0.99496389, 0.99496389, 0.99496389, 0.99496389, 0.99496389,
        0.99496389, 0.99496389, 0.99496389, 0.99496389, 0.99496389,
        0.99496389, 0.99496389, 0.99496389, 0.99496389],
       [0.98882011, 0.98882011, 0.93292068, 0.91869173, 0.90751184,
        0.91259361, 0.91767537, 0.991361  , 0.94308421, 0.94308421,
        0.94308421, 0.98983647, 0.95324774, 0.92885526, 0.94308421,
        0.92783891, 0.93292068, 0.89836466, 0.98882011, 0.99898365,
        0.92275714, 0.92275714, 0.99898365, 0.94816598, 0.99898365,
        0.96341128, 0.93800244, 0.91767537, 0.98882011, 0.991361  ,
        0.89836466, 0.99898365, 0.991361  , 0.95832951, 0.92275714,
        0.92275714, 0.92275714, 0.98882011, 0.99847547, 0.99898365,
        0.99644276, 0.99644276, 0.99898365, 0.97357481],
       [0.99705665, 0.99705665, 0.99705665, 0.98969829, 0.97498156,
        0.99705665, 0.99705665, 0.79102248, 0.97498156, 0.97498156,
        0.99705665, 0.99705665, 0.98969829, 0.99705665, 0.99705665,
        0.97498156, 0.99705665, 0.9676232 , 0.99705665, 0.99705665,
        0.99705665, 0.99705665, 0.70566546, 0.97498156, 0.99705665,
        0.97498156, 0.93818975, 0.99705665, 0.98233993, 0.99705665,
        0.99705665, 0.98233993, 0.9676232 , 0.83517266, 0.90875629,
        0.99705665, 0.99705665, 0.9676232 , 0.99705665, 0.99705665,
        0.99705665, 0.99705665, 0.97498156, 0.99705665],
       [0.99663486, 0.99663486, 0.99663486, 0.99663486, 0.99663486,
        0.99663486, 0.99663486, 0.87885498, 0.99663486, 0.99663486,
        0.99663486, 0.74424941, 0.97139632, 0.99663486, 0.99663486,
        0.99663486, 0.99663486, 0.99663486, 0.99663486, 0.99663486,
        0.99663486, 0.99663486, 0.97980916, 0.99663486, 0.99663486,
        0.99663486, 0.99663486, 0.99663486, 0.99663486, 0.99663486,
        0.99663486, 0.97980916, 0.91250638, 0.91250638, 0.97139632,
        0.99663486, 0.99663486, 0.91250638, 0.99663486, 0.99663486,
        0.99663486, 0.99663486, 0.99495229, 0.99663486],
       [0.99796963, 0.99796963, 0.99796963, 0.99796963, 0.98680256,
        0.99796963, 0.99796963, 0.99796963, 0.97766588, 0.97766588,
        0.99796963, 0.99796963, 0.99796963, 0.99796963, 0.99796963,
        0.98781775, 0.99796963, 0.99796963, 0.99796963, 0.99796963,
        0.99796963, 0.99796963, 0.99796963, 0.95736213, 0.99796963,
        0.99796963, 0.99796963, 0.99796963, 0.99796963, 0.99796963,
        0.99796963, 0.99796963, 0.99796963, 0.99796963, 0.96751401,
        0.99796963, 0.99796963, 0.99796963, 0.99796963, 0.99796963,
        0.99796963, 0.99796963, 0.99796963, 0.99796963],
       [0.99463222, 0.99463222, 0.99463222, 0.99463222, 0.99463222,
        0.99463222, 0.99463222, 0.99463222, 0.99463222, 0.99463222,
        0.99463222, 0.99463222, 0.99463222, 0.99463222, 0.99463222,
        0.99463222, 0.99463222, 0.99463222, 0.99463222, 0.99463222,
        0.99463222, 0.99463222, 0.99463222, 0.99463222, 0.99463222,
        0.99463222, 0.99463222, 0.99463222, 0.99463222, 0.99463222,
        0.99463222, 0.99463222, 0.99463222, 0.99463222, 0.99463222,
        0.99463222, 0.99463222, 0.99463222, 0.99463222, 0.46322174,
        0.99463222, 0.99463222, 0.99194833, 0.99463222],
       [0.99786403, 0.99786403, 0.99786403, 0.9743683 , 0.97650428,
        0.99786403, 0.99786403, 0.99786403, 0.99786403, 0.99786403,
        0.99786403, 0.99786403, 0.99786403, 0.95514453, 0.95514453,
        0.99786403, 0.99786403, 0.99786403, 0.99786403, 0.99786403,
        0.99786403, 0.99786403, 0.99786403, 0.99786403, 0.99786403,
        0.99786403, 0.99786403, 0.99786403, 0.99786403, 0.99786403,
        0.99786403, 0.99786403, 0.99786403, 0.99786403, 0.98184421,
        0.99786403, 0.99786403, 0.99786403, 0.99786403, 0.98718415,
        0.99786403, 0.99786403, 0.99786403, 0.99252409],
       [0.99479052, 0.99479052, 0.99479052, 0.99479052, 0.99479052,
        0.99479052, 0.99479052, 0.99479052, 0.99479052, 0.99479052,
        0.99479052, 0.99479052, 0.99479052, 0.99479052, 0.99479052,
        0.99479052, 0.99479052, 0.99479052, 0.99479052, 0.99479052,
        0.99479052, 0.99479052, 0.99479052, 0.99479052, 0.99479052,
        0.99479052, 0.99479052, 0.99479052, 0.99479052, 0.99479052,
        0.99479052, 0.99479052, 0.99479052, 0.99479052, 0.99479052,
        0.99479052, 0.99479052, 0.99479052, 0.99479052, 0.47905169,
        0.98437155, 0.98437155, 0.99479052, 0.99479052],
       [0.99737732, 0.99737732, 0.99737732, 0.99737732, 0.99737732,
        0.99737732, 0.99737732, 0.99737732, 0.99737732, 0.99737732,
        0.99737732, 0.94492377, 0.99737732, 0.99737732, 0.99737732,
        0.99737732, 0.99737732, 0.99737732, 0.99737732, 0.99737732,
        0.99737732, 0.99737732, 0.99737732, 0.99737732, 0.99737732,
        0.99737732, 0.99737732, 0.99737732, 0.99737732, 0.99737732,
        0.99737732, 0.99737732, 0.93181039, 0.99737732, 0.99737732,
        0.99737732, 0.99737732, 0.93443306, 0.99737732, 0.97115055,
        0.99737732, 0.99737732, 0.99737732, 0.99737732]])

def supra_calculator(user_input, positive, negative, all_features, labels, prevalence):
  postive_list = [1 if item in user_input else 0 for item in all_features]
  postive_array = np.array(postive_list).reshape(34,1)  #change the number g=here
  neg_array = 1- postive_array
  
  pos_multi = np.multiply(positive,postive_array)
  neg_multi = np.multiply(negative,neg_array)
  
  total_sum = pos_multi + neg_multi
  
  row_wise_sum = np.prod(total_sum, axis=0)
  
  pre_normalize = np.multiply(row_wise_sum, prevalence)
  normalized = pre_normalize/pre_normalize.sum()
  
  list1, list2 = (list(t) for t in zip(*sorted(zip(normalized, labels))))
  
  result = {}
  for i in range(5):
    result[str(list2[::-1][i])] = round(list1[::-1][i],5)
  
  return result