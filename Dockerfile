FROM python:2.7
ADD restful1.py /
RUN pip install flask flask_restful
CMD [ "python", "./restful1.py" ]
