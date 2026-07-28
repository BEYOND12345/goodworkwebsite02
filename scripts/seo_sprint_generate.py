#!/usr/bin/env python3
"""Good Hands SEO sprint — hubs, redirects, schema, sitemap helpers."""

from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

CSS = """
:root{--yellow-primary:#FFB800;--yellow-hover:#E6A600;--yellow-light:#FFF9E6;--charcoal:#2D3748;--dark-grey:#4A5568;--medium-grey:#718096;--light-grey:#EDF2F7;--bg-subtle:#F7FAFC;--white:#FFF;--radius:12px}
*{margin:0;padding:0;box-sizing:border-box}
body{font-family:'Nunito',sans-serif;line-height:1.65;color:var(--charcoal);background:#fff;padding-top:70px}
.container{max-width:860px;margin:0 auto;padding:0 24px}
.nav{position:fixed;top:0;left:0;right:0;height:70px;background:rgba(255,255,255,.96);border-bottom:1px solid var(--light-grey);z-index:1000;display:flex;align-items:center}
.nav-inner{max-width:1100px;width:100%;margin:0 auto;padding:0 24px;display:flex;justify-content:space-between;align-items:center}
.nav a{color:var(--charcoal);text-decoration:none;font-weight:500;margin-left:18px}
.nav .logo{font-weight:900;font-size:1.25rem;margin-left:0}
.nav .logo:hover,.nav a:hover{color:var(--yellow-primary)}
.hero{background:linear-gradient(135deg,#2D3748 0%,#4A5568 100%);color:#fff;padding:72px 0 56px;margin-bottom:40px}
.hero h1{font-size:clamp(2rem,5vw,3rem);line-height:1.15;margin-bottom:16px}
.hero p{font-size:1.15rem;opacity:.92;max-width:640px}
.meta{color:var(--medium-grey);font-size:.95rem;margin:8px 0 24px}
h2{font-size:1.6rem;margin:40px 0 14px}
h3{font-size:1.2rem;margin:28px 0 10px;color:var(--dark-grey)}
p{margin-bottom:16px;font-size:1.08rem}
ul{margin:0 0 20px 22px} li{margin-bottom:10px;font-size:1.05rem}
a{color:var(--charcoal);font-weight:700}
a:hover{color:var(--yellow-hover)}
.cta{background:var(--yellow-light);border-left:4px solid var(--yellow-primary);padding:28px;border-radius:var(--radius);margin:36px 0}
.cta a.btn{display:inline-block;background:var(--yellow-primary);padding:12px 22px;border-radius:10px;text-decoration:none;margin-right:12px;margin-top:8px}
.grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(200px,1fr));gap:12px;margin:20px 0 28px}
.card{border:1px solid var(--light-grey);border-radius:var(--radius);padding:16px;background:var(--bg-subtle);text-decoration:none;color:var(--charcoal);font-weight:600}
.card:hover{border-color:var(--yellow-primary);background:var(--yellow-light)}
.related{margin:48px 0;padding-top:28px;border-top:1px solid var(--light-grey)}
.footer{background:var(--charcoal);color:#fff;padding:40px 0;margin-top:56px}
.footer a{color:#fff}
@media(max-width:700px){.nav-links a{display:none}.hero{padding:56px 0 40px}}
"""

NAV = """
<nav class="nav"><div class="nav-inner">
  <a class="logo" href="index.html">GoodHands</a>
  <div class="nav-links">
    <a href="handyman-services-byron-bay.html">Services</a>
    <a href="areas.html">Areas</a>
    <a href="blog.html">Blog</a>
    <a href="contact.html">Contact</a>
    <a href="tel:0481457271">0481 457271</a>
  </div>
</div></nav>
"""


