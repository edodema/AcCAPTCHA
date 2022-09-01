FROM ubuntu:latest
COPY . /home
WORKDIR /home
# Install dependencies.
RUN apt-get update && apt-get upgrade -y && apt-get install -y \
    alsa-base \
    alsa-utils \
    pulseaudio \
    ffmpeg \
    libsm6 \
    libxext6 \
    python3 \
    python3-pip \ 
    python3-pyaudio \
    portaudio19-dev \
    python-all-dev \
    python3-all-dev

RUN pip3 install -r requirements.txt

# Prepare data.
RUN mv assets/words.json gui/static/assets && \
    tar -xk -f assets/captcha.tar.xz -C gui/static/assets/ && \ 
    tar -xk -f assets/images.tar.xz -C gui/static/assets/

# # Default command.
ENV PYTHONPATH=.
EXPOSE 8080
# CMD ["python3", "gui/main.py"]

# ! docker run --rm -it --device /dev/snd:/dev/snd -p 8080:8080 becaptcha
