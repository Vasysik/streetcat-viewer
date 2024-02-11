FROM python:3.10
ADD streetcat_viewer.py .
ADD restream_youtube.py .
ADD conf.py .
ADD auth_youtube.py .
ADD client.json .
ADD requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
CMD [ "python" , "./restream_youtube.py" ]