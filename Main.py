def predict_churn(tenure):
    if tenure < 12:
        return "High Risk"
    return "Low Risk"


print(predict_churn(6))