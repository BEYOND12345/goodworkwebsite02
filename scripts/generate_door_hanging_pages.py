#!/usr/bin/env python3
"""Generate door hanging / fitting / lock pages for GoodHands."""

from __future__ import annotations

from datetime import date
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
    <a href="door-hanging-fitting-northern-rivers.html">Door hanging</a>
    <a href="handyman-services-byron-bay.html">Services</a>
    <a href="areas.html">Areas</a>
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
    body: str,
    nearby: list[tuple[str, str]],
    area_served: list[str],
    services: list[str],
) -> str:
    nearby_html = "\n".join(
        f'<a class="card" href="{href}">{label}</a>' for href, label in nearby
    )
    areas = ", ".join(f'"{a}"' for a in area_served)
    svc = ", ".join(f'"{s}"' for s in services)
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
<meta name="geo.region" content="AU-NSW">
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
  "image": "https://goodhandshandyman.com.au/door-repair-before-after.png",
  "address": {{
    "@type": "PostalAddress",
    "addressLocality": "Byron Bay",
    "addressRegion": "NSW",
    "postalCode": "2481",
    "addressCountry": "AU"
  }},
  "geo": {{"@type": "GeoCoordinates", "latitude": "{lat}", "longitude": "{lng}"}},
  "areaServed": [{areas}],
  "serviceType": [{svc}],
  "priceRange": "$$"
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
  <h3>Need doors hung or locks fitted in {placename}?</h3>
  <p>Call Dan — same-week for most door jobs, same-day when a door or lock has failed.</p>
  <a class="btn" href="tel:0481457271">Call 0481 457271</a>
  <a class="btn" href="contact.html">Request a quote</a>
</div>
<div class="related">
  <h2>Related door services &amp; towns</h2>
  <div class="grid">
{nearby_html}
  </div>
</div>
</main>
<footer class="footer"><div class="container">
  <p><strong>GoodHands Handyman</strong> — Byron Bay home base · door hanging · locks · Northern Rivers to Tweed.</p>
  <p><a href="door-hanging-fitting-northern-rivers.html">Door hanging hub</a> · <a href="areas.html">All areas</a> · <a href="tel:0481457271">0481 457271</a></p>
