Django Blog Project

This is a simple Blog application built with Django.
It includes demo data so the content (title, author, description, images) shows immediately after setup.

🛠 Requirements

Python 3.x

Git

🚀 Setup & Run (Copy–Paste Friendly)
1️⃣ Clone the repository: 
git clone https://github.com/DhairyaDesai19/Django_Project.git

2️⃣ Go to project directory: 
cd Django_Project

3️⃣ Create virtual environment: 
python -m venv env

4️⃣ Activate virtual environment (Windows): 
env\Scripts\activate

5️⃣ Install dependencies: 
pip install -r requirements.txt

6️⃣ Apply migrations: 
python manage.py migrate

7️⃣ Load demo data (IMPORTANT)

This loads sample posts added via admin.: 

python manage.py loaddata data.json

8️⃣ Run the server: 
python manage.py runserver

🌐 Open in Browser: 
http://127.0.0.1:8000/

🔐 Admin Panel
http://127.0.0.1:8000/admin/


(Create a superuser if needed)

python manage.py createsuperuser
