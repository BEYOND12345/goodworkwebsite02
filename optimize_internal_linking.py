#!/usr/bin/env python3
"""
Optimize internal linking structure for better SEO
- Add contextual links between related pages
- Create topic clusters 
- Improve navigation flow
- Boost page authority distribution
"""

import os
import re
import glob

# Internal linking strategy mapping
INTERNAL_LINKS = {
    # High-authority pages should link to target pages
    'index.html': [
        {'text': 'emergency repairs', 'url': 'emergency-repairs.html'},
        {'text': 'deck restoration', 'url': 'deck-restoration.html'},
        {'text': 'gutter cleaning', 'url': 'gutter-cleaning.html'},
        {'text': 'Byron Bay handyman', 'url': 'handyman-byron-bay.html'},
        {'text': 'kitchen repairs', 'url': 'kitchen-repairs-byron-bay.html'},
        {'text': 'custom carpentry', 'url': 'custom-carpentry.html'},
    ],
    
    # Location pages should link to services
    'handyman-byron-bay.html': [
        {'text': 'deck restoration services', 'url': 'deck-restoration-byron-bay.html'},
        {'text': 'kitchen cabinet repairs', 'url': 'kitchen-repairs-byron-bay.html'},
        {'text': 'emergency repair service', 'url': 'emergency-repairs.html'},
        {'text': 'gutter cleaning', 'url': 'gutter-cleaning.html'},
    ],
    
    'handyman-ballina.html': [
        {'text': 'fence repairs', 'url': 'fence-repairs-ballina.html'},
        {'text': 'gutter cleaning services', 'url': 'gutter-cleaning-ballina.html'},
        {'text': 'emergency repairs', 'url': 'emergency-repairs.html'},
        {'text': 'deck restoration', 'url': 'deck-restoration.html'},
    ],
    
    # Service pages should cross-link
    'deck-restoration.html': [
        {'text': 'Byron Bay deck restoration', 'url': 'deck-restoration-byron-bay.html'},
        {'text': 'deck sanding', 'url': 'deck-sanding.html'},
        {'text': 'custom carpentry', 'url': 'custom-carpentry.html'},
        {'text': 'emergency repairs', 'url': 'emergency-repairs.html'},
    ],
    
    'gutter-cleaning.html': [
        {'text': 'Ballina gutter cleaning', 'url': 'gutter-cleaning-ballina.html'},
        {'text': 'emergency repairs', 'url': 'emergency-repairs.html'},
        {'text': 'property maintenance', 'url': 'airbnb-maintenance.html'},
    ],
    
    'kitchen-repairs-byron-bay.html': [
        {'text': 'kitchen door repairs', 'url': 'kitchen-door-repairs-northern-rivers.html'},
        {'text': 'custom carpentry', 'url': 'custom-carpentry.html'},
        {'text': 'Byron Bay handyman', 'url': 'handyman-byron-bay.html'},
    ],
    
    'custom-carpentry.html': [
        {'text': 'deck restoration', 'url': 'deck-restoration.html'},
        {'text': 'kitchen repairs', 'url': 'kitchen-repairs-byron-bay.html'},
        {'text': 'furniture assembly', 'url': 'furniture-assembly.html'},
    ],
    
    'emergency-repairs.html': [
        {'text': 'Byron Bay', 'url': 'handyman-byron-bay.html'},
        {'text': 'Ballina', 'url': 'handyman-ballina.html'},
        {'text': 'kitchen repairs', 'url': 'kitchen-repairs-byron-bay.html'},
        {'text': 'deck repairs', 'url': 'deck-restoration.html'},
    ],
    
    # Business pages
    'about.html': [
        {'text': 'services we provide', 'url': 'handyman-services-byron-bay.html'},
        {'text': 'service areas', 'url': 'areas.html'},
        {'text': 'transparent pricing', 'url': 'handyman-pricing-northern-rivers.html'},
    ],
    
    'contact.html': [
        {'text': 'service areas', 'url': 'areas.html'},
        {'text': 'pricing guide', 'url': 'handyman-pricing-northern-rivers.html'},
        {'text': 'emergency repairs', 'url': 'emergency-repairs.html'},
    ],
}

