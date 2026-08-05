#!/usr/bin/env python3
"""Generate IKEA / flatpack assembly pages for GoodHands."""

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
    <a href="ikea-assembly-byron-bay.html">IKEA assembly</a>
    <a href="furniture-assembly.html">Flatpack</a>
    <a href="areas.html">Areas</a>
    <a href="contact.html">Contact</a>
    <a href="tel:0481457271">0481 457271</a>
  </div>
</div></nav>
"""


def page(*, slug, title, meta, h1, hero, placename, lat, lng, body, nearby, areas, services) -> str:
    nearby_html = "\n".join(f'<a class="card" href="{h}">{l}</a>' for h, l in nearby)
    areas_j = ", ".join(f'"{a}"' for a in areas)
    svc_j = ", ".join(f'"{s}"' for s in services)
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
  "@type": ["HomeAndConstructionBusiness", "LocalBusiness", "Service"],
  "name": "GoodHands Handyman — IKEA & Flatpack Assembly",
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
  "areaServed": [{areas_j}],
  "serviceType": [{svc_j}],
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
  <h3>Got IKEA boxes in {placename}?</h3>
  <p>Send me the product links or photos — I’ll quote fast and book around your delivery day.</p>
  <a class="btn" href="tel:0481457271">Call 0481 457271</a>
  <a class="btn" href="contact.html">Request a quote</a>
</div>
<div class="related">
  <h2>Related assembly pages</h2>
  <div class="grid">
{nearby_html}
  </div>
</div>
</main>
<footer class="footer"><div class="container">
  <p><strong>GoodHands Handyman</strong> — IKEA &amp; flatpack assembly · Byron Bay to Tweed / Coolangatta border.</p>
  <p><a href="ikea-assembly-byron-bay.html">IKEA hub</a> · <a href="furniture-assembly.html">All flatpack</a> · <a href="tel:0481457271">0481 457271</a></p>
</div></footer>
</body>
</html>
"""


SERVICES = [
    "IKEA assembly",
    "PAX wardrobe assembly",
    "Flatpack furniture assembly",
    "Furniture installation",
    "Office furniture assembly",
]


