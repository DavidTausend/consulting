# Testing Documentation

Visit the deployed site: [Commit](https://news-bytes-f757f042ac64.herokuapp.com/)

## Table of Contents

- [Testing Documentation](#testing-documentation)
  * [Table of Contents](#table-of-contents)
    + [Automated Testing](#automated-testing)
      - [Validator Testing](#validator-testing)
        * [HTML Validation](#html-validation)
      - [CSS Validation](#css-validation)
    + [Javascript Validation](#javascript-validation)
      - [PEP8 Validation](#pep8-validation)
    + [Accessibility](#accessibility)
  * [Lighthouse Testing](#lighthouse-testing)
    + [Lighthouse Results](#lighthouse-results)
  * [Device Testing](#device-testing)
    + [Devices](#devices)
    + [Browsers](#browsers)
    + [Responsiveness](#responsiveness)
    + [Manual testing](#manual-testing)
      - [User Stories Testing](#user-stories-testing)
      - [Feature Testing](#feature-testing)
    + [Bugs](#bugs)
      - [Known Bugs](#known-bugs)
        * [Responsive Design Issues on Small Screens](#responsive-design-issues-on-small-screens)
        * [Image Upload Limits](#image-upload-limits)
      - [Solved Bugs](#solved-bugs)
      - [Database Connection Error on Heroku](#database-connection-error-on-heroku)
      - [PEP8 Compliance Errors](#pep8-compliance-errors)
      - [Empty Button Accessibility Error](#empty-button-accessibility-error)
      - [HTML Validation Errors](#html-validation-errors)
      - [Certificate Date Formatting Issue](#certificate-date-formatting-issue)

[Generate TOC](https://ecotrust-canada.github.io/markdown-toc/)

### Automated Testing

#### Validator Testing

##### HTML Validation

[W3C HTML Validation Service](https://validator.w3.org/): All HTML files were tested using the W3C HTML Validator. The service helped ensure the HTML syntax was correct, improving the accessibility and search engine optimization of the project. Errors and warnings were addressed to maintain clean and valid HTML.

|[Homepage](https://validator.w3.org/nu/?doc=https%3A%2F%2Fconsulting-d8d637d4e865.herokuapp.com%2F)|pass|

|[Portfolio](https://validator.w3.org/nu/?doc=https%3A%2F%2Fconsulting-d8d637d4e865.herokuapp.com%2Fportfolio%2F)|pass|

|[Certificates](https://validator.w3.org/nu/?doc=https%3A%2F%2Fconsulting-d8d637d4e865.herokuapp.com%2Fcertificates%2F)|pass|

|[Create a booking](https://validator.w3.org/nu/?doc=https%3A%2F%2Fconsulting-d8d637d4e865.herokuapp.com%2Fcreate_booking%2F)|pass|

|[Contact](https://validator.w3.org/nu/?doc=https%3A%2F%2Fconsulting-d8d637d4e865.herokuapp.com%2Fcontact%2F)|pass|

|[About me](https://validator.w3.org/nu/?doc=https%3A%2F%2Fconsulting-d8d637d4e865.herokuapp.com%2Fabout_me%2F)|pass|

|[Login](https://validator.w3.org/nu/?doc=https%3A%2F%2Fconsulting-d8d637d4e865.herokuapp.com%2Flogin%2F)|pass|

|[Bookings](https://validator.w3.org/nu/?doc=https%3A%2F%2Fconsulting-d8d637d4e865.herokuapp.com%2Fbookings%2F)|pass|

|[Update a booking]()|pass|

|[Submit a review](https://consulting-d8d637d4e865.herokuapp.com/consultants/1/reviews/submit/)|pass|

#### CSS Validation

[W3C CSS Validation Service] (https://jigsaw.w3.org/): The CSS files were validated using the W3C CSS Validator. The validation ensured that the CSS code was well-formed and adheres to the web standards, enhancing the appearance and performance of the website.

<div align="center"><img src="static/images/readme/testing/css/css.webp"></div>

### Javascript Validation

[JSHint](https://jshint.com/): JavaScript files were tested using JSHint, which is a static code analysis tool used in software development for checking if JavaScript source code complies with coding rules. This helped in identifying potential errors and enforcing coding best practices.

#### PEP8 Validation

[CI Python Linter](https://pep8ci.herokuapp.com/): The code was validated using the CI Python Linter to ensure it follows PEP8 standards. This helps maintain a clean and consistent codebase, making it easier to read and maintain.

<div align="center"><img src="static/images/readme/testing/py/admin.webp"></div>
<div align="center"><img src="static/images/readme/testing/py/apps.webp"></div>
<div align="center"><img src="static/images/readme/testing/py/asgi.webp"></div>
<div align="center"><img src="static/images/readme/testing/py/certificates.webp"></div>
<div align="center"><img src="static/images/readme/testing/py/cloudinary.webp"></div>
<div align="center"><img src="static/images/readme/testing/py/consultant.webp"></div>
<div align="center"><img src="static/images/readme/testing/py/manage.webp"></div>
<div align="center"><img src="static/images/readme/testing/py/middleware.webp"></div>
<div align="center"><img src="static/images/readme/testing/py/porfolio.webp"></div>
<div align="center"><img src="static/images/readme/testing/py/settings.webp"></div>
<div align="center"><img src="static/images/readme/testing/py/url.webp"></div>
<div align="center"><img src="static/images/readme/testing/py/view.webp"></div>
<div align="center"><img src="static/images/readme/testing/py/wsgi.webp"></div>

### Accessibility

The website was tested using the Wave accessibility tool to ensure it meets accessibility standards. This tool helps identify any accessibility issues that might hinder users with disabilities from effectively using the site.

<img src="static/images/readme/testing/wave/wave.webp" alt="wave validation results">

## Lighthouse Testing

Lighthouse, an open-source, automated tool for improving the quality of web pages, was used to audit the website for performance, accessibility, best practices, and SEO.

### Lighthouse Results

The results from Lighthouse testing showed the following scores:

Homepage

- Desktop
<img src="static/images/readme/testing/lighthouse/home_desktop.webp">
- Mobile
<img src="static/images/readme/testing/lighthouse/home_mobile.webp">

Portfolio

- Desktop
<img src="static/images/readme/testing/lighthouse/portfolio_desktop.webp">
- Mobile
<img src="static/images/readme/testing/lighthouse/portfolio_mobile.webp">

Certificates

- Desktop
<img src="static/images/readme/testing/lighthouse/cerificates_desktop.webp">
- Mobile
<img src="static/images/readme/testing/lighthouse/certicates_mobile.webp">


Create a booking

- Desktop
<img src="static/images/readme/testing/lighthouse/create_booking_desktop.webp">
- Mobile
<img src="static/images/readme/testing/lighthouse/create_booking_mobile.webp">


Contact

- Desktop
<img src="static/images/readme/testing/lighthouse/contact_desktop.webp">
- Mobile
<img src="static/images/readme/testing/lighthouse/contact_mobile.webp">


About me

- Desktop
<img src="static/images/readme/testing/lighthouse/about_desktop.webp">
- Mobile
<img src="static/images/readme/testing/lighthouse/about_mobile.webp">


Login

- Desktop
<img src="static/images/readme/testing/lighthouse/login_desktop.webp">
- Mobile
<img src="static/images/readme/testing/lighthouse/login_mobile.webp">


Bookings

- Desktop
<img src="static/images/readme/testing/lighthouse/bookings_desktop.webp">
- Mobile
<img src="static/images/readme/testing/lighthouse/bookings_mobile.webp">


Update a booking

- Desktop
<img src="static/images/readme/testing/lighthouse/admin_desktop.webp">
- Mobile
<img src="static/images/readme/testing/lighthouse/admin_mobile.webp">


Submit a review

- Desktop
<img src="static/images/readme/testing/lighthouse/submit_desktop.webp">
- Mobile
<img src="static/images/readme/testing/lighthouse/submit_mobile.webp">

Review

- Desktop
<img src="static/images/readme/testing/lighthouse/review_desktop.webp">
- Mobile
<img src="static/images/readme/testing/lighthouse/review_mobile.webp">

## Device Testing

### Devices

### Browsers

These are the different browsers I have tested my site on after deployment.

- Google Chrome
- Firefox
- Safari
- Samsung Internet

### Responsiveness

The application is designed to be fully responsive, ensuring a seamless user experience across various devices and screen sizes. This was achieved by using a combination of flexible grids, media queries, and responsive design principles. Key components and sections were tested on multiple devices, including desktops, tablets, and mobile phones, to ensure consistency and usability.

### Manual testing

Manual testing was conducted to verify that the application meets the specified requirements and performs as expected. This included testing various user interactions, form submissions, navigation flows, and overall user experience.

#### User Stories Testing

Each User Story was tested to ensure that the corresponding functionality works correctly and fulfills the specified user needs.

`User Goals`

|Site Owner Goals|How are they archieved|
|------------|------------------------|
| Easy registration and login process | Implemented a user-friendly registration and login system with clear instructions and validation feedback. |
| Book consultations easily | Provided a streamlined booking system with a simple form and clear availability indications. |
| View and manage bookings | Implemented a dashboard where users can view, update, and cancel their bookings. |
| Access consultant profiles | Displayed detailed consultant profiles with bios, specialties, and reviews. |
| Contact the site owner | Included a contact form for inquiries and support requests. |
| Provide feedback | Enabled users to submit and view reviews for consultants. |

`Company Goals`

|Site Owner Goals|How are they archieved|
|---------------|------------------------|
| Showcase services and projects | Created portfolio and services sections with detailed descriptions and images. |
| Capture leads and inquiries | Included a contact form and clear call-to-action buttons throughout the site. |
| Maintain a professional online presence | Designed the site with a modern, professional aesthetic and ensured all content is up-to-date. |
| Facilitate user engagement and feedback | Enabled review submissions and displayed user feedback prominently on consultant profiles. |

#### Feature Testing

`Navigation Bar (Desktop)`
|Feature|Expected Outcome|Testing Performed|Result|Pass/Fail|
|-------------------|---------------------------------------|----------------------------------------|------------------------------|-----------|
| Home Link         | Navigates to the home page            | Clicked the "Home" link in the navigation bar | Navigated to the home page    | Pass      |
| Portfolio Link    | Navigates to the portfolio page       | Clicked the "Portfolio" link in the navigation bar | Navigated to the portfolio page | Pass      |
| Certificates Link | Navigates to the certificates page    | Clicked the "Certificates" link in the navigation bar | Navigated to the certificates page | Pass      |
| About Me Link     | Navigates to the about me page        | Clicked the "About Me" link in the navigation bar | Navigated to the about me page | Pass      |
| Contact Link      | Navigates to the contact page         | Clicked the "Contact" link in the navigation bar | Navigated to the contact page | Pass      |
| Login/Logout Link | Logs in or out the user               | Clicked the "Login" or "Logout" link in the navigation bar | Logged in or out the user    | Pass      |


`Navigation Bar (Mobile)`
|Feature|Expected Outcome|Testing Performed|Result|Pass/Fail|
|-------------------|---------------------------------------|----------------------------------------|------------------------------|-----------|
| Menu Button       | Toggles the navigation menu           | Clicked the menu button                | Navigation menu toggled      | Pass      |
| Home Link         | Navigates to the home page            | Clicked the "Home" link in the navigation menu | Navigated to the home page    | Pass      |
| Portfolio Link    | Navigates to the portfolio page       | Clicked the "Portfolio" link in the navigation menu | Navigated to the portfolio page | Pass      |
| Certificates Link | Navigates to the certificates page    | Clicked the "Certificates" link in the navigation menu | Navigated to the certificates page | Pass      |
| About Me Link     | Navigates to the about me page        | Clicked the "About Me" link in the navigation menu | Navigated to the about me page | Pass      |
| Contact Link      | Navigates to the contact page         | Clicked the "Contact" link in the navigation menu | Navigated to the contact page | Pass      |
| Login/Logout Link | Logs in or out the user               | Clicked the "Login" or "Logout" link in the navigation menu | Logged in or out the user    | Pass      |

`Hero Section`
|Feature|Expected Outcome|Testing Performed|Result|Pass/Fail|
|-------------------|---------------------------------------|----------------------------------------|------------------------------|-----------|
| Heading             | Displays the main heading            | Viewed the hero section             | Main heading is displayed        | Pass      |
| Subheading          | Displays the subheading              | Viewed the hero section             | Subheading is displayed          | Pass      |
| Call to Action Button | Navigates to the portfolio page    | Clicked the "Portfolio" button      | Navigated to the portfolio page  | Pass      |
| Background Image    | Displays the background image correctly | Viewed the hero section          | Background image is displayed correctly | Pass      |

`Social Media Section`
|Feature|Expected Outcome|Testing Performed|Result|Pass/Fail|
|-------------------|---------------------------------------|----------------------------------------|------------------------------|-----------|
| Social Media Icons | Displays social media icons           | Viewed the social media section     | Social media icons are displayed | Pass      |
| Links to Social Media Pages | Navigates to the correct social media page | Clicked each social media icon | Navigated to the correct social media page | Pass      |

`Portfolio Section`
| Feature          | Expected Outcome                          | Testing Performed                     | Result                         | Pass/Fail |
|------------------|-------------------------------------------|--------------------------------------|--------------------------------|-----------|
| Portfolio Items  | Displays all portfolio items with title, description, image, and testimonial | Viewed the portfolio section | All portfolio items displayed correctly | Pass      |
| Portfolio Item Details | Displays detailed information of a portfolio item when clicked | Clicked on a portfolio item | Detailed information displayed correctly | Pass      |

`Certificates Section`
| Feature          | Expected Outcome                          | Testing Performed                     | Result                         | Pass/Fail |
|------------------|-------------------------------------------|--------------------------------------|--------------------------------|-----------|
| Certificates Items | Displays all certificates with title, description, image, issuing organization, and dates | Viewed the certificates section | All certificate items displayed correctly | Pass      |
| Certificate Item Details | Displays detailed information of a certificate when clicked | Clicked on a certificate item | Detailed information displayed correctly | Pass      |

`About Me Section`
| Feature          | Expected Outcome                          | Testing Performed                     | Result                         | Pass/Fail |
|------------------|-------------------------------------------|--------------------------------------|--------------------------------|-----------|
| Bio Information  | Displays the bio information correctly    | Viewed the about me section           | Bio information displayed correctly | Pass      |

`Contact Form`
| Feature          | Expected Outcome                          | Testing Performed                     | Result                         | Pass/Fail |
|------------------|-------------------------------------------|--------------------------------------|--------------------------------|-----------|
| Form Fields      | Displays name, email, and message fields  | Viewed the contact form               | All fields displayed correctly | Pass      |
| Form Submission  | Submits the form and shows a confirmation message | Filled out and submitted the form | Form submitted and confirmation message displayed | Pass      |

`User Authentication`
| Feature          | Expected Outcome                          | Testing Performed                     | Result                         | Pass/Fail |
|------------------|-------------------------------------------|--------------------------------------|--------------------------------|-----------|
| Registration     | Allows new users to register              | Filled out and submitted the registration form | User registered successfully | Pass      |
| Login            | Allows users to log in                    | Filled out and submitted the login form | User logged in successfully | Pass      |
| Logout           | Allows users to log out                   | Clicked the logout link              | User logged out successfully | Pass      |

`Admin Dashboard`
 Feature          | Expected Outcome                          | Testing Performed                     | Result                         | Pass/Fail |
|------------------|-------------------------------------------|--------------------------------------|--------------------------------|-----------|
| Dashboard Access | Allows admin to access the dashboard      | Logged in as admin and accessed the dashboard | Dashboard accessed successfully | Pass      |
| Manage Bookings  | Allows admin to manage bookings           | Viewed and edited bookings in the dashboard | Bookings managed successfully | Pass      |

`Booking System`
| Feature          | Expected Outcome                          | Testing Performed                     | Result                         | Pass/Fail |
|------------------|-------------------------------------------|--------------------------------------|--------------------------------|-----------|
| Create Booking   | Allows users to create a booking          | Filled out and submitted the booking form | Booking created successfully | Pass      |
| View Bookings    | Allows users to view their bookings       | Accessed the bookings page           | Bookings displayed correctly | Pass      |
| Update Booking Status | Allows admin to update booking status | Changed the status of a booking     | Booking status updated successfully | Pass      |

`Review System`
| Feature          | Expected Outcome                          | Testing Performed                     | Result                         | Pass/Fail |
|------------------|-------------------------------------------|--------------------------------------|--------------------------------|-----------|
| Submit Review    | Allows users to submit reviews            | Filled out and submitted the review form | Review submitted successfully | Pass      |
| View Reviews     | Allows users to view reviews              | Accessed the reviews page            | Reviews displayed correctly    | Pass      |
| Edit Review      | Allows users to edit their reviews        | Edited an existing review            | Review edited successfully     | Pass      |
| Delete Review    | Allows users to delete their reviews      | Deleted an existing review           | Review deleted successfully    | Pass      |

<br>

### Bugs

#### Known Bugs

##### Responsive Design Issues on Small Screens

Certain elements do not align properly or overlap when viewed on small screens, particularly in the portfolio section and affects user experience on mobile devices.

##### Image Upload Limits

Uploading large images sometimes results in a timeout or error and may face difficulties uploading large portfolio or certificate images.
Workaround: Resize images to smaller dimensions before uploading.

#### Solved Bugs

#### Database Connection Error on Heroku

The application was experiencing intermittent database connection errors on Heroku. I updated the database connection settings and ensured that the dj_database_url configuration is correctly set. This solved the issue of intermittent disconnections.

#### PEP8 Compliance Errors

Several PEP8 compliance errors were identified in the codebase, including line length issues and whitespace errors. The codebase was refactored to adhere to PEP8 guidelines, ensuring all lines are within the 79-character limit and removing trailing whitespaces.

#### Empty Button Accessibility Error

A button element was identified as empty during accessibility testing. I Added appropriate text inside the button element to ensure it is accessible to screen readers.

#### HTML Validation Errors

Several HTML validation errors were identified, including unclosed tags and elements used in incorrect contexts. The HTML structure was corrected to ensure all elements are properly nested and all tags are closed appropriately.

#### Certificate Date Formatting Issue

Certificate expiry dates were not displayed correctly when the expiry date was set to None. I Updated the template logic to handle None values and display "No expiry date" instead of leaving the field blank.


