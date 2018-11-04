rm db.sqlite3	
python3 manage.py makemigrations	
python3 manage.py migrate

#change this to init.py when finalized 
python3 manage.py shell < init2.py	
