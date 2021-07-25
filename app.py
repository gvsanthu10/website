from flask import Flask, jsonify, request, render_template
from ovary_utili import my_function, positive, negative, final_labels
import numpy as np

app = Flask(__name__)
		
@app.route('/')
def welcome():
	return render_template('index.html')

@app.route('/ovary')
def ovary():
	return render_template('ovary.html', data={})

@app.route('/ovary/predict', methods =['POST'])
def ovary_predict():
    # Put all form entries values in a list 
    features = request.form.getlist("Tumor")

    all_features = ['solid', 'solid_necrosis','cystic','unilocular','honeycomb','vegetations', 'papillary','multi','hypointese','calcification','haemo','dark','fat','diffusion','endo']
    postive_features = [1 if feature in features else 0 for feature in all_features]
    postive_features = np.array(postive_features).reshape(15,1)

    result1 =  my_function(pos_weights=positive, neg_weights=negative, some_pos_row=postive_features, labels=final_labels)
    first = {'Type': 'Score'} 


    # Check the output values and retrive the result with html tag based on the value
    if len(features) != 0:
        return render_template('ovary.html', data =  {**first, **result1})

    else:
        return render_template('ovary.html', 
                               data = {**first, **result1})

		
if __name__ == "__main__":
    app.run()