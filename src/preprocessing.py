import pandas as pd


def clean_and_prepare_data(df: pd.DataFrame) -> pd.DataFrame:
    # Drop unnecessary columns
    drop_cols = [
        "W_OID",
        "W_SHSN",
        "W_HCN",
        "RSTR",
        "PSU",
        "RFACT",
        "BWEIGHT",
        "FSIZE",
        "AGRI_SAL",
        "NONAGRI_SAL",
        "WAGES",
        "NETSHARE",
        "CASH_ABROAD",
        "CASH_DOMESTIC",
        "RENTALS_REC",
        "INTEREST",
        "PENSION",
        "DIVIDENDS",
        "OTHER_SOURCE",
        "NET_RECEIPT",
        "REGFT",
        "NET_LPR",
        "NET_CFG",
        "NET_FISH",
        "NET_FOR",
        "NET_RET",
        "NET_MFG",
        "NET_COM",
        "NET_TRANS",
        "NET_MIN",
        "NET_CONS",
        "NET_NEC",
        "EAINC",
        "LOSSES",
        "T_OTHREC",
        "T_TOREC",
        "FOOD_ACCOM_SRVC",
        "MS",
        "OCCUP",
        "KB",
        "CW",
        "HHTYPE",
        "MEMBERS",
        "AGELESS5",
        "AGE5_17",
        "EMPLOYED_PAY",
        "EMPLOYED_PROF",
        "SPOUSE_EMP",
        "BLDG_TYPE",
        "ROOF",
        "WALLS",
        "HSE_ALTERTN",
        "TOILET",
        "ELECTRIC",
        "WATER",
        "DISTANCE",
        "RADIO_QTY",
        "TV_QTY",
        "CD_QTY",
        "STEREO_QTY",
        "REF_QTY",
        "WASH_QTY",
        "AIRCON_QTY",
        "CAR_QTY",
        "LANDLINE_QTY",
        "CELLPHONE_QTY",
        "PC_QTY",
        "OVEN_QTY",
        "MOTOR_BANCA_QTY",
        "MOTORCYCLE_QTY",
        "POP_ADJ",
        "PCINC",
        "NATPC",
        "REGDC",
        "REGPC",
    ]
    df = df.drop(columns=drop_cols, errors="ignore")

    # Change column types
    type_map = {
        "W_REGN": "string",
        "URB": "string",
        "SEX": "string",
        "NATDC": "string",
        "JOB": "string",
    }
    df = df.astype({k: v for k, v in type_map.items() if k in df.columns})

    # Standardize 'W_REGN', 'URB', 'SEX', 'JOB'
    df.loc[df["W_REGN"].str.lower() == "41".lower(), "W_REGN"] = "4A"
    df.loc[df["W_REGN"].str.lower() == "42".lower(), "W_REGN"] = "4B"

    df.loc[df["URB"].str.lower() == "1".lower(), "URB"] = "Urban"
    df.loc[df["URB"].str.lower() == "2".lower(), "URB"] = "Rural"

    df.loc[df["SEX"].str.lower() == "1".lower(), "SEX"] = "Male"
    df.loc[df["SEX"].str.lower() == "2".lower(), "SEX"] = "Female"

    df.loc[df["JOB"].str.lower() == "1".lower(), "JOB"] = "With Job/Business"
    df.loc[df["JOB"].str.lower() == "2".lower(), "JOB"] = "No Job/Business"

    # Computed attributes
    if "T_FOOD_OUTSIDE" in df.columns and "T_FOOD" in df.columns:
        df["PROP_FOOD_OUTSIDE"] = df["T_FOOD_OUTSIDE"] / df["T_FOOD"]
    if "T_ALCOHOL" in df.columns and "T_TOBACCO" in df.columns:
        df["T_VICES"] = df["T_ALCOHOL"] + df["T_TOBACCO"]
    if "T_FURNISHING" in df.columns and "T_HOUSING_WATER" in df.columns:
        df["T_HOME"] = df["T_FURNISHING"] + df["T_HOUSING_WATER"]

    # Binned attributes (AGE_GROUP)
    if "AGE" in df.columns:
        age_bins = [0, 29, 39, 49, 59, 120]
        age_labels = ["Under 30", "30–39", "40–49", "50–59", "60+"]
        df["AGE_GROUP"] = pd.cut(df["AGE"], bins=age_bins, labels=age_labels)

    # Convert HGC
    if "HGC" in df.columns:
        df["HGC"] = df["HGC"].apply(convert_hgc_code_to_string)

    return df


def convert_hgc_code_to_string(code):
    exact_matches = {
        0: "No Grade Completed",
        10: "Preschool",
        280: "Elementary Graduate",
        350: "High School Graduate",
        900: "Post Baccalaureate",
    }

    if code in exact_matches:
        return exact_matches[code]
    elif 210 <= code <= 260:
        return "Elementary Undergraduate"
    elif 310 <= code <= 330:
        return "High School Undergraduate"
    elif 410 <= code <= 420:
        return "Post Secondary"
    elif 501 <= code <= 589:
        return "Post Secondary / TechVoc Graduate"
    elif 810 <= code <= 840:
        return "College Undergraduate"
    elif 601 <= code <= 689:
        return "College Graduate"
    else:
        return "N/A"
