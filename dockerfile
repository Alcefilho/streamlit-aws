FROM 415696084416.dkr.ecr.us-east-1.amazonaws.com/python-3.8-buster
EXPOSE 8501
WORKDIR /usr/src/app
COPY requeriments.txt .
RUN pip install  --no-cache-dir -r requeriments.txt
COPY . .
CMD streamlit run hello.py