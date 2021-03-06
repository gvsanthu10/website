from flask import Flask, jsonify, request, render_template
import numpy as np

app = Flask(__name__)

#Home page
@app.route('/')
def welcome():
	return render_template('index.html')

#more info
@app.route('/moreinfo')
def more_info():
	return render_template('more_info.html')

#disclaimer
@app.route('/disclaimer')
def disclaimer():
	return render_template('disclaimer.html')       

#ovary 
@app.route('/ovary')
def ovary():
	return render_template('ovary.html', data={})

@app.route('/ovary/predict', methods =['POST'])
def ovary_predict():
    # Put all form entries values in a list 
    features = request.form.getlist("Tumor")
    from ovary_utili import my_function, positive, negative, final_labels

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

#thyroid
@app.route('/thyroid')
def thyroid():
    return render_template('thyroid.html')

@app.route('/thyroid/predict', methods =['POST'])
def thyroid_predict():
    from thyroid_util import pos_weights, neg_weights, all_features, labels, thyroid_cal

    user_input = request.form.getlist("Thyroid")

    results = thyroid_cal(pos_weights, neg_weights, user_input, labels)
    
    return render_template('thyroid.html', result = results)

#adult white matter
@app.route('/adultwhitematter')
def whitematter():
    return render_template('whitematter.html', data={})

@app.route('/adultwhitematter/predict', methods =['POST'])
def whitematter_predict():
    from wm_util import  positive, negative, all_features, labels, prevalence, whitemattet_calculator

    user_input = request.form.getlist("wm")
    
    result1 =  whitemattet_calculator(user_input, positive, negative, all_features, labels, prevalence)
    first = {'Type': 'Score'} 
    
    if len(user_input) != 0:
        return render_template('whitematter.html', data =  {**first, **result1})

    else:
        return render_template('whitematter.html', 
                               data = {**first, **result1})

#supretentorial mass
@app.route('/supra')
def supra():
	return render_template('supratentorial.html', data={})

@app.route('/supra/predict', methods =['POST'])
def supratentorial_predict():
    from supra_util import  positive, negative, all_features, labels, prevalence, supra_calculator

    user_input = request.form.getlist("supra")
    
    result1 =  supra_calculator(user_input, positive, negative, all_features, labels, prevalence)
    first = {'Type': 'Score'} 
    
    if len(user_input) != 0:
        return render_template('supratentorial.html', data =  {**first, **result1})

    else:
        return render_template('supratentorial.html', 
                               data = {**first, **result1})

#pediatric white matter
@app.route('/pediatric')
def pead_wm():
	return render_template('pead.html', data={})

@app.route('/pediatric/predict', methods =['POST'])
def pead_wm_predict():
    from peds_util import  positive, negative, all_features, labels, prevalence, peads_calculator

    user_input = request.form.getlist("supra")
    
    result1 =  peads_calculator(user_input, positive, negative, all_features, labels, prevalence)
    first = {'Type': 'Score'} 
        
    if len(user_input) != 0:
        return render_template('pead.html', data =  {**first, **result1})

    else:
        return render_template('pead.html', 
                               data = {**first, **result1})


#sellar masses
@app.route('/sella')
def sella():
	return render_template('sella.html', data={})

@app.route('/sella/predict', methods =['POST'])
def sella_predict():
    from sella_util import  positive, negative, all_features, labels, prevalence, sella_calculator

    user_input = request.form.getlist("supra")
        
    result1 =  sella_calculator(user_input, positive, negative, all_features, labels, prevalence)
    first = {'Type': 'Score'} 
        
    return render_template('sella.html', data = {**first, **result1})

#spine 
@app.route('/spine')
def spine():
	return render_template('spine.html', data={})

