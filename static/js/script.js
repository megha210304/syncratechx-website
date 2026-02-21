document.addEventListener('DOMContentLoaded', () => {
    const mobileMenuBtn = document.querySelector('.mobile-menu-btn');
    const navLinks = document.querySelector('.nav-links');

    if (mobileMenuBtn && navLinks) {
        mobileMenuBtn.addEventListener('click', () => {
            navLinks.classList.toggle('active');
            const icon = mobileMenuBtn.querySelector('i');
            icon.classList.toggle('fa-bars');
            icon.classList.toggle('fa-times');
        });

        navLinks.querySelectorAll('a').forEach(link => {
            link.addEventListener('click', () => {
                navLinks.classList.remove('active');
                const icon = mobileMenuBtn.querySelector('i');
                if (icon && icon.classList.contains('fa-times')) {
                    icon.classList.remove('fa-times');
                    icon.classList.add('fa-bars');
                }
            });
        });
    }

    window.addEventListener('scroll', () => {
        const navbar = document.querySelector('.sticky-nav');
        if (!navbar) {
            return;
        }
        if (window.scrollY > 50) {
            navbar.classList.add('scrolled');
        } else {
            navbar.classList.remove('scrolled');
        }
    });

    const counters = document.querySelectorAll('.counter');
    const speed = 200;

    const startCounter = (counter) => {
        const target = +counter.getAttribute('data-target');
        let count = 0;
        const increment = target / speed;

        const updateCount = () => {
            if (count < target) {
                count += increment;
                counter.innerText = Math.ceil(count);
                setTimeout(updateCount, 1);
            } else {
                counter.innerText = target;
            }
        };
        updateCount();
    };

    const statsSection = document.querySelector('.stats');
    if (statsSection) {
        const observer = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    counters.forEach(counter => startCounter(counter));
                    observer.unobserve(entry.target);
                }
            });
        }, { threshold: 0.5 });
        observer.observe(statsSection);
    }

    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            const href = this.getAttribute('href');
            if (!href || href === '#') {
                return;
            }
            e.preventDefault();
            const target = document.querySelector(href);
            if (target) {
                target.scrollIntoView({
                    behavior: 'smooth'
                });
            }
        });
    });

    const blob = document.getElementById('cursor-blob');
    const prefersReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
    const blobDisabled = !blob || prefersReducedMotion || window.innerWidth < 768;

    if (!blobDisabled) {
        const blobSize = 420;
        let targetX = window.innerWidth / 2;
        let targetY = window.innerHeight / 3;
        let currentX = targetX;
        let currentY = targetY;

        const lerp = (start, end, factor) => start + (end - start) * factor;

        const handleMouseMove = (event) => {
            targetX = event.clientX;
            targetY = event.clientY;
        };

        const animateBlob = () => {
            currentX = lerp(currentX, targetX, 0.08);
            currentY = lerp(currentY, targetY, 0.08);
            const x = currentX - blobSize / 2;
            const y = currentY - blobSize / 2;
            blob.style.transform = `translate3d(${x}px, ${y}px, 0)`;
            requestAnimationFrame(animateBlob);
        };

        document.addEventListener('mousemove', handleMouseMove);
        animateBlob();
    } else if (blob) {
        blob.style.display = 'none';
    }
});
