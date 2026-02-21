Syncra TechX Website
====================

SyncraTechX is a small, production-style Flask application that serves a marketing site for an enterprise-focused IT services firm. It is designed to look and behave like a modern SaaS landing page: mobile‑first, animated, and conversion‑focused.

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

Contact Form Integration
------------------------

All contact interactions are centralized through an embedded Google Form on the `/contact` page.

The contact page:

- Presents a hero section with “Get in Touch” messaging
- Embeds the Google Form in a responsive card container
- Provides a fallback button that opens the form directly in a new tab

There is no server‑side form processing or email handling in Flask for contacts; this keeps the backend simple and shifts data collection to Google Forms.

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

- Configure environment variables such as `SECRET_KEY`
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

