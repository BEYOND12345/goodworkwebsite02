#!/usr/bin/env python3
"""Fix duplicate content issues for Google Search Console."""

import os
import re
from urllib.parse import urlparse

def add_canonical_tags():
    """Add canonical tags to all HTML pages."""
    html_files = [f for f in os.listdir('.') if f.endswith('.html')]
    base_url = "https://goodhandshandyman.com.au"
    files_updated = 0
    
    print("🔗 ADDING CANONICAL TAGS TO ALL PAGES")
    print("=" * 60)
    
    for file_path in html_files:
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Skip if already has canonical tag
            if 'rel="canonical"' in content or "rel='canonical'" in content:
                print(f"  ✅ {file_path} (already has canonical)")
                continue
            
            # Create canonical URL
            if file_path == 'index.html':
                canonical_url = f"{base_url}/"
            else:
                canonical_url = f"{base_url}/{file_path}"
            
            canonical_tag = f'    <link rel="canonical" href="{canonical_url}">'
            
            # Find insertion point (after last meta tag or before title)
            if '</title>' in content:
                insertion_point = content.find('</title>') + len('</title>')
                new_content = content[:insertion_point] + f"\n{canonical_tag}" + content[insertion_point:]
            elif '<meta' in content:
                # Find last meta tag
                meta_matches = list(re.finditer(r'<meta[^>]*>', content))
                if meta_matches:
                    last_meta_end = meta_matches[-1].end()
                    new_content = content[:last_meta_end] + f"\n{canonical_tag}" + content[last_meta_end:]
                else:
                    continue
            else:
                # Insert after head tag
                head_match = re.search(r'<head[^>]*>', content)
                if head_match:
                    head_end = head_match.end()
                    new_content = content[:head_end] + f"\n{canonical_tag}" + content[head_end:]
                else:
                    continue
            
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            
            print(f"  ✅ Added canonical to {file_path}")
            files_updated += 1
            
        except Exception as e:
            print(f"  ❌ Error processing {file_path}: {e}")
    
    return files_updated

def noindex_old_backup_files():
    """Add noindex tags to old/backup files to prevent duplicate content."""
    old_files = [
        'index-old-backup.html',
        'handyman-bangalow-old.html', 
        'deck-sanding-old.html',
        'fence-repairs-ballina-new.html',
        'handyman-lismore-new.html',
        'homepage-new.html',
        'master-homepage-index.html',
        'master-location-handyman-byron-bay.html',
        'master-services-overview.html',
        'master-template-gutter-cleaning.html'
    ]
    
    files_updated = 0
    
    print("\n🚫 ADDING NOINDEX TO OLD/BACKUP FILES")
    print("=" * 60)
    
    for file_path in old_files:
        if not os.path.exists(file_path):
            continue
            
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Skip if already has noindex
            if 'noindex' in content:
                print(f"  ✅ {file_path} (already noindexed)")
                continue
            
            noindex_tag = '    <meta name="robots" content="noindex, nofollow">'
            
            # Add after charset or first meta tag
            if '<meta charset' in content:
                charset_match = re.search(r'<meta charset[^>]*>', content)
                if charset_match:
                    insertion_point = charset_match.end()
                    new_content = content[:insertion_point] + f"\n{noindex_tag}" + content[insertion_point:]
                else:
                    continue
            else:
                # Add after head tag
                head_match = re.search(r'<head[^>]*>', content)
                if head_match:
                    head_end = head_match.end()
                    new_content = content[:head_end] + f"\n{noindex_tag}" + content[head_end:]
                else:
                    continue
            
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            
            print(f"  🚫 Added noindex to {file_path}")
            files_updated += 1
            
        except Exception as e:
            print(f"  ❌ Error processing {file_path}: {e}")
    
    return files_updated