def main() -> None:
    pages = []

    # Pillar — IKEA Byron-focused
    pages.append(dict(
        slug="ikea-assembly-byron-bay.html",
        title="IKEA Assembly Byron Bay to Tweed | PAX & Flatpack | GoodHands",
        meta="IKEA furniture assembly Byron Bay to Tweed and Coolangatta border. PAX wardrobes, beds, desks, same-day with delivery. Call 0481 457271.",
        h1="IKEA assembly — Byron Bay to Tweed",
        hero="Order online, I’ll build it. PAX wardrobes, MALM bedrooms, BESTA units, desks and full flatpack orders — Byron Bay home base through Ballina, Tweed and Coolangatta border.",
        placename="Byron Bay",
        lat="-28.6474",
        lng="153.6020",
        areas=["Byron Bay", "Ballina", "Lennox Head", "Tweed Heads", "Kingscliff", "Coolangatta", "Northern Rivers"],
        nearby=[
            ("ikea-pax-wardrobe-assembly.html", "PAX wardrobe assembly"),
            ("ikea-assembly-ballina.html", "IKEA Ballina"),
            ("ikea-assembly-tweed-heads.html", "IKEA Tweed"),
            ("ikea-assembly-coolangatta.html", "IKEA Coolangatta"),
            ("furniture-assembly.html", "All flatpack brands"),
            ("handyman-byron-to-tweed-corridor.html", "Corridor map"),
        ],
        body="""
<p>There’s no IKEA store in the Northern Rivers — people order online, get a wall of boxes, then need someone who actually enjoys building PAX. That’s me. I’m Dan from GoodHands: Byron Bay–based handyman, regular flatpack assembly across the Byron-to-Tweed corridor.</p>

<h2>What I assemble</h2>
<ul>
<li><strong>PAX wardrobes</strong> — hinged or sliding, including interiors</li>
<li>MALM beds, drawers, bedside tables</li>
<li>BESTA TV / storage, KALLAX, HEMNES, BILLY</li>
<li>ALEX desks, home office setups</li>
<li>METOD kitchen cabinets (assembly; licensed trades for plumbing/electrical)</li>
<li>Multi-item delivery-day builds (bedroom + living in one visit)</li>
</ul>

<h2>How it works</h2>
<ol>
<li>Send product links or photos of the boxes</li>
<li>I quote and book — often same day as delivery</li>
<li>I bring tools, build, wall-anchor tall units, remove packaging</li>
</ol>

<h2>Where I cover for IKEA jobs</h2>
<p><strong>Core:</strong> Byron Bay, Suffolk Park, Bangalow, Mullumbimby, Brunswick Heads, Ocean Shores, Lennox Head, Ballina.</p>
<p><strong>Tweed corridor:</strong> Pottsville, Kingscliff, Tweed Heads, Murwillumbah.</p>
<p><strong>Gold Coast border:</strong> Coolangatta / Tweed Heads South when travel fits — I’m not a Surfers Paradise daily run, but border IKEA jobs are fair game.</p>
<p>Not Sydney. Not central Gold Coast every day. Local corridor only — so you get a real local, not a franchise quote farm.</p>

<div class="grid">
<a class="card" href="ikea-assembly-ballina.html">IKEA Ballina</a>
<a class="card" href="ikea-assembly-tweed-heads.html">IKEA Tweed Heads</a>
<a class="card" href="ikea-assembly-coolangatta.html">IKEA Coolangatta / GC border</a>
<a class="card" href="ikea-pax-wardrobe-assembly.html">PAX wardrobes</a>
</div>

<h2>Other brands</h2>
<p>Fantastic Furniture, Officeworks, Bunnings, Koala, Mocka, Temple &amp; Webster, Kmart — same service. See <a href="furniture-assembly.html">furniture assembly</a> for the full flatpack list.</p>
"""
    ))

    # PAX money page — matches "ikea wardrobe assembly gold coast" intent locally
    pages.append(dict(
        slug="ikea-pax-wardrobe-assembly.html",
        title="IKEA PAX Wardrobe Assembly Byron Bay to Tweed | GoodHands",
        meta="IKEA PAX wardrobe assembly Byron Bay, Ballina, Tweed & Coolangatta border. Sliding doors, interiors, wall anchoring. Call 0481 457271.",
        h1="IKEA PAX wardrobe assembly",
        hero="PAX is the job people dread. I build them weekly — frames, interiors, hinged or sliding doors, levelled and anchored. Byron Bay through Tweed / Coolangatta border.",
        placename="Northern Rivers",
        lat="-28.6430",
        lng="153.6120",
        areas=["Byron Bay", "Ballina", "Tweed Heads", "Coolangatta", "Kingscliff", "Lennox Head"],
        nearby=[
            ("ikea-assembly-byron-bay.html", "IKEA assembly hub"),
            ("ikea-assembly-coolangatta.html", "Coolangatta / GC border"),
            ("ikea-assembly-ballina.html", "Ballina"),
            ("furniture-assembly.html", "All flatpack"),
            ("door-hanging-fitting-northern-rivers.html", "Door hanging"),
            ("contact.html", "Book a quote"),
        ],
        body="""
<p>Searching <strong>IKEA wardrobe assembly</strong>? PAX is usually what you mean. Sliding-door systems need careful track alignment; hinged doors need even gaps; interiors need the right order or you’ll rebuild half of it. I’ve done hundreds.</p>

<h2>PAX jobs I take</h2>
<ul>
<li>Single and multi-frame PAX builds</li>
<li>Sliding door systems (fiddly — my favourite kind of fiddly)</li>
<li>Hinged doors + soft-close</li>
<li>Interior fit-outs: shelves, drawers, softboxes, hanging rails</li>
<li>Corner configurations and walk-in style layouts</li>
<li>Wall anchoring for tip-over safety</li>
</ul>

<h2>Time &amp; booking</h2>
<p>A standard two-frame PAX is often 1.5–2.5 hours once parts are checked. Bigger sliding setups run longer. Send your IKEA order list and I’ll give a clear time/cost estimate. Best value: book me for delivery day so boxes don’t live in the hallway for a week.</p>

<h2>Byron to Tweed — including border</h2>
<p>Based in Byron Bay. Regular runs to Ballina, Lennox, Kingscliff, Tweed Heads. Coolangatta / Gold Coast border PAX jobs by arrangement — same coastal handyman, honest travel.</p>
"""
    ))

    towns = [
        ("ikea-assembly-ballina.html", "Ballina", "-28.8667", "153.5667",
         "IKEA Assembly Ballina | Flatpack & PAX | GoodHands",
         "IKEA assembly Ballina — PAX, beds, desks, delivery-day builds. Call 0481 457271.",
         "IKEA assembly in Ballina",
         "Flatpack and IKEA builds for Ballina homes — East Ballina, West Ballina, and nearby. PAX wardrobes, bedroom sets, desks.",
         "Ballina gets a lot of online IKEA deliveries. I assemble on delivery day when I can, wall-anchor tall units, and clear the packaging."),
        ("ikea-assembly-tweed-heads.html", "Tweed Heads", "-28.1780", "153.5410",
         "IKEA Assembly Tweed Heads | Flatpack Handyman | GoodHands",
         "IKEA assembly Tweed Heads — wardrobes, beds, office desks. Units and houses. Call 0481 457271.",
         "IKEA assembly in Tweed Heads",
         "IKEA and flatpack assembly for Tweed Heads houses and units. Byron-based, regularly on the Tweed corridor.",
         "Unit jobs need clean, compact work — I build in place carefully and leave the space tidy."),
        ("ikea-assembly-coolangatta.html", "Coolangatta", "-28.1690", "153.5340",
         "IKEA Assembly Coolangatta | Gold Coast Border | GoodHands",
         "IKEA assembly Coolangatta & Gold Coast border — PAX wardrobes, beds, desks. Northern Rivers–based. Call 0481 457271.",
         "IKEA assembly Coolangatta / Gold Coast border",
         "Need IKEA built on the Gold Coast border? I’m a Byron Bay handyman who takes Coolangatta / Tweed Heads South assembly jobs when timing works — PAX, bedrooms, desks.",
         "I’m not a Robina-to-Southport franchise. If you’re Coolangatta, Kirra, Bilinga or Tweed South, ask — border IKEA work is the northern end of my corridor."),
    ]

    for slug, town, lat, lng, title, meta, h1, hero, note in towns:
        pages.append(dict(
            slug=slug,
            title=title,
            meta=meta,
            h1=h1,
            hero=hero,
            placename=town,
            lat=lat,
            lng=lng,
            areas=[town, "Byron Bay", "Northern Rivers"],
            nearby=[
                ("ikea-assembly-byron-bay.html", "IKEA hub"),
                ("ikea-pax-wardrobe-assembly.html", "PAX wardrobes"),
                ("furniture-assembly.html", "All flatpack"),
                ("handyman-byron-to-tweed-corridor.html", "Corridor"),
                ("contact.html", "Contact"),
            ],
            body=f"""
<p>{note}</p>
<h2>Popular builds in {town}</h2>
<ul>
<li>PAX wardrobes (hinged &amp; sliding)</li>
<li>Bedroom sets — bed, drawers, bedside tables</li>
<li>BESTA / TV units and living storage</li>
<li>Desks and home office setups</li>
<li>Kids’ rooms and tip-over anchoring</li>
</ul>
<p>Full brand list and pricing guide on <a href="furniture-assembly.html">furniture assembly</a>. Corridor hub: <a href="ikea-assembly-byron-bay.html">IKEA assembly Byron Bay to Tweed</a>.</p>
"""
        ))

    written = []
    for p in pages:
        html = page(
            slug=p["slug"],
            title=p["title"],
            meta=p["meta"],
            h1=p["h1"],
            hero=p["hero"],
            placename=p["placename"],
            lat=p["lat"],
            lng=p["lng"],
            body=p["body"],
            nearby=p["nearby"],
            areas=p["areas"],
            services=SERVICES,
        )
        (ROOT / p["slug"]).write_text(html)
        written.append(p["slug"])
        print("wrote", p["slug"])

    # Sitemap
    sm_path = ROOT / "sitemap.xml"
    sm = sm_path.read_text()
    today = date.today().isoformat()
    for slug in written:
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
    print("sitemap ok", len(written), "pages")


if __name__ == "__main__":
    main()
