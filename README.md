## HackWar 3.0 Project

**Team Name :** Sentinal_Bots

**Organised By :** [Codex Iter](http://github.com/codex-iter)

### Problem Statement Title
Over 23 million artisans work in the Indian handicraft and handloom industry. A cross-border e-commerce marketplace will bring customers and sellers together on a single business platform. It will aid in the expansion of their firm as well as the overall economy of our country.
To provide a unique e-commerce platform for craftsmen to market their wares. Demand forecasting for required products, automatic quality checks on the objects, and sentiment analysis with next recommended actions for the artist will be implemented.
To globalise the Indian handicraft industry? Providing a shared platform for the creation, marketing, and sale of high-quality handicrafts and items.

**Theme Name :** E-Commerce Website

### Tech Stacks 
- HTML/CSS
- JS
- BootStrap
- Django REST Framework (Backend)
- SQLite (Default Django Database used)

### Hosting the Site
- Download the Repo
- Go to `Crafts_MarketPlace` (It is root folder) & run 
   ```
   python manage.py makemigrations
   python manage.py migrate
   python manage.py runserver
   ```
**Note** : First two lines are needed only if you make changes to models of the Database otherwise not required.
- Now if everything goes well , Visit : http://127.0.0.1:8000/

### Important Folders
- **Backend** Folder : This folder holds the admin panel & server-side settings. Here in `models.py` , models of database are created. 
 
 **Note** : Here we need to use `makemigrations` and `migrate` to update our database with updated models.
 - **frontend** Folder : This folder handles all the client side settings , templates , static files and Routes to different paths and pages.
 - **Crafts_MarketPlace** Folder : This folder carries all the root level settings which comes by default and can be modified accordingly.

### Team Members
- [Himanshu Mishra](https://github.com/himanshu251001) - Frontend & Idea Approach
- [Vaishnavi Khushi](https://github.com/vaishnavikhushi14) - Frontend & Design
- [Amrit Anand](https://github.com/Amrit232) - Frontend & Datasets
- [Kumar Spandan Pattanayak](https://github.com/5p7Ro0t) - Backend & Database
 
**Thank You Codex Iter for organising this wonderful Hackathon :blush:**
