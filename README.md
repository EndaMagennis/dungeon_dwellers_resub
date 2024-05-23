# Dungeon Dwellers 


  ![landing page](documentation/images/homepage_background.jpg)

  - [Deployed Site](https://dungeon-dwellers-resub-bcad99aabba4.herokuapp.com/)


## Card details for test payment
4242424242424242 24/42 42424

## About 
   
  Dungeon Dwellers is an e-commerce site aimed at board game enthusiasts. The name is evocative of the adventuring and exploration which is common for character dirven board games such as Dungeons & Dragons.

---

## UX


### User Stories

The ids in the tables below, link to a corresponding issue on a project board.

[User Stories Project Board](https://github.com/users/EndaMagennis/projects/5/views/1)

[Products Project Board](https://github.com/users/EndaMagennis/projects/10/views/1)

[Profile Project Board](https://github.com/users/EndaMagennis/projects/8/views/1)

[Wishlist Project Board](https://github.com/users/EndaMagennis/projects/9)


#### Site User

|id|user|feature|reason|finished?|
|-|-|-|-|-|
|[1](https://github.com/users/EndaMagennis/projects/5/views/1?pane=issue&itemId=56446212)|Site user|Intuative Design|Understand the layout and design of the website|Y|
|[2](https://github.com/users/EndaMagennis/projects/5/views/1?pane=issue&itemId=57253107)|Site user| Account Registration | Use additional features|Y|
|[3](https://github.com/users/EndaMagennis/projects/5/views/1?pane=issue&itemId=57253621)|Site User|Navigation|Use navigable links to peruse the site|Y|
|[4](https://github.com/users/EndaMagennis/projects/5/views/1?pane=issue&itemId=58526031)|Site User|Search bar| Can filter results on more relevant seraches|Y|
|[5](https://github.com/users/EndaMagennis/projects/5?pane=issue&itemId=57872462)|Site User|Save default user data|To avoid neeeding to fill order forms each time|Y|
|[6](https://github.com/users/EndaMagennis/projects/5?pane=issue&itemId=58519637)|Site User|Add items to a wishlist|To return to later without needing to buy immediately| Y|
|[7](https://github.com/users/EndaMagennis/projects/5/views/1?pane=issue&itemId=57256491)|Site User|Filtering by attributes|To order the items based on price and other attributes|N|
|[8](https://github.com/users/EndaMagennis/projects/5/views/1?pane=issue&itemId=57879979)|Site User|Updating Shopping Cart|Keep a running total of items while still allowing to browse the site|Y|
|[9](https://github.com/users/EndaMagennis/projects/5/views/1?pane=issue&itemId=58525298)|Site User|Messages notify of certain actions|To know that actions have taken place|Y|
|[10](https://github.com/users/EndaMagennis/projects/5/views/1?pane=issue&itemId=57873555)|Site user|Update profile data|So that I can update username and address|Y|
|[11](https://github.com/users/EndaMagennis/projects/5/views/1?pane=issue&itemId=58526346)|Site User|See order history on profile|to keep track of my purchases|N|
|[12](https://github.com/users/EndaMagennis/projects/5/views/1?pane=issue&itemId=59386779)|Site User|Make Secure Payments|So that I can purchase items directly from the site|Functional but always returns error w/handling|

## Major Stumbling Blocks

Twice during this project, I ran into issues with the database where the only solution was to flush the data and start again. The current repo is actually the second attempt at this project, which is why there are more issues on the project boards than represented in the github repo. 

## Business model

The business model is B2C, meaning the business sells to the customer. The focus is on one-off payements for products.

### A summary of the customer

Dungeon Dwellers is a site aimed at customers in a specific niche of boardgames and minatures. With a limited pool of a customer base, loyalty is a neccesity. As such, the sales process should be painless, providing top quality UX and UI.


### Strategy

Due to being a niche store, the customer base would expect the store to compete on the following:

- quality of products (licesned products)
- availability
- user experience
- service
- loayalty offers
- price


---

## Web Marketing

### facebook Business page

Facebook, with over 3billion users is an obvious choice for web marketing.
Additionally, Facebook offer many options for boosting engagement and SEO, both free and paid.

[Facebook Page](https://www.facebook.com/profile.php?id=61558423709057)

![Facebook business page](documentation/images/marketing-facebook.png)


## Technologies Used

- ### Languages:

  - [Python 3.12.0](https://www.python.org/downloads/release/python-3120/): used as the primary language used in backend functionality
  - [JavaScript](https://www.javascript.com/): used for interactive components
  - [HTML](https://www.w3schools.com/html/): used to create the skeleton of web pages
  - [CSS](https://www.w3schools.com/css/): used for styling the web pages

- ### Fameworks and Libraries:

  - [Django 4.2.8](https://docs.djangoproject.com/en/5.0/releases/4.2.8/): Python framework for full-stack development
  - [jQuery](https://jquery.com/): using AJAX requests to bridge frontend and backend
  - [Bootstrap](https://getbootstrap.com/): used to create consistent CSS styling

- ### Database:
  
  - [SQLite](https://www.sqlite.org/): was used as a development database.

  - [CI Database Maker](https://dbs.ci-dbs.net/): a cloud based postgreSQL database

- ### Other Tools and Dependencies
  - [Git](https://git-scm.com/): version control for continuous development
  - [Pip](https://pypi.org/project/pip/): python package manager for installing dependencies
  - [AllAuth](https://docs.allauth.org/en/latest/): python package for handling account authentication
  - [Gunicorn](https://gunicorn.org/): Unix model which creates Python wsgi Http server
  - [Django-allauth](https://docs.allauth.org/en/latest/release-notes/recent.html#id11): account creation library for django
  - [GitHub](https://github.com/): cloud repository for source code
  - [GitPod](https://www.gitpod.io/): Cloud IDE service used for the majority of development
  - [Heroku](https://id.heroku.com/login): Used to deploy the webisite
  - [VSCode](https://code.visualstudio.com/): Local IDE used as backup
  - [Chrome DevTools](https://developer.chrome.com/docs/devtools/open/): used to debug 
  - [Font Awesome](https://fontawesome.com/): used to supply icons
  - [Image Extractor](https://extract.pics/): used to scrape images from websites used within the project
  - [W3C Validator](https://validator.w3.org/): HTML validator
  - [W3C CSS validator](https://jigsaw.w3.org/css-validator/): CSS validator
  - [Code Institute Pep8 linter](pep8ci.herokuapp.com): python validation


 ## Features

Please refer to the [FEATURES.md](FEATURES.md) file for all feature-related documentation.

## Testing

Please refer to the [TESTING.md](TESTING.md) file for testing

---
## Design

- ### Wireframes

- Home view
    
    ![home view](documentation/wireframes/home_view.png)

- Profile view

    ![profile view](documentation/wireframes/products_view.png)

- Products view

    ![products view](documentation/wireframes/products_view.png)

- Product detail view

    ![product detail view](documentation/wireframes/product_detail_view.png)

- Bag view

    ![bag view](documentation/wireframes/bag_view.png)


## Information Architecture

### Database

- The database was created and hosted on [ElephantSQL](https://www.elephantsql.com/)

### Entity Relationship Diagram

- The ERD was created using [Lucidchart](https://lucid.co/)

![entitity relationship diagram](documentation/wireframes/erd.png)


## Testing

Please refer to [TESTING.md](TESTING.md)

## Deployment

- The site was deployed using [Heroku](https://id.heroku.com/login)
- The database was deployed to [ElephantSQL](https://www.elephantsql.com/)
- The app is available [here](https://board-ohm-5d4ddb906f72.herokuapp.com/)

## Credits

- [boardgamegeek](https://boardgamegeek.com/blogpost/156777/2023-year-in-review-day-four-all-the-board-games-a): is one location I used to pull images from for my models
- [boardgamequest](https://www.boardgamequest.com/top-10-board-games-of-2023/): the other site I pulled images from for my models
- [Edgar Sánchez Hidalgo](https://www.artstation.com/artwork/nELnqO): whose work was used for the background image
- [CodeInstiute](https://codeinstitute.net/ie/): for giving me the basics of django development used in the site
- [Code Institute - Boutique Ado](https://github.com/Code-Institute-Solutions/boutique_ado_v1/tree/933797d5e14d6c3f072df31adf0ca6f938d02218): which acted as a template for styling and functionality
- [Bootstrap](https://getbootstrap.com/): for giving me the classes for basic and clean styling used in the site
- [Django](https://www.djangoproject.com/): for basic templates and fuctionality used in the site 
- [Font Awesome](https://fontawesome.com/): for icons used in the site
- [Geeks For Geeks](https://www.geeksforgeeks.org/handling-ajax-request-in-django/): used to better understand ajax funtionality
- [Desphixs](https://www.youtube.com/@desphixs): foundation for adding products to a wishlist
- [GoFullPage](chrome://extensions/): can be found on Google Chrome extensions. Captures a full page view of any webpage, the images of which were used throughout documentation
- [Stack Overflow](https://stackoverflow.com/questions/28054991/combining-two-forms-in-one-django-view): to assist with combining several forms into one view
- [Code Institute Pep8 linter](pep8ci.herokuapp.com): allowing me to pep8 validate my python.

## Acknowledgements

- [Iuliia Konovalova](https://github.com/IuliiaKonovalova): my mentor who continually motivates me to go big.
- [CodeInstiute](https://codeinstitute.net/ie/): for giving me the tools and knoweldge
