FROM python:3.9-slim

# Set working directory
WORKDIR /home/data

# Create output directory
RUN mkdir -p /home/data/output

# Copy the script and text files into the container
COPY scripts.py /home/data/scripts.py
COPY text_files/IF.txt /home/data/IF.txt
COPY text_files/AlwaysRememberUsThisWay.txt /home/data/AlwaysRememberUsThisWay.txt

# Run the script when the container starts
CMD ["python", "/home/data/scripts.py"]