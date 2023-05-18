FROM public.ecr.aws/lambda/python:3.9

COPY requirements.txt .
COPY install-browsers.sh .

# install dependencies
RUN yum install xz atk cups-libs gtk3 libXcomposite alsa-lib tar \
    libXcursor libXdamage libXext libXi libXrandr libXScrnSaver \
    libXtst pango at-spi2-atk libXt xorg-x11-server-Xvfb \
    xorg-x11-xauth dbus-glib dbus-glib-devel unzip bzip2 -y -q

# install Chrome
RUN /usr/bin/bash ./install-browsers.sh

# install Python dependencies
RUN pip install --upgrade pip -q
RUN pip install -r ./requirements.txt -q

# remove unneeded packages
RUN yum remove xz tar unzip bzip2 -y

# copy handler and app code
COPY ./ .

ENV CHROME_VERSION=88.0.4324.150
ENV DRIVER_VERSION=88.0.4324.96

# Command can be overwritten by providing a different command in the template directly.
CMD ["handler.lambda_handler"]
