from fastapi import FastAPI, HTTPException, Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel, StrictFloat, Field
from typing import List

app = FastAPI(title="Aurvia Threshold Engine")


class ThresholdRequest(BaseModel):
    stream_values: List[StrictFloat] = Field(..., min_length=1)
    max_variance: StrictFloat


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(
    request: Request,
    exc: RequestValidationError
):
    return JSONResponse(
        status_code=400,
        content={
            "detail": "Invalid request payload. stream_values must contain numeric values and cannot be empty."
        },
    )


@app.post("/api/threshold")
async def threshold(data: ThresholdRequest):
    values = data.stream_values
    max_var = data.max_variance

    if len(values) == 0:
        raise HTTPException(
            status_code=400,
            detail="stream_values cannot be empty",
        )

    mean_val = sum(values) / len(values)

    max_deviation = max(
        abs(value - mean_val)
        for value in values
    )

    status = (
        "CRITICAL"
        if max_deviation > max_var
        else "STABLE"
    )

    return {
        "average": round(mean_val, 4),
        "max_variance": float(max_var),
        "element_count": len(values),
        "status": status,
    }

app.mount(
    "/",
    StaticFiles(directory="templates", html=True),
    name="frontend",
)