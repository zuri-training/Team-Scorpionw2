
# Project Structure

This is general overview of our project structure.

•	Created a folder in our text editor

•	Created a virtual environment in our terminal

•	Activated Django

•	Created a project “my_cms”

•	Created an application “account”

•	Created a new file “urls.py” in the app folder “account”. 

•	Django comes with its own base files so we did only a liitle modifications. Inside the “urls.py” base file, we added our app link inside the url pattern there.

•	Added the app to the settings.py in the project folder

•	Created a new folder “templates” inside the “account’ app folder. This is where all the html files will be in.

•	 Created another folder “static” inside the “account” app folder. This is where all the styling base files will be in i.e. style.css, scripts.js, images added etc.

So in summary, frontend was added to the backend through the “templates” and “static” folders. Frontend was linked to backend through some modifications in the urls.py and views.py base files.



##  Below is a sample of how our project is structured.

my_cms

├── account/

└── migrations

└── static/

	├── css
	├── fonts
	├── images
	├── js
└── templates/

    └── cms/
        ├── index.html
        ├── login.html
        └── dashboard.html
│   ├── __init__.py

│   ├── admin.py

│   ├── apps.py

│   ├── models.py

│   ├── tests.py

│   ├── urls.py

│   └── views.py

├── my_cms/

│   ├── __init__.py

│   ├── asgi.py

│   ├── settings.py

│   ├── urls.py

│   └── wsgi.py

├── manage.py

├── requirements.txt
