Syncra TechX Website
====================

Syncra TechX is a small, production-style Flask application that serves a marketing site for a tech and talent studio. It is designed to look and behave like a modern SaaS landing page: mobile‑first, animated, and conversion‑focused.

Project Structure
-----------------

The project follows a standard Flask layout:

- `app.py` – Flask application entrypoint and route definitions
- `templates/` – Jinja2 templates (`base.html`, `index.html`, `about.html`, `contact.html`, `404.html`, `500.html`)
- `static/`
  - `css/style.css` – mobile‑first responsive styles and animations
  - `js/script.js` – navbar behavior, smooth scrolling, stats counter
  - `images/logo.png` – Syncra TechX logo
- `requirements.txt` – Python dependencies (Flask + gunicorn)

Key Features
------------

- Mobile‑first responsive layout with CSS Grid and modern breakpoints
- Fluid typography using `clamp()` for consistent reading on 320–1920px widths
- Sticky, animated navbar that reacts on scroll
- Fully responsive hero section with trust signals and strong CTAs
- Services, stats, and industries sections styled for a SaaS feel
- Contact form with basic server‑side validation and optional email sending
- Custom branded 404 and 500 error pages

Getting Started (Local Development)
-----------------------------------

1. **Clone the repository**

   ```bash
   git clone https://github.com/megha210304/syncratechx-website.git
   cd syncratechx-website
   ```

2. **Create and activate a virtual environment** (recommended)

   ```bash
   python -m venv venv
   # Windows
   venv\Scripts\activate
   # macOS / Linux
   # source venv/bin/activate
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Run the development server**

   ```bash
   python app.py
   ```

5. **Open the site**

   Visit `http://127.0.0.1:5000/` in your browser.

Contact Form & Email Sending
----------------------------

The `/contact` route validates basic form fields and can optionally send an email when a message is submitted.

To enable email sending in a production environment, provide the following environment variables:

- `SMTP_SERVER` – SMTP host (for example, `smtp.gmail.com`)
- `SMTP_PORT` – SMTP port (commonly `465` for SSL)
- `SMTP_USER` – SMTP username (often the sending email address)
- `SMTP_PASSWORD` – SMTP password or app password
- `CONTACT_RECIPIENT` – email that should receive contact form submissions (defaults to `hr@headsyncratechx.com` if not set)

If these variables are not set, the contact form will still validate and display a success message, but email sending will be skipped safely.

Production Deployment
---------------------

This app is designed to be deployed behind a production WSGI server such as gunicorn.

1. **Set the Flask secret key**

   Configure a strong secret key via the environment:

   ```bash
   export SECRET_KEY="your‑strong‑random‑secret"
   ```

2. **Run with gunicorn**

   ```bash
   gunicorn "app:app"
   ```

Use your hosting provider (Render, Railway, etc.) to:

- Configure environment variables (`SECRET_KEY`, SMTP settings, `CONTACT_RECIPIENT`)
- Enable HTTPS / SSL
- Attach a custom domain

Development Notes
-----------------

- `.gitignore` excludes Python bytecode, virtual environments, and `.env` files.
- Front‑end behavior (navbar, counters, smooth scroll) is written in vanilla JavaScript and loaded once from `static/js/script.js`.
- Animations use AOS (Animate On Scroll), initialized globally in `base.html`.

License
-------

This repository is intended for demonstration and portfolio purposes. If you plan to reuse or extend this project for commercial work, review and adapt it to your specific requirements and organizational policies.