def page(
    *,
    slug: str,
    title: str,
    meta: str,
    h1: str,
    hero: str,
    placename: str,
    lat: str,
    lng: str,
    region: str,
    body: str,
    nearby: list[tuple[str, str]],
    schema_extra_area: list[str],
) -> str:
    nearby_html = "\n".join(
        f'<a class="card" href="{href}">{label}</a>' for href, label in nearby
    )
    areas = ", ".join(f'"{a}"' for a in schema_extra_area)
    return f"""<!DOCTYPE html>
<html lang="en-AU">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<meta name="description" content="{meta}">
<link rel="canonical" href="https://goodhandshandyman.com.au/{slug}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{meta}">
<meta property="og:type" content="website">
<meta property="og:url" content="https://goodhandshandyman.com.au/{slug}">
<meta property="og:locale" content="en_AU">
<meta name="robots" content="index, follow, max-image-preview:large">
<meta name="geo.region" content="{region}">
<meta name="geo.placename" content="{placename}">
<meta name="geo.position" content="{lat};{lng}">
<meta name="ICBM" content="{lat}, {lng}">
<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": ["HomeAndConstructionBusiness", "LocalBusiness"],
  "name": "GoodHands Handyman",
  "url": "https://goodhandshandyman.com.au/{slug}",
  "telephone": "+61481457271",
  "image": "https://goodhandshandyman.com.au/hero-handyman-working.webp",
  "address": {{
    "@type": "PostalAddress",
    "addressLocality": "Byron Bay",
    "addressRegion": "NSW",
    "postalCode": "2481",
    "addressCountry": "AU"
  }},
  "geo": {{"@type": "GeoCoordinates", "latitude": "{lat}", "longitude": "{lng}"}},
  "areaServed": [{areas}],
  "priceRange": "$$",
  "openingHoursSpecification": [{{
    "@type": "OpeningHoursSpecification",
    "dayOfWeek": ["Monday","Tuesday","Wednesday","Thursday","Friday"],
    "opens": "07:00",
    "closes": "18:00"
  }}]
}}
</script>
<link href="https://fonts.googleapis.com/css2?family=Nunito:wght@400;600;700;800&display=swap" rel="stylesheet">
<style>{CSS}</style>
</head>
<body>
{NAV}
<section class="hero"><div class="container">
  <h1>{h1}</h1>
  <p>{hero}</p>
</div></section>
<main class="container">
{body}
<div class="cta">
  <h3>Need a handyman in {placename}?</h3>
  <p>Call Dan at Good Hands — same-week for most jobs, same-day when it’s urgent.</p>
  <a class="btn" href="tel:0481457271">Call 0481 457271</a>
  <a class="btn" href="contact.html">Request a quote</a>
</div>
<div class="related">
  <h2>Nearby areas & related</h2>
  <div class="grid">
{nearby_html}
  </div>
</div>
</main>
<footer class="footer"><div class="container">
  <p><strong>GoodHands Handyman</strong> — Northern Rivers NSW &amp; Gold Coast border.</p>
  <p><a href="areas.html">All service areas</a> · <a href="handyman-services-byron-bay.html">Services</a> · <a href="tel:0481457271">0481 457271</a></p>
</div></footer>
</body>
</html>
"""


PAGES: list[dict] = []

