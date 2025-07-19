# Job Applicant Dashboard

This project is a Django web application designed to serve as a **Job Applicant Dashboard** specifically for the "Junior Developer" position. It offers a streamlined way to manage applicant information, portfolios, and associated projects through the Django Admin interface, providing a user-friendly front-end for viewing applicant details.

## ✨ Features

  * **Applicant Listing:** View a sortable table of all applicants with their first name, last name, email, and quick access "Go" and "Delete" actions.
  * **Applicant Detail Page:** Dive into a dedicated page for each applicant, showcasing their detailed portfolio and project information.
  * **Django Admin Integration:** Easily create, update, and link Users, Portfolios, and Projects directly within the Django administration panel.
  * **Bootstrap Styling:** The dashboard is styled using Bootstrap, hosted as a static CDN for a clean and responsive design.
  * **Django Template Tags:** Demonstrates effective use of `{% extends %}`, `{% include %}`, and `{% url %}` for efficient template management.
  * **Mixed View Types:** Utilizes a Function-Based View (FBV) for the applicant list and Class-Based Views (CBV) for detail and delete operations, showcasing different Django view patterns.

-----

## 🚀 Setup Instructions

Follow these steps to get the Job Applicant Dashboard up and running on your local machine.

### Prerequisites

Before you begin, ensure you have the following installed:

  * **Python 3.8+** (or a recent version like 3.9, 3.10, etc.)
  * **pip** (Python package installer, usually comes with Python)
  * **Git** (for cloning the repository)

### 1\. Clone the Repository

First, clone the project from its Git repository to your local machine:

```bash
git clone <your-repository-url>
cd job_applicant_dashboard
```

**Note:** Replace `<your-repository-url>` with the actual URL of your Git repository.

### 2\. Create and Activate a Virtual Environment

It's highly recommended to use a [virtual environment](https://docs.python.org/3/library/venv.html) to manage your project's dependencies, keeping them isolated from other Python projects.

```bash
# For macOS/Linux
python3 -m venv venv
source venv/bin/activate

# For Windows
py -m venv venv
.\venv\Scripts\activate
```

You should see `(venv)` at the beginning of your terminal prompt, indicating the virtual environment is active.

### 3\. Install Project Dependencies

With your virtual environment activated, install all necessary Python packages using the `requirements.txt` file:

```bash
pip install -r requirements.txt
```

**If you haven't created `requirements.txt` yet**, you'll need to install Django first, then generate the file:

```bash
pip install Django # Or any other packages you know you've used
pip freeze > requirements.txt # Then run this command
```

### 4\. Apply Database Migrations

Django uses migrations to set up your database tables based on your `models.py` definitions.

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5\. Create a Superuser (for Django Admin)

You'll need a superuser account to access the Django administration panel and populate your database with applicants, portfolios, and projects.

```bash
python manage.py createsuperuser
```

Follow the prompts to create your username, email address, and a secure password.

### 6\. Download and Setup Bootstrap Static Files

The project uses Bootstrap as a static CDN. You need to download its compiled files and place them in your project's `static` directory.

