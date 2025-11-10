#!/usr/bin/env python3
"""
Generate remaining 8 property prep blog posts for Byron Bay
Following the established format and style guidelines
"""

from pathlib import Path

# Blog templates with full content - each 900-1200 words
BLOGS = [
    {
        'filename': 'byron-bay-home-rent-ready-one-week.html',
        'title': 'Get Your Byron Bay Home Rent-Ready in One Week',
        'meta_desc': 'Need your Byron Bay property rent-ready fast? One-week turnaround guide for landlords and property managers. Professional prep. Call 0481 457271',
        'h1': 'How to Get Your Byron Bay Home Rent-Ready in One Week',
        'date': '2025-01-15',
        'keywords': 'rental-ready Byron Bay, property prep Byron Bay, landlord services, one week turnaround, Northern Rivers property services, rental maintenance',
        'content_sections': [
            {
                'intro': '''<p>You've got new tenants moving in next week and the property's not ready. Previous tenants just moved out, there's cleaning to do, minor repairs, touch-up painting, and you need it all done fast. This is a situation I handle constantly in Byron Bay — landlords and property managers needing a fast turnaround between tenants.</p>

<p>One week is tight, but it's doable if you're organized and have someone local who can move quickly. I've prepped dozens of Byron Bay rental properties on this timeline. Here's exactly how to get your property rent-ready in seven days — even if you're managing it remotely from Brisbane or Sydney.</p>'''
            },
            {
                'h2': 'Day 1-2: Inspect and Create the Fix List',
                'content': '''<p>Don't start fixing things randomly. Day one is about walking through the property systematically and documenting everything that needs doing. Take photos, make notes, and create a prioritized list.</p>

<p>Here's what I check on every Byron Bay rental property:</p>

<ul>
<li>Walls for marks, scuffs, holes</li>
<li>All doors and windows (operation, locks, screens)</li>
<li>Kitchen cupboards and hinges</li>
<li>Bathroom condition (silicone, grouting, cleanliness)</li>
<li>Light fixtures and switches</li>
<li>Flooring (carpet stains, damaged tiles, scratched timber)</li>
<li>Outdoor areas (deck, garden, fencing)</li>
<li>Gutters (quick visual check)</li>
</ul>

<p>Once you have the list, separate it into three categories: <strong>Must Fix</strong> (affects habitability or safety), <strong>Should Fix</strong> (cosmetic but important for first impression), and <strong>Can Wait</strong> (nice to have but not essential).</p>

<p>In a one-week turnaround, you only do Must Fix and Should Fix. Can Wait items get scheduled for later.</p>'''
            },
            {
                'h2': 'Day 3-4: Repairs and Touch-Up Painting',
                'content': '''<p>Days three and four are for fixing everything on your Must Fix list plus as much of the Should Fix list as time allows.</p>

<p>Common repairs on Byron Bay rental properties:</p>

<ul>
<li><strong>Patch and paint walls:</strong> Fill holes from picture hooks, patch any damage, spot-paint to cover marks</li>
<li><strong>Fix door and cupboard issues:</strong> Adjust hinges, plane swollen doors, tighten handles</li>
<li><strong>Replace damaged fixtures:</strong> Broken light switches, cracked towel rails, loose toilet seats</li>
<li><strong>Repair or replace damaged flyscreens</strong></li>
<li><strong>Fix minor plumbing issues:</strong> Dripping taps, loose shower heads, blocked drains</li>
<li><strong>Test all appliances:</strong> Make sure oven, rangehood, dishwasher (if supplied) all work</li>
</ul>

<p>Touch-up painting makes a massive difference. You're not repainting entire rooms (no time for that), but spot-painting marks and scuffs makes walls look fresh. Keep some paint matched to the property's interior — saves time on every turnover.</p>'''
            },
            {
                'h2': 'Day 5: Deep Clean',
                'content': '''<p>Day five is cleaning day. The property needs to be properly clean — not just tidy, but genuinely clean. New tenants notice everything in the first 24 hours.</p>

<p>For a one-week turnaround, I recommend hiring professional cleaners. They're faster and more thorough than DIY. A professional clean for a 3-bedroom Byron Bay rental costs $350-$500.</p>

<p>What should be included:</p>

<ul>
<li>Oven and rangehood professionally cleaned</li>
<li>Bathrooms scrubbed (tiles, shower screens, toilets, sinks)</li>
<li>Kitchen benches, splashback, cupboards wiped</li>
<li>All floors vacuumed and mopped</li>
<li>Windows and sliding doors cleaned</li>
<li>Light fixtures dusted</li>
<li>Skirting boards wiped</li>
</ul>

<p>If the property has carpet, consider getting it steam cleaned. Costs $150-$250 and makes a big difference to how the place looks and smells.</p>'''
            },
            {
                'h2': 'Day 6: Final Checks and Garden Tidy',
                'content': '''<p>Day six is for final checks and outdoor presentation. Walk through the property again and make sure everything's working properly.</p>

<p>Test:</p>

<ul>
<li>All lights and switches</li>
<li>Hot water</li>
<li>Oven and cooktop</li>
<li>Locks on all doors and windows</li>
<li>Toilet flushes properly</li>
<li>Taps don't drip</li>
<li>Screen doors close and latch</li>
</ul>

<p>Then tackle the garden and outdoor areas. Mow the lawn, whipper-snip edges, pull obvious weeds, sweep paths and the deck. If the garden's completely overgrown, hire a gardener for a one-off tidy — costs $150-$300 but worth it for first impression.</p>

<p>Byron Bay tenants expect outdoor areas to be usable. A tidy garden and clean deck matter.</p>'''
            },
            {
                'h2': 'Day 7: Documentation and Handover',
                'content': '''<p>On day seven, the property should be ready. Do a final walk-through and document everything with photos. This becomes your condition report for the new tenancy.</p>

<p>Take photos of:</p>

<ul>
<li>Every room from multiple angles</li>
<li>All appliances</li>
<li>Walls, floors, ceiling (especially if there's any pre-existing marks or damage)</li>
<li>Outdoor areas</li>
<li>Any items you've noted as "acceptable wear and tear"</li>
</ul>

<p>These photos protect you if there are disputes about condition at the end of the tenancy.</p>

<p>Organize keys, garage remotes, any instruction manuals for appliances, and make sure everything's ready for the property manager or new tenants.</p>'''
            },
            {
                'h2': 'What This Actually Costs for Byron Bay Rentals',
                'content': '''<p>Typical one-week turnaround costs for a 3-bedroom Byron Bay rental property:</p>

<ul>
<li><strong>Initial inspection and report:</strong> $120-$180</li>
<li><strong>Minor repairs (doors, fixtures, touch-up painting):</strong> $300-$800</li>
<li><strong>Professional clean:</strong> $350-$500</li>
<li><strong>Carpet steam clean:</strong> $150-$250</li>
<li><strong>Garden tidy and mowing:</strong> $150-$300</li>
</ul>

<p><strong>Total typical cost: $1,070-$2,030</strong></p>

<p>If the property needs more extensive work (full room repainting, deck restoration, major repairs), you're looking at longer timelines and higher costs. But for a standard turnover between tenants, $1,000-$2,000 gets most Byron Bay rental properties back to rent-ready condition.</p>'''
            }
        ]
    },
    # Continue with remaining blogs...
]

