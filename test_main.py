from Main import predict_churn

def test_high_risk():
    assert predict_churn(6) == "Low Risk"

def test_low_risk():
    assert predict_churn(24) == "Low Risk"