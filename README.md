README
# Nutrition-Sleep-Time

## 1. Table of Contents:

### 2. Distinctiveness and Complexity:
This project is the final requirement for the CS50's Web Programming with Python and JavaScript course offered by HarvardX on edX.org and is one of the two required courses for Computer Science for Python Programming program as well.

This web application project utilizes Django with four models, (first one is the built in User(AbstractUser) with the pass option). The second model, called Nutrition, is being utilized for monitoring and creating a database of daily primary nutrients including 'Protein', 'Fat', 'Saturated Fatty Acids', 'Carbohydrates', 'Sugars', 'Sodium', and 'Dietary Fiber'. Each category is a component needed for creating the chart on both nutritions.html file (for total intake nutrients and a gauge chart on sleepdaily.html) with the accurate data for each single day nutrients intake monitoring.

As a front end, within the included JavaScript file, are functions called drawStuff(), drawChart(), edit_button(), and analogClock(). Other than the last one, they all will be storing the data in the sql tables created within db.sqlite3 file. The analogClock() function shows the local time on all pages as a header(please see credits below). There is another time related function, digitalClock(), including digitalMin() and digitalHour() as built in functions, which has the ability to set an alarm on a separate page. Through the nutrition() function in the included views.py file as one of the required backends is the possibility of creating a diet journal, recording the intake vs maximum daily limit for each one, daily sugar consumption versus the maximum allowed amount of 38, for example.  another model, called Sleep, will be keeping track of the sleep irregularities with the emphasis on calculating the -go to bed time- in order to get the required sleep hours on a daily basis. The Note model has been adopted by network project functionality with the difference of being only accessible to the current authenticated user as a form of a daily dairy and memo monitoring virtual notebook which is considered both back end and front end. The design is mobile responsive with choosing the correct needed tags both in the included styles.css file as well as the main template for all the html files called layout.html. 

The ability to monitor basic food elements well as a sleep pattern regulator with detailed information and a visual chart makes this project a health tracker tool. It is also a good source to store and maintain a daily journal with the ability to add or edit entries, including past memos.  

### 3. Contained materials in source files (.py, .html, .css, .js, sqlite3, this README):
Being a requirement for any Django based web application, there are several python files as the basic constructors which are being stored in separate folders. Main folder, called final, includes asgi.py, wsgi.py, setting.py, urls.py, and . Their purpose in order are: asgi and wsgi supply an application callable which the application server uses to communicate with the code. WSGI stands for "Web Server Gateway Interface". It is used to forward requests from a web server (such as Apache or NGINX) to a backend Python web application or framework. From there, responses are then passed back to the webserver to reply to the requestor. setting.py contains all the configuration needed in Django installation, a Python module with module-level variables. urls.py is a clean URL scheme which is an important detail in a high-quality web application. Django allows custom designed URLs with no framework limitations. source: please see Acknowledgements below.
Next folder, called finalproject, contains a copy of all the migrations, a folder called static, including the css file, styles.css, for web page designs, a JavaScript file, index.js, with application related functions described above inside several files including view.py for main functions, forms.py to store all django forms, models.py with models explained above with the ability to save the data in related table. An audio folder needed for the alarm function to set the time for sleep hours, also mentioned above is included in the static folder beside an image storing folder, holding the index page background, a painting by myself!, as an appreciation and a reminder of the long journey it took to be able to write an readme file at this moment for a project I made after starting to learn computer programing and design which once seemed to an unrealistic illusion. I'm glad I started this journey. Templates of all html files are inside the template\finalproject folder. admin.py gives virtual access while still designing the website for manual alternations. apps.py, test.py, urls.py, and the main processor called views.py are the rest of required files created at the beginning of the project which have been built and customized for this project. The db.sqlite3 file stores the tables created by model.py with related data for testing. A single python file, called manage.py outside of the folders, is a Django's command-line utility for administrative tasks.

### 4. Video: <https://youtu.be/CtA7s39BJyQ>

### 3. Description
This web application is an easy tool to work with while monitoring nutrients and sleep patterns for a healthy lifestyle. Having personal issues with both gave me the initial idea for the final project. Getting more protein and healthy fiber while limiting the extra carbohydrate and sugar on a daily basis is essential for a healthy routine as well as sleeping at an appropriate time to make the body recharge fully. As a programming newbie I tried the best I could but there sure is many flaws that need to be worked on later on. Thank you for your interest.

### 4. Requirements
Having full knowledge of the daily nutrients and their impact on body as well as a healthy sleep pattern are required before using this application. The content has been modified for different media and screen display varieties; however the final quality is the best that could be done with open source software and information. 

### 5. Credits
**digitalClock**
in-(final\finalproject\static\finalproject\index.js)-
based on the [JavaScript Alarm Clock with Sound](https://www.codehim.com/date-time/javascript-alarm-clock-with-sound/) by Asif Mughal.
**analogClock**
in-(final\finalproject\static\finalproject\index.js)-
based on the [Simple Analog Clock Using Html, CSS & Javascript](https://dev.to/code_mystery/simple-analog-clock-using-html-css-javascript-2c6a
) by Foolish Developer.
**bed_time**
in-(final\finalproject\static\finalproject\views.py)-
based on the [When to Sleep?](https://edabit.com/challenge/e5XZ82bAk2rBo9EfS) by 
zatoichi49.

### 6. Acknowledgements
**toggle design**
in-(final\finalproject\static\finalproject\temlates\layout.html)-
adopted by [Menus part#1](https://github.com/frontend-joe) by 
Joe Harrison.
**drawStuff**
in-(final\finalproject\static\finalproject\index.js)-
based on the [Google Charts](https://developers.google.com/chart) by Google.
**README.md**
in current file-(final\finalproject\static\finalproject\README.md)-
based on the [README: Add Credits and Acknowledgements #21](https://github.com/fantaisie-software/purebasic/issues/21) by 
tajmone.
**Contained materials in source files**
in current file-(final\finalproject\static\finalproject\README.md)-
description of asgi, wsgi
based on the [How to deploy with ASGI](https://docs.djangoproject.com/en/4.1/howto/deployment/asgi/) by djangoproject.
based on the [What Is WSGI?](https://www.liquidweb.com/kb/what-is-wsgi/#:~:text=Purpose,Python%20web%20application%20or%20framework.) by liquidweb.
**special thank to**
This project and the whole consept of learning to code wouldn't be possible without the help of cs50s' design and support team. My main appreciation goes to Mbmbpossm for giving me the confidence and the hope I needed to get going.