# --- Northern Rivers pillar ---
PAGES.append(dict(
    slug="handyman-northern-rivers.html",
    title="Handyman Northern Rivers NSW | Byron to Tweed | GoodHands",
    meta="Handyman across the Northern Rivers NSW — Byron Bay, Ballina, Lismore, Tweed, hinterland. Coastal materials, same-week service. Call 0481 457271.",
    h1="Handyman for the whole Northern Rivers",
    hero="I’m Dan from GoodHands. Based in Byron Bay, I work coastal and hinterland jobs from Ballina and Lennox through Lismore, Mullumbimby, Bangalow and up to Tweed Heads — with the border / Coolangatta corridor when the job fits.",
    placename="Northern Rivers",
    lat="-28.6430",
    lng="153.6120",
    region="AU-NSW",
    schema_extra_area=["Northern Rivers", "Byron Bay", "Ballina", "Lismore", "Tweed Heads", "Mullumbimby", "Bangalow", "Lennox Head", "Ocean Shores", "Brunswick Heads", "Kingscliff", "Pottsville", "Murwillumbah"],
    nearby=[
        ("handyman-byron-bay.html", "Byron Bay"),
        ("handyman-ballina.html", "Ballina"),
        ("handyman-lismore.html", "Lismore"),
        ("handyman-tweed-heads.html", "Tweed Heads"),
        ("handyman-gold-coast.html", "Gold Coast border"),
        ("areas.html", "All areas"),
    ],
    body="""
<p>If you searched <strong>handyman Northern Rivers</strong>, you don’t need a Sydney franchise script. You need someone who knows salt air eats hinges, flood country needs different materials, and a property manager in Ballina won’t wait until “next available month.”</p>
<h2>Where I work across the Northern Rivers</h2>
<p>Primary coverage is the Byron–Ballina–Lismore–Tweed triangle and the towns between. Hinterland jobs (Bangalow, Mullumbimby, Murwillumbah) and Tweed Coast towns (Kingscliff, Pottsville, Brunswick Heads, Ocean Shores, South Golden Beach) are regular weeks for me.</p>
<div class="grid">
<a class="card" href="handyman-byron-bay.html">Byron Bay</a>
<a class="card" href="handyman-ballina.html">Ballina</a>
<a class="card" href="handyman-lismore.html">Lismore</a>
<a class="card" href="handyman-mullumbimby.html">Mullumbimby</a>
<a class="card" href="handyman-lennox-head.html">Lennox Head</a>
<a class="card" href="handyman-bangalow.html">Bangalow</a>
<a class="card" href="handyman-tweed-heads.html">Tweed Heads</a>
<a class="card" href="handyman-brunswick-heads.html">Brunswick Heads</a>
<a class="card" href="handyman-kingscliff.html">Kingscliff</a>
<a class="card" href="handyman-pottsville.html">Pottsville</a>
<a class="card" href="handyman-murwillumbah.html">Murwillumbah</a>
<a class="card" href="handyman-ocean-shores.html">Ocean Shores</a>
</div>
<h2>What Northern Rivers properties actually break</h2>
<ul>
<li><strong>Coastal:</strong> swollen kitchen doors, rusted hardware, grey decks, gutters full of salt grit</li>
<li><strong>Flood / river towns:</strong> moisture damage, doors out of square, outdoor timber that never fully dries</li>
<li><strong>Holiday rentals:</strong> turnover fixes before the next guest — locks, screens, deck rails, tapware</li>
<li><strong>Storm season:</strong> fences, flyscreens, emergency make-safe</li>
</ul>
<h2>Services I bring region-wide</h2>
<p>Kitchen and door repairs, deck restoration with coastal-grade products, gutter cleaning, fencing, Airbnb turnaround, emergency callouts, and general carpentry. See the full list on the <a href="handyman-services-byron-bay.html">services hub</a>.</p>
<h2>How quoting works on site</h2>
<p>I still walk the job. I don’t invent prices from the kerb. When the scope is clear I send the quote while we’re both looking at the problem — then invoice when the work’s done. That habit beats “I’ll email tonight” across every town in this region.</p>
""",
))

