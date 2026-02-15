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
