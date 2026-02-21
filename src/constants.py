numerical_cols = [
    "TOINC",
    "T_BREAD",
    "T_MEAT",
    "T_FISH",
    "T_MILK",
    "T_OIL",
    "T_FRUIT",
    "T_VEG",
    "T_SUGAR",
    "T_FOOD_NEC",
    "T_COFFEE",
    "T_MINERAL",
    "T_ALCOHOL",
    "T_TOBACCO",
    "T_OTHER_VEG",
    "T_FOOD_OUTSIDE",
    "T_CLOTH",
    "T_FURNISHING",
    "T_HEALTH",
    "T_HOUSING_WATER",
    "T_TRANSPORT",
    "T_COMMUNICATION",
    "T_RECREATION",
    "T_EDUCATION",
    "T_MISCELLANEOUS",
    "T_OTHER_EXPENDITURE",
    "T_OTHER_DISBURSEMENT",
    "T_NFOOD",
]

socio_demo_factors = {
    "National Income Decile of the Household": "NATDC",
    "Education Level of the Household Head": "HGC",
    "Region of the Household": "W_REGN",
    "Age Group of the Household Head": "AGE_GROUP",
    "Sex of the Household Head": "SEX",
    "Household Head Had a Job/Business During the Past Six Months": "JOB",
}

major_expenditure_categories = {
    "Food": "T_FOOD",
    "Vices": "T_VICES",
    "Clothing": "T_CLOTH",
    "Health": "T_HEALTH",
    "Home": "T_HOME",
    "Transportation": "T_TRANSPORT",
    "Communication": "T_COMMUNICATION",
    "Recreation": "T_RECREATION",
    "Education": "T_EDUCATION",
    "Miscellaneous": "T_MISCELLANEOUS",
    "Other Expenditures": "T_OTHER_EXPENDITURE",
    "Non-Family Expenditures": "T_OTHER_DISBURSEMENT",
}

food_categories = {
    "Bread and Cereals": "T_BREAD",
    "Meat": "T_MEAT",
    "Fish and Seafood": "T_FISH",
    "Milk, Cheese, and Eggs": "T_MILK",
    "Oils and Fats": "T_OIL",
    "Fruits": "T_FRUIT",
    "Vegetables": "T_VEG",
    "Sugar and Sweets": "T_SUGAR",
    "Coffee, Tea, Cocoa": "T_COFFEE",
    "Mineral Water, Juices, Softdrinks": "T_MINERAL",
    "Other Vegetables": "T_OTHER_VEG",
    "Food Not Elsewhere Classified": "T_FOOD_NEC",
}

socio_demo_factors_list = list(socio_demo_factors.items())

natdc_reindex = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]

hgc_reindex = [
    "No Grade Completed",
    "Preschool",
    "Elementary Undergraduate",
    "Elementary Graduate",
    "High School Undergraduate",
    "High School Graduate",
    "Post Secondary",
    "Post Secondary / TechVoc Graduate",
    "College Undergraduate",
    "College Graduate",
    "Post Baccalaureate",
]

w_regn_reindex = [
    "1",
    "2",
    "3",
    "4A",
    "4B",
    "5",
    "6",
    "7",
    "8",
    "9",
    "10",
    "11",
    "12",
    "13",
    "14",
    "15",
    "16",
]