# --- Gold Coast hub ---
PAGES.append(dict(
    slug="handyman-gold-coast.html",
    title="Handyman Gold Coast Border | Coolangatta & Tweed | GoodHands",
    meta="Handyman for the Gold Coast border — Coolangatta, Tweed Heads South corridor. Northern Rivers–based, coastal repairs done properly. Call 0481 457271.",
    h1="Handyman for the Gold Coast border",
    hero="GoodHands is based in Byron Bay / Northern Rivers. I take Gold Coast border work — Coolangatta and the Tweed Heads South corridor — when travel and timing make sense. Central/southern GC only by arrangement.",
    placename="Gold Coast",
    lat="-28.1670",
    lng="153.5370",
    region="AU-QLD",
    schema_extra_area=["Gold Coast", "Coolangatta", "Tweed Heads", "Tweed Heads South", "Bilinga", "Kirra", "Rainbow Bay"],
    nearby=[
        ("handyman-coolangatta.html", "Coolangatta"),
        ("handyman-tweed-heads.html", "Tweed Heads"),
        ("handyman-kingscliff.html", "Kingscliff"),
        ("handyman-northern-rivers.html", "Northern Rivers"),
        ("contact.html", "Get a quote"),
    ],
    body="""
<p><strong>Straight talk:</strong> I’m not a Robina-to-Southport every-day Gold Coast franchise. I’m a Northern Rivers handyman who regularly works the <strong>border corridor</strong> — Coolangatta, Tweed Heads, and nearby coastal stock. If you’re further into the GC (Burleigh, Surfers, Southport, Robina), ask first — I’ll say yes only when I can do the job properly on time.</p>
<h2>Why border jobs make sense</h2>
<p>Same coastal problems as Byron: salt air, humidity-swollen doors, holiday rental turnarounds, decks that need marine-minded products. The border isn’t a different planet — it’s a short run from Tweed work I already do.</p>
<h2>Gold Coast services I prioritise</h2>
<ul>
<li>Kitchen door / hinge / latch repairs in humid units and houses</li>
<li>Deck and outdoor timber maintenance near the beach</li>
<li>Airbnb / short-stay make-ready between guests</li>
<li>Emergency make-safe (doors, rails, fence lean) when I’m in the corridor</li>
<li>General carpentry and property maintenance</li>
</ul>
<h2>Towns & pages</h2>
<div class="grid">
<a class="card" href="handyman-coolangatta.html">Coolangatta handyman</a>
<a class="card" href="handyman-tweed-heads.html">Tweed Heads</a>
<a class="card" href="handyman-kingscliff.html">Kingscliff</a>
<a class="card" href="airbnb-maintenance-coolangatta.html">Coolangatta Airbnb fixes</a>
</div>
<p>For broader NSW coverage see <a href="handyman-northern-rivers.html">handyman Northern Rivers</a>.</p>
""",
))

