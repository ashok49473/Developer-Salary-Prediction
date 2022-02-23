# Developer Salary Prediction
### Project:
A web application to predict the salary of a developer based on his/her experience, country and other features.
### Data
- Stack Overflow Annual Developer Survey
- With nearly 80,000 responses fielded from over 180 countries and dependent territories, Stack Overflow Annual Developer Survey examines all aspects of the developer experience from career satisfaction and job search to education and opinions on open source software.
### Model
For Model Selection:
- Linear Regression
- Lasso
- SVR
- XGBRegressor
- LGBMRegressor
![models]()
*LGBMRegressor performed better*
- Hyperparameter tuning - Done✔
### Evaluation
- Obtained test rmse of ---
Error distribution
![err]()
Model Predictions vs Actual Salaries
![pred]()
Live app: https://share.streamlit.io/ashok49473/developer-salary-prediction/main/app.py

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
1. Create a virtual environment
`python -m venv streamlit_app`
2. Activate the virtual environment
`streamlit_app\Scripts\activate.bat
3.Clone or Download all the files
`git clone https://github.com/ashok49473/Developer-Salary-Prediction.git`
4. Install dependencies
`pip install -r requirements.txt`
5. Run and open localhost
`streamlit run app.py`
# App
![Home](https://github.com/ashok49473/Developer-Salary-Prediction/blob/main/artifacts/Screenshot%20(88).png)
# Thank you ..!
