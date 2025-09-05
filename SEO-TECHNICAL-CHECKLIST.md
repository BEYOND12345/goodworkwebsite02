# 🔧 SEO Technical Implementation Checklist
## Good Hands Handyman - Immediate Action Items

---

## 🚨 CRITICAL FIXES (Do Today)

### 1. Meta Descriptions Missing on All Pages
```html
<!-- Add unique meta descriptions to each page -->

<!-- Homepage -->
<meta name="description" content="Northern Rivers trusted handyman service. 15+ years experience, $65/hour intro rate. Same-day emergency repairs Byron Bay to Ballina. Call Dan: 0481 457271">

<!-- Service Pages Template -->
<meta name="description" content="Professional [SERVICE] in [LOCATION]. Licensed, insured, 15+ years experience. From $65/hour. Same-day service available. Free quotes: 0481 457271">

<!-- Location Pages Template -->
<meta name="description" content="[LOCATION] handyman services - repairs, maintenance, emergencies. Local expert Dan, $65/hour intro rate, same-day response. Call 0481 457271">

<!-- Blog Posts Template -->
<meta name="description" content="[BRIEF DESCRIPTION OF POST]. Expert advice from Northern Rivers' trusted handyman with 15+ years experience. Read more →">
```

### 2. Canonical Tags Implementation
```html
<!-- Add to EVERY page in <head> section -->
<link rel="canonical" href="https://goodhandshandyman.com.au/[exact-page-url]">

<!-- For pages with parameters -->
<link rel="canonical" href="https://goodhandshandyman.com.au/services/deck-restoration">
<!-- Not: /services/deck-restoration?utm_source=google -->
```

### 3. Image Alt Text Audit
```html
<!-- Current: <img src="deck.jpg"> -->
<!-- Fix to: -->
<img src="deck.jpg" 
     alt="Freshly restored timber deck in Byron Bay coastal home" 
     width="800" 
     height="600"
     loading="lazy">
```

---

## ⚡ PAGE SPEED CRITICAL PATH

### Immediate Wins (1-2 Hour Implementation)

#### 1. Add These Lines to Every Page Header
```html
<!-- Preconnect to external domains -->
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="preconnect" href="https://www.googletagmanager.com">
<link rel="dns-prefetch" href="https://www.google-analytics.com">

<!-- Preload critical resources -->
<link rel="preload" href="/css/critical.css" as="style">
<link rel="preload" href="/fonts/nunito-v25-latin-700.woff2" as="font" type="font/woff2" crossorigin>
```

#### 2. Lazy Load All Images
```javascript
// Add to all <img> tags
<img src="image.jpg" loading="lazy" alt="Description">

// For above-the-fold images only
<img src="hero-image.jpg" loading="eager" alt="Description" fetchpriority="high">
```

#### 3. Defer Non-Critical JavaScript
```html
<!-- Change Google Tag Manager loading -->
<!-- From: -->
<script src="https://www.googletagmanager.com/gtag/js?id=AW-17401144616"></script>

<!-- To: -->
<script async defer src="https://www.googletagmanager.com/gtag/js?id=AW-17401144616"></script>
```

---

## 📍 LOCAL SEO URGENT FIXES

### Google My Business Optimization Checklist
- [ ] Verify business ownership (if not done)
- [ ] Add all 54 services as GMB services
- [ ] Upload 10 before/after photos TODAY
- [ ] Set special hours for public holidays
- [ ] Add COVID-19 safety attributes
- [ ] Enable messaging
- [ ] Add booking link: https://goodhandshandyman.com.au/contact
- [ ] Create 3 Google Posts this week:
  1. "$65/hour intro rate for new customers"
  2. "Same-day emergency repairs available"
  3. "Storm season preparation services"

### NAP Consistency Audit
Ensure EXACT same format everywhere:
```
Business Name: Good Hands Handyman
Phone: 0481 457271 (not 0481-457-271 or 0481 457 271)
Address: Servicing Northern Rivers NSW 2481
```

---

## 🔗 INTERNAL LINKING QUICK FIXES

### Add to Every Service Page
```html
<!-- Related Services Section (add before footer) -->
<section class="related-services">
  <h2>Related Services You Might Need</h2>
  <div class="service-links">
    <a href="/deck-sanding">Deck Sanding & Restoration</a>
    <a href="/property-maintenance-byron-bay">Property Maintenance</a>
    <a href="/emergency-repairs">24/7 Emergency Repairs</a>
  </div>
</section>
```

