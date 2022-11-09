''' age
sex
bmi
children
smoker
region
charges -target  '''
import streamlit as st
import pickle as pk
model=pk.load(open('insurance (3).pkl','rb'))
def run():
    st.title("HEALTH INSURANCE AMOUNT PREDICTION")
    st.image('insurance.jpg')
    #Name
    n=st.text_input("Enter Your Name")
    #ACCno
    acc=st.text_input("Enter your AccNo")
    #age
    age=st.number_input("Enter Your Age",min_value=10,max_value=100,step=1)
    #gender
    g=("Female","Male")
    op=list(range(len(g)))
    sex=st.selectbox("Enter Your Gender",op,format_func=lambda x:g[x])
    #bmi
    bmi=st.number_input("Enter your BMI")
    #children
    child=st.number_input("Enter Number of your children",value=0)
    #smoker
    l=("No","Yes")
    op2=list(range(len(l)))
    smoke=st.selectbox("Smoke YES/NO",op2,format_func=lambda x:l[x])
    # Region
    reg=('southeast','southwest','northwest','northeast')
    op9=list(range(len(reg)))
    region=st.selectbox("Enter Your Region",op9,format_func=lambda x:reg[x])
    if st.button("SUBMIT"):
        lis=[[age,sex,bmi,child,smoke,region]]
        pred=model.predict(lis)
        st.success("Hello "+n+" || "
                 "Account No "+acc+" || "
                 "Your Insurance Cost {}".format(round(pred[0],2)))
run()





