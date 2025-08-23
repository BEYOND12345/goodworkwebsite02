# MASTER MOBILE NAVIGATION TEMPLATE
## For GoodHands Website - Complete Working Mobile Navigation

### 1. CSS STYLES (Add to <style> section or CSS file)
```css
/* Mobile Menu Button */
.mobile-menu-btn {
    display: none;
    flex-direction: column;
    background: none;
    border: none;
    cursor: pointer;
    padding: 8px;
    gap: 4px;
}

.mobile-menu-btn span {
    width: 24px;
    height: 2px;
    background: var(--charcoal);
    border-radius: 1px;
    transition: all 0.3s ease;
}

/* Mobile Menu Container */
.mobile-menu {
    display: none;
    position: absolute;
    top: 100%;
    left: 0;
    right: 0;
    background: var(--white);
    border-top: 1px solid var(--light-grey);
    box-shadow: var(--shadow-lg);
    z-index: 999;
}

.mobile-menu a {
    display: block;
    padding: 16px 24px;
    color: var(--charcoal);
    text-decoration: none;
    border-bottom: 1px solid var(--light-grey);
    transition: all 0.3s ease;
}

.mobile-menu a:hover {
    background: var(--yellow-light);
    color: var(--yellow-primary);
}

/* Mobile Responsive Media Query */
@media (max-width: 768px) {
    .nav-menu {
        display: none !important;
    }
    
    .mobile-menu-btn {
        display: flex;
    }
    
    .mobile-menu.active {
        display: block;
    }
    
    .nav-container {
        padding: 0 16px;
    }
}
```

### 2. HTML STRUCTURE (Add inside nav-container div, after nav-menu)
```html
<!-- Mobile Menu Button -->
<button class="mobile-menu-btn" onclick="toggleMobileMenu()" aria-label="Toggle menu">
    <span></span>
    <span></span>
    <span></span>
</button>

<!-- Mobile Menu -->
<div class="mobile-menu" id="mobileMenu">
    <a href="index.html" onclick="closeMobileMenu()">Home</a>
    <a href="handyman-services-byron-bay.html" onclick="closeMobileMenu()">Services</a>
    <a href="areas.html" onclick="closeMobileMenu()">Areas</a>
    <a href="about.html" onclick="closeMobileMenu()">About</a>
    <a href="contact.html" onclick="closeMobileMenu()">Contact</a>
    <a href="tel:0481457271" onclick="closeMobileMenu()" class="mobile-cta">Call Now</a>
</div>
```

### 3. JAVASCRIPT FUNCTIONS (Add before closing </body> tag)
```javascript
<script>
    // Mobile Menu Toggle Functions
    function toggleMobileMenu() {
        const mobileMenu = document.getElementById('mobileMenu');
        mobileMenu.classList.toggle('active');
    }

    function closeMobileMenu() {
        const mobileMenu = document.getElementById('mobileMenu');
        mobileMenu.classList.remove('active');
    }

    // Close mobile menu when clicking outside
    document.addEventListener('click', function(event) {
        const mobileMenu = document.getElementById('mobileMenu');
        const menuBtn = document.querySelector('.mobile-menu-btn');
        
        if (mobileMenu && menuBtn && !mobileMenu.contains(event.target) && !menuBtn.contains(event.target)) {
            mobileMenu.classList.remove('active');
        }
    });

    // Close mobile menu on window resize
    window.addEventListener('resize', function() {
        if (window.innerWidth > 768) {
            const mobileMenu = document.getElementById('mobileMenu');
            if (mobileMenu) {
                mobileMenu.classList.remove('active');
            }
        }
    });
</script>
```

### 4. COMPLETE NAVIGATION STRUCTURE
The complete navigation should look like this:

```html
<header class="header-nav">
    <div class="nav-container">
        <div class="nav-logo">
            <a href="index.html">GoodHands</a>
        </div>
        <nav class="nav-menu">
            <a href="index.html">Home</a>
            <a href="handyman-services-byron-bay.html">Services</a>
            <a href="areas.html">Areas</a>
            <a href="about.html">About</a>
            <a href="contact.html">Contact</a>
            <a href="tel:0481457271" class="nav-cta">Call Now</a>
        </nav>
        
        <!-- MOBILE NAVIGATION COMPONENTS -->
        <button class="mobile-menu-btn" onclick="toggleMobileMenu()" aria-label="Toggle menu">
            <span></span>
            <span></span>
            <span></span>
        </button>
        <div class="mobile-menu" id="mobileMenu">
            <a href="index.html" onclick="closeMobileMenu()">Home</a>
            <a href="handyman-services-byron-bay.html" onclick="closeMobileMenu()">Services</a>
            <a href="areas.html" onclick="closeMobileMenu()">Areas</a>
            <a href="about.html" onclick="closeMobileMenu()">About</a>
            <a href="contact.html" onclick="closeMobileMenu()">Contact</a>
            <a href="tel:0481457271" onclick="closeMobileMenu()" class="mobile-cta">Call Now</a>
        </div>
    </div>
</header>
```

### IMPLEMENTATION CHECKLIST
- [ ] CSS styles added (mobile-menu-btn, mobile-menu, media queries)
- [ ] Mobile menu button HTML added (with 3 span elements)
- [ ] Mobile menu container added (with id="mobileMenu")
- [ ] JavaScript functions added (toggleMobileMenu, closeMobileMenu)
- [ ] Event listeners added (click outside, window resize)
- [ ] Links updated to match page context
- [ ] Tested on mobile viewport (< 768px)