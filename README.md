# Developer Salary Prediction
### Project:
A web application to predict the salary of a developer based on his/her experience, country and other features.
Live app: https://share.streamlit.io/ashok49473/developer-salary-prediction/main/app.py
### Data
- Stack Overflow Annual Developer Survey
- With nearly 80,000 responses fielded from over 180 countries and dependent territories, Stack Overflow Annual Developer Survey examines all aspects of the developer experience from career satisfaction and job search to education and opinions on open source software.
- Data preprocessing - Done✔
- Categorical encoding
- Outliers Handling

### Model
For Model Selection:
- Linear Regression
- Lasso
- SVR
- XGBRegressor
- LGBMRegressor

![models](https://github.com/ashok49473/Developer-Salary-Prediction/blob/main/artifacts/models.PNG)
**LGBMRegressor performed better**
- Hyperparameter tuning - Done✔

### Evaluation
- Obtained test rmse of 28907.86 and r2 score of 0.59.

Model Predictions vs Actual Salaries
![pred](https://github.com/ashok49473/Developer-Salary-Prediction/blob/main/artifacts/download.png)


# Tools 🎯
- Windows 10
- Python 3.8
- lightGBM
- scikit-learn
- pandas
- seaborn
- numpy
- optuna
- streamlit

# Run on local machine 💻
1. Create a virtual environment <br>
`python -m venv streamlit_app`<br>
2. Activate the virtual environment<br>
`streamlit_app\Scripts\activate.bat<br>
3.Clone or Download all the files<br>
`git clone https://github.com/ashok49473/Developer-Salary-Prediction.git`<br>
4. Install dependencies<br>
`pip install -r requirements.txt`<br>
5. Run and open localhost<br>
`streamlit run app.py`<br>
# App
![Home](https://github.com/ashok49473/Developer-Salary-Prediction/blob/main/artifacts/Screenshot%20(88).png)
# Thank you ..!
