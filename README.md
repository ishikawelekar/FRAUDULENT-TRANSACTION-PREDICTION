# FRAUDULENT-TRANSACTION-PREDICTION
The Dataset is to be identify about a transaction to predict whether it is Fraudulent or Not.

# BUSINESS STATEMENT:
In recent times, the number of fraud transactions has increased drastically, due to which companies are facing a lot of challenges. For many banks, retaining high profitable customers is the most important business goal. Banking fraud, however, poses a significant threat to this goal. In this project, We are building a fraud detection model to help banks identify frauds and be vigilant enough to reduce losses incurred due to such unauthorised transactions by the fraudsters.

# DATASET DETAILS:
• step - maps a unit of time in the real world. In this case 1 step is 1 hour of time. Total steps 744 (30 days simulation).

• type - CASH-IN, CASH-OUT, DEBIT, PAYMENT and TRANSFER.

• amount - amount of the transaction in local currency.

• nameOrig - customer who started the transaction

• oldbalanceOrg - initial balance before the transaction

• newbalanceOrig - new balance after the transaction

• nameDest - customer who is the recipient of the transaction

• oldbalanceDest - initial balance recipient before the transaction. Note that there is not information for customers that start with M (Merchants).

• newbalanceDest - new balance recipient after the transaction. Note that there is not information for customers that start with M (Merchants).

• isFraud - This is the transactions made by the fraudulent agents inside the simulation. In this specific dataset the fraudulent behavior of the agents aims to profit by taking control or customers accounts and try to empty the funds by transferring to another account and then cashing out of the system.

• isFlaggedFraud - The business model aims to control massive transfers from one account to another and flags illegal attempts. An illegal attempt in this dataset is an attempt to transfer more than 200.000 in a single transaction.

# Steps involved:
• Exploratory data analysis (EDA) - the process of going through a dataset and finding out more about it.

• Model Visualization - the process of going to visualize each variable based on other variables.

• Model Cleaning - To clean the feature variables which doesn't give any beneficial information.

• Unbalanced Model comparison - comparing several different models to find the best one.

• Balancing model - Balancing model using OverRandom Sampling.

• Balanced Model comparison - comparing several different models to find the best one.

• Model Finalization -  To finalize model.

• Deployment

# Libraries Required
• pandas for data analysis.

• NumPy for numerical operations.

• Matplotlib/seaborn for plotting or data visualization.

• Scikit-Learn for machine learning modelling and evaluation.

• NumPy for numerical operations.

• Matplotlib/seaborn for plotting or data visualization.

• Scikit-Learn for machine learning modelling and evaluation.

# CONCLUSION
Good prediction results can be achieved with imbalanced datasets as well as with balanced ones. Decision Tree Classifier, Random Forest Classifier, XG Boost, Light GBM classifier, Ada Boost, and Bagging Classifier gave us the best results being able to detect more than 99.50% fraud transactions and at the same time not classifying some of non-fraud transactions as fraud. There is no perfect model It is up to the company and its objectives to decide which approach is the best in each particular situation.
