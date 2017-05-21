FROM heroku/miniconda

ADD ./my_demo/conda-requirements.txt /tmp/conda-requirements.txt

RUN conda create -n py3k anaconda python=3
RUN ["/bin/bash", "-c", "source activate py3k && conda install --yes --file /tmp/conda-requirements.txt"]

ADD ./my_demo /opt/my_demo
WORKDIR /opt/my_demo

RUN useradd -m user
USER user

CMD ["/bin/bash", "-c", "source activate py3k && python Controller.py"]
