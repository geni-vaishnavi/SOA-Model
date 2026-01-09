
# 1️ Lookup Tables 


YEAR_IN_BUSINESS_SCORE = {
    "< 1 Year": 0,
    "1 – 2 Years": 200,
    "> 2 Years – 6 Years": 400,
    "> 6 Years": 600
}

LOCATION_SCORE = {
    "Outside Prime Region": 200,
    "Within Riyadh, Jeddah, Eastern Region": 600
}

RELATIONSHIP_AGE_SCORE = {
    "New Relationship": 0,
    "1 – 3 Years": 300,
    "> 3 Years": 600
}

AUDITOR_QUALITY_SCORE = {
    "No Auditor": 0,
    "Class C Auditor": 300,
    "Class B Auditor": 400,
    "Class A Auditor": 450
}

AUDITOR_OPINION_SCORE = {
    "Adverse": 0,
    "Qualified": 200,
    "Unqualified": 500
}


NATIONALIZATION_SCORE = {
    "Non-Compliant": 0,
    "Partially Compliant": 133,
    "Compliant": 600
}


# 2️⃣ Weights 


WEIGHTS = {
    "year_in_business": 0.20,
    "location": 0.15,
    "relationship_age": 0.10,
    "auditor_quality": 0.20,
    "auditor_opinion": 0.20,
    "nationalization": 0.15
}


# 3️ SOA Calculation Engine 


def calculate_soa_score(inputs):
    """
    Calculates SOA score using Excel-equivalent logic:
    Lookup → Weight → Weighted Sum
    """

    total_score = 0

    total_score += YEAR_IN_BUSINESS_SCORE[inputs["year_in_business"]] * WEIGHTS["year_in_business"]
    total_score += LOCATION_SCORE[inputs["location"]] * WEIGHTS["location"]
    total_score += RELATIONSHIP_AGE_SCORE[inputs["relationship_age"]] * WEIGHTS["relationship_age"]
    total_score += AUDITOR_QUALITY_SCORE[inputs["auditor_quality"]] * WEIGHTS["auditor_quality"]
    total_score += AUDITOR_OPINION_SCORE[inputs["auditor_opinion"]] * WEIGHTS["auditor_opinion"]
    total_score += NATIONALIZATION_SCORE[inputs["nationalization"]] * WEIGHTS["nationalization"]

    
    return round(total_score)


# 4️ Test Case 


if __name__ == "__main__":

    example_inputs = {
        "year_in_business": "> 2 Years – 6 Years",
        "location": "Within Riyadh, Jeddah, Eastern Region",
        "relationship_age": "New Relationship",
        "auditor_quality": "Class A Auditor",
        "auditor_opinion": "Unqualified",
        "nationalization": "Partially Compliant"
    }

    final_score = calculate_soa_score(example_inputs)
    print("FINAL SOA SCORE:", final_score)
