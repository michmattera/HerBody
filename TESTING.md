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

Unittest was used by the developer to check the functionality for the django app.
Developer tried to check as much as possible with unittest.
First time using unittest so developer struggle a bit to test all part of the application.

The following file is where the developer worote the Unit Test:

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

    ![Booking confirmation]()

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

    ![Edit booking confirm]()

    </details>

<br>

3. Accounts pages

    <details>
    <summary>Login</summary>

    ![Login]()

    </details>

    <details>
    <summary>Logout_confirmation</summary>

    ![Logout confirmation]()

    </details>

    <details>
    <summary>Register</summary>

    ![Register]()

    </details>

3. Contact pages

    <details>
    <summary>Contact</summary>

    ![Contact]()

    </details>

    <details>
    <summary>Confirmation_contact</summary>

    ![Confirmation contact]()

    </details>

<br>

4. Error pages

    <details>
    <summary>400</summary>

    ![400]()

    </details>

    <details>
    <summary>404</summary>

    ![404]()

    </details>

    <details>
    <summary>500</summary>

    ![500]()

    </details>


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

    ![Contact]()

    </details>

<br>

2. Booking pages

    <details>
    <summary>Booking_confirmation</summary>

    ![Booking confirmation]()

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

    ![Edit booking confirm]()

    </details>

<br>

3. Accounts pages

    <details>
    <summary>Login</summary>

    ![Login](documentation/testing_files/lighthouse/mobile/lighthouse_login_mobile.PNG)

    </details>

    <details>
    <summary>Logout_confirmation</summary>

    ![Logout confirmation]()

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

    ![Confirmation contact]()

    </details>
    
<br>

4. Error pages

    <details>
    <summary>400</summary>

    ![400]()

    </details>

    <details>
    <summary>404</summary>

    ![404]()

    </details>

    <details>
    <summary>500</summary>

    ![500]()

    </details>


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