# crops-plus
This is a scikit-learn based project which predicts the type of soil based on 10 random samples submitted through a form. The algorithm communicates to the user interface via an API built with FastAPI.

## Getting Started
  1. Create a virtual environment and set a default python version ^3.x:
  ```shell
    mkvirtualenv env
  ```
  Refer [this](https://virtualenvwrapper.readthedocs.io/en/latest/) if not familiar with python virtual environments
  
  2. Activate the virtual environment:
  ```shell
    source env/bin/activate
  ```
  
  3. Install all the dependencies:
  ```shell
    pip3 install -r requirements.txt
  ```
  3. Clone this project
  
  ## About the project
  The algorithm utilizes **scikit-learn**, **numpy** and **pandas** to generate results. The results are taken to an API using **FastAPI** and **pydantic**. To deploy the API on **Azure**, the backend has been containerized with **Docker** and shipped with **Gunicorn** and **Uvicorn**.
