# Based on the latest datascience-notebook as of 4/30/21
ARG STARTER_IMAGE=jupyter/datascience-notebook:lab-3.4.4
FROM $STARTER_IMAGE

# Add in your own requirements below.
# For best maintainability use a specific version.
COPY requirements.txt .
RUN pip install -r requirements.txt
