FROM python:3.8-buster
EXPOSE 8501
WORKDIR /usr/src/app
COPY requeriments.txt .
RUN pip install  --no-cache-dir -r requeriments.txt
COPY . .
CMD streamlit run hello.py