@app.route('/spine/predict', methods =['POST'])
def spine_predict():
    # Put all form entries values in a list 
    user_input = request.form.getlist("Thyroid")
    from spine_util import spine_calculator, positive, negative, all_features, labels


    result1 =  spine_calculator(user_input, positive, negative, all_features, labels)
    first = {'Type': 'Score'} 


    # Check the output values and retrive the result with html tag based on the value
    if len(user_input) != 0:
        return render_template('spine.html', data =  {**first, **result1})

    else:
        return render_template('spine.html', 
                               data = {**first, **result1})

###########################################end

#main infra page
@app.route('/infra')
def infra():
	return render_template('infraintra.html', data={})

#infra predictpage
@app.route('/infra/predict', methods=['GET', 'POST'])
def infra_predict():
	
	#getting userinput
	user_input = request.form.getlist("infra_intra")
	
	#importing data from util
	from infra_util import positive, negative, all_features, labels, prevalence, infra_intra_axial_calculator

	#empty dict for test
	result1 = infra_intra_axial_calculator(user_input, positive, negative, all_features, labels, prevalence)
	#print(result1)

	#Creating labels for google charts
	first = {'Type': 'Score'} 
	return render_template('infraintra.html', data =  {**first, **result1})

###########################################end

#main page
@app.route('/liver')  #change here
def liver():
	return render_template('liver.html', data={}) #change here

# predictpage
@app.route('/liver/predict', methods=['GET', 'POST'])  #change here
def liver_predict(): #change here
    
	#geting userinput
    user_input = request.form.getlist("infra_intra") 


	#importing data from util
    from liver_util import positive, negative, all_features, labels, prevalence, liver_calculator

	#empty dict for test
    result1 = liver_calculator(user_input, positive, negative, all_features, labels, prevalence)
	#print(result1)

	#Creating labels for google charts
    first = {'Type': 'Score'} 
    return render_template('liver.html', data =  {**first, **result1}) #change here

###########################################end

#main  page
@app.route('/pancreas')  #change here
def pancreas(): #change here
	return render_template('pancreas.html', data={}) #change here

# predictpage
@app.route('/pancreas/predict', methods=['GET', 'POST'])  #change here
def pancreas_predict(): #change here
    
	#geting userinput
    user_input = request.form.getlist("infra_intra") 


	#importing data from util
    from pancreas_util import positive, negative, all_features, labels, prevalence, pancreas_calculator

	#empty dict for test
    result1 = pancreas_calculator(user_input, positive, negative, all_features, labels, prevalence)
    #print(user_input)

	#Creating labels for google charts
    first = {'Type': 'Score'} 
    return render_template('pancreas.html', data =  {**first, **result1}) #change here

###########################################end

#main  page
@app.route('/pancreascystic')  #change here
def pancreas_cystic(): #change here
	return render_template('pancreascystic.html', data={}) #change here

# predictpage
@app.route('/pancreascystic/predict', methods=['GET', 'POST'])  #change here
def pancreas_cystic_predict(): #change here
    
	#geting userinput
    user_input = request.form.getlist("Tumor")
    #print(user_input) 

	#importing data from util
    from pancreas_cystic import positive, negative, all_features, labels, prevalence, pancreas_cystic_calculator

	#empty dict for test
    result1 = pancreas_cystic_calculator(user_input, positive, negative, all_features, labels, prevalence)
    #print(user_input)

	#Creating labels for google charts
    first = {'Type': 'Score'} 
    return render_template('pancreascystic.html', data =  {**first, **result1}) #change here

###########################################end

#main  page for infra_intra
@app.route('/infraintraventricular')  #change here
def infraintraventricular(): #change here
	return render_template('infra_intraventricular.html', data={}) #change here

# predictpage
@app.route('/infraintraventricular/predict', methods=['GET', 'POST'])  #change here
def infraintraventricular_predict(): #change here
    
	#geting userinput
    user_input = request.form.getlist("infra_intra")
    #print(user_input) 

	#importing data from util
    from infra_intraventricular_util import positive, negative, all_features, labels, prevalence, infra_intraventricular_calculator

	#empty dict for test
    result1 = infra_intraventricular_calculator(user_input, positive, negative, all_features, labels, prevalence)
    

	#Creating labels for google charts
    first = {'Type': 'Score'} 
    return render_template('infra_intraventricular.html', data =  {**first, **result1}) #change here

