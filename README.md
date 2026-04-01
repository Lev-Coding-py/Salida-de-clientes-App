# Salida de clientes App 🛡️

> Una aplicacion de Machine Learning que predice si un cliente esta a punto de irse.

[![Demo en vivo](https://img.shields.io/badge/demo-en%20Render-5affb0?style=flat-square)](https://churnshield-api-p1gs.onrender.com/)

---
![ChurnShield App](https://github.com/user-attachments/assets/e5c4619d-44cc-47c3-b340-a7a15765c422)

---

Todas las empresas pierden clientes, pero estas salidas pueden anticiparse. El dataset viene de una empresa Telco.

---

## Qué hace

Ingresa los datos a traves de una interfaz web, esta informacion se envia al backend por medio de FastAPI, que pasa por un modelo de machine learning entrenado y guardado a traves de joblib y devuelve la probabilidad de churn, con sugerencias o recomendaciones para evitarlo.

---

## Cómo está construido

**Modelo de machine learning** — Se entreno con un modelo de regresion logistica que obtuvo un Recall del 85% que indica que es optimo para detectar salida de clientes sin equivocarse mucho. Ademas para conectar la interfaz web con el modelo ML se probo diferentes combinaciones utilizando MLflow hasta encontrar el mejor resultado y se guardo el mejor resultado con joblib.

**FastAPI** — A traves de una API `/predecir` conectar los resultados entrenados con el modelo ML  con la interfaz web.
**Web (frontend)** — Esta interfaz ha sido creada con sugerencias y apoyo de inteligencia artificial generativa. Expone los valores mas importantes que se consideran ante la salida de un cliente.

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

## Posibles mejoras
Posibles Mejoras 

-Versionado de Modelos ML: Implementar una carpeta de versionado v1, v2, v3 para saber que versión se está utilizando o implementar nuevas versiones, ya que en casos reales los datos cambian y se debe reentrenar los datos. 

-Una interfaz que me permita ver la cantidad de clientes en peligro y dashboards inteligentes. 

-GitHub (CI/CD) para que cada vez que suba un código se ejecuten test automáticos. 

-Utilizar un mejor modelo predictivo y utilizar método SHAP para ver influencia de variables. 

-Generalizar el proyecto y utilizar la nube. 

-Utilizar Streamlit que te permite transformar tus scripts de Python en dashboards interactivos en minutos. Sin embargo no permite total flexibilidad, ni escalabilidad. 

- Conectar tu API de FastAPI con n8n para que el modelo detecte un riesgo de fuga se disparé un flujo automático, es decir, enviar un correo para alertar al equipo de ventas. 

---

## Frameworks y librerías

`Python` · `scikit-learn` · `FastAPI` · `Pydantic` · `pandas` · `joblib` · `Docker` · `Render`


