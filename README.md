![CI logo](/static/media/hero/hero3.jpg)


https://onlinbook-m-three.herokuapp.com/

https://git.heroku.com/onlinbook-m-three.git


Welcome Conics Con online
**,June 20 2022**

### Introduction

This website was made as all the lovers of comic books you want to create a share space where people can create join or read any comic books they feel close to, come on jones.

## Table of Content

1.[UX - User Experience](#ux) 

  * [Project Goals](#project-goals)
    * [MVC framework](#MVC-framework)
    * [Authentication](#authentication)
    * [E-commerce](#e-commerce)
    * [Control-system](#control-system)


  * [User Stories](#user-stories)
    * [Database schema](#database-schema)
    * [Functionality](#functionality)
        
        .[Create](#create)
        .[Read](#read)
        .[Update](#update)
        .[Delete](#delete)


2.[Design](#design)

  * [colour](#colour)
    
  * [Typography](#typography)

  * [Images](#images)
    * [Pexels](#Pexels)
    * [Marvel](#https://www.marvel.com/comics?&options%5Boffset%5D=0&totalcount=12)
    
    

  * [Icons](#icons)
    * [Font Awesome ](#font-awesome)
    * [Bootstrap](#bootstrap)

  * [Layout](#layout)

  * [Wire frames](#wire-frames)

3.[Features](#features)

  * [Validator](#validator)
     * [HTML-VAL](#val)
     * [CSS-VAL](#val)

  * [Testing](#Testing)
  
  * [Bugs](#Bugs)

4.[Data](#data)

  * [Application](#application)
    * [CodeBase](#codebase)
    * [TDD Approach](#tdd)
    * [Template Django](#template)
    * [Schema](#schema)
    * [Version control](#version)

5.[Deployment](#Deployment)

    * Horoku

    * Github

    * Mongo DB

   * [Credit](#Credit)
   * [Acknowledgements](#Acknowledgement)





# UX - User experience

We want to give her use of the place where they can come and feel comfortable, here and `Comics online` we aim to have easily viewed purchases in shopping cart to avoid overspending

Give them a place where easily register in their account or login or recover their passwords, in case they forget it 
We aim to have a fully functional in store that receive emails and confirmations of the registration of their account,
And make sure each user has a personalise profile within them cells can become a seller on our website.

## Project Goals

Here at Conics Con online, we were outside firstly to be able to view and navigate through the website making it easy to purchase see product list have individual product details quickly identify clearance special offers meal plans in apparel,

We want our visitors to be able to register the user account for a super user or regular user would like nothing more than the best for easily logging in validate their passwords have overall good user experience,

We will give our customers the ability to store and search particular products become a super user to even become a seller on our website purchasing and check out automatically help them to have a better experience on how our site can benefit them,
By using our admin manager in a store managers sources to different back in front in five minutes we would like to keep our customers safe from any threats by using confirmation emails and making sure that each customer must have a functional email and password to use our site.



---


## Wire frames

![Mockup](/media/framework/add-Comic.png)

### Mobile app

This is an example of the email and password and login page on the mobile app easily downloaded and accessible when will available

![Mockup](/media/framework/login.png)

### Layout of website

![Mockup](/media/framework/homepage.png)

From the layout of the website shoppers will be easily views of the list of products as individual products & thire details, these are quickly identified and items specified, and offers are clearly sense of direction through a drop-down menu for ease of use.


---

## Authentication

Using '''allauth''' confirmation emails will be sent back and forth between the user and our server system to ensure everything has been passed security, usually '''django.core''' mainframe all emails will be handled in the backend of the console,

This will be done in steps to differentiate our customers between our sellers who will be able to add their own products, & Sign Users that will be able to shop our Products, either by using a username or email address, all this will insuring that email to verify your account is necessary and mandatory.

In this way no user can answer to a site without having first using a real email so they will be asked to verify the email twice to create an account and it will be sent a confirmation email to their account enter their email address to make sure it is a working and functional email address.

As an extra precaution a minimum number of letters is required to create a username no less than five letters in so that the system understands we will give a redirect login URL to get our customers back to the main page of Iam site which will automatically receive the information that is how we plan to authenticate.

### Superusers

* As a superuser you'll be able to edit add or delete items from the store and become a seller of your own products on the Conics Con online this is done with the admin on location of the shop was super users can be registered by our team, they will have full control to edit there products add new items to the shop or change the existing items such as prices, description, images, or update to existing product.


### Side uses 

* excite user can easily register for an account easy login easily recover their passwords in case of misuse and have a personalise use a page where there they can see a list of there pass purchases,


---


## E-commerce

This section of the store will be handled by '''stripe''' payment system and link to our e-commerce store here customers will be able to check out and make purchases directly from their account, 
It will be handled in the background, customers will receive confirmation emails with shipping and handling details, for each specific products and information from their past purchases will be displayed and also if they qualify for any discounts in shipping.


---

## Control-system

Using '''Heroku''' will be able to log in and check how the site is doing to the backend of the site will be able to monitor as a super admin user can use the website admin to make sure the website is running smoothly,

You'll be able to monitor the push notification  of are users are that are registered to the admin and simultaneously get all the account details that are stored.

Well we can monitor if a customer as a new product or delete a current product this all will be registered to the terminal which again will be pushed to our server at Heroku


---

# User Stories

* first visit: Have a very eye appealing look the first time users easily navigated all the information is clearly displayed and very customisable to their preferences with this we hope to have a first time user register for an account, and become a customer

~~~
    * How fast is the website loading.
    * Is the website easy to understand.
    * Does it have quick responses.
    * How's the design.
    * All the links should work.
    * Easy to navigate.
    * Not confusing.
    * Simple. 
    * Interactive.

~~~

* Returning visitor: have a personal account and be able to view my profile be able to access my personal account information, easily required  access to my account, verified my account system is working and securely stored in my past orders and change my address or payment system if I want to I need to.

~~~
    * can I see my shopping bag
    * can I increase the amount of my purchase
    * is there a different sizes available
    * can I find different trainers
    * deals or discount
    * is there a new arrivals
    * can I can I join a group lesson
~~~

These are some of the user experiences and stories we would like to fulfil for customers here `Conics Con online`


---

## Database schema

Using the '''django''' we make a front end user base any backend user based to interact with each other to handle the data, while he's sitting would be mostly use by Superusers it is also playing a role for our regular users or shoppers were super users has a fully functioning user admin panel we also won our general users to be able to create read an update their information, 

as a superusers from the front or back in will be able to use a framework called CRUD, that stands for create read update and delete all files will be duplicated from the users front end plate and sent it back into storage in the admin using the '''django''' and '''Reroku''', by using the method of get or post request, we hope to handle all our clients needs to this process.


  ### Functionality

    * Create {An SQL INSERT statement adds one or more records to any single table in a relational database.}
        ** 

    * Read {The SQL SELECT statement returns a result set of records, from one or more table}

    * Update {The SQL SELECT statement returns a result set of records, from one or more table}

    * Delete {In the database structured query language (SQL), the DELETE statement removes one or more records from a table. A subset may be defined for deletion using a condition, otherwise all records are removed.[1] Some database management systems (DBMSs), like MySQL, allow deletion of rows from multiple tables with one DELETE statement (this is sometimes called multi-table DELETE).}


---

# Design

We are going for a simple design of white and off-white makes it easier on the eyes of the customers we want to let our showcase of colours of products and meal plans with a showcase of our website and we do not want to take that away by having too much extra ordinary colours,


## colours 

chosen for the site Conics Con online have come from a website the website Colours:

* Full colours graph:

![alt](/media/framework/Screenshot%202022-03-23%20at%203.40.26%20PM.png)


## TYPOGRAPHY 

1. The main font that is going to be used is Open Sans,
   Light 300 italic, this font is going be used throughout the whole website, this font came from Google fonts.

   * Why Open Sans:
      [Google fonts](https://fonts.google.com/specimen/Open+Sans#about)
   
   * Designed by: Matteson Typographics.
      [Type Design & Consulting](https://mattesontypographics.com/)
  

2. The secondary fonts for (h2) that were used were: Arial Narrow Bold sans-serif, Font was generated straight from the CSS3 browser! 
None can be provided..

   * Why Arial Narrow Bold  sans-serif: 
      were used to add symmetry to the website!

      For Visual Example of Font:[Arial](https://www.cssfontstack.com/Arial-Narrow)


3. The territory fonts for (h3) that were used are: Georgia, 'Times New Roman', Times, serif, Font was generated straight from the CSS3 browser! None can be provided..

   * Why Georgia, 'Times New Roman', Times, serif:
      was used to add a different feel to the headers!

      For Visual Example of Font:[Georgia](https://www.cssfontstack.com/Georgia)


## Images 
will be Sourced from [Pexels]()
Which is free to use to my personal account which I also give donations and display my own work.
He has a full example taking by Ella:

![alt]()

* images shows from simply shredded.com have been purchased by me where I bought a workout plan that I currently follow
[Simply Shredded](https://simplyshredded.com/)





## ICONS 

All items provided came from across the websites such as bootstraps and font awesome.

* Social Media were sourced from [Font Awesome](https://fontawesome.com) and [Google Fonts](https://fonts.google.com/icons)

* Other icons were sourced from [Bootstrap](https://getbootstrap.com/docs/4.0/extend/icons/)

---
# Features

~~~
Our features will be special as when a customer is updating their processes do I have spinning icons to notify him that every transaction performed, we will have certain automations, in the future with links to Facebook Instagram and Twitter,
~~~

## VALIDATORS 

 These are validating websites that were used to validate my website properly.

   * HTML Validator 
   [HTML Validation](https://jsonformatter.org/html-validator)

   * W3C Markup Validation Service:
   [W3C Validation](https://validator.w3.org/#validate_by_input)

   * Css Validation Service:
   [CSS Validation](https://jigsaw.w3.org/css-validator/#validate_by_input)


# Deployment

To run a frontend (HTML, CSS, Javascript only) application in Gitpod, in the terminal, type:

`python3 -m http.server`

A blue button should appear to click: _Make Public_,

Another blue button should appear to click: _Open Browser_.

To run a backend Python file, type `python3 app.py`, if your Python file is named `app.py` of course.

A blue button should appear to click: _Make Public_,

Another blue button should appear to click: _Open Browser_.

In Gitpod you have superuser security privileges by default. Therefore you do not need to use the `sudo` (superuser do) command in the bash terminal in any of the lessons.


1. Log in to your Heroku account and go to *Account Settings* in the menu under your avatar.
2. Scroll down to the *API Key* and click *Reveal*
3. Copy the key
4. In Gitpod, from the terminal, run `heroku_config`
5. Paste in your API key when asked

## Credit
Give full credit for the photos to Pexels, for everyone who work so hard to take such a beautiful photos, to make this project reality.

I like to also think and give credit to AliExpress for their apparel images that inspired me to make this website

## Acknowledgements

I would like to acknowledge my mentor Rachel Wallets and the slut community for helping me to get this far with my project, also Code Institute
------

'''
Thank you 
- Mario F Wilson :tada:
'''