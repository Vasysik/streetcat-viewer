FROM python:3.10
ADD streetcat_viewer.py .
ADD restream_youtube.py .
ADD conf.py .
ADD auth_youtube.py .
ADD client.json .
RUN pip install pytchat==0.5.5 google-api-python-client==1.7.2 
CMD [“python”, “./restream_youtube.py”]