def fix_duplicate_titles():
    """Fix duplicate page titles to make them unique."""
    
    title_fixes = {
        # Kingscliff area pages with same title
        'handyman-pottsville.html': 'Pottsville Handyman Services | Northern Rivers Property Care | GoodHands',
        'handyman-west-burleigh.html': 'West Burleigh Handyman | Gold Coast Property Maintenance | GoodHands',
        'handyman-casuarina.html': 'Casuarina Handyman Services | Tweed Coast Property Care | GoodHands',
        'handyman-currumbin.html': 'Currumbin Handyman | Gold Coast Valley Property Maintenance | GoodHands',
        'handyman-palm-beach.html': 'Palm Beach Handyman | Gold Coast Southern Property Care | GoodHands',
        'handyman-tallebudgera.html': 'Tallebudgera Handyman Services | Gold Coast Hinterland | GoodHands',
        'handyman-miami.html': 'Miami Handyman | Gold Coast Beachside Property Care | GoodHands',
        'handyman-elanora.html': 'Elanora Handyman Services | Gold Coast Forest Property Care | GoodHands',
        
        # Service pages with duplicate titles
        'bathroom-repairs.html': 'Bathroom Repairs Northern Rivers | Plumbing & Tiling Services | GoodHands',
        'holiday-rental-maintenance.html': 'Holiday Rental Maintenance | Airbnb Property Care Northern Rivers | GoodHands',
        'tv-wall-mounting.html': 'TV Wall Mounting Services | Professional Installation Northern Rivers | GoodHands',
        'door-repairs.html': 'Door Repairs Northern Rivers | Hardware & Flyscreen Services | GoodHands',
        'power-washing.html': 'Power Washing Services | Pressure Cleaning Northern Rivers | GoodHands',
        
        # Gutter cleaning duplicates
        'gutter-cleaning-northern-rivers.html': 'Gutter Cleaning Northern Rivers | Professional Gutter Services | GoodHands',
        'master-template-gutter-cleaning.html': 'Template: Gutter Cleaning Services | GoodHands (NOINDEX)',
        
        # Fence repair duplicates
        'fence-repairs-ballina-new.html': 'Ballina Fence Repairs NEW | Professional Fencing Services | GoodHands (NOINDEX)',
        
        # Homepage duplicates
        'homepage-new.html': 'GoodHands Homepage NEW | Northern Rivers Handyman (NOINDEX)',
        
        # Lismore duplicates
        'handyman-lismore-new.html': 'Lismore Handyman NEW | Post-Flood Restoration Specialist (NOINDEX)',
    }
    
    files_updated = 0
    
    print("\n📄 FIXING DUPLICATE PAGE TITLES")
    print("=" * 60)
    
    for file_path, new_title in title_fixes.items():
        if not os.path.exists(file_path):
            continue
            
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Replace title
            title_pattern = r'<title>([^<]*)</title>'
            if re.search(title_pattern, content):
                new_content = re.sub(title_pattern, f'<title>{new_title}</title>', content)
                
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                
                print(f"  📝 Updated title: {file_path}")
                files_updated += 1
            
        except Exception as e:
            print(f"  ❌ Error processing {file_path}: {e}")
    
    return files_updated

def clean_up_master_templates():
    """Add noindex to master template files."""
    template_files = [
        'master-homepage-index.html',
        'master-location-handyman-byron-bay.html', 
        'master-services-overview.html',
        'master-template-gutter-cleaning.html'
    ]
    
    files_updated = 0
    
    print("\n🎭 NOINDEXING MASTER TEMPLATE FILES")
    print("=" * 60)
    
    for file_path in template_files:
        if not os.path.exists(file_path):
            continue
            
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Skip if already noindexed
            if 'noindex' in content:
                print(f"  ✅ {file_path} (already noindexed)")
                continue
            
            # Add noindex tag
            noindex_tag = '    <meta name="robots" content="noindex, nofollow">'
            
            if '<meta charset' in content:
                charset_match = re.search(r'<meta charset[^>]*>', content)
                if charset_match:
                    insertion_point = charset_match.end()
                    new_content = content[:insertion_point] + f"\n{noindex_tag}" + content[insertion_point:]
                    
                    with open(file_path, 'w', encoding='utf-8') as f:
                        f.write(new_content)
                    
                    print(f"  🚫 Added noindex to template: {file_path}")
                    files_updated += 1
            
        except Exception as e:
            print(f"  ❌ Error processing {file_path}: {e}")
    
    return files_updated

def main():
    """Main function to fix duplicate content issues."""
    print("🔧 FIXING GOOGLE SEARCH CONSOLE DUPLICATE CONTENT ISSUES")
    print("=" * 70)
    
    # Add canonical tags
    canonical_count = add_canonical_tags()
    
    # Noindex old/backup files
    noindex_count = noindex_old_backup_files()
    
    # Fix duplicate titles
    title_count = fix_duplicate_titles()
    
    # Clean up master templates
    template_count = clean_up_master_templates()
    
    print(f"\n📊 SUMMARY OF FIXES APPLIED")
    print("=" * 60)
    print(f"Canonical tags added: {canonical_count}")
    print(f"Files noindexed: {noindex_count + template_count}")
    print(f"Duplicate titles fixed: {title_count}")
    
    total_fixes = canonical_count + noindex_count + title_count + template_count
    
    if total_fixes > 0:
        print(f"\n🎉 DUPLICATE CONTENT FIXES COMPLETED!")
        print(f"Total files updated: {total_fixes}")
        print("\n📝 Next Steps:")
        print("  1. Submit updated sitemap to Google Search Console")
        print("  2. Request re-indexing of main pages")
        print("  3. Monitor 'Duplicate without user-selected canonical' reports")
        print("  4. Check rankings improvement in 1-2 weeks")
    else:
        print(f"\n⚠️ No fixes applied - check file permissions or paths")

if __name__ == "__main__":
    main()