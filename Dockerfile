FROM python
WORKDIR /app
COPY . /app
RUN pip install nltk
CMD python cleanWords.py