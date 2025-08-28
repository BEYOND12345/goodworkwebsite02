#!/usr/bin/env python3
"""Check for 404 errors by verifying sitemap URLs against actual files."""

import os
import re
import xml.etree.ElementTree as ET

def extract_urls_from_sitemap():
    """Extract all URLs from sitemap.xml"""
    try:
        tree = ET.parse('sitemap.xml')
        root = tree.getroot()
        
        # Handle XML namespace
        namespace = {'ns': 'http://www.sitemaps.org/schemas/sitemap/0.9'}
        urls = []
        
        for url in root.findall('ns:url', namespace):
            loc = url.find('ns:loc', namespace)
            if loc is not None:
                urls.append(loc.text)
        
        return urls
    except Exception as e:
        print(f"Error reading sitemap: {e}")
        return []

def check_file_exists(url):
    """Check if the HTML file exists for a given URL"""
    # Extract filename from URL
    if url.endswith('/'):
        filename = 'index.html'
    else:
        filename = url.split('/')[-1]
        if not filename.endswith('.html'):
            filename += '.html'
    
    return os.path.exists(filename), filename

def find_missing_pages():
    """Find pages listed in sitemap that don't exist as files"""
    urls = extract_urls_from_sitemap()
    missing_pages = []
    existing_pages = []
    
    print("🔍 CHECKING SITEMAP URLs AGAINST ACTUAL FILES")
    print("=" * 60)
    
    for url in urls:
        exists, filename = check_file_exists(url)
        if exists:
            existing_pages.append((url, filename))
        else:
            missing_pages.append((url, filename))
    
    return missing_pages, existing_pages

def check_internal_links():
    """Check for broken internal links in HTML files"""
    html_files = [f for f in os.listdir('.') if f.endswith('.html')]
    broken_links = []
    
    print("\n🔗 CHECKING INTERNAL LINKS")
    print("=" * 60)
    
    for file_path in html_files:
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Find all href links to HTML files
            link_pattern = r'href=["\']([^"\']*\.html)["\']'
            matches = re.findall(link_pattern, content)
            
            for link in matches:
                # Skip external links and anchors
                if link.startswith('http') or link.startswith('#'):
                    continue
                
                # Check if target file exists
                target_file = link.split('#')[0]  # Remove anchor part
                if not os.path.exists(target_file):
                    broken_links.append((file_path, link))
        
        except Exception as e:
            print(f"Error checking {file_path}: {e}")
    
    return broken_links

def main():
    """Main function to check for 404 errors"""
    print("🚨 GOOGLE SEARCH CONSOLE 404 ERROR INVESTIGATION")
    print("=" * 60)
    
    # Check sitemap vs actual files
    missing_pages, existing_pages = find_missing_pages()
    
    if missing_pages:
        print(f"\n❌ MISSING PAGES ({len(missing_pages)} found):")
        print("=" * 40)
        for url, filename in missing_pages:
            print(f"  Missing: {filename}")
            print(f"  URL: {url}")
            print()
    else:
        print("\n✅ All sitemap URLs have corresponding files")
    
    # Check internal links
    broken_links = check_internal_links()
    
    if broken_links:
        print(f"\n🔗 BROKEN INTERNAL LINKS ({len(broken_links)} found):")
        print("=" * 40)
        for source_file, broken_link in broken_links[:10]:  # Show first 10
            print(f"  In file: {source_file}")
            print(f"  Broken link: {broken_link}")
            print()
        
        if len(broken_links) > 10:
            print(f"  ... and {len(broken_links) - 10} more broken links")
    else:
        print("\n✅ No broken internal links found")
    
    print(f"\n📊 SUMMARY")
    print("=" * 40)
    print(f"Total sitemap URLs: {len(existing_pages) + len(missing_pages)}")
    print(f"Existing files: {len(existing_pages)}")
    print(f"Missing files: {len(missing_pages)}")
    print(f"Broken internal links: {len(broken_links)}")
    
    if missing_pages or broken_links:
        print("\n⚠️  ACTION REQUIRED:")
        if missing_pages:
            print("  1. Remove missing URLs from sitemap.xml")
            print("  2. Or create the missing HTML files")
        if broken_links:
            print("  3. Fix broken internal links")
        print("  4. Submit updated sitemap to Google Search Console")
    else:
        print("\n🎉 No 404 errors found - sitemap and links are clean!")

if __name__ == "__main__":
    main()