TOWNS = [
    dict(
        slug="handyman-coolangatta.html",
        title="Handyman Coolangatta QLD | Border Coastal Repairs | GoodHands",
        meta="Handyman Coolangatta — kitchen doors, decks, Airbnb turnarounds on the QLD/NSW border. Call Dan 0481 457271.",
        h1="Handyman Coolangatta",
        hero="Coastal units and houses on the point — humidity, salt, short-stay turnovers. I work Coolangatta from the Northern Rivers / Tweed side of the border.",
        placename="Coolangatta", lat="-28.1690", lng="153.5350", region="AU-QLD",
        areas=["Coolangatta", "Kirra", "Bilinga", "Rainbow Bay", "Tweed Heads"],
        nearby=[("handyman-gold-coast.html", "Gold Coast hub"), ("handyman-tweed-heads.html", "Tweed Heads"), ("handyman-kingscliff.html", "Kingscliff")],
        body="""
<p>Coolangatta jobs look a lot like Byron coastal work: doors that stick after rain, hardware that rusts early, decks that grey fast, and Airbnb managers who need it fixed before the next check-in.</p>
<h2>Common Coolangatta jobs</h2>
<ul>
<li>Kitchen cupboard doors and hinges in humid apartments</li>
<li>Latch and lock fixes for holiday lets</li>
<li>Deck rail / board make-safe near the beach</li>
<li>Flyscreens and minor storm damage</li>
</ul>
<p>See also <a href="airbnb-maintenance-coolangatta.html">Airbnb maintenance Coolangatta</a> and the wider <a href="handyman-gold-coast.html">Gold Coast border</a> page.</p>
""",
    ),
    dict(
        slug="handyman-brunswick-heads.html",
        title="Handyman Brunswick Heads NSW | Coastal Repairs | GoodHands",
        meta="Handyman Brunswick Heads — decks, kitchens, holiday rentals, salt-air repairs. Same-week service. Call 0481 457271.",
        h1="Handyman Brunswick Heads",
        hero="River-and-coast town with salt air and holiday traffic. I cover Brunswick Heads alongside Ocean Shores and Byron.",
        placename="Brunswick Heads", lat="-28.5400", lng="153.5500", region="AU-NSW",
        areas=["Brunswick Heads", "Ocean Shores", "South Golden Beach", "New Brighton"],
        nearby=[("handyman-ocean-shores.html", "Ocean Shores"), ("handyman-south-golden-beach.html", "South Golden Beach"), ("handyman-byron-bay.html", "Byron Bay")],
        body="""
<p>Brunswick Heads properties cop coastal moisture and busy holiday seasons. I handle the same practical work I do across the Byron shire — kitchens, decks, screens, fences, and quick rental turnarounds.</p>
<h2>Local notes</h2>
<ul>
<li>Salt air: marine-minded fixings and oils where it matters</li>
<li>Holiday lets: fix it between guests, don’t leave it for Sunday admin</li>
<li>Easy pairing with Ocean Shores / South Golden Beach jobs the same day</li>
</ul>
""",
    ),
    dict(
        slug="handyman-kingscliff.html",
        title="Handyman Kingscliff NSW | Tweed Coast | GoodHands",
        meta="Handyman Kingscliff — coastal homes and holiday rentals on the Tweed Coast. Decks, kitchens, emergency fixes. 0481 457271.",
        h1="Handyman Kingscliff",
        hero="Tweed Coast beach town — salt, wind, and short-stay stock. Regular corridor for me between Tweed Heads and Pottsville.",
        placename="Kingscliff", lat="-28.2550", lng="153.5780", region="AU-NSW",
        areas=["Kingscliff", "Cabarita Beach", "Bogangar", "Tweed Heads"],
        nearby=[("handyman-tweed-heads.html", "Tweed Heads"), ("handyman-pottsville.html", "Pottsville"), ("handyman-coolangatta.html", "Coolangatta")],
        body="""
<p>Kingscliff sits in the sweet spot of my Tweed Coast run. Coastal decks, kitchen humidity problems, and Airbnb turnarounds are the usual brief.</p>
<h2>What I get called for</h2>
<ul>
<li>Deck boards, rails, and coastal oiling advice</li>
<li>Doors and cupboards that swell in humidity</li>
<li>Fence and gate repairs after wind</li>
<li>Guest-ready fixes for holiday managers</li>
</ul>
""",
    ),
    dict(
        slug="handyman-pottsville.html",
        title="Handyman Pottsville NSW | Tweed Coast | GoodHands",
        meta="Handyman Pottsville NSW — kitchens, decks, fences, rental maintenance on the Tweed Coast. Call 0481 457271.",
        h1="Handyman Pottsville",
        hero="Growing Tweed Coast town between Kingscliff and Brunswick. I cover Pottsville on the same coastal run as Tweed Heads work.",
        placename="Pottsville", lat="-28.3850", lng="153.5660", region="AU-NSW",
        areas=["Pottsville", "Hastings Point", "Cabarita Beach", "Kingscliff"],
        nearby=[("handyman-kingscliff.html", "Kingscliff"), ("handyman-brunswick-heads.html", "Brunswick Heads"), ("handyman-tweed-heads.html", "Tweed Heads")],
        body="""
<p>Pottsville is part of the Tweed Coast corridor I already service. Same coastal materials thinking, same on-site quoting habit, same-week for most standard jobs.</p>
<h2>Typical Pottsville work</h2>
<ul>
<li>General handyman and carpentry</li>
<li>Kitchen door and hinge repairs</li>
<li>Outdoor timber and fence repairs</li>
<li>Property maintenance for owners who aren’t always on site</li>
</ul>
""",
    ),
    dict(
        slug="handyman-murwillumbah.html",
        title="Handyman Murwillumbah NSW | Hinterland | GoodHands",
        meta="Handyman Murwillumbah — hinterland homes, moisture issues, general repairs across the Tweed Valley. Call 0481 457271.",
        h1="Handyman Murwillumbah",
        hero="Tweed Valley hinterland — different moisture profile to the beach, same need for clear quotes and reliable turn-up times.",
        placename="Murwillumbah", lat="-28.3280", lng="153.3960", region="AU-NSW",
        areas=["Murwillumbah", "Tweed Valley", "Uki", "Condong"],
        nearby=[("handyman-tweed-heads.html", "Tweed Heads"), ("handyman-lismore.html", "Lismore"), ("handyman-northern-rivers.html", "Northern Rivers")],
        body="""
<p>Murwillumbah jobs are often hinterland moisture, older timber, and practical repairs for homes that aren’t beachfront but still live in a wet climate.</p>
<h2>Common calls</h2>
<ul>
<li>Doors out of square after wet seasons</li>
<li>Timber repairs and general carpentry</li>
<li>Outdoor structures and fencing</li>
<li>Maintenance for owners managing from elsewhere</li>
</ul>
""",
    ),
    dict(
        slug="handyman-casino.html",
        title="Handyman Casino NSW | Richmond Valley | GoodHands",
        meta="Handyman Casino NSW — practical repairs for Richmond Valley homes. Travel from Northern Rivers base. Call 0481 457271.",
        h1="Handyman Casino",
        hero="Richmond Valley town on my inland run with Lismore. I take Casino jobs when travel stacks sensibly with other Northern Rivers work.",
        placename="Casino", lat="-28.8650", lng="153.0480", region="AU-NSW",
        areas=["Casino", "Richmond Valley", "Lismore"],
        nearby=[("handyman-lismore.html", "Lismore"), ("handyman-ballina.html", "Ballina"), ("handyman-northern-rivers.html", "Northern Rivers")],
        body="""
<p>Casino isn’t a daily stop like Byron — but it’s part of the Northern Rivers map I cover. If you’ve been stuck waiting on “someone from town,” call and I’ll tell you honestly when I can be there.</p>
<h2>Jobs that make sense here</h2>
<ul>
<li>General handyman and carpentry</li>
<li>Doors, kitchens, outdoor timber</li>
<li>Property maintenance for local owners</li>
</ul>
""",
    ),
]

