#!/usr/bin/env python3
"""Generate 6 Good Hands founder posts with natural SMASH backlinks."""

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title_tag}</title>
    <meta name="description" content="{meta}">
    <meta name="keywords" content="{keywords}">
    <link rel="canonical" href="https://goodhandshandyman.com.au/{slug}.html">

    <meta property="og:title" content="{headline}">
    <meta property="og:description" content="{meta}">
    <meta property="og:type" content="article">
    <meta property="og:url" content="https://goodhandshandyman.com.au/{slug}.html">
    <meta property="og:image" content="https://goodhandshandyman.com.au/hero-handyman-working.webp">
    <meta property="og:locale" content="en_AU">

    <meta name="robots" content="index, follow, max-image-preview:large">
    <meta name="article:author" content="Dan, GoodHands Handyman">
    <meta name="article:section" content="Business">
    <meta name="article:published_time" content="{date_iso}">

    <script type="application/ld+json">
    {{
        "@context": "https://schema.org",
        "@type": "BlogPosting",
        "headline": "{headline}",
        "description": "{meta}",
        "author": {{
            "@type": "Person",
            "name": "Dan Neale",
            "jobTitle": "Handyman",
            "worksFor": {{
                "@type": "Organization",
                "name": "GoodHands Handyman"
            }}
        }},
        "datePublished": "{date_iso}",
        "publisher": {{
            "@type": "Organization",
            "name": "GoodHands Handyman",
            "url": "https://goodhandshandyman.com.au"
        }},
        "mainEntityOfPage": "https://goodhandshandyman.com.au/{slug}.html",
        "areaServed": {{
            "@type": "AdministrativeArea",
            "name": "Northern Rivers, NSW"
        }}
    }}
    </script>

    <link href="https://fonts.googleapis.com/css2?family=Nunito:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">
    <style>
        * {{ margin: 0; padding: 0; box-sizing: border-box; }}
        body {{ font-family: 'Nunito', sans-serif; line-height: 1.7; color: #2D3748; background: #fff; padding-top: 70px; }}
        .container {{ max-width: 800px; margin: 0 auto; padding: 0 24px; }}
        .site-nav {{ position: fixed; top: 0; left: 0; right: 0; height: 70px; background: rgba(255,255,255,0.95); border-bottom: 1px solid #EDF2F7; display: flex; align-items: center; z-index: 1000; }}
        .site-nav .inner {{ max-width: 800px; width: 100%; margin: 0 auto; padding: 0 24px; display: flex; justify-content: space-between; align-items: center; }}
        .site-nav a {{ color: #2D3748; text-decoration: none; font-weight: 500; }}
        .site-nav .logo {{ font-weight: 900; font-size: 1.25rem; }}
        .site-nav .logo:hover {{ color: #FFB800; }}
        h1 {{ font-size: 2.5rem; margin: 48px 0 24px; color: #2D3748; line-height: 1.2; }}
        h2 {{ font-size: 1.75rem; margin: 40px 0 16px; color: #2D3748; }}
        h3 {{ font-size: 1.25rem; margin: 24px 0 12px; color: #4A5568; }}
        p {{ margin-bottom: 20px; font-size: 1.125rem; }}
        .meta {{ color: #718096; margin-bottom: 32px; font-size: 0.95rem; }}
        .cta-box {{ background: #FFF9E6; padding: 32px; border-radius: 12px; margin: 40px 0; border-left: 4px solid #FFB800; }}
        .cta-box h3 {{ margin-top: 0; color: #2D3748; }}
        .cta-box a {{ color: #2D3748; font-weight: 600; text-decoration: none; }}
        .cta-box a:hover {{ color: #E6A600; text-decoration: underline; }}
        a.body-link {{ color: #2D3748; font-weight: 700; text-decoration: underline; text-decoration-color: #FFB800; text-underline-offset: 3px; }}
        a.body-link:hover {{ color: #E6A600; }}
        ul {{ margin: 20px 0 20px 24px; }}
        li {{ margin-bottom: 12px; font-size: 1.125rem; }}
        strong {{ color: #2D3748; }}
        .related {{ margin: 48px 0; padding: 32px 0; border-top: 1px solid #EDF2F7; }}
        .related ul {{ list-style: none; margin: 16px 0 0; padding: 0; }}
        .related li {{ margin-bottom: 10px; }}
        .related a {{ color: #2D3748; font-weight: 600; text-decoration: none; }}
        .related a:hover {{ color: #FFB800; }}
        @media (max-width: 768px) {{
            h1 {{ font-size: 2rem; }}
            h2 {{ font-size: 1.5rem; }}
            .container {{ padding: 0 20px; }}
        }}
    </style>
</head>
<body>
    <nav class="site-nav">
        <div class="inner">
            <a class="logo" href="index.html">GoodHands</a>
            <div style="display:flex;gap:20px;">
                <a href="blog.html">Blog</a>
                <a href="contact.html">Contact</a>
                <a href="tel:0481457271">0481 457271</a>
            </div>
        </div>
    </nav>
    <div class="container">
        <article>
            <div class="meta">{date_display} | Dan Neale · GoodHands Handyman</div>
            <h1>{headline}</h1>
{body}
            <div class="cta-box">
                <h3>Need a handyman in the Northern Rivers?</h3>
                <p>I still run Good Hands on the tools — kitchens, decks, fences, emergency fixes across Byron Bay and surrounds.</p>
                <p><strong>Call Dan:</strong> <a href="tel:0481457271">0481 457271</a> · <a href="{internal_href}">{internal_label}</a> · <a href="contact.html">Request a quote</a></p>
            </div>
            <div class="related">
                <h2>Related on GoodHands</h2>
                <ul>
                    <li><a href="{internal_href}">{internal_label}</a></li>
                    <li><a href="about.html">About Dan</a></li>
                    <li><a href="blog.html">More from the blog</a></li>
                    <li><a href="handyman-byron-bay.html">Byron Bay handyman services</a></li>
                </ul>
            </div>
        </article>
    </div>
</body>
</html>
"""

ARTICLES = [
    {
        "slug": "i-still-run-good-hands-handyman-why-i-built-an-app",
        "title_tag": "I Still Run Good Hands Handyman | Why I Built an App",
        "headline": "I Still Run Good Hands Handyman. Here's Why I Built an App.",
        "meta": "Dan from Good Hands Handyman still works on the tools. Why admin Sundays and lost quotes pushed him to build SMASH.",
        "keywords": "good hands handyman, dan neale byron bay, handyman built app, smash invoices founder, northern rivers handyman",
        "date_iso": "2026-07-14",
        "date_display": "July 14, 2026",
        "internal_href": "about.html",
        "internal_label": "About Good Hands",
        "excerpt": "I still fix kitchens and decks around Byron. Admin Sundays and “I’ll email the quote tonight” were costing me jobs — so I built something for myself.",
        "body": """
            <p>I'm Dan. I run <strong>Good Hands Handyman</strong> out of Byron Bay — kitchens, decks, fences, Airbnb turnarounds, the jobs that keep Northern Rivers properties working. I'm still on the tools most days. That hasn't changed.</p>

            <p>What changed is what happens after I put the drill down.</p>

            <p>People assume if you build software you must have quit the trade. I didn't. Good Hands is still how I pay attention to real houses: swollen cupboard doors in coastal humidity, grey decks that need proper marine oil, fences that lean after a windy night. The van still smells like timber and sunscreen.</p>

            <h2>Admin Sundays used to own me</h2>

            <p>For a long time my week looked like this. Monday to Friday: on site. Promise people I'll “email the quote tonight.” Friday night: too knackered. Saturday: maybe another emergency lockout or a property manager who needs a place guest-ready. Sunday night: laptop open, trying to remember what I said in someone's kitchen on Tuesday.</p>

            <p>I'm not a natural typist. Dyslexia makes the admin side slower than the work itself. Not an excuse — just the truth. The craft I can do with my eyes closed. Turning a job into a clean quote or invoice used to eat the only quiet day I had.</p>

            <p>And the sticky-note system doesn't scale. Photos on the phone. Half a sentence in Notes. A voice memo I never listen to again. By Sunday the details have gone soft. That's when you undercharge a call-out you forgot, or pad a number because you're guessing.</p>

            <h2>“I'll email the quote tonight” loses jobs</h2>

            <p>Here's the bit that actually hurt the business. A customer stands with you in the kitchen. They want a number. You say you'll send something later. Then another bloke quotes them that afternoon from his phone in the driveway.</p>

            <p>Guess who gets the job.</p>

            <p>I lost work that way more than once. Not because my rates were wrong. Not because the work wasn't solid. Because I was second. In this area — Byron, Lennox, Ballina, Mullumbimby — people move fast when something's broken, especially holiday rentals with a checkout in the morning and new guests at three.</p>

            <p>Polite delay feels professional. It also hands the decision to whoever closed it first.</p>

            <h2>I tried ChatGPT. Wording was fine. Prices weren't.</h2>

            <p>Like a lot of tradies, I tried AI. ChatGPT could write a polite email. It could make a quote <em>sound</em> professional — better than my Sunday typing, if I'm honest.</p>

            <p>What it couldn't do was use <strong>my</strong> rates. My call-out. My travel across the Northern Rivers. My labour. My markup on materials from Bunnings or the timber yard. It guessed. Guessed numbers are worse than no quote. You either undercharge and resent the job, or overcharge and look like you don't know your market.</p>

            <p>Fluent sentences aren't the same as knowing what a hinge job costs in salt air.</p>

            <h2>So I built something for my own jobs</h2>

            <p>I didn't set out to become a software guy. I set out to stop losing Sundays and stop losing jobs to whoever quoted first. I needed to talk through a job the way I already think about it on site — then verify the prices against my own catalogue — then send it before I left the driveway.</p>

            <p>That habit became <a class="body-link" href="https://smashinvoices.com/voice-invoicing">voice to invoice</a> for me: roughly thirty seconds of talking once I've seen the work, check the line items, send. Quotes first when they're deciding. Invoice when the work's done — ideally before I drive off.</p>

            <p>If you want the longer version of how Good Hands led to the product, that's <a class="body-link" href="https://smashinvoices.com/founder">the story behind SMASH</a>. Short version: I built it for my own vans and kitchens. Other tradies can use it too.</p>

            <h2>Handyman first. Still.</h2>

            <p>I still turn up. I still measure twice. I still care whether the latch lines up and the deck oil is coastal-grade. The app exists so the paperwork doesn't cancel the life I actually want when the tools go back in the van.</p>

            <p>If you're a homeowner reading this — you're hiring a bloke on the tools, not a call centre. If you're another tradie — you already know the Sunday feeling. Fix the habit before it owns your weekends.</p>
""",
    },
    {
        "slug": "the-job-usually-goes-to-whoever-quotes-first",
        "title_tag": "The Job Goes to Whoever Quotes First | Good Hands",
        "headline": "The Job Usually Goes to Whoever Quotes First",
        "meta": "Why “I'll email a quote tonight” loses handyman jobs in Byron Bay — and how Dan sends an instant quote on site.",
        "keywords": "handyman quote byron bay, instant quote on site, first quote wins, on site estimate northern rivers",
        "date_iso": "2026-07-15",
        "date_display": "July 15, 2026",
        "internal_href": "get-quote.html",
        "internal_label": "Get a quote from Good Hands",
        "excerpt": "Customer in the kitchen wants a number now. Email-later loses. Here's the on-site quote habit that changed how I win work.",
        "body": """
            <p>Picture this. Suffolk Park kitchen. Cupboard doors swollen from humidity, hinges chewed, customer already stressed because the property manager wants it fixed before Friday's guests.</p>

            <p>They ask: “Roughly what are we looking at?”</p>

            <p>Old me: “I'll have a proper quote over to you tonight.”</p>

            <p>Then I'd get in the van, do two more jobs, forget a measurement, and send something Wednesday. By then they'd already said yes to someone else. Not always cheaper. Just first.</p>

            <h2>First quote isn't about being cheapest</h2>

            <p>Most of the time the job doesn't go to the lowest number. It goes to the person who gave a clear, priced answer while the problem was still in front of everyone's face.</p>

            <p><strong>First quote wins</strong> — not as a slogan, as a habit. Standing there with the doors open, you can see the labour, the hardware, whether you're replacing two doors or six. You can show them why a cheap hinge will fail again in coastal air. Delay that into an email later and you're competing with whoever texted a number from the driveway an hour after you left.</p>

            <p>Homeowners aren't trying to be difficult. They're trying to stop thinking about the broken thing. Whoever helps them decide wins the booking.</p>

            <h2>What “I'll email tonight” actually costs you</h2>

            <ul>
                <li>You forget a detail and underquote</li>
                <li>You pad the number because you're guessing from memory</li>
                <li>They've already booked the next person</li>
                <li>Sunday finds you rebuilding quotes from messy notes</li>
                <li>You sound unsure even when the work is straightforward</li>
            </ul>

            <p>None of that is about being a bad handyman. It's about leaving the decision open when your competitor closed it.</p>

            <h2>What I do now in the kitchen or the van</h2>

            <p>I still walk the job properly. I still measure. I don't invent prices to sound fast. If I need to see behind a panel or check whether the chipboard is swollen under the sink, I say so.</p>

            <p>What I don't do anymore is promise paperwork for tonight. I talk the job out loud the way I'd explain it to another tradie — doors, hinges, labour hours, materials, travel if I'm coming back from Ballina — then I check the line items against my own rates before I hit send.</p>

            <p>That <a class="body-link" href="https://smashinvoices.com/blog/first-quote-wins-instant-quote-on-site">first quote wins</a> loop is the whole game: talk → verify → send. On a good day it's about thirty seconds once I've seen the work. Customer gets an <a class="body-link" href="https://smashinvoices.com/voice-invoicing">instant quote on site</a> on their phone. I get a yes or a clear no while I'm still there.</p>

            <h2>A yes on site beats a maybe by email</h2>

            <p>Sometimes they need to check with a partner or a property owner. Fine. At least the number exists. They're not waiting on me to “get organised tonight.” The quote is already in their inbox while we're both looking at the same cupboard.</p>

            <p>For Airbnb and property managers around Byron, speed isn't a nice-to-have. Checkout is morning. Guests arrive afternoon. A quote that arrives Wednesday might as well not exist.</p>

            <h2>The habit matters more than the tool</h2>

            <p>You can do a version of this with a notes app and a template if you're disciplined. I wasn't — not with dyslexia and a full week of jobs. I built SMASH for my own jobs so I could send a quote on site without typing a novel. Other tradies can use it too.</p>

            <p>But don't wait for perfect software to change the rule: don't leave the driveway without a number in their hands when the job is clear enough to price.</p>
""",
    },
    {
        "slug": "chatgpt-handyman-estimates-prices-were-wrong",
        "title_tag": "ChatGPT Handyman Estimates Were Wrong | Good Hands",
        "headline": "I Asked ChatGPT for Handyman Estimates. The Prices Were Wrong.",
        "meta": "ChatGPT wrote fine quote wording but guessed Dan's handyman rates. Why catalog prices beat AI estimates.",
        "keywords": "chatgpt handyman estimate, ai quote prices wrong, handyman rates byron bay, voice quoting catalog",
        "date_iso": "2026-07-16",
        "date_display": "July 16, 2026",
        "internal_href": "handyman-pricing-northern-rivers.html",
        "internal_label": "Handyman pricing Northern Rivers",
        "excerpt": "AI wrote a polished quote email. The dollars were fiction. Here's why wording isn't the same as knowing your rates.",
        "body": """
            <p>I'll say the quiet part out loud: I tried ChatGPT for quoting.</p>

            <p>I run Good Hands Handyman across Byron Bay and the Northern Rivers. I'm better with a circular saw than a spreadsheet. So when everyone started saying AI would do the admin, I pasted a job description in — kitchen doors, coastal humidity, return visit for hardware — and asked for an estimate email.</p>

            <p>The wording? Fine. Polite. Professional. Better than my Sunday-night typing, honestly.</p>

            <p>The prices? Wrong.</p>

            <h2>It guessed my rates. Guessed is not good enough.</h2>

            <p>It invented labour numbers that weren't mine. It missed how I think about call-out versus a return visit. Travel from Byron toward Ballina or Tweed wasn't right. Markup on materials didn't match what I actually charge when I pick up hinges, latch sets, or timber.</p>

            <p>If I'd sent that quote, I'd either look expensive for the wrong reasons or cheap for the dangerous ones. Neither builds trust. A customer doesn't care that the email sounded clever if the number feels made up.</p>

            <p>That's the whole story I wrote up properly here: <a class="body-link" href="https://smashinvoices.com/blog/chatgpt-got-my-handyman-estimates-wrong">ChatGPT got my estimates wrong</a>. Short version for other tradies: AI can dress the email. It does not know your catalogue.</p>

            <h2>Why Northern Rivers pricing isn't a national average</h2>

            <p>Coastal work has its own costs. Salt air eats cheap hardware. Humidity swells doors. Decks need marine-grade products, not whatever was on special. Travel time between towns is real. A “typical Australian handyman rate” scraped from the internet doesn't know any of that about <em>my</em> week.</p>

            <p>ChatGPT is trained on averages and confident prose. Your business runs on specific prices you've learned the hard way.</p>

            <h2>What I actually need on a job</h2>

            <p>When I'm in someone's kitchen in Mullumbimby or under a deck in Lennox, I need:</p>

            <ul>
                <li>My labour rates — not a national average</li>
                <li>My call-out / travel habits for this area</li>
                <li>Materials priced the way I buy and mark them</li>
                <li>A quote the customer can say yes to while I'm still there</li>
            </ul>

            <p>That's why I moved to <a class="body-link" href="https://smashinvoices.com/voice-invoicing">voice quoting with my rates</a>. I talk the job. I verify every line against my own prices. Then I send. About thirty seconds when the job is clear — not because AI is magic, because the catalogue is mine.</p>

            <h2>Honest take on AI for tradies</h2>

            <p>Use ChatGPT if you want help wording a tricky email to a property manager. Use it to clean up a paragraph. Don't let it invent what a hinge job costs in Byron Bay salt air.</p>

            <p>Your reputation sits in the number, not the adjectives. Customers remember whether the final invoice matched what they expected. They don't remember that your email used nice transitions.</p>

            <p>I built SMASH for my own jobs after I got tired of pretty emails with wrong dollars. Other tradies can use it too — just don't confuse fluent sentences with real pricing.</p>
""",
    },
    {
        "slug": "send-quote-on-site-then-invoice-before-i-leave",
        "title_tag": "Quote On Site, Invoice Before I Leave | Good Hands",
        "headline": "I Send the Quote on Site — Then the Invoice Before I Leave",
        "meta": "How Dan from Good Hands wins the job with an on-site quote, then invoices before driving off — no Sunday admin.",
        "keywords": "voice to invoice, invoice before you leave, on site quote handyman, same day invoice byron bay",
        "date_iso": "2026-07-17",
        "date_display": "July 17, 2026",
        "internal_href": "contact.html",
        "internal_label": "Contact Good Hands",
        "excerpt": "Same visit: quote wins the work, do the job, invoice before you hit the highway. Cashflow beats Sunday admin.",
        "body": """
            <p>Most tradie advice splits quoting and invoicing into two different headaches. On my Good Hands jobs, I try to keep them in the same visit whenever the work allows it.</p>

            <p>Quote while the problem is in front of us. Do the work (or lock the date). Invoice before I leave. That's the loop that stopped my Sundays filling up with paperwork.</p>

            <h2>Part one: win the job in the driveway</h2>

            <p>Customer wants certainty. “I'll email a quote tonight” feels polite. It's also how you lose the booking to whoever sent a number first.</p>

            <p>So I talk the quote on site — labour, materials, anything fiddly — then verify it against my prices and send it to their phone. They're looking at the same swollen door or leaning panel I am. Questions happen immediately.</p>

            <p>If you want the thirty-second version of that habit, I wrote it up as how I <a class="body-link" href="https://smashinvoices.com/blog/send-quote-on-site-30-seconds-handyman">send a quote on site</a> without rebuilding the whole job from memory later.</p>

            <h2>Part two: get paid before Sunday finds you</h2>

            <p>Here's the part that changed my cashflow. When the job's done — say I've rehung the doors, adjusted the latch, cleaned up — I don't put “invoice” on a sticky note for the weekend.</p>

            <p>I do <a class="body-link" href="https://smashinvoices.com/voice-invoicing">voice to invoice</a> before I put the van in gear. Talk what I actually did. Check the lines. Send. Customer has the PDF while they're still thinking about the fix, not three days later when the urgency's gone and the inbox is full.</p>

            <p>“Send the invoice before you leave” sounds obvious written down. On a hot afternoon when you just want a cold drink, it's the easy thing to skip. Skipping is how Sunday becomes another shift.</p>

            <h2>Why same-visit paperwork matters</h2>

            <ul>
                <li><strong>Memory is fresh</strong> — you invoice what you did, not what you half-remember</li>
                <li><strong>Customer expects it</strong> — the work just finished; payment talk feels natural</li>
                <li><strong>Fewer awkward chases</strong> — the paperwork exists while the job is still real to them</li>
                <li><strong>Weekend stays a weekend</strong> — you're not rebuilding the week from photos and texts</li>
            </ul>

            <h2>When the full loop isn't possible</h2>

            <p>Not every job invoices the same day. Some need parts from the supplier. Some need a return visit after paint dries or concrete sets. Some quotes turn into bookings next week.</p>

            <p>The point isn't perfection. The point is the default. Don't automatically shove paperwork into “I'll do it Sunday.” Quote when they're deciding. Invoice when the work is done — ideally before you hit the highway toward the next town.</p>

            <h2>Handyman first, cashflow second — both matter</h2>

            <p>I'm still on the tools. Good Hands is still the business on the side of the van. I care more about a clean latch alignment than a fancy PDF. But unpaid work and forgotten invoices don't keep the lights on either.</p>

            <p>I built SMASH for my own jobs so quote → work → invoice could fit inside one visit when it should. Other tradies can use it too.</p>
""",
    },
    {
        "slug": "fence-job-how-i-quote-in-the-driveway",
        "title_tag": "Fence Job: How I Quote in the Driveway | Good Hands",
        "headline": "Fence Job: How I Quote in the Driveway",
        "meta": "A Byron Bay fence repair walkthrough — what Dan says on site, how he prices it, and how the customer gets the quote on their phone.",
        "keywords": "fence repair quote byron bay, handyman driveway quote, colorbond fence estimate northern rivers",
        "date_iso": "2026-07-18",
        "date_display": "July 18, 2026",
        "internal_href": "colorbond-fence-repairs-byron-bay.html",
        "internal_label": "Colorbond fence repairs Byron Bay",
        "excerpt": "Storm-loosened panels, driveway chat, quote on their phone before I leave. A real Good Hands quoting walkthrough.",
        "body": """
            <p>This is a normal Good Hands morning — not a demo, not a polished case study. Fence job after a windy night. Ballina side of the region. Property manager wants it safe before the weekend guests arrive.</p>

            <p>I'm writing this so other tradies (and curious homeowners) can see what quoting looks like when you refuse to say “I'll email tonight.”</p>

            <h2>What I see when I pull up</h2>

            <p>Two Colorbond panels leaning. A post that's moved just enough that the gate scrapes. Nothing dramatic — the kind of job that looks small until you price the fix properly. There's always a chance the post needs a real dig-and-set, not a temporary shove.</p>

            <p>I walk it with the customer. We talk about make-safe today versus a proper repair. I don't invent a number from the street before I've looked at the footings and the hardware.</p>

            <h2>What I say out loud (the quote in plain English)</h2>

            <p>Roughly how it comes out of my mouth — not a script, just the checklist in my head:</p>

            <ul>
                <li>Labour to straighten and re-fix the lean — how long I reckon it'll take</li>
                <li>Whether the post needs a proper dig-and-set or a temporary make-safe today</li>
                <li>Panel / hardware if anything's bent beyond saving</li>
                <li>Travel back if parts mean a second visit</li>
                <li>Anything I won't know until I start (and how I'll handle extras)</li>
            </ul>

            <p>No fake dollar amounts in this article. Every fence is different, and I won't invent a price for a blog. The point is the sequence: see it, say it, check it, send it.</p>

            <h2>Verify, then put it on their phone</h2>

            <p>Still in the driveway, I turn that talk into a priced quote against my own rates. Customer looks at it on their phone while we're both staring at the same leaning panel. Questions happen immediately — “Can we do the make-safe today and the post next week?” — instead of three emails later when they've already forgotten which panel we meant.</p>

            <p>That's <a class="body-link" href="https://smashinvoices.com/voice-invoicing">voice to invoice on the job</a> for me: talk the fence the way I'd explain it to another tradie, verify the lines, send before I reverse out. Talk → verify → send. About thirty seconds once the scope is clear.</p>

            <h2>Why the driveway matters around here</h2>

            <p>If I said “I'll email tonight,” they'd call two other people by lunch. Standing there with a clear quote, we either book it or we don't. Either way I'm not doing Sunday archaeology trying to remember which post was rotten.</p>

            <p>Storm season in the Northern Rivers makes this worse. Everyone wants fences and gates sorted yesterday. The tradie who can price on site while looking at the damage gets the work. The tradie who promises a PDF later gets the leftover jobs — if any.</p>

            <h2>After they say yes</h2>

            <p>If it's a same-day make-safe, I do the work and invoice before I leave when I can. If it's a return visit for a post set, the quote already exists — we're not renegotiating from scratch next week.</p>

            <p>Need fence help around Byron or Ballina? That's still Good Hands work — <a href="colorbond-fence-repairs-byron-bay.html">Colorbond fence repairs</a> are a regular part of the week for me.</p>

            <p>I built SMASH for my own jobs so the driveway quote didn't have to wait until I got home. Other tradies can use it too.</p>
""",
    },
    {
        "slug": "i-stopped-saving-invoices-for-sunday-night",
        "title_tag": "I Stopped Saving Invoices for Sunday Night | Good Hands",
        "headline": "I Stopped Saving Invoices for Sunday Night",
        "meta": "Dan from Good Hands stopped batching invoices on Sundays. Same-day voice to invoice keeps weekends free.",
        "keywords": "handyman sunday admin, invoice without typing, same day invoice habit, voice to invoice tradie",
        "date_iso": "2026-07-19",
        "date_display": "July 19, 2026",
        "internal_href": "about.html",
        "internal_label": "About Dan / Good Hands",
        "excerpt": "Batch admin was killing my weekends. Same-day invoicing brought them back — I'm still a handyman first.",
        "body": """
            <p>There was a stretch where Sunday night meant invoices.</p>

            <p>Not family. Not the beach. Not sitting on my own deck for once. Me, a laptop, and a week of Good Hands jobs half-remembered from photos on my phone. The business was busy — which should feel good — but the paperwork turned the only quiet day into another shift.</p>

            <h2>Batch admin feels efficient. It isn't.</h2>

            <p>You tell yourself you'll “do the invoices in one hit.” Then Friday's fence blurs into Wednesday's kitchen. You undercharge a call-out you forgot. You chase a payment for a job you can't clearly describe. You go to bed annoyed at a business you actually like.</p>

            <p>Dyslexia doesn't help when you're typing the same details six times. I'd rather sand a deck than fight a blank invoice form at 9pm. The tools make sense. The blinking cursor doesn't.</p>

            <p>Batching also tricks you into thinking you're organised. You're not. You're delaying decisions until the memories are worse.</p>

            <h2>The habit that replaced Sunday</h2>

            <p>I stopped treating invoicing as a weekend chore. When the job's done, I send it — ideally before I leave the driveway or the kitchen.</p>

            <p><a class="body-link" href="https://smashinvoices.com/voice-invoicing">Voice to invoice</a> is how I do that without turning the van into an office: talk what I did, verify the prices against my catalogue, send. About thirty seconds when the job is clear. <a class="body-link" href="https://smashinvoices.com/blog/what-is-voice-to-invoice">Invoice without typing</a> sounds like a slogan until you've spent a year typing every Sunday.</p>

            <h2>What same-day invoicing fixed for me</h2>

            <ul>
                <li>Fewer “what was that job again?” moments</li>
                <li>Customers get the PDF while the work is still fresh</li>
                <li>Less awkward chasing weeks later</li>
                <li>Weekends that aren't a second unpaid shift</li>
            </ul>

            <p>I'm not claiming perfect cashflow enlightenment. I'm claiming a boring habit that works: don't save the whole week for Sunday night.</p>

            <h2>I'm still a handyman first</h2>

            <p>This isn't a story about quitting the tools for software. I still turn up for kitchens, decks, fences, and the messy emergency jobs across the Northern Rivers. Good Hands is the work. The admin habit just stopped cancelling the rest of my life.</p>

            <p>Some weeks aren't perfect. Parts delay an invoice. A big job spans two visits. A property manager needs a different billing entity. The rule is simpler than perfection: don't default to Sunday.</p>

            <p>If you're a homeowner — this is why I might send the invoice while I'm still packing the van. It's not pushy. It's how I keep the books honest and the weekends human.</p>

            <p>I built SMASH for my own jobs so weekends could be weekends again. Other tradies can use it too.</p>
""",
    },
]


def main() -> None:
    for article in ARTICLES:
        html = TEMPLATE.format(**article)
        path = ROOT / f"{article['slug']}.html"
        path.write_text(html, encoding="utf-8")
        print(f"Wrote {path.name}")


if __name__ == "__main__":
    main()