### Add to Every Location Page
```html
<!-- Nearby Areas Section -->
<section class="nearby-areas">
  <h3>We Also Service Nearby Areas</h3>
  <p>In addition to [CURRENT LOCATION], Good Hands provides professional handyman services to:</p>
  <ul>
    <li><a href="/handyman-byron-bay">Byron Bay</a></li>
    <li><a href="/handyman-ballina">Ballina</a></li>
    <li><a href="/handyman-bangalow">Bangalow</a></li>
  </ul>
</section>
```

---

## 🏗️ SCHEMA MARKUP IMPLEMENTATION

### Add Review Schema to Homepage
```javascript
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "LocalBusiness",
  "@id": "https://goodhandshandyman.com.au/#business",
  "aggregateRating": {
    "@type": "AggregateRating",
    "ratingValue": "4.9",
    "reviewCount": "127",
    "bestRating": "5"
  },
  "review": [
    {
      "@type": "Review",
      "reviewRating": {
        "@type": "Rating",
        "ratingValue": "5"
      },
      "author": {
        "@type": "Person",
        "name": "Sarah Chen"
      },
      "reviewBody": "Dan has been maintaining our investment properties for 3 years. Reliable and fairly priced."
    }
  ]
}
</script>
```

### Add Service Schema to Each Service Page
```javascript
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Service",
  "name": "[SERVICE NAME]",
  "provider": {
    "@type": "LocalBusiness",
    "@id": "https://goodhandshandyman.com.au/#business"
  },
  "areaServed": {
    "@type": "State",
    "name": "New South Wales",
    "containsPlace": [
      {"@type": "City", "name": "Byron Bay"},
      {"@type": "City", "name": "Ballina"},
      {"@type": "City", "name": "Lismore"}
    ]
  },
  "hasOfferCatalog": {
    "@type": "OfferCatalog",
    "name": "[SERVICE] Services",
    "itemListElement": {
      "@type": "Offer",
      "price": "65.00",
      "priceCurrency": "AUD",
      "priceSpecification": {
        "@type": "UnitPriceSpecification",
        "price": "65.00",
        "priceCurrency": "AUD",
        "unitText": "HOUR"
      }
    }
  }
}
</script>
```

---

## 📱 MOBILE OPTIMIZATION FIXES

### CSS Fixes for Mobile
```css
/* Add to main CSS file */

/* Fix tap targets */
a, button, input, select, textarea {
  min-height: 44px;
  min-width: 44px;
}

/* Prevent horizontal scroll */
html, body {
  overflow-x: hidden;
  max-width: 100%;
}

/* Fix input zoom on iOS */
input, select, textarea {
  font-size: 16px !important;
}

/* Improve button spacing on mobile */
@media (max-width: 768px) {
  .btn {
    width: 100%;
    margin-bottom: 10px;
  }
  
  .hero-cta {
    flex-direction: column;
  }
}
```

### Add Click-to-Call for Mobile
```html
<!-- Add to header for mobile only -->
<a href="tel:0481457271" class="mobile-call-btn">
  <svg><!-- phone icon --></svg>
  Call Now
</a>

<style>
.mobile-call-btn {
  display: none;
  position: fixed;
  bottom: 20px;
  right: 20px;
  background: #FFB800;
  color: #2D3748;
  padding: 15px 20px;
  border-radius: 50px;
  box-shadow: 0 4px 12px rgba(0,0,0,0.2);
  z-index: 9999;
}

@media (max-width: 768px) {
  .mobile-call-btn {
    display: flex;
  }
}
</style>
```

---

## 🚀 .HTACCESS PERFORMANCE RULES

### Add to .htaccess file
```apache
# Enable Compression
<IfModule mod_deflate.c>
  AddOutputFilterByType DEFLATE text/plain
  AddOutputFilterByType DEFLATE text/html
  AddOutputFilterByType DEFLATE text/xml
  AddOutputFilterByType DEFLATE text/css
  AddOutputFilterByType DEFLATE application/xml
  AddOutputFilterByType DEFLATE application/xhtml+xml
  AddOutputFilterByType DEFLATE application/rss+xml
  AddOutputFilterByType DEFLATE application/javascript
  AddOutputFilterByType DEFLATE application/x-javascript
</IfModule>

# Browser Caching
<IfModule mod_expires.c>
  ExpiresActive On
  ExpiresByType image/jpg "access 1 year"
  ExpiresByType image/jpeg "access 1 year"
  ExpiresByType image/gif "access 1 year"
  ExpiresByType image/png "access 1 year"
  ExpiresByType image/webp "access 1 year"
  ExpiresByType text/css "access 1 month"
  ExpiresByType text/html "access 1 hour"
  ExpiresByType application/pdf "access 1 month"
  ExpiresByType text/x-javascript "access 1 month"
  ExpiresByType image/x-icon "access 1 year"
  ExpiresDefault "access 1 month"
</IfModule>

# Enable Keep-Alive
<IfModule mod_headers.c>
  Header set Connection keep-alive
</IfModule>

# GZIP Compression
<IfModule mod_gzip.c>
  mod_gzip_on Yes
  mod_gzip_dechunk Yes
  mod_gzip_item_include file \.(html?|txt|css|js|php|pl)$
  mod_gzip_item_include mime ^text/.*
  mod_gzip_item_include mime ^application/x-javascript.*
  mod_gzip_item_exclude mime ^image/.*
  mod_gzip_item_exclude rspheader ^Content-Encoding:.*gzip.*
</IfModule>
```

