Initial setup:
1.Crete virtual environment
python -m venv venv
2.Activate venv 
venv\Scripts\Activate.ps1 
3.Install dependencies 
pip install -r requirements.txt

4.create database named "productdb" in mysql
create database productdb;#run this line in mysql workbench
5.set database_url variable in core/config.py
"mysql+pymysql://username:password@host:port/<dbname>"

Command to run application:
uvicorn app.main:app --reload

Swagger UI:
http://127.0.0.1:8000/docs

openapi.json:
http://127.0.0.1:8000/openapi.json