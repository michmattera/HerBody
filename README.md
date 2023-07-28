# HerBody

## Am I responsive image 

![Screenshot](./static/images/)

_____________________________________________________________________________

### Link to the finished site: [LINK](https://her-body.herokuapp.com/)


_____________________________________________________________________________
## Content:
- ### Project Goals and target audience
    - [Achieved](#achieved)
    - [Future implements](#future-projects)
    - [Audience](#audience)
- ### Project management
    - [Project boards](#github-project-board-user-stories-issues)
    - [Site user goal](#site-user-goal)
    - [Site owner goal](#site-owner-goal)
    - [User Stories](#user-stories)
- ### Wireframes and templates
    - [Lucid Chart](#lucid-chart)
    - [DrawSql Chart](#drawsql-chart)
    - [Database Structure](#database-and-structure)
    - [Uizard Template](#uizard-templates)
- ### Main functionality
    - [Booking functionality](#booking-functionality)
        - [Create a session](#create-a-session)
        - [Sessions - view all your sessions](#sessions-view-all-sessions)
        - [Sessions - edit a session](#edit-a-session)
        - [Sessions - delete a session](#delete-a-session)
        - [Sessions - confirm a session](#confirm-a-session)
    - [Contact](#contact)
    - [Account](#account)
        - [Login](#login)
        - [Register](#register)
        - [Logout](#logout)
- ### Design and Features
    - [Design and Features element](#design-and-features-element)
        - [Navbar](#navbar)
        - [Home page](#home-page)
        - [Footer](#footer)
        - [Messages](#messages)
        - [Error pages](#error-pages)
    - [Colour Scheme](#colour-scheme)
    - [Typography](#typography)
    - [Imagery](#imagery)
- ### Technologies Used
    - [Languages used](#languages)
    - [Frameworks, Packages & Programs Used](#frameworks-packages--programs-used)
- ### Testing
    - [TESTING.md](#testingmd)
- ### Development and Deployment
    - [Development](#development)
    - [Deploy to Heroku](#deployment)
- ### Credits
    - [Code](#code)
    - [Youtube tutorials](#youtube-tutorials-i-have-watched)
    - [Acknowledgements](#acknowledgements)



_____________________________________________________________________________
## Project goals and target audience.  
### Achieved:

-   Creating a website where user can register, login and logout.
-   Creating a website for a company where you can book your private sessions, see unavailable ones and edit or delete them.
-   Creating a website where the use can contact the company , and receive a confirmation email.

### Future projects: 

-   Creating a website where user could choose between 3 differents trainers.
-   Creating a webste where user could reset the password and email, and create his profile with more information.

### Audience:

- The target audience for the website are only girls.
- Medium age between 15 / 60 years old.
- Girls interested in getting in good shape and in getting private one on one self-defense lessons that the company offers.

#### Current Users:

- Current users have different ways to contact the company, such as phone number , email and a direct contact form in the website .
- Current users are able to login, and book and menage their sessions directly from the website.
- Current users can at any time delete their profile.

#### New users:

- New users are able to see what the company offers in the website.
- New users are tempt to register and login thanks to an only-login user feature that offer them 2 free sessions per week to book directly from the website.

[Back to top](#herBody)

_____________________________________________________________________________ 
## Project management

### Agile method.

- HerBody was developed using an agile method. That includes using GitHub issues, user stories and kanban boards.
- That gave me an overview of tasks structured in a to-do, in-progress and done way.

The project was divided in different iterations to divide the issues and the user stories in main Epic .
Inside each Iteration ( Epic ) developer created different issues , user stories, task and bugs , and differentiate the Iteration in diferent Boards.
Below are shown the links for:
1. The iteration
2. The main board user 
3. Small description for the Iteration


#### Iteration 1:

1. [Iteration 1](https://github.com/michmattera/HerBody/milestone/2?closed=1)
2. Starting to create core functionality ,superuser and administrator tasks .
3. [Board 1](https://github.com/users/michmattera/projects/3)

#### Iteration 2:

1. [Iteration 2](https://github.com/michmattera/HerBody/milestone/3?closed=1)
2. Create login and logout functionality, with html templates to display to user.
3. [Board 2](https://github.com/users/michmattera/projects/4)

#### Iteration 3:

1. [Iteration 3](https://github.com/michmattera/HerBody/milestone/4?closed=1)
2. Create booking models, main functionality.
3. [Board 3](https://github.com/users/michmattera/projects/5)

#### Iteration 4:

1. [Iteration 4](https://github.com/michmattera/HerBody/milestone/5?closed=1)
2. Second part main functionality for booking. Create models and views to delete and style booking functionality.
3. [Board 4](https://github.com/users/michmattera/projects/6)

#### Iteration 5:

1. [Iteration 5](https://github.com/michmattera/HerBody/milestone/6?closed=1)
2. Creating contact page, basic functionality, basic css.
3. [Board 5](https://github.com/users/michmattera/projects/7)

#### Iteration 6:

1. [Iteration 6](https://github.com/michmattera/HerBody/milestone/7)
2. Style all pages , link Coudinary pictures and create logo.
3. [Board 6](https://github.com/users/michmattera/projects/8)

#### Iteration 7:

1. [Iteration 7](https://github.com/michmattera/HerBody/milestone/8)
2. Focus on finishing the style for booking pages and media queries.
3. [Board 7](https://github.com/users/michmattera/projects/9)

#### Iteration 8:

1. [Iteration 8](https://github.com/michmattera/HerBody/milestone/9)
2. Focus on deploy again the project to heroku, fix important bugs and api, start automated and manual testing.
3. [Board 8](https://github.com/users/michmattera/projects/10)

#### Iteration 9:

1. [Iteration 9](https://github.com/michmattera/HerBody/milestone/10)
2. Focus on manual and automated testing.
3. [Board 9](https://github.com/users/michmattera/projects/11)

#### Iteration 10:

1. [Iteration 10](https://github.com/michmattera/HerBody/milestone/11)
2. Finish ReadMe and Testing.
3. [Board 10](https://github.com/users/michmattera/projects/12)



### Site User Goal

Site user has different goals:

- Being able to login
- Being able to logout
- Being able to register
- Being able to contact the company for any information or issues
- Being able to book a private session
- Being able to see available and unavailable sessions
- Being able to see what feature the company offer
- Being able to delete or edit the session

### Site Owner Goal

The site owner has being given a superuser , which have different features that a normal user.
Site owner has different goals:

- Being able to see all sessions booked
- Being able to see all contacts form submitted
- Being able to see all contacts information for the user
- Being able to see available and unavailable sessions
- Being able to attract as many new users as possible
- Being able to delete all sessions
- Being able to give as much information on the company to give trasparency
- Being able to authenticate users with password to give extra security to the account created
- Being able to accept free sessions just for logged in users, so that they have to create an account to be able to book it


### User stories

User stories were divided for Iteration ( Epic ), they were than divided in :

- Must-Have
- Should-Have
- Could-Have
- Won't-Have

_____________________________________________________________________________
## Wireframes and templates.  

### Lucid Charts
_____________________________________________________________________________
## Design and Features

### Design and Features

_____________________________________________________________________________

## Main functionality

### Booking functionality

Just logged in user can access the booking functionality.
All booking functionality has been created in the Booking folder, than divided in :

- [Booking views](booking/views.py "Link to booking views")
- [Booking forms](booking/forms.py "Link to booking forms")
- [Booking models](booking/models.py "Link to booking models")
- [Booking url](booking/urls.py "Link to booking url")

#### Create a session

Create a session is the first functionality created for the CRUD.
<br>
User can create a session in [Book a session template](templates/booking/booking_form.html "Link to book a session template").
<br>
<br>
In this template it is shown to the user based on the day of the week the avilable slots.

- Monday is closed so is always exluded
- Past dates are exluded
- The user has to book from 1 day before, so the same day should be excluded as well

For each day the user can choose between 3 different slot:
- At 9 am
- At 11 am
- At 16 pm 

<details>
<summary>Book a session functionality</summary>

![Book a session functionality](/assets/images/read-me-images/)

</details>

<br>
If the slot is available the user can click the slot, and will be brought to the booking confirmation template , where the user can confirm or cancel the booking . Will than be redirected to the booking list.

<details>
<summary>Booking confirmation functionality</summary>

![Booking confirmation functionality](/assets/images/read-me-images/)

</details>

#### Sessions - view all your sessions

All the bookings are shown to the user in the [Booking list template](templates/booking/booking_list.html "Link to booking list template") where the booking summary will appear, bringing the user to the Read of the CRUD functionality.
Here a summary of the booking user, booking date and time will appear.
As well here the user will have the possibility to edit or delete the booking .

<details>
<summary>Booking list functionality</summary>

![Booking list functionality](/assets/images/read-me-images/)

</details>

#### Sessions - edit a session

If thre user clicks on edit booking he will be brought to a similar page than when he wanted to book a session, with the same functionality, where as well he will see all the sesions available and not, and where the session clicked by the user to edit is still unavailable [Edit booking template](templates/booking/edit_booking.html "Link to edit booking template").
<br>
<br>
Similar to the book a session functionality, he will be brought to a confirmation page.


#### Sessions - delete a session

If the user clicks on the delete booking [Delete Booking template](templates/booking/delete_booking.html "Link to delete booking template") where a confirmation to the user will appear.
<br>
<br>
The user will have than 2 choices :

1. Confirm = The booking will be deleted, the user redirected to the booking list template
2. Cancel = The user will just be redirect to the booking list page , and the booking will still be there.


<details>
<summary>Delete Booking functionality</summary>

![Delete Booking functionality](/assets/images/read-me-images/)

</details>

#### Sessions - confirm a session

When the user book an a new session , or clicks on edit a new session, after selecting the slot, they will be brought to a confirmation page.
<br>
<br>
[Confirmation template](templates/booking/booking_confirmation.html "Link to booking confirmation template")
<br>
<br>
They are slightly different:

1. From book a session = The page will show a summary of the booking
2. From edit a session page = The page will show asummary of the old booking and a summary of a new one.
<br>
<br>
The user will have than 2 choices :

- Confirm = The booking will be saved, the user redirected to the booking list template.
- Cancel = The user will just be redirect to the booking list page , and the booking will still be there.


<details>
<summary>Confirmation page</summary>

![Confirmation page functionality](/assets/images/read-me-images/)

</details>

<details>
<summary>Confirmation page from edit</summary>

![Confirmation page from edit functionality](/assets/images/read-me-images/)

</details>

_____________________________________________________________________________

 ### Contact

Contact page functionality , will have a form , where the user will be prompted to enter:

- Name
- Email
- Subject
- Message

If the user is logged in than automatically the name and the email will be inserted automatically, while if the user is not logged in no.
The user than will have a success message and will be redirected to a contact confirmation page , just to confirm the correct submission of the form.

<details>
<summary>Contact functionality</summary>

![Contact functionality](/assets/images/read-me-images/)

</details>

_____________________________________________________________________________

 ### Account

 Account templates can be found in an account folder , where there will be:

- Login
- Register
- Logout

 ### Login

 The [Login template](templates/account/login.html "Link to login template") is a form where the user will be prompted to ask just the username and the password .
 If the username or the password are not correct than it will show a error message.
 If not than the user will be redirect to the home page.

 <details>
<summary>Login functionality</summary>

![Login functionality](/assets/images/read-me-images/)

</details>

 ### Register

 The [Register template](templates/account/register.html "Link to register template") is a form where the user will be prompted to ask just the username, the email, the password and a confirmation of the password .
 If there are any error in the form than it will show a error message.
 If not it will be redirect to the login page.

 <details>
<summary>Register functionality</summary>

![Register functionality](/assets/images/read-me-images/)

</details>

 ### Logout

 The [Logout template](templates/account/logout.html "Link to logout template") is a template page where the user will be asked to confirm if he wants to logout or not.
 He will have two choices:

 1. Confirm = Logging out the user, redirecting to the homepage.
 1. Cancel = Just redirecting him to the previuos page.

 <details>
<summary>Logout functionality</summary>

![Logout functionality](/assets/images/read-me-images/)

</details>

_____________________________________________________________________________

## Design and features

### Design and features element

Design and features throughout the page is consistent.

#### Navbar

The navbar has the following common and different features base on different media query size:

##### Common features =

1. Fixed on the top.
2. Dropdown is different if user is logged in or not:
    - Logged in user = Will have displayed book a session , my bookings and logout button
    - Not logged in user = Will have displayed Login and Register

##### For screen bigger than 992px =

1. When the user land in the page, it does not have any background-color, but when is scrolling down, it becomes bigger and take the main colour #d63384 as his background
2. Elements inside the navigation bar are all displayed and divided from right and left:
    - Home , About, Contact, Dropdown on the right
    - Logo on the left

##### For screen smaller than 992px =

1. When the user land in the page, it does have a dark background #241e30.
2. Elements inside the navigation bar are all displayed and divided from right and left:
    - Menu dropdown on the right
    - Logo on the left
3. The dropdown menu will than open all the elements on the left when clicked

 <details>
<summary>Navbar</summary>

![Navbar functionality](/assets/images/read-me-images/)

</details>


#### Home page

The homepage is divided in different sections:

- The first one with a 100% background image with a small text on the top and a button that differ from logged and not logged user
    - Logged user: SignUp
    - Not logged user: Book a session
- Second section with three different features, that pass from 3 column to one column for smaller screen size.
- Central section with a big paragraph.
And testimonial section where as before it changes the number of column , passing from 3, to 2 to 1 column for different media size.

 <details>
<summary>Homepage</summary>

![Homepage functionality](/assets/images/read-me-images/)

</details>



#### Footer

The footer has the following common and different features base on different media query size:

##### features =

1. Not fixed on the bottom , with dak color: #241e30.
2. It has four different features: 
    - Socials: with three different links that open in a new page
    - Contact: Contact information
    - Opening hours: With opening hours and dates
    - Copyright: With name of the developer, and different background color: #d63384.
3. Depending on different size as well it change elements position for better user interface.

 <details>
<summary>Footer functionality</summary>

![Footer functionality](/assets/images/read-me-images/)

</details>


#### Messages

Developer decided to use django.messages , adding just a small timeout javascript function to set a timer for the message to fade alone.
The color were the default color from django:
- Green = Correct 
- Red = Error
- Yellow = Warning

Almost all templates page have implemented the messages .
Developer decided to insert messages loop in includes folder inside the template and then include them in the templates directly.

 <details>
<summary>Messages functionality</summary>

![Messages functionality](/assets/images/read-me-images/)

</details>


#### Error pages

Developer decided to use and implement personalized error pages such as :
- 404
- 500
- 400

All have the same structure, same of the delete booking template.
All of them has as well a link that take the user back to the homepage, and a different error explanation.

 <details>
<summary>Error pages</summary>

![Error pages functionality](/assets/images/read-me-images/)

</details>


### Colour Scheme

The color scheme that the developer choose was based on a dark pink as the main colour for the application : #d63384 .
It was chosen because pink is usually associated with womans , and an only girls gym site want to let the user know at first impact that womans are represented .
<br>
<br>
With the help of [Colourmind](http://colormind.io/template/material-dashboard/) palette generator were than chosen the other 2 main color for the application.

- #241E30
- #F3EFEE

 <details>
<summary>Colour scheme</summary>

![Color scheme](/assets/images/read-me-images/)

</details>

____________________________________________________________________________

 ## Testing

Testing information can be found in a separate testing [file](TESTING.md "Link to testing file")
 







