from src.preprocessing import load_data, fix_total_charges, encode_features


def test_total_charges_is_numeric():
    df = fix_total_charges(load_data())
    assert df["TotalCharges"].dtype == "float64"


def test_total_charges_has_no_missing():
    df = fix_total_charges(load_data())
    assert df["TotalCharges"].isna().sum() == 0


def test_zero_tenure_has_zero_charges():
    df = fix_total_charges(load_data())
    new_customers = df[df["tenure"] == 0]
    assert (new_customers["TotalCharges"] == 0).all()


def test_encoded_data_is_all_numeric():
    df = encode_features(fix_total_charges(load_data()))
    assert df.select_dtypes(exclude="number").empty


def test_customer_id_is_dropped():
    df = encode_features(fix_total_charges(load_data()))
    assert "customerID" not in df.columns


def test_churn_is_zero_or_one():
    df = encode_features(fix_total_charges(load_data()))
    assert set(df["Churn"].unique()) == {0, 1}