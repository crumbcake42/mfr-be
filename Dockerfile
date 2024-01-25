FROM unit:1.31.1-python3.11

# Install Python dependencies
COPY requirements.txt /config/requirements.txt
RUN python3 -m pip install -r /config/requirements.txt
