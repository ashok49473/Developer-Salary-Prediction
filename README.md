# Developer Salary Prediction
### Project:
- This is a machine learning-based solution to predict the salary of a software developer based on various factors such as years of experience, location, and education.
- The main advantage of this project is that it can save time and resources for both employers and job seekers in determining a fair salary range. Additionally, the project can help identify trends and disparities in developer salaries, allowing for more informed decision making in the job market.
-  The use of machine learning also enables more accurate salary predictions compared to traditional methods.

Here is a web application to predict the salary of a developer based on his/her experience, country and other features.<br>
Live app: [Click here](https://ashok49473-developer-salary-prediction-app-6jbn9h.streamlit.app)
### Data
- Source:[Stack Overflow Annual Developer Survey](https://insights.stackoverflow.com/survey)
- With nearly 80,000 responses fielded from over 180 countries and dependent territories, Stack Overflow Annual Developer Survey examines all aspects of the developer experience from career satisfaction and job search to education and opinions on open source software.
- Data preprocessing ✔
- Categorical encoding ✔
- Outliers Handling ✔
- Model Training and Evaluation ✔
- Deployment ✔
### Model
For Model Selection:
- Linear Regression
- Lasso
- SVR
- XGBRegressor
- LGBMRegressor

![models](https://github.com/ashok49473/Developer-Salary-Prediction/blob/main/artifacts/models.PNG)
- **LGBMRegressor performed better**


### Evaluation
- Obtained r2 score of 0.59
- **Model Predictions vs Actual Salaries**

![pred](https://github.com/ashok49473/Developer-Salary-Prediction/blob/main/artifacts/download.png)


# Tools🎯
- Windows 10
- Python 3.8
- lightGBM
- scikit-learn
- pandas
- seaborn
- numpy
- optuna
- streamlit

# Installation💻
1. Create a virtual environment <br>
`python -m venv streamlit_app`<br>
2. Activate the virtual environment<br>
`streamlit_app\Scripts\activate.bat`<br>
3.Clone or Download all the files<br>
`git clone https://github.com/ashok49473/Developer-Salary-Prediction.git`<br>
4. Install dependencies<br>
`pip install -r requirements.txt`<br>
5. Run and open localhost<br>
`streamlit run app.py`<br>

# App
![Home](https://github.com/ashok49473/Developer-Salary-Prediction/blob/main/artifacts/Screenshot%20(88).png)
##### Ashok kumar Palivela 