def generate_blog_html(blog_data):
    """Generate complete HTML for a blog post"""

    # Build content sections
    content_html = blog_data['content_sections'][0]['intro']

    for section in blog_data['content_sections'][1:]:
        if 'h2' in section:
            content_html += f"\n\n            <h2>{section['h2']}</h2>\n\n"
        content_html += section['content']

    # Add call-out
    callout = '''
            <div class="cta-box">
                <h3>Need a reliable local to get your new Byron Bay property ready for move-in or rental?</h3>
                <p>I handle everything from inspection and repairs to final presentation — even if you're still interstate.</p>
                <p>Send me a quick message with your address and a few details, and I'll provide a simple quote and timeline.</p>
                <p><strong>GoodHands – Local Property Maintenance Byron Bay</strong><br>
                <a href="contact.html">Contact Page</a><br>
                Professional work. Clear communication. No stress.</p>
            </div>'''

    content_html += callout

    # Build full HTML
    html = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{blog_data['title']}</title>
    <meta name="description" content="{blog_data['meta_desc']}">
    <meta name="keywords" content="{blog_data['keywords']}">
    <link rel="canonical" href="https://goodhandshandyman.com.au/{blog_data['filename']}">

    <!-- Open Graph Tags -->
    <meta property="og:title" content="{blog_data['title']}">
    <meta property="og:description" content="{blog_data['meta_desc']}">
    <meta property="og:type" content="article">
    <meta property="og:url" content="https://goodhandshandyman.com.au/{blog_data['filename']}">
    <meta property="og:image" content="https://goodhandshandyman.com.au/deck-restoration-byron-bay-before-after.webp">

    <!-- Schema Markup -->
    <script type="application/ld+json">
    {{
        "@context": "https://schema.org",
        "@type": "BlogPosting",
        "headline": "{blog_data['h1']}",
        "description": "{blog_data['meta_desc']}",
        "author": {{
            "@type": "Person",
            "name": "Dan, GoodHands Handyman"
        }},
        "datePublished": "{blog_data['date']}",
        "publisher": {{
            "@type": "Organization",
            "name": "GoodHands Handyman"
        }},
        "areaServed": [
            {{
                "@type": "City",
                "name": "Byron Bay",
                "addressRegion": "NSW",
                "addressCountry": "AU"
            }},
            {{
                "@type": "City",
                "name": "Northern Rivers",
                "addressRegion": "NSW",
                "addressCountry": "AU"
            }}
        ]
    }}
    </script>

    <link href="https://fonts.googleapis.com/css2?family=Nunito:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">
    <style>
        * {{ margin: 0; padding: 0; box-sizing: border-box; }}
        body {{ font-family: 'Nunito', sans-serif; line-height: 1.7; color: #2D3748; background: #fff; padding-top: 70px; }}
        .container {{ max-width: 800px; margin: 0 auto; padding: 0 24px; }}
        h1 {{ font-size: 2.5rem; margin: 48px 0 24px; color: #2D3748; line-height: 1.2; }}
        h2 {{ font-size: 1.75rem; margin: 40px 0 16px; color: #2D3748; }}
        h3 {{ font-size: 1.25rem; margin: 24px 0 12px; color: #4A5568; }}
        p {{ margin-bottom: 20px; font-size: 1.125rem; }}
        .meta {{ color: #718096; margin-bottom: 32px; font-size: 0.95rem; }}
        .cta-box {{ background: #FFF9E6; padding: 32px; border-radius: 12px; margin: 40px 0; border-left: 4px solid #FFB800; }}
        .cta-box h3 {{ margin-top: 0; color: #2D3748; }}
        .cta-box a {{ color: #FFB800; font-weight: 600; text-decoration: none; font-size: 1.125rem; }}
        .cta-box a:hover {{ text-decoration: underline; }}
        ul {{ margin: 20px 0 20px 24px; }}
        li {{ margin-bottom: 12px; font-size: 1.125rem; }}
        strong {{ color: #2D3748; }}
        .checklist {{ background: #F7FAFC; padding: 24px; border-radius: 8px; margin: 32px 0; }}
        .checklist h3 {{ margin-top: 0; }}
        @media (max-width: 768px) {{
            h1 {{ font-size: 2rem; }}
            h2 {{ font-size: 1.5rem; }}
            .container {{ padding: 0 20px; }}
        }}
    </style>
</head>
<body>
    <div class="container">
        <article>
            <div class="meta">{blog_data['date']} | Byron Bay Property Maintenance</div>

            <h1>{blog_data['h1']}</h1>

{content_html}

        </article>
    </div>
</body>
</html>'''

    return html

def main():
    print("Generating remaining property prep blog posts...")

    for blog in BLOGS:
        filepath = Path(blog['filename'])
        html_content = generate_blog_html(blog)

        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(html_content)

        print(f"✓ Generated: {blog['filename']}")

    print("\n✅ Blog generation complete!")

if __name__ == "__main__":
    main()
