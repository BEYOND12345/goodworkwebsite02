#!/usr/bin/env python3
"""Final website updates and optimizations for Good Hands Handyman website."""

import os
import re
import glob
from pathlib import Path

def add_missing_mobile_js():
    """Add mobile menu JavaScript to pages that are missing it."""
    mobile_js = '''
    <script>
    // Mobile Menu Toggle
    document.addEventListener('DOMContentLoaded', function() {
        const mobileMenuBtn = document.querySelector('.mobile-menu-btn');
        const mobileMenu = document.querySelector('.mobile-menu');
        
        if (mobileMenuBtn && mobileMenu) {
            mobileMenuBtn.addEventListener('click', function() {
                mobileMenu.classList.toggle('active');
                
                // Animate hamburger icon
                const spans = mobileMenuBtn.querySelectorAll('span');
                spans.forEach(span => span.classList.toggle('active'));
            });
            
            // Close menu when clicking outside
            document.addEventListener('click', function(e) {
                if (!mobileMenuBtn.contains(e.target) && !mobileMenu.contains(e.target)) {
                    mobileMenu.classList.remove('active');
                    const spans = mobileMenuBtn.querySelectorAll('span');
                    spans.forEach(span => span.classList.remove('active'));
                }
            });
        }
    });
    </script>
    '''
    
    files_updated = 0
    
    for file_path in glob.glob('*.html'):
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Skip if already has mobile JS or doesn't have mobile menu
        if 'mobile-menu-btn' not in content or 'Mobile Menu Toggle' in content:
            continue
            
        # Add before closing body tag
        if '</body>' in content:
            content = content.replace('</body>', f'{mobile_js}\n</body>')
            
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            files_updated += 1
    
    return files_updated

def fix_meta_descriptions_with_html():
    """Remove HTML tags from meta descriptions."""
    files_fixed = 0
    
    for file_path in glob.glob('*.html'):
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Find meta descriptions with HTML tags
        meta_pattern = r'<meta name="description" content="([^"]*<[^>]*>[^"]*)">'
        matches = re.findall(meta_pattern, content)
        
        if matches:
            for match in matches:
                # Remove HTML tags from meta description
                clean_description = re.sub(r'<[^>]*>', '', match)
                old_meta = f'<meta name="description" content="{match}">'
                new_meta = f'<meta name="description" content="{clean_description}">'
                content = content.replace(old_meta, new_meta)
            
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            files_fixed += 1
    
    return files_fixed

def optimize_lazy_loading():
    """Add lazy loading to images that don't have it."""
    files_updated = 0
    
    for file_path in glob.glob('*.html'):
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Find img tags without lazy loading
        img_pattern = r'<img\s+([^>]*?)(?<!loading="lazy")(?<!loading=\'lazy\')>'
        
        def add_lazy_loading(match):
            img_attrs = match.group(1)
            # Skip if already has loading attribute or if it's likely a critical image
            if 'loading=' in img_attrs or 'hero' in img_attrs.lower():
                return match.group(0)
            return f'<img {img_attrs} loading="lazy">'
        
        new_content = re.sub(img_pattern, add_lazy_loading, content)
        
        if new_content != content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            files_updated += 1
    
    return files_updated

def fix_missing_alt_tags():
    """Add alt tags to images that are missing them."""
    files_updated = 0
    
    for file_path in glob.glob('*.html'):
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Find img tags without alt attributes
        img_pattern = r'<img\s+([^>]*?)(?<!alt="[^"]*")(?<!alt=\'[^\']*\')>'
        
        def add_alt_tag(match):
            img_attrs = match.group(1)
            if 'alt=' in img_attrs:
                return match.group(0)
            
            # Extract filename for generic alt text
            src_match = re.search(r'src="([^"]*)"', img_attrs)
            if src_match:
                filename = src_match.group(1).split('/')[-1].split('.')[0]
                alt_text = filename.replace('-', ' ').replace('_', ' ').title()
                return f'<img {img_attrs} alt="{alt_text}">'
            
            return f'<img {img_attrs} alt="GoodHands Handyman Service">'
        
        new_content = re.sub(img_pattern, add_alt_tag, content)
        
        if new_content != content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            files_updated += 1
    
    return files_updated

def validate_internal_links():
    """Check for broken internal links."""
    html_files = set(f for f in glob.glob('*.html'))
    broken_links = []
    
    for file_path in html_files:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Find internal HTML links
        link_pattern = r'href="([^"]*\.html)"'
        matches = re.findall(link_pattern, content)
        
        for link in matches:
            if link.startswith('http') or link.startswith('#'):
                continue
                
            target_file = link.split('#')[0]  # Remove anchor
            if target_file not in html_files:
                broken_links.append((file_path, link))
    
    return broken_links

def main():
    """Run all final updates."""
    print("🔧 FINAL WEBSITE UPDATES FOR GOOD HANDS HANDYMAN")
    print("=" * 60)
    
    # Add mobile JavaScript
    mobile_updates = add_missing_mobile_js()
    print(f"✅ Mobile JS added to {mobile_updates} files")
    
    # Fix meta descriptions with HTML
    meta_fixes = fix_meta_descriptions_with_html()
    print(f"✅ Meta descriptions fixed in {meta_fixes} files")
    
    # Optimize lazy loading
    lazy_updates = optimize_lazy_loading()
    print(f"✅ Lazy loading added to {lazy_updates} files")
    
    # Fix missing alt tags
    alt_updates = fix_missing_alt_tags()
    print(f"✅ Alt tags added to {alt_updates} files")
    
    # Validate internal links
    broken_links = validate_internal_links()
    if broken_links:
        print(f"⚠️  Found {len(broken_links)} broken internal links:")
        for file_path, link in broken_links[:10]:  # Show first 10
            print(f"   {file_path}: {link}")
    else:
        print("✅ No broken internal links found")
    
    print("\n📊 SUMMARY")
    print("=" * 60)
    total_updates = mobile_updates + meta_fixes + lazy_updates + alt_updates
    print(f"Total files updated: {total_updates}")
    print(f"Website health: {'✅ EXCELLENT' if not broken_links else '⚠️  NEEDS ATTENTION'}")
    
    if total_updates > 0:
        print("\n🎉 Website updates completed successfully!")
        print("📈 Performance and SEO improvements applied")
    else:
        print("\n✅ Website already optimized - no updates needed")

if __name__ == "__main__":
    main()