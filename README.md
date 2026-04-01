# Salida de clientes App 🛡️

> Una aplicacion de Machine Learning que predice si un cliente esta a punto de irse.

[![Demo en vivo](https://img.shields.io/badge/demo-en%20Render-5affb0?style=flat-square)](https://churnshield-api-p1gs.onrender.com/)

---
![ChurnShield App](https://github.com/user-attachments/assets/e5c4619d-44cc-47c3-b340-a7a15765c422)

---

Todas las empresas pierden clientes, pero estas salidas pueden anticiparse. El dataset viene de una empresa Telco de la plataforma Kaggle.

---

## Qué hace

Ingresa los datos a traves de una interfaz web, esta informacion se envia al backend por medio de FastAPI, que pasa por un modelo de machine learning entrenado y guardado a traves de joblib y devuelve la probabilidad de churn, con sugerencias o recomendaciones para evitarlo.

---

## Cómo está construido

**Modelo de machine learning** — Se entreno con un modelo de regresion logistica que obtuvo un Recall del 85% que indica que es optimo para detectar salida de clientes sin equivocarse mucho.

**FastAPI** — A traves de una API `/predecir` conecta el backend con la interfaz web.

**Web (frontend-backend)** — Esta interfaz ha sido creada con sugerencias y apoyo de inteligencia artificial generativa. Expone los valores mas importantes que se consideran ante la salida de un cliente.

**Infraestructura** — Se utilizo Docker para contener toda la interfaz en una imagen para que sea compatible con diferentes versiones de cada computadora.

---

## Estructura del proyecto

```
churnshield/
├── main.py                    # App FastAPI + lógica de inferencia
├── churn_predictor_app.html   # Interfaz de usuario
├── Dockerfile                 # Definición del contenedor
├── requirements.txt
├── modelos_serializados/
│   └── churn_model_BEST.pkl   # Pipeline scikit-learn serializado
└── CUSTOMER__LOGISTIC_REGRESION_GITHUB.ipynb  # Notebook de entrenamiento
```

---

## Demo en vivo

La demo esta publicada en 👉 **[churnshield-api-p1gs.onrender.com](https://churnshield-api-p1gs.onrender.com/)**

Para ello se guardo la imagen de Docker que ha sido subida a la web a traves de Docker Hub y se implanto en la pagina Render.

---

## Frameworks y librerías

`Python` · `scikit-learn` · `FastAPI` · `Pydantic` · `pandas` · `joblib` · `Docker` · `Render`


