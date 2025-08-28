#!/usr/bin/env python3
"""Fix broken internal links causing 404 errors."""

import os
import re

def fix_broken_links():
    """Fix broken internal links by replacing them with existing pages or removing them."""
    
    # Map broken links to existing alternatives or None to remove
    link_fixes = {
        # Service pages that don't exist - map to existing services
        'kitchen-cupboard-door-wont-close-byron-bay.html': 'kitchen-door-repairs-northern-rivers.html',
        'deck-looks-grey-splintery-byron-bay.html': 'deck-restoration-byron-bay.html',
        'flyscreen-repairs.html': 'door-repairs.html',
        'property-maintenance.html': 'handyman-services-byron-bay.html',
        'security-installation.html': 'handyman-services-byron-bay.html',
        
        # Location pages that don't exist - map to existing locations or remove
        'handyman-brunswick-heads.html': 'handyman-byron-bay.html',
        'handyman-suffolk-park.html': 'handyman-byron-bay.html',
        'handyman-federal.html': 'handyman-lismore.html',
        'handyman-nimbin.html': 'handyman-lismore.html',
        'handyman-casino.html': 'handyman-lismore.html',
        'handyman-kingscliff.html': 'handyman-tweed-heads.html',
        'handyman-murwillumbah.html': 'handyman-tweed-heads.html',
        'handyman-evans-head.html': 'handyman-ballina.html',
        'handyman-south-golden-beach.html': 'handyman-ocean-shores.html',
        
        # Pages that might be referenced but don't exist
        'tv-mounting.html': 'tv-wall-mounting.html',
        'gutter-repairs.html': 'gutter-cleaning.html',
    }
    
    html_files = [f for f in os.listdir('.') if f.endswith('.html')]
    files_fixed = 0
    links_fixed = 0
    
    for file_path in html_files:
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            original_content = content
            
            # Fix each broken link
            for broken_link, replacement in link_fixes.items():
                if broken_link in content:
                    if replacement:
                        content = content.replace(f'href="{broken_link}"', f'href="{replacement}"')
                        content = content.replace(f"href='{broken_link}'", f"href='{replacement}'")
                        print(f"✅ Fixed: {broken_link} → {replacement} in {file_path}")
                        links_fixed += 1
                    else:
                        # Remove the entire link element if no replacement
                        link_pattern = rf'<a[^>]*href=["\'][^"\']*{re.escape(broken_link)}["\'][^>]*>.*?</a>'
                        matches = re.findall(link_pattern, content, re.IGNORECASE | re.DOTALL)
                        if matches:
                            for match in matches:
                                content = content.replace(match, '')
                                print(f"🗑️ Removed broken link: {broken_link} from {file_path}")
                                links_fixed += 1
            
            # Write back if content changed
            if content != original_content:
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(content)
                files_fixed += 1
        
        except Exception as e:
            print(f"Error processing {file_path}: {e}")
    
    return files_fixed, links_fixed

def create_missing_service_area_pages():
    """Create basic pages for missing service areas to prevent future 404s."""
    
    # Template for location pages
    location_template = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Handyman {location} | Professional Property Maintenance | GoodHands</title>
    <meta name="description" content="Professional handyman services in {location}. Property maintenance, repairs, renovations. Call 0481 457271 for reliable service.">
    <meta name="robots" content="noindex, follow">
    
    <script type="application/ld+json">
    {{
        "@context": "https://schema.org",
        "@type": "LocalBusiness",
        "name": "GoodHands Handyman",
        "description": "Professional handyman services in {location}",
        "address": {{
            "@type": "PostalAddress",
            "addressLocality": "{location}",
            "addressRegion": "NSW", 
            "addressCountry": "AU"
        }},
        "telephone": "+61481457271",
        "email": "info@goodhandshandyman.com.au",
        "url": "https://goodhandshandyman.com.au"
    }}
    </script>
</head>
<body>
    <h1>Handyman Services {location}</h1>
    <p>Professional handyman services available in {location}. Please <a href="contact.html">contact us</a> for availability.</p>
    <p><a href="index.html">← Back to Home</a></p>
</body>
</html>'''
    
    # Basic service area locations that might be needed
    missing_locations = [
        'Brunswick Heads',
        'Suffolk Park', 
        'Federal',
        'Nimbin',
        'Casino',
        'Evans Head',
        'South Golden Beach'
    ]
    
    pages_created = 0
    
    for location in missing_locations:
        filename = f"handyman-{location.lower().replace(' ', '-')}.html"
        if not os.path.exists(filename):
            content = location_template.format(location=location)
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"📄 Created: {filename}")
            pages_created += 1
    
    return pages_created

def main():
    """Main function to fix 404 errors."""
    print("🔧 FIXING 404 ERRORS - BROKEN INTERNAL LINKS")
    print("=" * 60)
    
    # Fix broken links
    files_fixed, links_fixed = fix_broken_links()
    
    print(f"\n📊 BROKEN LINKS FIXED:")
    print(f"Files updated: {files_fixed}")
    print(f"Links fixed: {links_fixed}")
    
    # Optionally create missing pages (commented out to avoid cluttering)
    # pages_created = create_missing_service_area_pages()
    # print(f"New pages created: {pages_created}")
    
    if files_fixed > 0:
        print("\n✅ 404 Error fixes completed!")
        print("📝 Next steps:")
        print("   1. Test the website for broken links")
        print("   2. Submit updated sitemap to Google Search Console")
        print("   3. Request re-crawling of affected pages")
    else:
        print("\n⚠️ No broken links found to fix")

if __name__ == "__main__":
    main()