###########################################end

#main  page for charii
@app.route('/charii')  #change here
def charii(): #change here
	return render_template('charii.html', data={}) #change here

# predictpage
@app.route('/charii/predict', methods=['GET', 'POST'])  #change here
def charii_predict(): #change here
    
	#geting userinput
    user_input = request.form.getlist("Tumor")
    #print(user_input) 

	#importing data from util
    from charii_util import positive, negative, all_features, labels, charii_calculator

	#empty dict for test
    result1 = charii_calculator(user_input, positive, negative, all_features, labels)
    

	#Creating labels for google charts
    first = {'Type': 'Score'} 
    return render_template('charii.html', data =  {**first, **result1}) #change here

###########################################end

#main  page for extraaxial
@app.route('/extraaxial')  #change here
def extraaxial(): #change here
	return render_template('extraaxial.html', data={}) #change here

# predictpage
@app.route('/extraaxial/predict', methods=['GET', 'POST'])  #change here
def extraaxial_predict(): #change here
    
	#geting userinput
    user_input = request.form.getlist("Tumor")
    #print(user_input) 

	#importing data from util
    from extraaxial_util import positive, negative, all_features, labels, prevalence, extraaxial_calculator

	#empty dict for test
    result1 = extraaxial_calculator(user_input, positive, negative, all_features, labels, prevalence)
    

	#Creating labels for google charts
    first = {'Type': 'Score'} 
    return render_template('extraaxial.html', data =  {**first, **result1}) #change here

###########################################end

#main  page for nf
@app.route('/nf')  #change here
def nf(): #change here
	return render_template('nf.html', data={}) #change here

# predictpage
@app.route('/nf/predict', methods=['GET', 'POST'])  #change here
def nf_predict(): #change here
    
	#geting userinput
    user_input = request.form.getlist("Tumor")
    #print(user_input) 

	#importing data from util
    from nf_util import positive, negative, all_features, labels, nf_calculator

	#empty dict for test
    result1 = nf_calculator(user_input, positive, negative, all_features, labels)
    

	#Creating labels for google charts
    first = {'Type': 'Score'} 
    return render_template('nf.html', data =  {**first, **result1}) #change here

###########################################end

#main  page for pineal
@app.route('/pineal')  #change here
def pineal(): #change here
	return render_template('pineal.html', data={}) #change here

# predictpage
@app.route('/pineal/predict', methods=['GET', 'POST'])  #change here
def pineal_predict(): #change here
    
	#geting userinput
    user_input = request.form.getlist("Tumor")
    #print(user_input) 

	#importing data from util
    from pineal_util import positive, negative, all_features, labels, prevalence, pinear_calculator

	#empty dict for test
    result1 = pinear_calculator(user_input, positive, negative, all_features, labels, prevalence)
    

	#Creating labels for google charts
    first = {'Type': 'Score'} 
    return render_template('pineal.html', data =  {**first, **result1}) #change here

###########################################end

#main  page for prostate
@app.route('/prostate')  #change here
def prostate(): #change here
	return render_template('prostate.html', data={}) #change here

# predictpage
@app.route('/prostate/predict', methods=['GET', 'POST'])  #change here
def prostate_predict(): #change here
    
	#geting userinput
    user_input = request.form.getlist("Tumor")
    #print(user_input) 

	#importing data from util
    from prostate_util import positive, negative, all_features, labels, prevalence, prostate_calculator

	#empty dict for test
    result1 = prostate_calculator(user_input, positive, negative, all_features, labels, prevalence)
    

	#Creating labels for google charts
    first = {'Type': 'Score'} 
    return render_template('prostate.html', data =  {**first, **result1}) #change here

