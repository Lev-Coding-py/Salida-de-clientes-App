from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pydantic import BaseModel
import pandas as pd
import joblib


# cargo el modelo que entrenamos
model = joblib.load("modelos_serializados/churn_model_BEST.pkl")

app = FastAPI()

# esto es para que el html pueda hablar con la api sin problemas de cors
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# sirvo los archivos de la carpeta para que el html sea accesible
app.mount("/static", StaticFiles(directory="."), name="static")

# cuando entras a localhost:8000 te muestra el html
@app.get("/")
def home():
    return FileResponse("churn_predictor_app.html")


# los datos que llegan del formulario
class Cliente(BaseModel):
    SeniorCitizen: int
    tenure: float
    TotalCharges: float

    Contract_Month_to_month: int = 0
    Contract_One_year: int = 0
    Contract_Two_year: int = 0

    PaymentMethod_Bank_transfer_automatic: int = 0
    PaymentMethod_Credit_card_automatic: int = 0
    PaymentMethod_Electronic_check: int = 0
    PaymentMethod_Mailed_check: int = 0

    OnlineSecurity_No: int = 0
    OnlineSecurity_No_internet_service: int = 0
    OnlineSecurity_Yes: int = 0

    TechSupport_No: int = 0
    TechSupport_No_internet_service: int = 0
    TechSupport_Yes: int = 0


# armo el dataframe con los nombres exactos que espera el modelo
def preparar_datos(cliente):
    return pd.DataFrame([{
        "SeniorCitizen": cliente.SeniorCitizen,
        "tenure": cliente.tenure,
        "TotalCharges": cliente.TotalCharges,

        "Contract_Month-to-month": cliente.Contract_Month_to_month,
        "Contract_One year": cliente.Contract_One_year,
        "Contract_Two year": cliente.Contract_Two_year,

        "PaymentMethod_Bank transfer (automatic)": cliente.PaymentMethod_Bank_transfer_automatic,
        "PaymentMethod_Credit card (automatic)": cliente.PaymentMethod_Credit_card_automatic,
        "PaymentMethod_Electronic check": cliente.PaymentMethod_Electronic_check,
        "PaymentMethod_Mailed check": cliente.PaymentMethod_Mailed_check,

        "OnlineSecurity_No": cliente.OnlineSecurity_No,
        "OnlineSecurity_No internet service": cliente.OnlineSecurity_No_internet_service,
        "OnlineSecurity_Yes": cliente.OnlineSecurity_Yes,

        "TechSupport_No": cliente.TechSupport_No,
        "TechSupport_No internet service": cliente.TechSupport_No_internet_service,
        "TechSupport_Yes": cliente.TechSupport_Yes,
    }])


# solo para verificar que la api esta viva
@app.get("/health")
def health():
    return {"status": "ok"}


# aqui llega la prediccion desde el formulario
@app.post("/predecir")
def predecir(cliente: Cliente):
    try:
        df = preparar_datos(cliente)
        pred = int(model.predict(df)[0])
        prob_no, prob_churn = model.predict_proba(df)[0]

        return {
            "prediccion": pred,
            "resultado": "CHURN ⚠️" if pred == 1 else "NO CHURN ✅",
            "probabilidad_churn": round(prob_churn, 4),
            "probabilidad_no_churn": round(prob_no, 4),
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))