# HoodWatch

>[Nzau~Mercy](https://github.com/NzauM)  
  
# Description  
Hood watch is an app that allows you to be in the loop with everything happening in your neighbourhood.A user must sign up first and then they can 
see all the posts and businesses in the neighbourhood.They can also post their business or post announcements.
##  Live Link  
 Click [Nzauhood](https://nzauhood.herokuapp.com)  to visit the site
  
## Screenshots 
###### Home page
 
<img src="https://ucarecdn.com/1761b8cf-3918-4b9b-b415-cbced8e25f0e/home.png">

 
## User Story  
  
* Sign in with the application to start using.
* Set up a profile about me and a general location and my neighborhood name.
* Find a list of different businesses in my neighborhood.
* Find Contact Information for the health department and Police authorities near my neighborhood.
* Create Posts that will be visible to everyone in my neighborhood.
* Change My neighborhood when I decide to move out.
* Only view details of a single neighborhood.
  
## Setup and Installation  
To get the project .......  
  
##### Cloning the repository:  
 ```bash 
https://github.com/NzauM/Hoodwatch.git
```
##### Navigate into the folder and install requirements  
 ```bash 
cd HoodWatch 
```
##### Install and activate Virtual  
 ```bash 
- python3 -m venv virtual - source virtual/bin/activate  
```  
##### Install Dependencies  
 ```bash 
 pip install -r requirements.txt 
```  
 ##### Setup Database  
  SetUp your database User,Password, Host then make migrate  
 ```bash 
python manage.py makemigrations hood
 ``` 
 Now Migrate  
 ```bash 
 python manage.py migrate 
```
##### Run the application  
 ```bash 
 python manage.py runserver 
``` 
##### Testing the application  
 ```bash 
 python manage.py test 
```
Open the application on your browser `127.0.0.1:8000`.  
  
 
## Technology used  
  
* [Python3.6](https://www.python.org/)  
* [Django 2.2.6](https://docs.djangoproject.com/en/2.2/)  
* [Heroku](https://heroku.com)  
  
  
## Known Bugs  
* There are no known bugs currently but pull requests are allowed incase you spot a bug  
  
## Contact Information   
If you have any question or contributions, please email me at [mikeycharlesm7@gmail.com]  
  
## License 


[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://github.com/NzauM/Instagram/blob/master/LICENSE)
MIT License
\_ **Nzau Mercy @2020**
