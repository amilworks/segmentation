FROM ubuntu
ENV DEBIAN_FRONTEND noninteractive
RUN apt-get -y update                                            && \
    apt-get -y upgrade                                           && \
    apt-get -y install                                              \
      python
RUN apt-get -y install python-lxml python-numpy
RUN apt-get -y install python-pip
RUN apt-get -y install python-scipy python-configparser python-h5py
RUN apt-get -y install libgtk2.0-dev
RUN pip install opencv-python
RUN pip install nibabel
RUN pip install tables
RUN pip install --user --install-option="--prefix=" -U scikit-learn
RUN pip install -i https://biodev.ece.ucsb.edu/py/bisque/dev/+simple bisque-api==0.5.9
RUN pip install requests==2.10.0
WORKDIR /module
COPY PythonScriptWrapper /module/
COPY PythonScriptWrapper.py /module/
COPY Segmentation.py /module/
COPY pydist /module/pydist/
ENV PATH /module:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
#CMD [ 'python' '/Segmentation.py' ]
CMD [ 'PythonScriptWrapper' ]