</div></footer>
</body>
</html>
"""


TOWNS = [
    {
        "slug": "door-hanging-byron-bay.html",
        "town": "Byron Bay",
        "title": "Door Hanging Byron Bay | Fit, Replace & Lock Fitting | GoodHands",
        "meta": "Door hanging Byron Bay — hang internal doors, replace door leaves, fit handles and locks. Coastal humidity know-how. Call 0481 457271.",
        "h1": "Door hanging in Byron Bay",
        "hero": "Need doors hung or replaced in Byron Bay? I hang internal doors, replace damaged leaves, and fit handles and locks — trimmed and adjusted so they close properly in coastal humidity.",
        "lat": "-28.6474",
        "lng": "153.6020",
        "local_note": "Byron Bay doors swell and stick in summer humidity. When you’re hanging a new door or replacing an old one, sealing edges and setting clearances for coastal air matters as much as getting the hinges square.",
        "areas": ["Byron Bay", "Suffolk Park", "Belongil", "Bangalow"],
        "nearby": [
            ("door-hanging-fitting-northern-rivers.html", "Door hanging hub"),
            ("door-hanging-ballina.html", "Hang doors Ballina"),
            ("door-repairs-byron-bay-northern-rivers.html", "Door repairs Byron"),
            ("door-lock-replacement-northern-rivers.html", "Lock & handle fitting"),
            ("handyman-byron-bay.html", "Handyman Byron Bay"),
            ("emergency-door-repairs-byron-bay.html", "Emergency doors"),
        ],
    },
    {
        "slug": "door-hanging-ballina.html",
        "town": "Ballina",
        "title": "Door Hanging Ballina | Internal Doors & Lock Fitting | GoodHands",
        "meta": "Door hanging Ballina — hang and replace internal doors, fit handles and locks. River/coastal properties. Same-week. Call 0481 457271.",
        "h1": "Door hanging in Ballina",
        "hero": "Hang new doors, replace old ones, and fit locks or handles across Ballina — East Ballina, West Ballina, and nearby. Practical carpentry, clear quote, same-week for most jobs.",
        "lat": "-28.8667",
        "lng": "153.5667",
        "local_note": "Ballina properties get river moisture and salt air. Doors that were “fine in Sydney” often need trimming and better latch alignment once they’ve been in a Ballina house for a season.",
        "areas": ["Ballina", "East Ballina", "West Ballina", "Lennox Head"],
        "nearby": [
            ("door-hanging-fitting-northern-rivers.html", "Door hanging hub"),
            ("door-hanging-byron-bay.html", "Hang doors Byron"),
            ("door-hanging-lennox-head.html", "Hang doors Lennox"),
            ("door-repairs-ballina-lismore.html", "Door repairs Ballina"),
            ("handyman-ballina.html", "Handyman Ballina"),
            ("door-lock-replacement-northern-rivers.html", "Lock fitting"),
        ],
    },
    {
        "slug": "door-hanging-tweed-heads.html",
        "town": "Tweed Heads",
        "title": "Door Hanging Tweed Heads | Replace Doors & Fit Locks | GoodHands",
        "meta": "Door hanging Tweed Heads — hang internal doors, replace leaves, fit handles and locks. Units and houses. Call 0481 457271.",
        "h1": "Door hanging in Tweed Heads",
        "hero": "Door hanging and replacement for Tweed Heads homes and units — new internal doors, hardware fitting, and lock swaps. Based in Byron, regularly working the Tweed corridor.",
        "lat": "-28.1780",
        "lng": "153.5410",
        "local_note": "Tweed Heads has a mix of houses and apartments. Unit doors often need careful hinge and latch work without damaging surrounds — I’m used to working cleanly in occupied places.",
        "areas": ["Tweed Heads", "Tweed Heads South", "Banora Point", "Coolangatta"],
        "nearby": [
            ("door-hanging-fitting-northern-rivers.html", "Door hanging hub"),
            ("door-hanging-kingscliff.html", "Hang doors Kingscliff"),
            ("door-repairs-tweed-heads.html", "Door repairs Tweed"),
            ("handyman-tweed-heads.html", "Handyman Tweed"),
            ("handyman-coolangatta.html", "Coolangatta"),
            ("door-lock-replacement-northern-rivers.html", "Lock fitting"),
        ],
    },
    {
        "slug": "door-hanging-lennox-head.html",
        "town": "Lennox Head",
        "title": "Door Hanging Lennox Head | Fit & Replace Doors | GoodHands",
        "meta": "Door hanging Lennox Head — hang internal doors, replace damaged doors, fit handles and locks. Coastal homes. Call 0481 457271.",
        "h1": "Door hanging in Lennox Head",
        "hero": "Hang or replace doors in Lennox Head coastal homes. Trim, hinge, latch, and adjust — plus handle and lock fitting when you’re refreshing bedrooms or rentals.",
        "lat": "-28.8000",
        "lng": "153.6000",
        "local_note": "Exposed coastal homes in Lennox see swollen timber and corroded hardware faster. New doors get sealed and set with clearances that leave room for humidity movement.",
        "areas": ["Lennox Head", "Skennars Head", "Ballina"],
        "nearby": [
            ("door-hanging-fitting-northern-rivers.html", "Door hanging hub"),
            ("door-hanging-ballina.html", "Hang doors Ballina"),
            ("door-hanging-byron-bay.html", "Hang doors Byron"),
            ("handyman-lennox-head.html", "Handyman Lennox"),
            ("sliding-door-repair-northern-rivers.html", "Sliding doors"),
            ("door-lock-replacement-northern-rivers.html", "Lock fitting"),
        ],
    },
    {
        "slug": "door-hanging-kingscliff.html",
        "town": "Kingscliff",
        "title": "Door Hanging Kingscliff | Internal Doors & Locks | GoodHands",
        "meta": "Door hanging Kingscliff — hang and replace internal doors, fit handles and locks on the Tweed Coast. Call 0481 457271.",
        "h1": "Door hanging in Kingscliff",
        "hero": "Door hanging and lock fitting for Kingscliff and nearby Tweed Coast homes — new internal doors hung properly, old leaves replaced, hardware fitted and adjusted.",
        "lat": "-28.2560",
        "lng": "153.5780",
        "local_note": "Kingscliff holiday homes and rentals often need a few doors done in one visit before guests arrive. Bundle jobs and I’ll quote the lot clearly.",
        "areas": ["Kingscliff", "Casuarina", "Cabarita Beach", "Pottsville"],
        "nearby": [
            ("door-hanging-fitting-northern-rivers.html", "Door hanging hub"),
            ("door-hanging-tweed-heads.html", "Hang doors Tweed"),
            ("handyman-kingscliff.html", "Handyman Kingscliff"),
            ("handyman-pottsville.html", "Pottsville"),
            ("door-lock-replacement-northern-rivers.html", "Lock fitting"),
            ("airbnb-maintenance.html", "Airbnb maintenance"),
        ],
    },
]


def town_body(t: dict) -> str:
    return f"""
