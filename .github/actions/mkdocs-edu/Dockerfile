FROM python:bullseye

# Install additional software
RUN apt-get update && \
    export DEBIAN_FRONTEND=noninteractive && \
    apt-get -y install --no-install-recommends \
  ghostscript \
  imagemagick \
  zip

# Make sure that ImageMagick can convert PDF to images
RUN sed -i '/disable ghostscript format types/,+6d' /etc/ImageMagick-6/policy.xml

# Install Poetry
RUN pip install poetry

# Install entrypoint
COPY entrypoint.sh /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]
