FROM ubuntu:bionic

RUN apt-get update && apt-get install -y git python3

WORKDIR scriptPython

COPY hello.py .

CMD ["bash"]
CMD ["python3", "hello.py"]