<p>{t['local_note']}</p>
<h2>Door jobs I do in {t['town']}</h2>
<ul>
<li><strong>Hang new internal doors</strong> — measure, trim, hinge, bore for latch/handle, adjust</li>
<li><strong>Replace damaged door leaves</strong> in existing frames that are still sound</li>
<li><strong>Rehang doors</strong> that sag, rub, or won’t latch</li>
<li><strong>Fit handles, privacy sets and locks</strong> (like-for-like and standard upgrades)</li>
<li><strong>Bundle multi-door jobs</strong> for renovations and rental turnovers</li>
</ul>
<h2>What I don’t pretend to be</h2>
<p>I’m a handyman/carpenter for hanging and fitting — not a locksmith for restricted rekeys, lockouts, or high-security master systems. Fire doors and structural opening changes need a specialist; I’ll tell you straight if that’s the case.</p>
<h2>Related</h2>
<p>Already have a door that sticks or is broken? See <a href="door-repairs-byron-bay-northern-rivers.html">door repairs</a> or the full corridor hub for <a href="door-hanging-fitting-northern-rivers.html">door hanging &amp; fitting</a>.</p>
"""


def pillar_body() -> str:
    town_cards = "\n".join(
        f'<a class="card" href="{t["slug"]}">Hang doors {t["town"]}</a>' for t in TOWNS
    )
    return f"""
<p>If you searched <strong>hang a door</strong>, <strong>door fitting</strong>, or <strong>door installation</strong>, you’re in the right place. GoodHands is a Byron Bay–based handyman service that hangs doors, replaces door leaves, and fits handles and locks across the Byron Bay to Tweed corridor.</p>

<h2>What’s included in door hanging &amp; fitting</h2>
<ul>
<li>Hang new internal doors into existing frames</li>
<li>Replace old or damaged door leaves</li>
<li>Trim for height/width, mortise hinges, bore for latch and handle</li>
<li>Fit passage sets, privacy sets, and standard locksets</li>
<li>Adjust for smooth close and clean latch — including coastal swollen openings</li>
<li>Multi-door packages for renovations, rentals, and Airbnb turnovers</li>
</ul>

<h2>Typical jobs people book</h2>
<ul>
<li>“Hang three bedroom doors — doors and handles supplied”</li>
<li>“Replace the laundry door and fit a privacy set”</li>
<li>“New internal doors after painting — bore and hang”</li>
<li>“Door won’t latch after humidity — rehang / adjust / replace if needed”</li>
<li>“Fit new handles and locks on rental turnover”</li>
</ul>

<h2>Rough guide on cost</h2>
<p>Simple adjustments and handle/lock swaps are usually the smaller end. Hanging a new internal door in an existing frame is typically in the <strong>$150–$350 labour</strong> range depending on trim, hardware, and access. Multi-door jobs are more efficient per door. I quote on site before I start.</p>