for t in TOWNS:
    PAGES.append(dict(
        slug=t["slug"],
        title=t["title"],
        meta=t["meta"],
        h1=t["h1"],
        hero=t["hero"],
        placename=t["placename"],
        lat=t["lat"],
        lng=t["lng"],
        region=t["region"],
        schema_extra_area=t["areas"],
        nearby=t["nearby"] + [("areas.html", "All areas"), ("contact.html", "Contact")],
        body=t["body"],
    ))

# Service × town expansions
SERVICE_PAGES = [
    dict(
        slug="deck-restoration-ballina.html",
        title="Deck Restoration Ballina | Coastal Timber | GoodHands",
        meta="Deck restoration Ballina NSW — sanding, boards, coastal oils. Same thinking as Byron salt air, local to the Richmond River. 0481 457271.",
        h1="Deck restoration in Ballina",
        hero="Ballina decks get river humidity and coastal air. I restore and maintain outdoor timber with products that last here — not generic inland advice.",
        placename="Ballina", lat="-28.8669", lng="153.5635", region="AU-NSW",
        areas=["Ballina", "East Ballina", "West Ballina", "Lennox Head"],
        nearby=[("deck-restoration-byron-bay.html", "Byron deck restoration"), ("handyman-ballina.html", "Ballina handyman"), ("gutter-cleaning-ballina.html", "Ballina gutters")],
        body="""
<p>If your Ballina deck is grey, splintery, or soft in spots, the fix is the same discipline I use on Byron coastal decks: clean properly, replace what’s gone, oil with something that handles moisture.</p>
<ul>
<li>Board replacement and rail repairs</li>
<li>Sanding and coastal oil systems</li>
<li>Honest call on repair vs replace</li>
</ul>
<p>Also see <a href="deck-restoration.html">Northern Rivers deck restoration</a> and <a href="handyman-ballina.html">handyman Ballina</a>.</p>
""",
    ),
    dict(
        slug="deck-restoration-tweed-heads.html",
        title="Deck Restoration Tweed Heads | Border Coastal | GoodHands",
        meta="Deck restoration Tweed Heads — coastal timber, rails, oils for the NSW/QLD border. Call 0481 457271.",
        h1="Deck restoration Tweed Heads",
        hero="Border coastal decks take wind and salt. I service Tweed Heads outdoor timber on the same run as Kingscliff and Coolangatta work.",
        placename="Tweed Heads", lat="-28.1770", lng="153.5410", region="AU-NSW",
        areas=["Tweed Heads", "Tweed Heads South", "Banora Point", "Coolangatta"],
        nearby=[("handyman-tweed-heads.html", "Tweed handyman"), ("deck-restoration-byron-bay.html", "Byron decks"), ("handyman-coolangatta.html", "Coolangatta")],
        body="""
<p>Tweed Heads decks fail for the same reasons as Byron beachfront timber — salt, UV, and cheap coatings. I inspect structure, replace soft boards, and finish with coastal-minded products.</p>
""",
    ),
    dict(
        slug="deck-restoration-lennox-head.html",
        title="Deck Restoration Lennox Head | Salt Air | GoodHands",
        meta="Deck restoration Lennox Head — coastal decks, rails, marine-minded oils. Call 0481 457271.",
        h1="Deck restoration Lennox Head",
        hero="Exposed coastal decks above the beach — high UV and salt. Regular work for me alongside Ballina and Byron jobs.",
        placename="Lennox Head", lat="-28.8120", lng="153.5930", region="AU-NSW",
        areas=["Lennox Head", "Skennars Head", "Ballina"],
        nearby=[("handyman-lennox-head.html", "Lennox handyman"), ("deck-restoration-ballina.html", "Ballina decks"), ("deck-restoration-byron-bay.html", "Byron decks")],
        body="""
<p>Lennox decks cop more wind and UV than hinterland timber. I quote on site after I’ve walked the boards — no driveway guesses.</p>
""",
    ),
    dict(
        slug="airbnb-maintenance-tweed-heads.html",
        title="Airbnb Maintenance Tweed Heads | Guest-Ready Fixes | GoodHands",
        meta="Airbnb maintenance Tweed Heads — locks, screens, decks, kitchens between guests. Fast turnaround. 0481 457271.",
        h1="Airbnb maintenance Tweed Heads",
        hero="Short-stay stock on the border needs same-day / same-week fixes. I handle guest-ready repairs across Tweed Heads and nearby coast.",
        placename="Tweed Heads", lat="-28.1770", lng="153.5410", region="AU-NSW",
        areas=["Tweed Heads", "Tweed Heads South", "Coolangatta", "Kingscliff"],
        nearby=[("airbnb-maintenance-byron-bay-fast-turnaround.html", "Byron Airbnb"), ("airbnb-maintenance-coolangatta.html", "Coolangatta Airbnb"), ("handyman-tweed-heads.html", "Tweed handyman")],
        body="""
<p>Property managers don’t need a lecture — they need the door latching, the screen fixed, and the rail safe before the next guest. That’s the Tweed Airbnb brief.</p>
""",
    ),
    dict(
        slug="airbnb-maintenance-coolangatta.html",
        title="Airbnb Maintenance Coolangatta | Turnaround Repairs | GoodHands",
        meta="Airbnb maintenance Coolangatta — fast guest-ready handyman fixes on the Gold Coast border. Call 0481 457271.",
        h1="Airbnb maintenance Coolangatta",
        hero="Border holiday units turn over hard. I do practical make-ready repairs when I’m on the Coolangatta / Tweed run.",
        placename="Coolangatta", lat="-28.1690", lng="153.5350", region="AU-QLD",
        areas=["Coolangatta", "Kirra", "Bilinga", "Tweed Heads"],
        nearby=[("handyman-coolangatta.html", "Coolangatta handyman"), ("airbnb-maintenance-tweed-heads.html", "Tweed Airbnb"), ("handyman-gold-coast.html", "Gold Coast hub")],
        body="""
<p>Coolangatta short-stays break the same things everywhere: doors, screens, tapware, furniture assembly leftovers, balcony rails. I quote fast and get it guest-ready.</p>
""",
    ),
    dict(
        slug="gutter-cleaning-byron-bay.html",
        title="Gutter Cleaning Byron Bay | Leaf & Salt Build-Up | GoodHands",
        meta="Gutter cleaning Byron Bay — leaf litter, salt grit, overflow fixes. Protect eaves and decks. Call 0481 457271.",
        h1="Gutter cleaning Byron Bay",
        hero="Coastal gutters clog with leaf litter and salt grit. I clear them properly and flag rust or fall issues while I’m up there.",
        placename="Byron Bay", lat="-28.6430", lng="153.6120", region="AU-NSW",
        areas=["Byron Bay", "Suffolk Park", "Belongil", "Ewingsdale"],
        nearby=[("gutter-cleaning-ballina.html", "Ballina gutters"), ("handyman-byron-bay.html", "Byron handyman"), ("deck-restoration-byron-bay.html", "Byron decks")],
        body="""
<p>Byron gutters aren’t optional maintenance. Overflow stains walls, softens eaves, and dumps water onto decks. I clean and report what I find — no upsell theatre.</p>
""",
    ),
]

