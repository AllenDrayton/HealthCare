# Import necessary library
import joblib 
import streamlit as st

model = joblib.load('health_cost.joblib') 

st.image("g1.gif", use_column_width=True )

# Title and description for your app
st.title("Health Cost Prediction App")
st.write("This app predicts health insurance costs based on age, sex, BMI, children, and smoking status.")

# Sidebar for user input
st.subheader("User Information ")

# Age input
age = st.slider("Age", 18, 60, 30)

# Sex input
sex = st.selectbox("Sex", ["male", "female"])

# BMI input
#bmi = st.sidebar.slider("BMI (Body Mass Index)", 15.0, 50.0, 25.0)
st.header('BMI Calculator')

weight = st.number_input("Enter Your Weight (in kgs)")
height = st.number_input("Enter Your height (in cms)")

try:
    bmi = weight / ((height/100)**2)
except:
    st.text("Enter some value of height")

if(st.button('Calculate BMI')):
    st.text("Your BMI Index is {}".format(bmi))

    if(bmi < 16):
        st.error("You are Extremely Underweight")
    elif(bmi >= 16 and bmi < 18.5):
        st.warning("You are Underweight")
    elif(bmi >= 18.5 and bmi < 25):
        st.success("Healthy")
    elif(bmi >= 25 and bmi < 30):
        st.warning("Overweight")
    elif(bmi >= 30):
        st.error("Extremely Overweight")


bmi = st.number_input("Enter your Bmi Result here")

# Children input
children = st.slider("Number of Children", 0, 5, 0)

# Smoking input
smoker = st.selectbox("Smoker?", ["yes", "no"])

# Convert categorical inputs to numerical
sex = 1 if sex == "female" else 0
smoker = 1 if smoker == "yes" else 0






# Display prediction

st.header("Predict Health Insurance Cost ?")
if(st.button('Predict the cost')):
# Create feature vector
    features = [age, sex, bmi, children, smoker]
# Make predictions
    prediction =model.predict([features])
    added_cost = prediction[0]


    st.success(f"The estimated cost is ${added_cost+3000:.2f}")
    