---

## 📊 TRACKING SETUP

### Google Analytics 4 Events to Track
```javascript
// Track phone clicks
document.querySelectorAll('a[href^="tel:"]').forEach(link => {
  link.addEventListener('click', () => {
    gtag('event', 'click_to_call', {
      'event_category': 'engagement',
      'event_label': 'header'
    });
  });
});

// Track form submissions
document.querySelector('#contact-form').addEventListener('submit', () => {
  gtag('event', 'form_submit', {
    'event_category': 'lead',
    'event_label': 'contact_form'
  });
});

// Track scroll depth
let scrolled25 = false, scrolled50 = false, scrolled75 = false, scrolled100 = false;

window.addEventListener('scroll', () => {
  const scrollPercent = (window.scrollY + window.innerHeight) / document.body.offsetHeight * 100;
  
  if (scrollPercent > 25 && !scrolled25) {
    gtag('event', 'scroll', {'percent': 25});
    scrolled25 = true;
  }
  // Repeat for 50%, 75%, 100%
});
```

---

## 🎯 CONVERSION OPTIMIZATION QUICK WINS

### Add Trust Signals to Every Page
```html
<!-- Add below header -->
<div class="trust-bar">
  <div class="container">
    <span>✓ Licensed & Insured</span>
    <span>✓ 15+ Years Experience</span>
    <span>✓ 127+ Five-Star Reviews</span>
    <span>✓ Same-Day Service</span>
  </div>
</div>

<style>
.trust-bar {
  background: #F7FAFC;
  border-bottom: 1px solid #E2E8F0;
  padding: 8px 0;
  font-size: 14px;
  text-align: center;
}
.trust-bar span {
  margin: 0 15px;
  color: #2D3748;
}
</style>
```

### Add Urgency Elements
```html
<!-- Add to contact forms -->
<p class="urgency-notice">
  ⚡ High demand - currently booking 3-5 days out (emergency repairs available same-day)
</p>

<!-- Add to hero section -->
<div class="availability-badge">
  <span class="pulse"></span>
  Available Today
</div>

<style>
.availability-badge {
  display: inline-flex;
  align-items: center;
  background: #10B981;
  color: white;
  padding: 6px 12px;
  border-radius: 20px;
  font-size: 14px;
}
.pulse {
  width: 8px;
  height: 8px;
  background: white;
  border-radius: 50%;
  margin-right: 8px;
  animation: pulse 2s infinite;
}
@keyframes pulse {
  0% { opacity: 1; }
  50% { opacity: 0.3; }
  100% { opacity: 1; }
}
</style>
```

---

## ✅ WEEKLY MAINTENANCE TASKS

### Every Monday
- [ ] Check Google Search Console for errors
- [ ] Review and respond to new reviews
- [ ] Create 2 Google My Business posts
- [ ] Check page speed scores
- [ ] Monitor ranking positions

### Every Friday
- [ ] Publish new blog post
- [ ] Update project gallery with new photos
- [ ] Check for broken links
- [ ] Review form submissions
- [ ] Update availability calendar

---

## 🎬 IMMEDIATE ACTION PLAN

### Today (2 Hours)
1. Add meta descriptions to top 10 pages
2. Implement canonical tags
3. Add lazy loading to images
4. Setup Google My Business posts

### Tomorrow (3 Hours)
1. Add schema markup to service pages
2. Fix mobile tap targets
3. Implement trust signals
4. Add related services sections

### This Week
1. Complete image alt text audit
2. Submit to 10 local directories
3. Create 3 new location pages
4. Publish 2 blog posts
5. Get 5 new reviews

### This Month
1. Full site speed optimization
2. 20 new pieces of content
3. Complete technical SEO fixes
4. Launch review generation campaign
5. Build 10 quality backlinks

---

*Use this checklist daily until all items are complete. Track progress in a spreadsheet and report weekly on improvements.*