###########################################end


#main  page for sol pul nodule
@app.route('/solpulnodule')  #change here
def solpulnodule(): #change here
	return render_template('solpulnodule.html', data={}) #change here

# predictpage
@app.route('/solpulnodule/predict', methods=['GET', 'POST'])  #change here
def solpulnodule_predict(): #change here
    
	#geting userinput
    user_input = request.form.getlist("Tumor")
    #print(user_input) 

	#importing data from util
    from solpulnodule_util import positive, negative, all_features, labels, solpulnodule_calculator

	#empty dict for test
    result1 = solpulnodule_calculator(user_input, positive, negative, all_features, labels)
    

	#Creating labels for google charts
    first = {'Type': 'Score'} 
    return render_template('solpulnodule.html', data =  {**first, **result1}) #change here

###########################################end

#main  page for cpa masses
@app.route('/cpa')  #change here
def cpa(): #change here
	return render_template('cpangle.html', data={}) #change here

# predictpage
@app.route('/cpa/predict', methods=['GET', 'POST'])  #change here
def cpangle_predict(): #change here
    
	#geting userinput
    user_input = request.form.getlist("Tumor")
    #print(user_input) 

	#importing data from util
    from cpa_util import positive, negative, all_features, labels, prevalence, cpa_calculator

	#empty dict for test
    result1 = cpa_calculator(user_input, positive, negative, all_features, labels, prevalence)
    

	#Creating labels for google charts
    first = {'Type': 'Score'} 
    return render_template('cpangle.html', data =  {**first, **result1}) #change here

###########################################end

#main  page for neuro cystic masses
@app.route('/neurocystic')  #change here
def neurocystic(): #change here
	return render_template('neurocystic.html', data={}) #change here

# predictpage
@app.route('/neurocystic/predict', methods=['GET', 'POST'])  #change here
def neurocystic_predict(): #change here
    
	#geting userinput
    user_input = request.form.getlist("Tumor")
    #print(user_input) 

	#importing data from util
    from neurocystic_util import positive, negative, all_features, labels, prevalence, neurocystic_calculator

	#empty dict for test
    result1 = neurocystic_calculator(user_input, positive, negative, all_features, labels, prevalence)
    

	#Creating labels for google charts
    first = {'Type': 'Score'} 
    return render_template('neurocystic.html', data =  {**first, **result1}) #change here

###########################################end

#main  page for solid pul nodule1
@app.route('/solpulnodule1')  #change here
def solpulnodule1(): #change here
	return render_template('solpulnodule1.html', data={}) #change here

# predictpage
@app.route('/solpulnodule1/predict', methods=['GET', 'POST'])  #change here
def solpul_predict(): #change here
    
	#geting userinput
    user_input = request.form.getlist("Tumor")
    print(user_input) 

	#importing data from util
    from solidpulnodule1_util import positive, negative, all_features, labels, solpulnodule1_calculator

	#empty dict for test
    result1 = solpulnodule1_calculator(user_input, positive, negative, all_features, labels)
    

	#Creating labels for google charts
    first = {'Type': 'Score'} 
    return render_template('solpulnodule1.html', data =  {**first, **result1}) #change here

###########################################end

#main  page for breast
@app.route('/breast')  #change here
def breast(): #change here
	return render_template('breast.html', data={}) #change here

# predictpage
@app.route('/breast/predict', methods=['GET', 'POST'])  #change here
def breast_predict(): #change here
    
	#geting userinput
    user_input = request.form.getlist("Tumor")
    #print(user_input) 

	#importing data from util
    from breast_util import positive, negative, all_features, labels, breast_calculator

	#empty dict for test
    result1 = breast_calculator(user_input, positive, negative, all_features, labels)
    

	#Creating labels for google charts
    first = {'Type': 'Score'} 
    return render_template('breast.html', data =  {**first, **result1}) #change here

###########################################end

		
if __name__ == "__main__":
    app.run()
