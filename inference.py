""" This file is for inference of a NLP model """

import argparse
from transformers import BigBirdPegasusForConditionalGeneration, AutoTokenizer



def extract_text(input_url_pdf: str, output_path_pdf: str):
    """"Function to extract text from chosen pdf"""

    # URL = "https://arxiv.org/pdf/1908.08593.pdf"
    response = requests.get(input_url_pdf)
    with open(output_path_pdf, "wb") as file:
        file.write(response.content)

    with open(output_path_pdf, "rb") as file:
        reader = PyPDF2.PdfReader(file)
        page = reader.pages[0]
        text = page.extract_text()

    return text


def model_inference(input_url_tokenizer: str, input_url_model: str, text: str):
    """function to run model inference on extracted text"""
    # google/bigbird-pegasus-large-pubmed
    tokenizer = AutoTokenizer.from_pretrained(input_url_tokenizer)
    inputs = tokenizer(text, return_tensors="pt")

    # by default encoder-attention is `block_sparse` with num_random_blocks=3,
    # block_size=64
    model = BigBirdPegasusForConditionalGeneration.from_pretrained(input_url_model)
    prediction = model.generate(**inputs)
    prediction = tokenizer.batch_decode(prediction)
    return prediction


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='PDF Text Extraction and Model Inference')
    input_url_model="google/bigbird-pegasus-large-pubmed"
    input_url_tokenizer="google/bigbird-pegasus-large-pubmed"
    extr_text = "Example text"
    result = model_inference(input_url_tokenizer, input_url_model, extr_text)
    print(result)