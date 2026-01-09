from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field



# 1️ Lookup tables


YEAR_IN_BUSINESS_SCORE = {
    1: 600,
    2: 400,
    3: 200,
    4: 0
}

LOCATION_SCORE = {
    1: 600,
    2: 300,
    3: 0
}

RELATIONSHIP_AGE_SCORE = {
    1: 600,
    2: 400,
    3: 200,
    4: 0
}

AUDITOR_QUALITY_SCORE = {
    1: 600,
    2: 450,
    3: 300,
    4: 150,
    5: 0
}

AUDITOR_OPINION_SCORE = {
    1: 600,
    2: 450,
    3: 0,
    4: 0,
    5: 0
}

NATIONALIZATION_SCORE = {
    1: 600,
    2: 450,
    3: 300,
    4: 0,
    5: 0
}



# 2️ Weights


WEIGHTS = {
    "year_in_business": 0.20,
    "location": 0.15,
    "relationship_age": 0.10,
    "auditor_quality": 0.20,
    "auditor_opinion": 0.20,
    "nationalization": 0.15
}



# 3️ SOA calculation engine


def calculate_soa_score(inputs):
    total = 0

    total += YEAR_IN_BUSINESS_SCORE[inputs.year_in_business] * WEIGHTS["year_in_business"]
    total += LOCATION_SCORE[inputs.location] * WEIGHTS["location"]
    total += RELATIONSHIP_AGE_SCORE[inputs.relationship_age] * WEIGHTS["relationship_age"]
    total += AUDITOR_QUALITY_SCORE[inputs.auditor_quality] * WEIGHTS["auditor_quality"]
    total += AUDITOR_OPINION_SCORE[inputs.auditor_opinion] * WEIGHTS["auditor_opinion"]
    total += NATIONALIZATION_SCORE[inputs.nationalization] * WEIGHTS["nationalization"]

    return round(total, 1)


# 4️ FastAPI input 


class SOAInput(BaseModel):
    year_in_business: int = Field(..., ge=1, le=4)
    location: int = Field(..., ge=1, le=3)
    relationship_age: int = Field(..., ge=1, le=4)
    auditor_quality: int = Field(..., ge=1, le=5)
    auditor_opinion: int = Field(..., ge=1, le=5)
    nationalization: int = Field(..., ge=1, le=5)


class SOAOutput(BaseModel):
    soa_score: float



# 5️ FastAPI app


app = FastAPI(
    title="SOA Scoring API",
    description="Status of Account scoring engine",
    version="1.0.0"
)


@app.post("/calculate-soa", response_model=SOAOutput)
def calculate_soa(data: SOAInput):
    try:
        score = calculate_soa_score(data)
        return {"soa_score": score}
    except KeyError:
        raise HTTPException(status_code=400, detail="Invalid input value")
