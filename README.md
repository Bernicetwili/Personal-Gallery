# Gallery
## Author  
  
>[Bernice Twili](https://github.com/Bernicetwili)  
  
# Description  
This is a Django application for personal gallery that allows a user to upload images for other to see and be able to to share by coping the image link.
  
##  Live Link  
 Click [View Site](https://twiligallery.herokuapp.com/)  to visit the site
  
## Screenshots 
###### Home page
 
[![Screenshot-from-2021-05-17-04-59-12.png](https://i.postimg.cc/nhvQyMTP/Screenshot-from-2021-05-17-04-59-12.png)](https://postimg.cc/Wd13rNBG)
 
## User Story  
  
* View different photos that interest them  
* Click a single image to view it and the description
* Search for different categories   
* Copy a link to the photo to share with my friends.  

  
## BDD  
  
  
  
## Setup and Installation  
To get the code..  
  
##### Cloning the repository:  
 ```bash 
https://github.com/Bernicetwili/Gallery.git  
```
##### Navigate into the folder and install requirements  
 ```bash 
cd Gallery pip install -r requirements.txt 
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
python manage.py makemigrations pictures 
 ``` 
 Now Migrate  
 ```bash 
 python manage.py migrate 
```
##### Run the application  
 ```bash 
 python manage.py runserver 
``` 
##### Running the application  
 ```bash 
 python manage.py server 
```
##### Testing the application  
 ```bash 
 python manage.py test 
```
Open the application on your browser `127.0.0.1:8000`.  
  
  
## Technology used  
  
* [Python3.6](https://www.python.org/)  
* [Django 1.11](https://docs.djangoproject.com/en/2.2/)  
* [Heroku](https://heroku.com)  
  
  
## Known Bugs  
* There are no known bugs currently but pull requests are allowed incase you spot a bug  
  
## Contact Information   
If you have any question or contributions, please email me at [bernicetwili0@gmail.com]  
  
## License & Copyright
© Bernice Twili

Licensed under [MIT License](LICENSE)