# Related services suggestions for footer/sidebar
RELATED_SERVICES = {
    'deck-restoration.html': [
        'gutter-cleaning.html',
        'custom-carpentry.html', 
        'painting-services.html'
    ],
    'gutter-cleaning.html': [
        'deck-restoration.html',
        'emergency-repairs.html',
        'airbnb-maintenance.html'
    ],
    'kitchen-repairs-byron-bay.html': [
        'custom-carpentry.html',
        'flooring-installation.html',
        'painting-services.html'
    ]
}

def add_contextual_links(filepath, links):
    """Add contextual internal links to page content"""
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Track changes
    changes_made = 0
    
    # Find main content areas to add links
    # Look for service descriptions, about sections, etc.
    
    for link_data in links:
        anchor_text = link_data['text']
        target_url = link_data['url']
        
        # Create variations of the anchor text to match
        text_variations = [
            anchor_text,
            anchor_text.lower(),
            anchor_text.title(),
            anchor_text.capitalize()
        ]
        
        for text_var in text_variations:
            # Don't link if already linked
            existing_link_pattern = f'<a[^>]*{re.escape(text_var)}[^>]*</a>'
            if re.search(existing_link_pattern, content, re.IGNORECASE):
                continue
                
            # Don't link if it's in navigation or footer
            # Look for the text in main content sections
            pattern = rf'\b({re.escape(text_var)})\b(?![^<]*</a>)(?![^<]*</nav>)(?![^<]*</footer>)'
            
            # Only replace first occurrence to avoid over-linking
            matches = list(re.finditer(pattern, content, re.IGNORECASE))
            if matches and len(matches) > 0:
                match = matches[0]
                # Make sure we're not inside an existing tag
                before_match = content[:match.start()]
                if '<a' not in before_match[-100:] or '</a>' in before_match[-100:]:
                    replacement = f'<a href="{target_url}">{match.group(1)}</a>'
                    content = content[:match.start()] + replacement + content[match.end():]
                    changes_made += 1
                    break  # Only link first occurrence
    
    if changes_made > 0:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"✅ Added {changes_made} contextual links to {os.path.basename(filepath)}")
    
    return changes_made

def add_related_services_section(filepath, related_pages):
    """Add a related services section to service pages"""
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Skip if already has related services
    if 'related-services' in content.lower() or 'other services' in content.lower():
        return False
    
    # Map URLs to titles
    url_to_title = {
        'deck-restoration.html': 'Deck Restoration',
        'deck-sanding.html': 'Deck Sanding',
        'gutter-cleaning.html': 'Gutter Cleaning',
        'emergency-repairs.html': 'Emergency Repairs',
        'custom-carpentry.html': 'Custom Carpentry',
        'kitchen-repairs-byron-bay.html': 'Kitchen Repairs',
        'painting-services.html': 'Painting Services',
        'furniture-assembly.html': 'Furniture Assembly',
        'airbnb-maintenance.html': 'Airbnb Maintenance',
        'flooring-installation.html': 'Flooring Installation',
        'fence-repairs-ballina.html': 'Fence Repairs'
    }
    
    # Build related services HTML
    related_html = '''
    <!-- Related Services -->
    <section class="related-services" style="padding: 60px 0; background: var(--bg-subtle);">
        <div class="container">
            <h2 style="text-align: center; margin-bottom: 40px; color: var(--charcoal);">Other Services You Might Need</h2>
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 24px;">'''
    
    for related_url in related_pages:
        if related_url in url_to_title:
            title = url_to_title[related_url]
            related_html += f'''
                <div style="background: white; padding: 24px; border-radius: var(--border-radius); box-shadow: var(--shadow-sm); text-align: center;">
                    <h3 style="margin-bottom: 12px; color: var(--charcoal);">{title}</h3>
                    <a href="{related_url}" style="color: var(--yellow-primary); text-decoration: none; font-weight: 600;">Learn More →</a>
                </div>'''
    
    related_html += '''
            </div>
        </div>
    </section>'''
    
    # Insert before footer or at end of main content
    footer_pattern = r'<footer'
    if re.search(footer_pattern, content, re.IGNORECASE):
        content = re.sub(footer_pattern, related_html + '\n\n<footer', content, flags=re.IGNORECASE)
    else:
        # Insert before closing body tag
        content = content.replace('</body>', related_html + '\n</body>')
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"✅ Added related services section to {os.path.basename(filepath)}")
    return True

