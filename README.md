# Dr.slot

[![GitHub commit activity](https://img.shields.io/github/commit-activity/t/Bruce0C/dr.slot)](https://www.github.com/Bruce0C/dr.slot/commits/main)
[![GitHub last commit](https://img.shields.io/github/last-commit/Bruce0C/dr.slot)](https://www.github.com/Bruce0C/dr.slot/commits/main)
[![GitHub repo size](https://img.shields.io/github/repo-size/Bruce0C/dr.slot)](https://www.github.com/Bruce0C/dr.slot)
[![badge](https://img.shields.io/badge/deployment-Heroku-purple)](https://drslot-e9b130b994da.herokuapp.com)

dr.slot is a Django-based web application designed to manage appointments for healthcare services. The project allows users to book appointments for various services such as doctor care and nursing care. It provides a simple and user-friendly interface for both users and administrators to manage appointments efficiently.

![screenshot](documentation/mockup.png)

source: [dr.slot amiresponsive](https://ui.dev/amiresponsive?url=https://drslot-e9b130b994da.herokuapp.com)


## UX

### The 5 Planes of UX

**1. Strategy**

 - **Purpose**
     - Provide healthcare providers with tools to manage appointments and availability efficiently.
     - Offer patients an intuitive platform to book, reschedule, or cancel appointments.
     - Enable administrators to oversee and manage users, appointments, and services.

**Primary User Needs**
- Patients need a seamless way to book, view, reschedule, or cancel appointments.
- Doctors need tools to manage their availability and appointments.
- Admins need the ability to manage users, appointments, and services.

**Business Goals**
- Build a reliable appointment management system that fosters trust between patients and healthcare providers.
- Streamline the process of booking and managing appointments for both patients and doctors.
- Provide a scalable and user-friendly platform that can handle multiple users and services.

**2. Scope**

**Features**
- User authentication and role-based access (patients, doctors, admins).
- Appointment booking, rescheduling, and cancellation for patients.
- Availability management for doctors.
- Admin dashboard for managing users, appointments, and services.
- Email notifications for appointment confirmations, reminders, and updates.
- Error handling (e.g., 404 error page for invalid URLs).

**Content Requirements**
- Appointment details (date, time, service, doctor, and patient).
- User account management (register, log in, reset password).
- Doctor availability schedules.
- Admin tools for managing users, appointments, and services.

**3. Structure**

**Information Architecture**

- **Navigation Menu:**
     - Links to Home, Appointments, Login/Register, and Admin Dashboard (for admins).
- **Hierarchy:**
     - Appointment booking and management features are prioritized for patients.
     - Doctors have access to availability and appointment management tools.
     - Admins have access to a dashboard for managing users, appointments, and services.

**User Flow**

1. Patients register for an account → log in to book an appointment.
2. Patients view available services and time slots → select a service, date, and time.
3. Patients receive confirmation and reminders via email.
4. Doctors log in to manage their availability and view appointments.
5. Admins log in to manage users, appointments, and services.

**4. Skeleton**

**Wireframes**

- **Homepage:**
     - Clear call-to-action buttons for booking appointments and logging in.
     - Overview of available services and doctors.
- **Patient Dashboard:**
     - List of upcoming appointments with options to reschedule or cancel.
     - Button to book a new appointment.
- **Doctor Dashboard:**
     - Calendar view of appointments.
    - Interface for setting availability.
- **Admin Dashboard:**
     - User management section (view, add, edit, delete users).
     - Appointment management section (view, filter, export appointments).
     - Service management section (add, edit, delete services).

**5. Surface**
**Visual Design Elements**

- **Colours:**
     - Use a clean and professional color scheme (e.g., blue and white) to convey trust and reliability.
- **Typography:**
     - Use a modern, readable font (e.g., Open Sans or Roboto) for clarity.
- **Icons and Buttons:**
     - Use intuitive icons for actions like booking, editing, and canceling appointments.
     - Clear and accessible buttons for primary actions (e.g., "Book Appointment," "Log In").
- **Responsive Design:**
     - Ensure the platform is mobile-friendly and adapts to different screen sizes.

### Colour Scheme

I used [coolors.co](https://coolors.co/080708-3772ff-df2935-fdca40-e6e8e6) to generate my color palette.

- `#` primary text.
- `#` primary highlights.
- `#` secondary text.
- `#` secondary highlights.

![screenshot](documentation/coolors.png)

### Typography

- [...](https://fonts.google.com/specimen/Montserrat) was used for the primary headers and titles.
- [...](https://fonts.google.com/specimen/Lato) was used for all other secondary text.
- [Font Awesome](https://fontawesome.com) icons were used throughout the site.

## Wireframes

To follow best practice, wireframes were developed for mobile, tablet, and desktop sizes.
I've used [Balsamiq](https://balsamiq.com/wireframes) to design my site wireframes.

| Page | Mobile | Tablet | Desktop |
| --- | --- | --- | --- |
| Register | ![screenshot](documentation/wireframes/mobile-register.png) | ![screenshot](documentation/wireframes/tablet-register.png) | ![screenshot](documentation/wireframes/desktop-register.png) |
| Login | ![screenshot](documentation/wireframes/mobile-login.png) | ![screenshot](documentation/wireframes/tablet-login.png) | ![screenshot](documentation/wireframes/desktop-login.png) |
| Home | ![screenshot](documentation/wireframes/mobile-home.png) | ![screenshot](documentation/wireframes/tablet-home.png) | ![screenshot](documentation/wireframes/desktop-home.png) | 
| Appointments | ![screenshot](documentation/wireframes/mobile-home.png) | ![screenshot](documentation/wireframes/tablet-home.png) | ![screenshot](documentation/wireframes/desktop-home.png) |

## User Stories

| Target | Expectation | Outcome |
| --- | --- | --- |
|As a patient| I want to create an account |so that I can log in and manage my appointments.|
|As a patient| I want to log in to my account| so that I can view my upcoming appointments.|
|As a user| I want to reset my password if I forget it |so that I can regain access to my account.|
|As a patient| I want to book an appointment with a doctor or healthcare provider |so that I can receive medical care.|
|As a patient| I want to reschedule or cancel my appointment |so that I can manage my schedule effectively.|
|As a patient| I want to receive email notifications for my appointment confirmation and reminders |so that I don’t miss my appointments.|
|As an admin| I want to manage user accounts (patients and doctors) |so that I can ensure the system is used appropriately.|
|As an admin| I want to view all appointments in the system |so that I can monitor the overall schedule.|
|As a user| I want the website to be mobile-friendly |so that I can access it on my phone or tablet.|
|As a user| I want the system to load quickly |so that I can access information without delays. |

## Features

### Existing Features

| Feature | Notes | Screenshot |
| --- | --- | --- |
| Register account | Authentication is handled by allauth, allowing users to register accounts. | ![screenshot](documentation/features/register.png) |
| Login | Authentication is handled by allauth, allowing users to log in to their existing accounts. | ![screenshot](documentation/features/login.png) |
| Logout | Authentication is handled by allauth, allowing users to log out of their accounts. | ![screenshot](documentation/features/logout.png) |
| 404 | The 404 error page will indicate when a user has navigated to a page that doesn't exist, replacing the default Heroku 404 page with one that ties into the site's look and feel. | ![screenshot](documentation/features/404.png) |