1.  Go to the [official Bootstrap website](https://getbootstrap.com/).

2.  Navigate to the "Download" section and download the **"Compiled CSS and JS"** version.

3.  Once downloaded, extract the contents of the archive.

4.  Inside your project's root directory (`job_applicant_dashboard/`), create a folder named `static` if it doesn't already exist.

5.  Inside the `static` folder, create another folder named `bootstrap`.

6.  Copy the `css` and `js` folders from the extracted Bootstrap download into `job_applicant_dashboard/static/bootstrap/`.

    Your project structure should look like this:

    ```
    job_applicant_dashboard/
    └── static/
        └── bootstrap/
            ├── css/
            │   └── bootstrap.min.css
            │   └── ... (other Bootstrap CSS files)
            └── js/
                └── bootstrap.bundle.min.js
                └── ... (other Bootstrap JS files)
    ```

### 7\. Run the Development Server

Now you're ready to start the Django development server:

```bash
python manage.py runserver
```

The application will typically be accessible in your web browser at: `http://127.0.0.1:8000/`

-----

## 🛠️ Populating Data

After running the server, your dashboard will be empty. You need to add data through the Django Admin:

1.  **Access Django Admin:** Open your browser and go to `http://127.0.0.1:8000/admin/`. Log in using the superuser credentials you created earlier.
2.  **Create Users:**
      * Navigate to **"Authentication and Authorization"** \> **"Users"**.
      * Click **"Add user"**.
      * Create at least three users, filling in their `Username`, `First name`, `Last name`, and `Email address`. Set a password for each.
          * **Giyu Tomioka:** (e.g., username: `giyu.tomioka`, First Name: `Giyu`, Last Name: `Tomioka`)
          * **Sasaki Shumei:** (e.g., username: `sasaki.shumei`, First Name: `Sasaki`, Last Name: `Shumei`)
          * **Miyano Yoshikazu:** (e.g., username: `miyano.yoshikazu`, First Name: `Miyano`, Last Name: `Yoshikazu`)
3.  **Create Projects:**
      * Navigate to **"Portfolio App"** \> **"Projects"**.
      * Click **"Add Project"**.
      * Create a few sample projects, filling in `Project name` and `Project description`. For example:
          * `Project Name: E-commerce Platform Backend`, `Description: API development for online store.`
          * `Project Name: Personal Portfolio Website`, `Description: Responsive front-end design using React.`
          * `Project Name: Data Analysis Dashboard`, `Description: Interactive visualization using Python & Plotly.`
4.  **Create Portfolios:**
      * Navigate to **"Portfolio App"** \> **"Portfolios"**.
      * Click **"Add Portfolio"**.
      * For each of the users you created, create a corresponding Portfolio:
          * Select the **`User`** from the dropdown (e.g., `giyu.tomioka`).
          * Enter a **`Portfolio title`** (e.g., "Giyu Tomioka | Aspiring Junior Developer & Problem Solver").
          * Enter a **`Portfolio description`** (e.g., "Driven and detail-oriented, Giyu's portfolio showcases foundational programming skills...").
          * Select a **`Project`** from the dropdown. *Remember: A project can only be linked to one portfolio. If you try to select an already linked project, it will throw an error.*
          * Save each Portfolio.

-----

## 📋 Usage

  * **Applicant List:** Open your browser and navigate to `http://127.0.0.1:8000/` to see the table of all applicants you've added.
  * **Applicant Detail:** Click the **"Go"** button next to any applicant's entry to view their detailed portfolio and project information. The URL will change to something like `/portfolio/giyu.tomioka/`.
  * **Delete Applicant:** Click the **"Delete"** button next to an applicant to remove them and their associated portfolio from the database. You will be prompted for confirmation.

-----

## 🛑 Important Files

  * `job_applicant_dashboard/settings.py`: Main project settings, including `INSTALLED_APPS` and static file configuration.
  * `job_applicant_dashboard/urls.py`: Main URL routing for the project.
  * `portfolio/models.py`: Database models for `Project` and `Portfolio`.
  * `portfolio/views.py`: Logic for the dashboard pages (applicant list, detail, delete).
  * `portfolio/urls.py`: URL patterns specific to the `portfolio` app.
  * `portfolio/admin.py`: Registers models with the Django Admin.
  * `templates/`: Directory containing all HTML templates.
      * `base.html`: Base layout for all pages.
      * `includes/navbar.html`: Reusable navigation bar.
      * `portfolio/applicant_list.html`: Template for listing applicants.
      * `portfolio/applicant_detail.html`: Template for showing applicant portfolio details.
      * `portfolio/applicant_confirm_delete.html`: Template for delete confirmation.
  * `static/`: Directory for static assets like Bootstrap.
  * `.gitignore`: Specifies files and directories to be ignored by Git (like virtual environments and databases).
  * `requirements.txt`: Lists all Python package dependencies.

-----

## 📚 Built With

  * [Django](https://www.djangoproject.com/) - The high-level Python web framework.
  * [Bootstrap](https://getbootstrap.com/) - The most popular HTML, CSS, and JS framework for developing responsive, mobile-first projects on the web.

-----
