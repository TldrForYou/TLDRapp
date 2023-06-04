import mlflow
import pandas as pd
import os
from dotenv import load_dotenv
# import uvicorn
from fastapi import FastAPI, File, UploadFile, HTTPException, Response
import requests
import pdfplumber
import io
from inference import *
load_dotenv()

app = FastAPI()

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
        extr_text = pdf.get_text_from_pdf_file(pdf_response=response)
        input_url_model = "google/bigbird-pegasus-large-pubmed"
        input_url_tokenizer = "google/bigbird-pegasus-large-pubmed"
        return model_inference(input_url_tokenizer, input_url_model, extr_text)
    else:
        return Response(status_code=response.status_code)
