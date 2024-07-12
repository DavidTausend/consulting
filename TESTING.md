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
      - [Solved Bugs](#solved-bugs)
- [Paste Your Document In Here](#paste-your-document-in-here)
  * [And a table of contents](#and-a-table-of-contents)
  * [On the right](#on-the-right)

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

<div align="center"><img src="assets/images/readme/testing/css/css.webp"></div>

### Javascript Validation

[JSHint](https://jshint.com/): JavaScript files were tested using JSHint, which is a static code analysis tool used in software development for checking if JavaScript source code complies with coding rules. This helped in identifying potential errors and enforcing coding best practices.

#### PEP8 Validation

[CI Python Linter](https://pep8ci.herokuapp.com/): The code was validated using the CI Python Linter to ensure it follows PEP8 standards. This helps maintain a clean and consistent codebase, making it easier to read and maintain.

<div align="center"><img src="assets/images/readme/testing/py/admin.webp"></div>
<div align="center"><img src="assets/images/readme/testing/py/apps.webp"></div>
<div align="center"><img src="assets/images/readme/testing/py/asgi.webp"></div>
<div align="center"><img src="assets/images/readme/testing/py/certificates.webp"></div>
<div align="center"><img src="assets/images/readme/testing/py/cloudinary.webp"></div>
<div align="center"><img src="assets/images/readme/testing/py/consultant.webp"></div>
<div align="center"><img src="assets/images/readme/testing/py/manage.webp"></div>
<div align="center"><img src="assets/images/readme/testing/py/middleware.webp"></div>
<div align="center"><img src="assets/images/readme/testing/py/profolio.webp"></div>
<div align="center"><img src="assets/images/readme/testing/py/settings.webp"></div>
<div align="center"><img src="assets/images/readme/testing/py/url.webp"></div>
<div align="center"><img src="assets/images/readme/testing/py/view.webp"></div>
<div align="center"><img src="assets/images/readme/testing/py/wsgi.webp"></div>

### Accessibility

The website was tested using the Wave accessibility tool to ensure it meets accessibility standards. This tool helps identify any accessibility issues that might hinder users with disabilities from effectively using the site.

<img src="assets/images/readme/testing/wave.webp" alt="wave validation results">

## Lighthouse Testing

Lighthouse, an open-source, automated tool for improving the quality of web pages, was used to audit the website for performance, accessibility, best practices, and SEO.

### Lighthouse Results

The results from Lighthouse testing showed the following scores:

Homepage

- Desktop
<img src="assets/images/readme/testing/lighthouse/home_desktop.webp">
- Mobile
<img src="assets/images/readme/testing/lighthouse/home_mobile.webp">

Portfolio

- Desktop
<img src="assets/images/readme/testing/lighthouse/portfolio_desktop.webp">
- Mobile
<img src="assets/images/readme/testing/lighthouse/portfolio_mobile.webp">

Certificates

- Desktop
<img src="assets/images/readme/testing/lighthouse/cerificates_desktop.webp">
- Mobile
<img src="assets/images/readme/testing/lighthouse/certicates_mobile.webp">


Create a booking

- Desktop
<img src="assets/images/readme/testing/lighthouse/create_booking_desktop.webp">
- Mobile
<img src="assets/images/readme/testing/lighthouse/create_booking_mobile.webp">


Contact

- Desktop
<img src="assets/images/readme/testing/lighthouse/contact_desktop.webp">
- Mobile
<img src="assets/images/readme/testing/lighthouse/contact_mobile.webp">


About me

- Desktop
<img src="assets/images/readme/testing/lighthouse/about_desktop.webp">
- Mobile
<img src="assets/images/readme/testing/lighthouse/about_mobile.webp">


Login

- Desktop
<img src="assets/images/readme/testing/lighthouse/login_desktop.webp">
- Mobile
<img src="assets/images/readme/testing/lighthouse/login_mobile.webp">


Bookings

- Desktop
<img src="assets/images/readme/testing/lighthouse/bookings_desktop.webp">
- Mobile
<img src="assets/images/readme/testing/lighthouse/bookings_mobile.webp">


Update a booking

- Desktop
<img src="assets/images/readme/testing/lighthouse/admin_desktop.webp">
- Mobile
<img src="assets/images/readme/testing/lighthouse/admin_mobile.webp">


Submit a review

- Desktop
<img src="assets/images/readme/testing/lighthouse/submit_desktop.webp">
- Mobile
<img src="assets/images/readme/testing/lighthouse/submit_mobile.webp">

Review

- Desktop
<img src="assets/images/readme/testing/lighthouse/review_desktop.webp">
- Mobile
<img src="assets/images/readme/testing/lighthouse/review_mobile.webp">

## Device Testing

### Devices

### Browsers

These are the different browsers I have tested my site on after deployment.

- Google Chrome
- Firefox
- Safari
- Samsung Internet

### Responsiveness


### Manual testing

#### User Stories Testing

`User Goals`

|Site Owner Goals|How are they archieved|
|||

`Company Goals`

|Site Owner Goals|How are they archieved|
|||

#### Feature Testing

<br>

### Bugs

#### Known Bugs

#### Solved Bugs

