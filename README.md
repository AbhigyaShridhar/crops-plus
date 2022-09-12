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
  
  4. To run and test the project locally, run:
  ```shell
    uvicorn main:app
  ```
  than go to `127.0.0.0:8000/docs` to view the **swagger UI** for the API
  The **Gunicorn** command to deploy the API on cloud has been given in the dockerfile.
  However, you can check if it's working properly by running `gunicorn -w 4 -k uvicorn.workers.UvicornWorker main:app`
  
  ## About the project
  The algorithm utilizes **scikit-learn**, **numpy** and **pandas** to generate results. The results are taken to an API using **FastAPI** and **pydantic**. To deploy the API on **Azure**, the backend has been containerized with **Docker** and shipped with **Gunicorn** and **Uvicorn**.
  
  
  See `wix.js`, the frontend was created using **Wix** and it was integrated with the algorithm using **Velo**. This file contains the fetch code which delivers the algorithm result to the UI.
