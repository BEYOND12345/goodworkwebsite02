#!/usr/bin/env python3
"""
Add safe internal links - "Related Services" sections
SAFE: Adds at bottom of content, doesn't touch Dan's writing
"""

import re
from pathlib import Path

# Map blog posts to related service/location pages
RELATED_LINKS = {
    'deck-maintenance-byron-bay-salt-air.html': {
        'related': [
            ('deck-restoration.html', 'Professional Deck Restoration'),
            ('deck-sanding.html', 'Deck Sanding Services'),
            ('handyman-byron-bay.html', 'Byron Bay Handyman Services'),
        ]
    },
    'kitchen-repairs-byron-bay-common-problems.html': {
        'related': [
            ('kitchen-door-repairs-northern-rivers.html', 'Kitchen Door Repairs'),
            ('handyman-byron-bay.html', 'Byron Bay Handyman'),
            ('contact.html', 'Get a Free Quote'),
        ]
    },
    'heritage-property-repairs-byron-bay-council-rules.html': {
        'related': [
            ('handyman-byron-bay.html', 'Byron Bay Handyman Services'),
            ('handyman-bangalow.html', 'Heritage Properties Bangalow'),
            ('contact.html', 'Contact for Heritage Work'),
        ]
    },
    'emergency-storm-repairs-byron-bay.html': {
        'related': [
            ('emergency-repairs.html', 'Emergency Repair Services'),
            ('fence-repairs-ballina.html', 'Fence Repairs'),
            ('handyman-byron-bay.html', 'Byron Bay Handyman'),
        ]
    },
    'airbnb-maintenance-byron-bay-fast-turnaround.html': {
        'related': [
            ('airbnb-maintenance.html', 'Airbnb Maintenance Services'),
            ('property-manager-services.html', 'Property Manager Services'),
            ('handyman-byron-bay.html', 'Byron Bay Handyman'),
        ]
    },
    'deck-restoration-season-byron-bay-october-november.html': {
        'related': [
            ('deck-restoration.html', 'Deck Restoration Services'),
            ('deck-sanding.html', 'Professional Deck Sanding'),
            ('handyman-byron-bay.html', 'Byron Bay Handyman'),
        ]
    },
    'fly-screen-season-byron-bay-summer-ready.html': {
        'related': [
            ('fly-screen-repairs-byron-bay.html', 'Fly Screen Repairs'),
            ('handyman-byron-bay.html', 'Byron Bay Handyman'),
            ('contact.html', 'Get a Quote'),
        ]
    },
    'summer-proofing-airbnb-byron-bay-property-managers.html': {
        'related': [
            ('airbnb-maintenance.html', 'Airbnb Maintenance'),
            ('property-manager-services.html', 'Property Manager Services'),
            ('handyman-byron-bay.html', 'Byron Bay Services'),
        ]
    },
    'holiday-season-property-prep-northern-rivers-christmas.html': {
        'related': [
            ('gutter-cleaning.html', 'Gutter Cleaning'),
            ('deck-restoration.html', 'Deck Restoration'),
            ('contact.html', 'Book Your Service'),
        ]
    },
}

def add_related_services(filepath, related_links):
    """Add Related Services section before footer"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        # Check if already has related services
        if 'Related Services' in content or 'related-services' in content:
            return False, "already has related section"

        # Create related services HTML
        links_html = '\n'.join([
            f'            <li><a href="{url}">{text}</a></li>'
            for url, text in related_links
        ])

        related_section = f'''
    <!-- Related Services -->
    <section style="padding: 60px 0; background: #F7FAFC;">
        <div class="container" style="max-width: 1200px; margin: 0 auto; padding: 0 24px;">
            <h2 style="font-size: 1.75rem; font-weight: 700; margin-bottom: 24px; color: #2D3748;">Related Services</h2>
            <ul style="list-style: none; padding: 0; display: grid; gap: 12px;">
{links_html}
            </ul>
        </div>
    </section>
'''

        # Find closing article tag and insert before it
        article_match = re.search(r'</article>', content, re.IGNORECASE)
        if not article_match:
            # Try footer as fallback
            footer_match = re.search(r'<footer', content, re.IGNORECASE)
            if not footer_match:
                return False, "no article or footer found"
            insert_pos = footer_match.start()
        else:
            insert_pos = article_match.start()

        # Insert related services before closing article (or footer)
        updated_content = content[:insert_pos] + related_section + '\n        ' + content[insert_pos:]

        # Write
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(updated_content)

        return True, "success"

    except Exception as e:
        return False, str(e)

def main():
    print("Adding safe internal links (Related Services sections)...")
    print("=" * 60)

    updated = 0
    for filename, data in RELATED_LINKS.items():
        filepath = Path(filename)
        if filepath.exists():
            success, message = add_related_services(filepath, data['related'])
            if success:
                print(f"✓ {filename}")
                updated += 1
            else:
                print(f"⊘ {filename} - {message}")
        else:
            print(f"✗ {filename} - not found")

    print("=" * 60)
    print(f"\n✓ Added Related Services to {updated} pages")
    print("  - Links appear before footer")
    print("  - No changes to Dan's content")
    print("  - Improves internal linking structure")

if __name__ == "__main__":
    main()
