
# 1️ LOOKUP TABLES 


# Year in Business
YEAR_IN_BUSINESS_SCORE = {
    1: 600,   # > 10 Years
    2: 400,   # 5 – 10 Years
    3: 200,   # > 2 – 5 Years
    4: 0      # ≤ 2 Years
}

# Location of Business
LOCATION_SCORE = {
    1: 600,   # Major Regions
    2: 300,   # Other Cities
    3: 0      # Outside Main Regions
}

# Relationship Age
RELATIONSHIP_AGE_SCORE = {
    1: 600,   # > 5 Years
    2: 400,   # 3 – 5 Years
    3: 200,   # 1 – 3 Years
    4: 0      # < 1 Year
}

# Auditor Quality
AUDITOR_QUALITY_SCORE = {
    1: 600,   # Class A
    2: 450,   # Class B
    3: 300,   # Unknown
    4: 150,   # Management Accounts
    5: 0      # Unaudited
}

# Auditor Opinion
AUDITOR_OPINION_SCORE = {
    1: 600,   # Unqualified
    2: 450,   # Qualified
    3: 0,     # Adverse
    4: 0,     # Disclaimer
    5: 0      # Non-audited
}

# Nationalization Scheme
NATIONALIZATION_SCORE = {
    1: 600,   # Platinum
    2: 450,   # High Green
    3: 300,   # Mid / Low Green
    4: 0,     # Red
    5: 0      # Not Available
}


# 2️ WEIGHTS (EXACT FROM EXCEL)

WEIGHTS = {
    "year_in_business": 0.20,
    "location": 0.15,
    "relationship_age": 0.10,
    "auditor_quality": 0.20,
    "auditor_opinion": 0.20,
    "nationalization": 0.15
}


# 3️ CALCULATION ENGINE (SUMPRODUCT)


def calculate_soa_score(inputs):
    total = 0

    total += YEAR_IN_BUSINESS_SCORE[inputs["year_in_business"]] * WEIGHTS["year_in_business"]
    total += LOCATION_SCORE[inputs["location"]] * WEIGHTS["location"]
    total += RELATIONSHIP_AGE_SCORE[inputs["relationship_age"]] * WEIGHTS["relationship_age"]
    total += AUDITOR_QUALITY_SCORE[inputs["auditor_quality"]] * WEIGHTS["auditor_quality"]
    total += AUDITOR_OPINION_SCORE[inputs["auditor_opinion"]] * WEIGHTS["auditor_opinion"]
    total += NATIONALIZATION_SCORE[inputs["nationalization"]] * WEIGHTS["nationalization"]

    return round(total, 1)   


# 4️ TERMINAL INPUT 


def get_input(prompt, valid):
    while True:
        try:
            v = int(input(prompt))
            if v in valid:
                return v
            print("❌ Invalid option")
        except ValueError:
            print("❌ Enter a number")


# 5️  MAIN PROGRAM


if __name__ == "__main__":

    print("\nSTATUS OF ACCOUNT (SOA) SCORING\n")

    inputs = {}
    inputs["year_in_business"] = get_input(
        "Year in Business (1=>10Y, 2=5–10Y, 3=2–5Y, 4=<2Y): ",
        YEAR_IN_BUSINESS_SCORE.keys()
    )
    inputs["location"] = get_input(
        "Location (1=Major, 2=Other, 3=Outside): ",
        LOCATION_SCORE.keys()
    )
    inputs["relationship_age"] = get_input(
        "Relationship Age (1=>5Y, 2=3–5Y, 3=1–3Y, 4=<1Y): ",
        RELATIONSHIP_AGE_SCORE.keys()
    )
    inputs["auditor_quality"] = get_input(
        "Auditor Quality (1=A, 2=B, 3=Unknown, 4=Mgmt, 5=None): ",
        AUDITOR_QUALITY_SCORE.keys()
    )
    inputs["auditor_opinion"] = get_input(
        "Auditor Opinion (1=Unqualified, 2=Qualified, 3=Adverse, 4=Disclaimer, 5=Non): ",
        AUDITOR_OPINION_SCORE.keys() 
    )
    inputs["nationalization"] = get_input(
        "Nationalization (1=Platinum, 2=High Green, 3=Mid/Low, 4=Red, 5=NA): ",
        NATIONALIZATION_SCORE.keys()
    )

    score = calculate_soa_score(inputs)

    print("\nFINAL SOA SCORE :", score)
