import mlflow
import pandas as pd
import os
from dotenv import load_dotenv
# import uvicorn
from fastapi import FastAPI, File, UploadFile, HTTPException, Response
import requests
import pdfplumber
import io
load_dotenv()

app = FastAPI()

class Model:
    def __init__(self, model_name, model_stage):
        """

        Args:
            model_name:
            model_stage:
        """
        self.model = mlflow.pyfunc.load_model(f"models:/{model_name}/{model_stage}")


    def predict(self, data):
        """

        Args:
            data:

        Returns:

        """
        return self.model.predict(data)


class PDFProcessor:

    def get_pdf_from_url(self, url: str):
        return requests.get(url)


    def get_text_from_pdf_file(self, pdf_response: Response):
        try:
            with pdfplumber.open(io.BytesIO(pdf_response.content)) as pdf:
                text = ""
                for page in pdf.pages:
                    text += page.extract_text()
            return text
        except:
            assert ConnectionError


@app.post("/summarise_pdf")
async def get_test_method(pdf_url: str):
    pdf = PDFProcessor()
    response = pdf.get_pdf_from_url(pdf_url)
    if response.status_code == 200:
        return pdf.get_text_from_pdf_file(pdf_response=response)
    else:
        return Response(status_code=response.status_code)
