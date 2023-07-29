# **HERBODY TESTING**  

[Read Me file](/README.md)

[View Github repository](https://github.com/michmattera/HerBody)

[View the live project here](https://her-body.herokuapp.com/)


## **Table of contents**
***
1. [Browser Testing](#browser-testing)
2. [Unit Testing](#unit-testing)
3. [Manual Testing](#manual-Testing)
    1. [Navigation Buttons](#navigation-buttons)
    2. [Social-Media](#social-media)
4. [Code validator](#code-validator)
     1. [Lighthouse](#lighthouse)
     1. [Css](#css)
     1. [Js](#js)
     1. [Html](#html)
     5. [Python](#python)
5. [Bugs](#bugs)
    1. [Solved](#solved)
    2. [Not solved](#not-solved)
5. [Responsive](#responsive)

## **Browser testing**

The following browser has been tested and checked:

| Browser | Checked |
| --- | --- |
| Google chrome | :heavy_check_mark: |
| Microdoft edge | :heavy_check_mark: |
| Safari|  :heavy_check_mark: |
| Firefox | :heavy_check_mark: |

<details>
<summary> Google Chrome:</summary>

![Google Chrome](documentation/testing_files/google_chrome.PNG)

</details>

<details>
<summary> Microsoft Edge:</summary>

![Microsoft Edge](documentation/testing_files/edge.PNG)

</details>

<details>
<summary> Safari:</summary>

![Safari](documentation/testing_files/safari.jpg)

</details>

<details>
<summary> Firefox:</summary>

![Firefox](documentation/testing_files/modzilla_firefox.PNG)

</details>


## **Unit Testing**

Unittest was used by the developer to check the functionality of the Django app.
The developer tried to check as much as possible with the unit test.
First time using unit test so the developer struggle a bit to test all parts of the application.

The following file is where the developer wrote the Unit Test:

- [Booking Unit Test](booking/tests/)
- [Myproject Unit Test](myproject/tests/)

<details>
<summary> Review unittest</summary>

![Review Unittest]()

</details>

## Manual testing

### Navigation Buttons

<details>
<summary>Navigation logged in</summary>

![Navigation logged in](documentation/testing_files/nav_logged_in.gif)

</details>

<details>
<summary>Navigation logged out</summary>

![Navigation logged out](documentation/testing_files/nav_logged_out.gif)

</details>

### Social-Media

Social media links all opens in new page and are situated in the footer.

<details>
<summary>Social media</summary>

![Social Media](documentation/testing_files/social_media.gif)

</details>


## Code Validator

All code in the application was checked .

| Language | Checked |
| --- | --- |
| Css | :heavy_check_mark: |
| Js | :heavy_check_mark: |
| HTML |  :heavy_check_mark: |
| Python | :heavy_check_mark: |

### Lighthouse

Lighthouse reports were made for all pages , for desktop and mobile.

Lighthouse desktop:

1. General pages

    <details>
    <summary>Home</summary>

    ![Home](documentation/testing_files/lighthouse/desktop/lighthouse_home_desktop.PNG)

    </details>

    <details>
    <summary>About</summary>

    ![About](documentation/testing_files/lighthouse/desktop/lighthouse_about_desktop.jpg)

    </details>

    <details>
    <summary>Contact</summary>

    ![Contact](documentation/testing_files/lighthouse/desktop/lighthouse_contact_desktop.PNG)

    </details>

<br>

2. Booking pages

    <details>
    <summary>Booking_confirmation</summary>

    ![Booking confirmation](documentation/testing_files/lighthouse/desktop/lighthouse_booking_confirmation_desktop.PNG)

    </details>

    <details>
    <summary>Booking_form</summary>

    ![Booking form](documentation/testing_files/lighthouse/desktop/lighthouse_book_a_session_desktop.PNG)

    </details>

    <details>
    <summary>Booking_list</summary>

    ![Booking list](documentation/testing_files/lighthouse/desktop/lighthouse_booking_list_desktop.PNG)

    </details>

    <details>
    <summary>Delete_booking</summary>

    ![Delete booking](documentation/testing_files/lighthouse/desktop/lghthouse_delete_booking_desktop.PNG)

    </details>

    <details>
    <summary>Edit_booking</summary>

    ![Edit booking](documentation/testing_files/lighthouse/desktop/lighthouse_edit_booking_desktop.PNG)

    </details>

    <details>
    <summary>Edit_booking_confirm</summary>

    ![Edit booking confirm](documentation/testing_files/lighthouse/desktop/lighthouse_edit_booking_confirm_desktop.PNG)

    </details>

<br>

3. Accounts pages

    <details>
    <summary>Login</summary>

    ![Login](documentation/testing_files/lighthouse/desktop/lighthouse_login_desktop.PNG)

    </details>

    <details>
    <summary>Logout_confirmation</summary>

    ![Logout confirmation](documentation/testing_files/lighthouse/desktop/lighthouse_logout_desktop.PNG)

    </details>

    <details>
    <summary>Register</summary>

    ![Register](documentation/testing_files/lighthouse/desktop/lighthouse_register_desktop.PNG)

    </details>

3. Contact pages

    <details>
    <summary>Contact</summary>

    ![Contact](documentation/testing_files/lighthouse/desktop/lighthouse_contact_desktop.PNG)

    </details>

    <details>
    <summary>Confirmation_contact</summary>

    ![Confirmation contact](documentation/testing_files/lighthouse/desktop/lighthouse_confirmation_contact_desktop.PNG)

    </details>

<br>

4. Error pages

Error pages have the same structure as the delete_booking.
After deploying to Heroku, the lighthouse for error pages is not loaded.


Lighthouse mobile:

1. General pages

    <details>
    <summary>Home</summary>

    ![Home](documentation/testing_files/lighthouse/mobile/lighthouse_home_mobile.PNG)

    </details>

    <details>
    <summary>About</summary>

    ![About](documentation/testing_files/lighthouse/mobile/lighthouse_about_mobile.PNG)

    </details>

    <details>
    <summary>Contact</summary>

    ![Contact](documentation/testing_files/lighthouse/mobile/lighthouse_contact_mobile.PNG)

    </details>

<br>

2. Booking pages

    <details>
    <summary>Booking_confirmation</summary>

    ![Booking confirmation](documentation/testing_files/lighthouse/mobile/lighthouse_booking_confirmation_mobile.PNG)

    </details>

    <details>
    <summary>Booking_form</summary>

    ![Booking form](documentation/testing_files/lighthouse/mobile/lighthouse_book_a_session_mobile.PNG)

    </details>

    <details>
    <summary>Booking_list</summary>

    ![Booking list](documentation/testing_files/lighthouse/mobile/lighthouse_booking_list_mobile.PNG)

    </details>

    <details>
    <summary>Delete_booking</summary>

    ![Delete booking](documentation/testing_files/lighthouse/mobile/lighthouse_delete_booking_mobile.PNG)

    </details>

    <details>
    <summary>Edit_booking</summary>

    ![Edit booking](documentation/testing_files/lighthouse/mobile/lighthouse_edit_booking_mobile.PNG)

    </details>

    <details>
    <summary>Edit_booking_confirm</summary>

    ![Edit booking confirm](documentation/testing_files/lighthouse/mobile/lighthouse_edit_booking_confirm_mobile.PNG)

    </details>

<br>

3. Accounts pages

    <details>
    <summary>Login</summary>

    ![Login](documentation/testing_files/lighthouse/mobile/lighthouse_login_mobile.PNG)

    </details>

    <details>
    <summary>Logout_confirmation</summary>

    ![Logout confirmation](documentation/testing_files/lighthouse/mobile/lighthouse_logout_mobile.PNG)

    </details>

    <details>
    <summary>Register</summary>

    ![Register](documentation/testing_files/lighthouse/mobile/lightouse_register_mobile.PNG)

    </details>

3. Contact pages

    <details>
    <summary>Contact</summary>

    ![Contact](documentation/testing_files/lighthouse/mobile/lighthouse_contact_mobile.PNG)

    </details>

    <details>
    <summary>Confirmation_contact</summary>

    ![Confirmation contact](documentation/testing_files/lighthouse/mobile/lighthouse_confirmation_contact_mobile.PNG)

    </details>
    
<br>

4. Error pages

Error pages have the same structure as the delete_booking.
After deploying to Heroku, the lighthouse for error pages is not loaded.


### Css

All personal css was passed through validator.

<details>
<summary>Css</summary>

![Css](documentation/testing_files/languages_validator/css_validator.PNG)

</details>

### JS

All personal Js was passed through validator.

<details>
<summary>JS</summary>

![JS](documentation/testing_files/languages_validator/js_validator.PNG)

</details>

### HTML

All HTML pages were passed through validator.

<details>
<summary>Home</summary>

![Home](documentation/testing_files/languages_validator/w3c_validator_html_home.gif)

</details>

<details>
<summary>About</summary>

![About](documentation/testing_files/languages_validator/w3c_validator_about.gif)

</details>

<details>
<summary>Contact</summary>

![Contact](documentation/testing_files/languages_validator/w3c_validator_html_contact.gif)

</details>

<details>
<summary>Login</summary>

![Login](documentation/testing_files/languages_validator/w3c_validator_html_login.gif)

</details>

<details>
<summary>Register</summary>

![Register](documentation/testing_files/languages_validator/w3c_validator_html_register.gif)

</details>

<details>
<summary>Logout</summary>

![Logout](documentation/testing_files/languages_validator/w3c_validator_logout.gif)

</details>

<details>
<summary>Book a session</summary>

![Book a session](documentation/testing_files/languages_validator/w3c_validator_book_a_session.gif)

</details>

<details>
<summary>Booking list</summary>

![Booking list](documentation/testing_files/languages_validator/w3c_validator_html_booking_list.gif)

</details>

<details>
<summary>Booking confirmation</summary>

![Booking confirmation](documentation/testing_files/languages_validator/w3c_validator_html_booking_confirmation.gif)

</details>

<details>
<summary>Edit booking</summary>

![Edit booking](documentation/testing_files/languages_validator/w3c_validator_html_edit_booking.gif)

</details>

<details>
<summary>Confirm edit booking</summary>

![Confirm edit booking](documentation/testing_files/languages_validator/w3c_validator_html_edit_confirm_booking.gif)

</details>

<details>
<summary>Delete booking</summary>

![Delete booking](documentation/testing_files/languages_validator/w3c_validator_html_delete_booking.gif)

</details>

### Python

All python files were checked

## **Bugs**

Many bugs and issues were found by the developer during the making of this application.
Below is a list of all the most important bugs solved and unsolved by the developer.
All bugs were then described in Issues with the Label **Bug**


### Solved 

Many bugs were found by the developer. All bugs are listed here:

- [Bugs solved](https://github.com/michmattera/HerBody/issues?q=is%3Aissue+label%3Abug+is%3Aclosed)

Bugs are listed there, with a comment and an explanation of how the developer solved it.

Bigger issue :

- Heroku deployment: The developer faces a big issue when trying to redeploy to Heroku after finishing stilying and inserting the images. Heroku log would print that it wasn't finding the Cloudinary API. 

    1. Developer changed the API, and repush but same issue. 
    2. Then it set again the debug to TRUE, push, set debug to FALSE and the app was opening. 
    3. Developer then changes again the url and adds static files URL to each page to solve the cloudinary issue.

    <details>
    <summary>Heroku issue</summary>

    ![Heroku issue](documentation/testing_files/bugs/heroku_home_console.PNG)

    </details>

### Not solved 

A few small bugs were left unsolved by the developer.

1. HTML validator: In base.html the developer found when doing the HTML validator an end stray tag in the navigation bootstrap, shown below. Even if the developer checks and re-pushes the code to GitHub the validator always find this end div not closed.

    <details>
    <summary>Bug validator</summary>

    ![Bug: validator](documentation/testing_files/bugs/validator_html_bug.PNG)

    </details>

2. Logo mobile Apple: The developer found that just in Safari mobile the logo is slightly squeezed. The developer saw that the error is just in Apple while trying responsive on the pc and Android works normally. Below are the differences :

    <details>
    <summary>Bug apple</summary>

    ![Bug: apple](documentation/testing_files/bugs/bug_apple.jpg)

    </details>

    <details>
    <summary>No bug android</summary>

    ![No bug android](documentation/testing_files/bugs/android_no_bug.jpg)

    </details>

3. Refresh confirmation page: Developer found out that if the user does not click on cancel or confirm but just refreshes the page, the page refresh and says an error occurred, while at the same time, the booking is saved and then appears in the booking list. The developer tried to change the booking form and booking confirmation, but it was brought to another issue, were the booking was not brought up anymore in the page. The developer did not have time to fix it.

    <details>
    <summary>Refresh bug</summary>

    ![Refresh bug](documentation/testing_files/bugs/confirm_booking_bug.PNG)

    </details>


## **Responsive**

All pages were tested and checked for responsiveness.

