from Main import predict_churn

def test_high_risk():
    assert predict_churn(6) == "High Risk"

def test_low_risk():
    assert predict_churn(24) == "Low Risk"