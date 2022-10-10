import pandas as pd
import numpy as np
import pickle
import streamlit as st
from PIL import Image
import joblib
classifier = joblib.load("mts.pkl")

def welcome():
	return 'welcome all'

# defining the function which will make the prediction using
# the data which the user inputs
def prediction(Age, BusinessTravel, DailyRate, Department, DistanceFromHome,Education, EducationField, EnvironmentSatisfaction, Gender,HourlyRate, JobInvolvement, JobLevel, JobRole,
JobSatisfaction, MaritalStatus, MonthlyIncome, MonthlyRate,NumCompaniesWorked, OverTime, PercentSalaryHike,PerformanceRating, RelationshipSatisfaction, StockOptionLevel,
TotalWorkingYears, TrainingTimesLastYear, WorkLifeBalance,YearsAtCompany, YearsInCurrentRole, YearsSinceLastPromotion,YearsWithCurrManager):
    series={"Age":Age,
     "BusinessTravel":BusinessTravel,
     "DailyRate":DailyRate,
     "Department":Department,
     "DistanceFromHome":DistanceFromHome,
     "Education":Education,
     "EducationField":EducationField,
     "EnvironmentSatisfaction":EnvironmentSatisfaction,
     "Gender":Gender,
     "HourlyRate":HourlyRate,
     "JobInvolvement":JobInvolvement,
     "JobLevel":JobLevel,
     "JobRole":JobRole,
     "JobSatisfaction":JobSatisfaction,
     "MaritalStatus":MaritalStatus,
     "MonthlyIncome":MonthlyIncome,
     "MonthlyRate":MonthlyRate,
     "NumCompaniesWorked":NumCompaniesWorked,
     "OverTime":OverTime,
     "PercentSalaryHike":PercentSalaryHike,
     "PerformanceRating":PerformanceRating,
     "RelationshipSatisfaction":RelationshipSatisfaction,
     "StockOptionLevel":StockOptionLevel,
     "TotalWorkingYears":TotalWorkingYears,
     "TrainingTimesLastYear":TrainingTimesLastYear,
     "WorkLifeBalance":WorkLifeBalance,
     "YearsAtCompany":YearsAtCompany,
     "YearsInCurrentRole":YearsInCurrentRole,
     "YearsSinceLastPromotion":YearsSinceLastPromotion,
     " YearsWithCurrManager":YearsWithCurrManager}
    vector=pd.DataFrame(series,index=[0])
    prediction=classifier.predict(vector)
    return prediction
	

# this is the main function in which we define our webpage
def main():
    st.title("Employee Attrition Prediction")
    html_temp = """
	<div style ="background-color:yellow;padding:13px">
	<h1 style ="color:black;text-align:center;">Employee Attrition Prediction ML App </h1>
	</div>
	"""
    st.markdown(html_temp, unsafe_allow_html = True)
    Age = st.text_input("Age")
    BusinessTravel=st.radio("BusinessTravel {'Travel_Rarely':0, 'Travel_Frequently':1, 'Non-Travel':2}",('012'))
    DailyRate=st.text_input("DailyRate")
    Department=st.radio("Department {'Research & Development':0, 'Sales':1, 'Human Resources':2}",('012'))
    DistanceFromHome=st.text_input("DistanceFromHome")
    Education=st.radio("Education {1:'Below College' , 2:'College' , 3:'Bachelor' , 4:'Master' , 5:'Doctor'}",('12345'))
    EducationField=st.radio("EducationField {'Life Sciences':0, 'Medical':1, 'Marketing':2, 'Technical Degree':3, 'Other':4, 'Human Resources':5}",('012345'))
    EnvironmentSatisfaction=st.radio("EnvironmentSatisfaction {1:'Low', 2:'Medium' , 3:'High' , 4:'Very High'}",('1234'))
    Gender=st.radio("Gender {'Male':0 ,'Female':1}",('01'))
    HourlyRate=st.text_input("HourlyRate")
    JobInvolvement=st.radio("JobInvolvement {1:'Low', 2:'Medium' , 3:'High' , 4:'Very High'}",('1234'))
    JobLevel=st.text_input("JobLevel on a scale of (1 to 5)")
    JobRole=st.radio("JobRole {'Sales Executive': 0, 'Research Scientist': 1, 'Laboratory Technician': 2, 'Manufacturing Director': 3, 'Healthcare Representative': 4, 'Manager': 5, 'Sales Representative': 6, 'Research Director': 7, 'Human Resources': 8}",("012345678"))
    JobSatisfaction=st.radio("JobSatisfaction  {1:'Low', 2:'Medium' , 3:'High' , 4:'Very High'}",('1234'))
    MaritalStatus=st.radio("MaritalStatus {'Married': 0, 'Single': 1, 'Divorced': 2}",('012'))
    MonthlyIncome=st.text_input("MonthlyIncome")
    MonthlyRate=st.text_input("MonthlyRate")
    NumCompaniesWorked=st.text_input("NumCompaniesWorked")
    OverTime=st.radio("OverTime {'No':0,'Yes':1}",('01'))
    PercentSalaryHike=st.text_input("'PercentSalaryHike")
    PerformanceRating=st.radio("PerformanceRating {1:'Low' , 2:'Good' , 3:'Excellent' , 4:'Outstanding'}",('1234'))
    RelationshipSatisfaction=st.radio("RelationshipSatisfaction  {1:'Low', 2:'Medium' , 3:'High' , 4:'Very High'}",('1234'))
    StockOptionLevel=st.text_input("StockOptionLevel on a scale of (0 to 3)")
    TotalWorkingYears=st.text_input("TotalWorkingYears")
    TrainingTimesLastYear=st.text_input("TrainingTimesLastYear")
    WorkLifeBalance=st.radio("WorkLifeBalance {1:'Bad' , 2:'Good' , 3:'Better' , 4:'Best'}",('1234'))
    YearsAtCompany=st.text_input("YearsAtCompany")
    YearsInCurrentRole=st.text_input("YearsInCurrentRole")
    YearsSinceLastPromotion=st.text_input("YearsSinceLastPromotion")
    YearsWithCurrManager=st.text_input("YearsWithCurrManager")
    result=''
    if st.button("Predict"):
        result = prediction(Age, BusinessTravel, DailyRate, Department, DistanceFromHome,Education, EducationField, EnvironmentSatisfaction, Gender,HourlyRate, JobInvolvement, JobLevel, JobRole,JobSatisfaction, MaritalStatus, MonthlyIncome, MonthlyRate,NumCompaniesWorked, OverTime, PercentSalaryHike,PerformanceRating, RelationshipSatisfaction, StockOptionLevel,TotalWorkingYears, TrainingTimesLastYear, WorkLifeBalance,YearsAtCompany, YearsInCurrentRole, YearsSinceLastPromotion,YearsWithCurrManager)
        if result==[1]:
            st.success("The Employee is going to leave the Company")
        else:
            st.success("The Employee will stay in the Company")
        
if __name__=='__main__':
	main()