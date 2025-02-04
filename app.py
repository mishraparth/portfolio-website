from flask import Flask, render_template, request
import pandas as pd
import pickle

app = Flask(__name__)

# Load the Model 1 (already done in the previous step)
with open('model.pkl', 'rb') as file:
    model = pickle.load(file)
with open('encoders.pkl', 'rb') as file:
    encoders = pickle.load(file)
with open('scaler.pkl', 'rb') as file:
    scaler = pickle.load(file)

categorical_features = ['State', 'City', 'Locality', 'Property_Type', 'Furnished_Status', 'Public_Transport_Accessibility', 'Parking_Space', 'Security', 'Amenities', 'Facing', 'Owner_Type', 'Availability_Status']
numerical_features = ['BHK', 'Size_in_SqFt', 'Price_per_SqFt', 'Floor_No', 'Total_Floors', 'Age_of_Property', 'Nearby_Schools', 'Nearby_Hospitals']

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/model1', methods=['GET', 'POST'])
def model1():
    if request.method == 'POST':
        input_data = {
            'State': request.form['state'],
            'City': request.form['city'],
            'Locality': request.form['locality'],
            'Property_Type': request.form['property_type'],
            'BHK': int(request.form['bhk']),
            'Size_in_SqFt': float(request.form['size_in_sqft']),
            'Price_per_SqFt': float(request.form['price_per_sqft']),
            'Furnished_Status': request.form['furnished_status'],
            'Floor_No': int(request.form['floor_no']),
            'Total_Floors': int(request.form['total_floors']),
            'Age_of_Property': int(request.form['age_of_property']),
            'Nearby_Schools': int(request.form['nearby_schools']),
            'Nearby_Hospitals': int(request.form['nearby_hospitals']),
            'Public_Transport_Accessibility': request.form['public_transport_accessibility'],
            'Parking_Space': request.form['parking_space'],
            'Security': request.form['security'],
            'Amenities': request.form['amenities'],
            'Facing': request.form['facing'],
            'Owner_Type': request.form['owner_type'],
            'Availability_Status': request.form['availability_status']
        }

        input_df = pd.DataFrame([input_data])
        
        for feature in categorical_features:
            input_df[feature] = encoders[feature].transform(input_df[feature])

        input_df[numerical_features] = scaler.transform(input_df[numerical_features])

        predicted_price = model.predict(input_df)[0]
        return render_template('model1.html', prediction=predicted_price)
    return render_template('model1.html')

@app.route('/graph')
def graph():
    return render_template('graph.html')

if __name__ == '__main__':
    app.run(debug=True)
