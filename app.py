image: python:3.8

stages:
  - deploy

deploy:
  stage: deploy
  script:
    - pip install -r requirements.txt
    - streamlit run app.py 