def create_service_area_links():
    """Add service area cross-linking"""
    
    service_areas = [
        ('handyman-byron-bay.html', 'Byron Bay'),
        ('handyman-ballina.html', 'Ballina'), 
        ('handyman-bangalow.html', 'Bangalow'),
        ('handyman-lennox-head.html', 'Lennox Head'),
        ('handyman-mullumbimby.html', 'Mullumbimby'),
        ('handyman-ocean-shores.html', 'Ocean Shores'),
        ('handyman-tweed-heads.html', 'Tweed Heads'),
    ]
    
    for filepath, area_name in service_areas:
        full_path = f'/Users/danielneale/GoodHands_02/{filepath}'
        if not os.path.exists(full_path):
            continue
            
        with open(full_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Skip if already has area links
        if 'nearby service areas' in content.lower():
            continue
            
        # Add nearby areas section
        nearby_areas = [area for area in service_areas if area[1] != area_name][:3]
        
        nearby_html = '''
    <!-- Nearby Service Areas -->
    <section style="padding: 40px 0; background: var(--yellow-light);">
        <div class="container">
            <h3 style="text-align: center; margin-bottom: 24px;">We Also Service These Nearby Areas</h3>
            <div style="display: flex; justify-content: center; gap: 24px; flex-wrap: wrap;">'''
        
        for nearby_url, nearby_name in nearby_areas:
            nearby_html += f'''
                <a href="{nearby_url}" style="padding: 12px 24px; background: white; border-radius: var(--border-radius); color: var(--charcoal); text-decoration: none; font-weight: 600; box-shadow: var(--shadow-sm);">
                    {nearby_name}
                </a>'''
        
        nearby_html += '''
            </div>
        </div>
    </section>'''
        
        # Insert before footer
        content = re.sub(r'<footer', nearby_html + '\n\n<footer', content, flags=re.IGNORECASE)
        
        with open(full_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"✅ Added nearby areas links to {os.path.basename(filepath)}")

def main():
    """Optimize internal linking structure"""
    
    print("🔗 Optimizing Internal Linking Structure")
    print("="*60)
    
    total_links = 0
    total_sections = 0
    
    # Add contextual links
    print("Adding contextual links...")
    for filepath, links in INTERNAL_LINKS.items():
        full_path = f'/Users/danielneale/GoodHands_02/{filepath}'
        if os.path.exists(full_path):
            links_added = add_contextual_links(full_path, links)
            total_links += links_added
    
    print()
    
    # Add related services sections
    print("Adding related services sections...")
    for filepath, related in RELATED_SERVICES.items():
        full_path = f'/Users/danielneale/GoodHands_02/{filepath}'
        if os.path.exists(full_path):
            if add_related_services_section(full_path, related):
                total_sections += 1
    
    print()
    
    # Add service area cross-links
    print("Adding service area cross-links...")
    create_service_area_links()
    
    print()
    print("="*60)
    print(f"✨ Internal linking optimization complete!")
    print(f"   Contextual links added: {total_links}")
    print(f"   Related services sections: {total_sections}")
    print(f"   Service area cross-links: Added to all location pages")
    print()
    print("💡 Benefits:")
    print("   • Improved page authority distribution")
    print("   • Better user navigation flow")
    print("   • Enhanced topic clustering")
    print("   • Increased page depth and engagement")

if __name__ == "__main__":
    main()