for t in SERVICE_PAGES:
    PAGES.append(dict(
        slug=t["slug"],
        title=t["title"],
        meta=t["meta"],
        h1=t["h1"],
        hero=t["hero"],
        placename=t["placename"],
        lat=t["lat"],
        lng=t["lng"],
        region=t["region"],
        schema_extra_area=t["areas"],
        nearby=t["nearby"] + [("contact.html", "Contact")],
        body=t["body"],
    ))


def write_pages() -> None:
    for p in PAGES:
        html = page(
            slug=p["slug"],
            title=p["title"],
            meta=p["meta"],
            h1=p["h1"],
            hero=p["hero"],
            placename=p["placename"],
            lat=p["lat"],
            lng=p["lng"],
            region=p["region"],
            body=p["body"],
            nearby=p["nearby"],
            schema_extra_area=p["schema_extra_area"],
        )
        (ROOT / p["slug"]).write_text(html, encoding="utf-8")
        print("wrote", p["slug"])


REDIRECTS = """# Force www to non-www
https://www.goodhandshandyman.com.au/* https://goodhandshandyman.com.au/:splat 301!

# Stub / soft-404 cleanups (meta-refresh pages → real 301s)
/services.html /handyman-services-byron-bay.html 301
/get-quote.html /contact.html 301
/about-dan-byron-bay-handyman.html /about.html 301
/emergency-handyman-byron-bay.html /emergency-repairs.html 301
/emergency-handyman-ballina.html /emergency-repairs.html 301
/emergency-handyman-lismore.html /emergency-repairs.html 301
/emergency-door-repair-byron-bay.html /emergency-door-repairs-byron-bay.html 301

# Legacy GSC / old URLs
/handyman-quote-northern-rivers.html /contact.html 301
/fly-screen-repairs.html /fly-screen-repairs-byron-bay.html 301
/latest-updates.html /blog.html 301
/emergency-handyman-bangalow.html /handyman-bangalow.html 301
/emergency-handyman-mullumbimby.html /handyman-mullumbimby.html 301
/emergency-handyman-tweed-heads.html /handyman-tweed-heads.html 301
/bathroom-repairs-byron-bay.html /handyman-services-byron-bay.html 301
/fence-repairs-northern-rivers.html /fence-repairs-ballina.html 301
/painting-services-northern-rivers.html /painting-services.html 301
/how-much-does-handyman-cost-byron-bay-quote-guide.html /how-much-does-handyman-cost-byron-bay-pricing-guide.html 301
"""


def write_redirects() -> None:
    (ROOT / "_redirects").write_text(REDIRECTS, encoding="utf-8")
    print("wrote _redirects")


if __name__ == "__main__":
    write_pages()
    write_redirects()
    print("total pages", len(PAGES))
