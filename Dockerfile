# Copyright 2024 Michael Sparks
# 
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at:
# 
#     http://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


# Use an official Python runtime as a base image
FROM python:3.10-slim

# Set environment variables

# Prevent python from trying to write .pyc files to a read only container when deployed
ENV PYTHONDONTWRITEBYTECODE=1

# Forces stdout to be unbuffered and flush the terminal when printing, meaning data
# is output immediately, which can be useful with docker logs
ENV PYTHONUNBUFFERED=1

# Set the working directory in the container
WORKDIR /app

# Copy and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the source code into the container
COPY src/ontology_service.py ontology_service.py

# Define the command to run the script
ENTRYPOINT ["python", "ontology_service.py"]
