#!/usr/bin/env python3
"""Fix broken schema markup across all HTML files."""

import os
import re
import glob

def fix_schema_markup(file_path):
    """Fix broken schema markup in a single file."""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Fix broken schema tags like <script type="application/ld+json">type="application/ld+json"</script>
    broken_pattern = r'<script type="application/ld\+json">type="application/ld\+json"</script>'
    
    # Count occurrences
    matches = re.findall(broken_pattern, content)
    if not matches:
        return False, 0
    
    # Replace with proper LocalBusiness schema
    schema_replacement = '''<script type="application/ld+json">
    {
        "@context": "https://schema.org",
        "@type": "LocalBusiness",
        "name": "GoodHands Handyman",
        "description": "Professional handyman services across Northern Rivers NSW",
        "address": {
            "@type": "PostalAddress",
            "addressLocality": "Northern Rivers",
            "addressRegion": "NSW",
            "addressCountry": "AU"
        },
        "telephone": "+61481457271",
        "email": "info@goodhandshandyman.com.au",
        "url": "https://goodhandshandyman.com.au",
        "@id": "https://www.google.com/maps/place/?cid=12688451943747857598"
    }
    </script>'''
    
    # Replace first occurrence with proper schema
    content = re.sub(broken_pattern, schema_replacement, content, count=1)
    
    # Remove any additional broken schemas
    content = re.sub(broken_pattern, '', content)
    
    # Write back
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    return True, len(matches)

def main():
    """Fix schema markup in all HTML files."""
    html_files = glob.glob('*.html')
    fixed_files = 0
    total_fixes = 0
    
    print("🔧 FIXING SCHEMA MARKUP ACROSS WEBSITE")
    print("=" * 50)
    
    for file_path in html_files:
        was_fixed, fix_count = fix_schema_markup(file_path)
        if was_fixed:
            fixed_files += 1
            total_fixes += fix_count
            print(f"✅ Fixed {fix_count} schema issues in {file_path}")
    
    print("\n📊 SUMMARY")
    print("=" * 50)
    print(f"Files processed: {len(html_files)}")
    print(f"Files fixed: {fixed_files}")
    print(f"Total schema issues fixed: {total_fixes}")
    
    if fixed_files > 0:
        print("\n🎉 Schema markup fixes completed successfully!")
    else:
        print("\n✅ No broken schema markup found.")

if __name__ == "__main__":
    main()