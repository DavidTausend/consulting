<h1 align="center">Consulting</h1>

<img src="/static/images/portfolio/consulting.webp" alt="Consulting picture">

<h3 align="center"><a href="https://consulting-d8d637d4e865.herokuapp.com/">➡️ View the live project here ⬅️</a></h3>

<br/>

<div align="center">

</div>

## Introduction

Consulting is a web application designed to showcase a collection of projects that highlight the journey in cloud infrastructure, application development, and problem-solving. It includes a portfolio section, certificates, and a contact form for consultations.

<br>

## Table of Contents

- [Introduction](#introduction)
- [Table of Contents](#table-of-contents)
- [User Experience (UX)](#user-experience--ux-)
  * [User Stories](#user-stories)
    + [User goals](#user-goals)
    + [Company goals](#company-goals)
- [Design](#design)
  * [Typography](#typography)
  * [Color Scheme](#color-scheme)
  * [Wireframes](#wireframes)
    + [Desktop](#desktop)
    + [Tablet](#tablet)
    + [Mobile](#mobile)
    + [Entity-Relationship Diagram](#entity-relationship-diagram)
- [Agile Workflow](#agile-workflow)
  * [Epics, User Stories and Tasks](#epics--user-stories-and-tasks)
    + [Epics](#epics)
    + [User Stories](#user-stories-1)
    + [Tasks](#tasks)
  * [Github Project Boards](#github-project-boards)
    + [User Stores List](#user-stores-list)
    + [Kanban Board](#kanban-board)
    + [MoSCoW Prioritization](#moscow-prioritization)
    + [Story Points and Stars](#story-points-and-stars)
    + [Project Milestones](#project-milestones)
    + [MVP Milestone](#mvp-milestone)
    + [Post-MVP Milestone](#post-mvp-milestone)
    + [Enhancement Milestone](#enhancement-milestone)
- [Features](#features)
  * [Navigation Bar](#navigation-bar)
  * [Hero Section](#hero-section)
  * [Social Media Section](#social-media-section)
  * [Portfolio Section](#portfolio-section)
  * [Certificates Section](#certificates-section)
  * [About Me Section](#about-me-section)
  * [Contact Form](#contact-form)
  * [User Authentication](#user-authentication)
  * [Admin Dashboard](#admin-dashboard)
  * [Booking System](#booking-system)
  * [Review System](#review-system)
- [Future Implementations](#future-implementations)
  * [Programming Languages](#programming-languages)
  * [Applications, Plugins & Tools Used](#applications--plugins---tools-used)
- [Deployment & Local Development](#deployment---local-development)
  * [Deployment](#deployment)
  * [Local Development](#local-development)
    + [Heroku Deployment](#heroku-deployment)
    + [Environment Variables](#environment-variables)
    + [How to Fork](#how-to-fork)
    + [How to Clone](#how-to-clone)
    + [Committing and Pushing Changes](#committing-and-pushing-changes)
- [Testing](#testing)
- [Credits](#credits)
  * [Content](#content)
    + [Challenges](#challenges)
    + [External Articles and Guides](#external-articles-and-guides)
    + [Community Contributions and Forums](#community-contributions-and-forums)
    + [Design and Spacing Techniques](#design-and-spacing-techniques)
  * [Software Design Documentation](#software-design-documentation)
  * [Media](#media)
  * [Acknowledgments](#acknowledgments)

[Generate TOC](https://ecotrust-canada.github.io/markdown-toc/)

<br>

## User Experience (UX)

### User Stories

#### User goals

- As a user, I want to view a collection of projects to understand the developer's expertise and experience.
- As a user, I want to see the certifications the developer has obtained to validate their skills.
- As a user, I want to contact the developer for consultation services easily.
- As a user, I want to access the website on any device, including my phone, tablet, or desktop.

#### Company goals

- As a company, we want to display our projects in a portfolio to attract potential clients.
- As a company, we want to show our certifications to establish credibility and expertise.
- As a company, we want to provide a contact form to engage users and offer consultation services.
- As a company, we want to ensure the website has a professional and appealing design to create a positive impression.


## Design

### Typography

The primary font used throughout the website is Arial, sans-serif, providing a clean and professional look. Various font sizes are implemented to create a clear hierarchy, making it easy to differentiate between headings, subheadings, and body text.

### Color Scheme

The color scheme of the project is inspired by a sleek, modern design. The primary color is black (#000) which is used for the sidebar background and text, creating a strong contrast. The secondary color is white (#fff) for the main content background, ensuring readability. An accent color of bright blue (#0008fe) is used for buttons and hover effects, adding a pop of color and enhancing the user interface. Additional colors include gray (#adb5bd) for secondary text and light gray (#f9f9f9) for sections like the contact form background.

### Wireframes

Wireframes were created to plan the structure and layout of the website. They provided a clear visual representation of the user interface, helping to streamline the design and development process. Key wireframes include:

#### Desktop

<div align="center"><img src="static/images/readme/wireframe/desktop.webp" alt="Wireframe Desktop"></div>

#### Tablet

<div align="center"><img src="static/images/readme/wireframe/tablet.webp" alt="Wireframe Tablet"></div>

#### Mobile

<div align="center"><img src="static/images/readme/wireframe/mobile.webp" alt="Wireframe Tablet"></div>

#### Entity-Relationship Diagram

<div align="center"><img src="static/images/readme/testing/erd.webp" alt="Entity-Relationship Diagram"></div>

This ERD provides a clear structure of how different entities relate to each other within the project database.

## Agile Workflow

### Epics, User Stories and Tasks

In this project, Agile methodologies were employed to ensure a flexible and iterative approach to development. The work was divided into Epics, User Stories, and Tasks, managed through GitHub Project Boards.

#### Epics

Epics are large bodies of work that can be broken down into a number of smaller tasks or User Stories. They represent significant areas of functionality within the project. Examples of Epics in this project include:

- User Management
- Booking System
- Website Content and Structure
- Payment and Transactions
- User Experience and Accessibility

#### User Stories

User Stories are short, simple descriptions of a feature told from the perspective of the user. Each User Story addresses specific user needs and provides value to the end-user. Examples of User Stories in this project include:

1. User Registration and Authentication
2. Booking System
3. Consultant Profiles
4. Contact Information and Inquiry Form
5. Advanced Search and Filters for Consultations
6. Secure Payment System
7. Real-time Notifications
8. Admin Dashboard for Bookings Management
9. User Reviews and Feedback System
10. Accessibility and Mobile Responsiveness
11. Portfolio Section
12. Certificates Section
13. Homepage Design and Functionality
14. About Me Section

<div align="center"><img src="static/images/readme/testing/user_story.webp" alt="User Stories List"></div>

#### Tasks

Tasks are the individual steps needed to complete a User Story. They are the smallest units of work in the Agile workflow. Examples of Tasks for the User Story "User Registration and Authentication" might include:

- Create the registration form
- Implement user authentication
- Validate user input
- Set up email verification

### Github Project Boards

GitHub Project Boards were used to manage the project's workflow and track progress.

#### User Stores List

The User Stories List provides an overview of all User Stories, their status, priority, and assignees.

<div align="center"><img src="static/images/readme/testing/user_story_list.webp" alt="User Stories List"></div>

#### Kanban Board

The Kanban Board visualizes the flow of work, showing what is to be done, what is in progress, and what has been completed. This helps in managing tasks efficiently and ensures that the team is focused on the current priorities.

<div align="center"><img src="static/images/readme/testing/kanban_board.webp" alt="Kanban Board"></div>

#### MoSCoW Prioritization

MoSCoW Prioritization was used to categorize the User Stories based on their importance:

- **Must Have**: Critical features that are essential for the MVP.
- **Should Have**: Important features that are not critical but add significant value.
- **Could Have**: Nice-to-have features that enhance the user experience.
- **Won't Have**: Features that are out of scope for the current development cycle.

<div align="center"><img src="static/images/readme/testing/moscow.webp" alt="MoSCoW Prioritization"></div>

#### Story Points and Stars 

Story Points and Stars were used to estimate the effort required to complete each User Story. This helps in planning and allocating resources effectively.

#### Project Milestones

Project Milestones were set to track the progress of the project. Each milestone represents a significant point in the project timeline, such as the completion of the MVP or the implementation of critical features.

#### MVP Milestone

The MVP (Minimum Viable Product) Milestone includes the essential features needed to deploy a functional version of the application. This milestone focuses on delivering the core functionality.

#### Post-MVP Milestone

The Post-MVP Milestone includes additional features and enhancements that were not included in the initial MVP. These features aim to improve the user experience and add more value to the application.

#### Enhancement Milestone

The Enhancement Milestone includes ongoing improvements and optimizations to the application. This milestone ensures that the application remains up-to-date and continues to meet user needs.

## Features

### Navigation Bar

The navigation bar provides easy access to various sections of the site, including Home, Portfolio, Certificates, About Me, and Contact pages. It ensures seamless navigation and a consistent user experience.

<div align="center"><img src="static/images/readme/features/navbar.webp" alt="Navigation Bar"></div>

### Hero Section

The hero section introduces the site with a prominent heading and a call-to-action button. It provides a brief overview of the site's purpose and encourages users to explore further.

<div align="center"><img src="static/images/readme/features/hero.webp" alt="Hero Section"></div>

### Social Media Section

The social media section includes icons that link to various social media profiles, allowing users to connect and engage through multiple platforms.

<div align="center"><img src="static/images/readme/features/social_media.webp" alt="Social Media Section"></div>

### Portfolio Section

The portfolio section showcases a collection of projects with detailed descriptions and client testimonials, demonstrating expertise and past work.

<div align="center"><img src="static/images/readme/features/portfolio.webp" alt="Portfolio Section"></div>

### Certificates Section

The certificates section displays various certifications with images, descriptions, issuing organizations, and dates, highlighting professional qualifications.

<div align="center"><img src="static/images/readme/features/certificates.webp" alt="Certificates Section"></div>

### About Me Section

The about me section provides a detailed biography, sharing personal background, passions, and professional journey, creating a personal connection with visitors.

<div align="center"><img src="static/images/readme/features/about_me.webp" alt="About Me Section"></div>

### Contact Form

The contact form allows users to easily reach out for consultations, inquiries, or further information. It includes fields for name, email, and message.

<div align="center"><img src="static/images/readme/features/contact_form.webp" alt="Contact Form"></div>

### User Authentication

The user authentication feature includes secure login and registration functionality, ensuring that only authorized users can access certain sections of the site.

<div align="center"><img src="static/images/readme/features/authentication.webp" alt="User Authentication"></div>

### Admin Dashboard

The admin dashboard provides tools for managing bookings, and user inquiries. It streamlines administrative tasks and content updates.

<div align="center"><img src="static/images/readme/features/admin_dashboard.webp" alt="Admin Dashboard"></div>

### Booking System

The booking system allows users to schedule consultations with consultants. It includes functionality for creating, viewing, and updating bookings.

<div align="center"><img src="static/images/readme/features/booking.webp" alt="Booking System"></div>
<div align="center"><img src="static/images/readme/features/view_booking.webp" alt="View Booking"></div>

### Review System

The review system enables users to submit, view, edit, and delete reviews for consultants, fostering a transparent and feedback-driven environment.

<div align="center"><img src="static/images/readme/features/review.webp" alt="Review System"></div>

## Future Implementations

- Blog Section: Add a blog to share insights, tutorials, and updates.
- Search Functionality: Implement a search feature to help users find specific projects or certificates quickly.
- Client Testimonials: Allow clients to submit testimonials directly through the website.
- Advanced Analytics: Integrate advanced analytics to track user interactions and engagement.
- Enhanced Security: Implement additional security measures to protect user data and ensure privacy.

### Programming Languages

- [Python](<https://en.wikipedia.org/wiki/Python_(programming_language)>)
- [HTML5](https://en.wikipedia.org/wiki/HTML5)
- [CSS3](https://en.wikipedia.org/wiki/CSS)
- [JavaScript](https://en.wikipedia.org/wiki/JavaScript)
- [Django](https://www.djangoproject.com/)

### Applications, Plugins & Tools Used

[Gitpod](https://www.gitpod.io): An online IDE used for development and collaboration.

[Github](https://github.com/): Version control and repository hosting service.

[TinyPNG](https://tinypng.com/): Image compression tool used to optimize images for the web.

[Git](https://git-scm.com/): Version control system used for tracking changes in source code during development.

[ChatGPT](https://chat.openai.com/auth/login): AI tool used for generating code snippets, documentation, and providing assistance.

[Am I Responsive](https://ui.dev/amiresponsive): Tool for testing and showcasing responsive web design on different devices.

[Preview](https://support.apple.com/de-de/guide/preview/welcome/mac): Apple's built-in app for viewing and editing PDFs and images.

[Slack](https://slack.com): Communication and collaboration platform used for team discussions and project management.

[Google Chrome](https://www.google.com/): Web browser used for testing and debugging the application.

[Balsamiq](https://balsamiq.com): Wireframing tool used to create visual representations of the website's layout and structure.

[Python Tutor](https://pythontutor.com/javascript.html#mode=edit): Tool for visualizing Python code execution and understanding its behavior.

[Heroku](https://dashboard.heroku.com/login): Cloud platform used for deploying, managing, and scaling the web application.

[PEP](https://pep8ci.herokuapp.com/): Tool used to ensure code quality and adherence to PEP 8 Python coding standards.

[Cloudinary] (https://cloudinary.com): Cloud-based image and video management service used for uploading, storing, and serving media files.

## Deployment & Local Development

### Deployment

### Local Development

1. Clone the repository from GitHub by clicking the "Code" button and copying the URL.
2. Open your preferred IDE and open a terminal session in the directory you want to clone the repository to.
3. Type git clone followed by the URL you copied in step 1 and press enter.
4. (Optional): Set up a virtual environment in the project folder using python3 -m venv [virtual_environment name]
5. (Optional): To activate the virtual environment on Windows run myvenv\Scripts\activate and on macOS and Linux, run source myvenv/bin/activate
6. Install the required dependencies by typing pip install -r requirements.txt in the terminal.
- Note: The project is setup to use environment variables. You will need to set these up in your local environment. See Environment Variables for more information.
7. Connect your database of choice and run the migrations by typing python manage.py migrate in the terminal.
8. Create a superuser by typing python manage.py createsuperuser in the terminal and following the prompts.
9. (Optional):: Fixtures for Users and also the individual blog posts are included in the project in the fixtures directory. To add the pre-populated data to the database, run python manage.py loaddata fixtures/[fixture_name].json.
10. Run the app by typing python manage.py runserver in the terminal and opening the URL in your browser.

#### Heroku Deployment

1. Ensure the project repository has been uploaded to Github.
2. Login to the Heroku dashboard and create a new app.
3. Connect your GitHub repository to your Heroku app.
4. In the Settings tab, ensure that the Python Buildpack is added.
5. Set environment variables in the Config Vars section of the Settings tab.
6. In the Deploy tab, enable automatic deploys from your GitHub repository.
7. Click the "Deploy Branch" button to deploy the app.
8. Once the app has been deployed, click the "Open App" button to view the app.

#### Environment Variables

For local deployment, you will need to create a .env file in the root directory of the project and set the environment variables in this file.

- Note: Ensure the .env file is included in the .gitignore file to exclude it from your GitHub repo to prevent the environment variables from being publicly exposed.

For Heroku deployment, you will need to set the environment variables through the Heroku CLI or through the Heroku dashboard under 'Config Vars'.

You need to define the following environment variables:

- SECRET_KEY: The secret key for your Django project. This is a critical setting that's used for cryptographic signing, and should be kept secret at all times. It's used to provide cryptographic signing, and should be a long, random string of bytes.

- DEBUG: A boolean that turns on/off debug mode. Set to True for development to enable detailed error pages and logging for debugging. Set to False in production to improve performance and security.

- DATABASE_URL: The URL for your database. This should include the database engine, username, password, host, port, and database name. For a Postgres database, it typically looks like postgres://USER:PASSWORD@HOST:PORT/DB_NAME.

- CLOUDINARY_API_KEY: Your Cloudinary account's API key. This key is used to authenticate requests to Cloudinary's services for uploading and managing images and other media assets.

- CLOUDINARY_API_SECRET: Your Cloudinary account's API secret. This secret is used alongside the API key to securely sign requests to Cloudinary.

- CLOUDINARY_CLOUD_NAME: Your Cloudinary account's cloud name. This is the unique name that identifies your cloud within Cloudinary. It's used in the URL structure for accessing uploaded resources.

#### How to Fork

To fork the repository:

1. Log in (or sign up) to GitHub.
2. Go to the repository for this project: [DavidTausend/consulting](https://davidtausend.github.io/consulting)
3. Click the "Fork" button in the top right corner.

#### How to Clone

To clone the repository:

1. Log in (or sign up) to GitHub.
2. Go to the repository for this project: [DavidTausend/consulting](https://davidtausend.github.io/consulting)
3. Click on the "Code" button, select whether you would like to clone with HTTPS, SSH, or GitHub CLI, and copy the link shown.
4. Open the terminal in your code editor and change the current working directory to the location you want to use for the cloned directory.
5. Type `git clone` into the terminal and then paste the link you copied in step 3. Press enter.

#### Committing and Pushing Changes

After making changes to your local copy, you can commit and push them to GitHub:

1. Open the terminal in the directory of your cloned repository.
2. Use `git status` to see the changes you've made.
3. Use `git add .` to stage all changes for commit, or `git add <filename>` to stage specific files.
4. Use `git commit -m "Your commit message here"` to commit your changes with a descriptive message.
5. Use `git push origin main` to push your changes to the main branch on GitHub.

## Testing

[Testing documetation](TESTING.md)

## Credits

### Content

#### Challenges

- Integrating various services like Cloudinary and Heroku required a good understanding of the APIs and deployment processes.
- Ensuring the application is responsive and accessible was a continuous process, involving multiple rounds of testing and refinement.

#### External Articles and Guides

The development of this project was greatly aided by various external resources that provided guidance and insights:

- [Django Documentation](https://docs.djangoproject.com/en/5.0/): The official documentation for Django, which was invaluable for understanding framework specifics.
- Bootstrap Documentation: For styling and responsive design guidelines.
- Cloudinary Documentation: For managing image uploads and delivery.

#### Community Contributions and Forums

- [Stack Overflow](https://stackoverflow.com/): For troubleshooting and resolving coding issues.
- [Django Community](https://forum.djangoproject.com/): For discussions and advice on best practices in Django development.
- [GitHub Community](https://github.com/): For repositories, code examples, and collaborative discussions.

#### Design and Spacing Techniques
- [CSS Tricks](https://css-tricks.com/): For CSS tips and techniques.
- [MDN Web Docs](https://developer.mozilla.org/en-US/): For detailed information on HTML, CSS, and JavaScript.

### Software Design Documentation

Detailed documentation for the software design, including architecture diagrams, data models, and user flows, was created to ensure a structured development process. This documentation included:

- Architecture Diagrams: Illustrating the overall structure of the application, including components and their interactions.
- Data Models: Defining the structure of the database and relationships between different entities.
- User Flows: Mapping out the user journey through the application to ensure a seamless experience.

### Media

- Images: All images used in the project were either created specifically for the project, sourced from free or from certificates, high-quality images.

- Icons: Icons were sourced from Font Awesome, providing a consistent and visually appealing icon set.

### Acknowledgments

Special thanks to the following individuals and organizations for their support and contributions to this project:

- Code Institute: For providing a comprehensive course that laid the foundation for this project.
- Mentor: For guidance and feedback throughout the development process.
- Friends and Family: For their encouragement and support.
- Community Contributors: To everyone who provided feedback, suggestions, and support through forums and social media.

This project would not have been possible without the collective efforts and resources of the community. Thank you to everyone who contributed, directly or indirectly, to the successful completion of this project.

[Back to Top ^](#introduction)