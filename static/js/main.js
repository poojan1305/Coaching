// ===== NAVBAR =====
const navbar = document.querySelector('.navbar');
const navToggle = document.querySelector('.nav-toggle');
const navLinks = document.querySelector('.nav-links');

window.addEventListener('scroll', () => {
  if (window.scrollY > 60) {
    navbar.classList.add('scrolled');
  } else {
    navbar.classList.remove('scrolled');
  }
});

if (navToggle) {
  navToggle.addEventListener('click', () => {
    navLinks.classList.toggle('open');
    navToggle.classList.toggle('active');
  });
  navLinks.querySelectorAll('a').forEach(link => {
    link.addEventListener('click', () => {
      navLinks.classList.remove('open');
    });
  });
}

// Mark active nav
const currentPath = window.location.pathname;
document.querySelectorAll('.nav-links a').forEach(a => {
  const href = a.getAttribute('href');
  if (href === currentPath || (href !== '/' && currentPath.startsWith(href))) {
    a.classList.add('active');
  } else if (href === '/' && currentPath === '/') {
    a.classList.add('active');
  }
});

// ===== COUNTER ANIMATION =====
function animateCounter(el) {
  const target = parseFloat(el.getAttribute('data-target'));
  const suffix = el.getAttribute('data-suffix') || '';
  const prefix = el.getAttribute('data-prefix') || '';
  const duration = 2000;
  const isDecimal = target % 1 !== 0;
  let startTime = null;

  function update(currentTime) {
    if (!startTime) startTime = currentTime;
    const elapsed = currentTime - startTime;
    const progress = Math.min(elapsed / duration, 1);
    const eased = 1 - Math.pow(1 - progress, 3);
    const current = eased * target;
    el.textContent = prefix + (isDecimal ? current.toFixed(1) : Math.floor(current)) + suffix;
    if (progress < 1) requestAnimationFrame(update);
    else el.textContent = prefix + (isDecimal ? target.toFixed(1) : target) + suffix;
  }
  requestAnimationFrame(update);
}

// ===== INTERSECTION OBSERVER =====
const observer = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      entry.target.classList.add('visible');
      // Counters
      if (entry.target.classList.contains('counter-num')) {
        animateCounter(entry.target);
      }
      observer.unobserve(entry.target);
    }
  });
}, { threshold: 0.15 });

document.querySelectorAll('.fade-in, .counter-num').forEach(el => observer.observe(el));

// ===== AUTO-DISMISS MESSAGES =====
setTimeout(() => {
  document.querySelectorAll('.message').forEach(m => {
    m.style.transition = 'opacity 0.5s ease';
    m.style.opacity = '0';
    setTimeout(() => m.remove(), 500);
  });
}, 5000);

// ===== SMOOTH SCROLL =====
document.querySelectorAll('a[href^="#"]').forEach(a => {
  a.addEventListener('click', e => {
    const href = a.getAttribute('href');
    if (href === '#') return;
    const target = document.querySelector(href);
    if (target) {
      e.preventDefault();
      target.scrollIntoView({ behavior: 'smooth', block: 'start' });
    }
  });
});

// ===== RESULTS FILTER =====
const boardFilter = document.getElementById('boardFilter');
const yearFilter = document.getElementById('yearFilter');
const searchInput = document.getElementById('searchInput');

if (boardFilter || yearFilter || searchInput) {
  function applyFilters() {
    const form = document.getElementById('filterForm');
    if (form) form.submit();
  }

  if (boardFilter) boardFilter.addEventListener('change', applyFilters);
  if (yearFilter) yearFilter.addEventListener('change', applyFilters);
}