<h2>Where I cover</h2>
<p>Byron Bay home base, then Ballina, Lennox Head, Tweed Heads, Kingscliff, and the towns between — same corridor as the rest of GoodHands.</p>
<div class="grid">
{town_cards}
<a class="card" href="door-lock-replacement-northern-rivers.html">Lock &amp; handle fitting</a>
<a class="card" href="door-repairs-byron-bay-northern-rivers.html">Door repairs</a>
<a class="card" href="sliding-door-repair-northern-rivers.html">Sliding doors</a>
<a class="card" href="emergency-door-repairs-byron-bay.html">Emergency doors</a>
</div>

<h2>Handyman vs locksmith vs carpenter</h2>
<p>For hanging internal doors and fitting standard hardware, a skilled handyman/carpenter is the right call. Call a locksmith for restricted keys, rekey systems, and lockouts. Call a builder for new openings or structural frame work. I’ll tell you which bucket you’re in.</p>

<h2>Coastal doors need coastal clearances</h2>
<p>Humidity around Byron, Ballina and the Tweed Coast makes timber move. I hang and seal with that in mind so you’re not back planing the same door every February.</p>
"""


def main() -> None:
    services = [
        "Door hanging",
        "Door fitting",
        "Door installation",
        "Door replacement",
        "Lock fitting",
        "Door handle installation",
    ]

    pillar = page(
        slug="door-hanging-fitting-northern-rivers.html",
        title="Door Hanging & Fitting Northern Rivers | Replace Doors & Locks | GoodHands",
        meta="Door hanging and fitting from Byron Bay to Tweed — hang internal doors, replace leaves, fit handles and locks. Call 0481 457271.",
        h1="Door hanging, replacement & lock fitting",
        hero="Hang new doors, replace damaged ones, and fit handles or locks across the Byron Bay to Tweed corridor. Trim, hinge, latch, adjust — done properly for coastal homes.",
        placename="Northern Rivers",
        lat="-28.6430",
        lng="153.6120",
        body=pillar_body(),
        nearby=[
            ("door-hanging-byron-bay.html", "Byron Bay"),
            ("door-hanging-ballina.html", "Ballina"),
            ("door-hanging-tweed-heads.html", "Tweed Heads"),
            ("door-hanging-lennox-head.html", "Lennox Head"),
            ("door-hanging-kingscliff.html", "Kingscliff"),
            ("door-lock-replacement-northern-rivers.html", "Locks & handles"),
            ("door-repairs-byron-bay-northern-rivers.html", "Door repairs"),
            ("handyman-byron-to-tweed-corridor.html", "Corridor map"),
        ],
        area_served=[
            "Byron Bay",
            "Ballina",
            "Lennox Head",
            "Tweed Heads",
            "Kingscliff",
            "Northern Rivers",
        ],
        services=services,
    )
    (ROOT / "door-hanging-fitting-northern-rivers.html").write_text(pillar)
    print("wrote pillar")

    for t in TOWNS:
        html = page(
            slug=t["slug"],
            title=t["title"],
            meta=t["meta"],
            h1=t["h1"],
            hero=t["hero"],
            placename=t["town"],
            lat=t["lat"],
            lng=t["lng"],
            body=town_body(t),
            nearby=t["nearby"],
            area_served=t["areas"],
            services=services,
        )
        (ROOT / t["slug"]).write_text(html)
        print("wrote", t["slug"])

    # Sitemap entries
    sm_path = ROOT / "sitemap.xml"
    sm = sm_path.read_text()
    today = date.today().isoformat()
    new_slugs = ["door-hanging-fitting-northern-rivers.html"] + [t["slug"] for t in TOWNS]
    for slug in new_slugs:
        if slug in sm:
            continue
        entry = f"""
<url>
  <loc>https://goodhandshandyman.com.au/{slug}</loc>
  <lastmod>{today}</lastmod>
  <changefreq>weekly</changefreq>
  <priority>0.9</priority>
</url>
"""
        sm = sm.replace("</urlset>", entry + "\n</urlset>")
    sm_path.write_text(sm)
    print("sitemap updated")


if __name__ == "__main__":
    main()
