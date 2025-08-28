#!/usr/bin/env python3
"""Analyze duplicate content and canonical tag issues for Google Search Console."""

import os
import re
from collections import defaultdict
import hashlib

def get_page_content_hash(file_path):
    """Get a hash of the main content (excluding nav/footer)."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Extract main content (rough approach)
        # Remove common elements that appear on all pages
        patterns_to_remove = [
            r'<header.*?</header>',
            r'<nav.*?</nav>', 
            r'<footer.*?</footer>',
            r'<script.*?</script>',
            r'<style.*?</style>',
            r'<meta.*?>',
            r'<link.*?>',
            r'<title>.*?</title>'
        ]
        
        main_content = content
        for pattern in patterns_to_remove:
            main_content = re.sub(pattern, '', main_content, flags=re.DOTALL | re.IGNORECASE)
        
        # Get hash of remaining content
        return hashlib.md5(main_content.encode()).hexdigest()
        
    except Exception as e:
        return None

def find_potential_duplicates():
    """Find pages with similar content."""
    html_files = [f for f in os.listdir('.') if f.endswith('.html')]
    content_hashes = {}
    duplicate_groups = defaultdict(list)
    
    print("🔍 ANALYZING PAGE CONTENT FOR DUPLICATES")
    print("=" * 60)
    
    for file_path in html_files:
        content_hash = get_page_content_hash(file_path)
        if content_hash:
            if content_hash in content_hashes:
                # Found potential duplicate
                if content_hash not in duplicate_groups:
                    duplicate_groups[content_hash].append(content_hashes[content_hash])
                duplicate_groups[content_hash].append(file_path)
            else:
                content_hashes[content_hash] = file_path
    
    return duplicate_groups

def check_canonical_tags():
    """Check which pages have canonical tags."""
    html_files = [f for f in os.listdir('.') if f.endswith('.html')]
    pages_with_canonical = []
    pages_without_canonical = []
    
    print("\n🔗 CANONICAL TAG ANALYSIS")
    print("=" * 60)
    
    for file_path in html_files:
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            if 'rel="canonical"' in content or "rel='canonical'" in content:
                pages_with_canonical.append(file_path)
            else:
                pages_without_canonical.append(file_path)
        except Exception as e:
            print(f"Error reading {file_path}: {e}")
    
    return pages_with_canonical, pages_without_canonical

def identify_old_backup_pages():
    """Identify pages that might be old/backup versions."""
    html_files = [f for f in os.listdir('.') if f.endswith('.html')]
    
    potential_duplicates = {
        'old_versions': [],
        'backup_versions': [],
        'new_versions': [],
        'similar_names': defaultdict(list)
    }
    
    print("\n📁 IDENTIFYING POTENTIAL DUPLICATE FILES")
    print("=" * 60)
    
    for file_path in html_files:
        # Check for obvious old/backup patterns
        if '-old' in file_path:
            potential_duplicates['old_versions'].append(file_path)
        elif 'backup' in file_path:
            potential_duplicates['backup_versions'].append(file_path)
        elif '-new' in file_path:
            potential_duplicates['new_versions'].append(file_path)
        
        # Group similar names
        base_name = re.sub(r'-?(old|new|backup)(-.*)?\.html$', '.html', file_path)
        if base_name != file_path:
            potential_duplicates['similar_names'][base_name].append(file_path)
    
    return potential_duplicates

def check_title_duplicates():
    """Check for duplicate page titles."""
    html_files = [f for f in os.listdir('.') if f.endswith('.html')]
    title_groups = defaultdict(list)
    
    print("\n📄 CHECKING FOR DUPLICATE PAGE TITLES")
    print("=" * 60)
    
    for file_path in html_files:
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            title_match = re.search(r'<title>(.*?)</title>', content, re.IGNORECASE)
            if title_match:
                title = title_match.group(1).strip()
                title_groups[title].append(file_path)
        except Exception as e:
            pass
    
    # Find duplicate titles
    duplicate_titles = {title: files for title, files in title_groups.items() if len(files) > 1}
    
    return duplicate_titles

def main():
    """Main analysis function."""
    print("🔍 GOOGLE SEARCH CONSOLE DUPLICATE CONTENT ANALYSIS")
    print("=" * 70)
    
    # Check canonical tags
    with_canonical, without_canonical = check_canonical_tags()
    
    print(f"Pages WITH canonical tags: {len(with_canonical)}")
    if with_canonical:
        for page in with_canonical[:5]:
            print(f"  ✅ {page}")
        if len(with_canonical) > 5:
            print(f"  ... and {len(with_canonical) - 5} more")
    
    print(f"\nPages WITHOUT canonical tags: {len(without_canonical)}")
    if without_canonical:
        for page in without_canonical[:10]:
            print(f"  ❌ {page}")
        if len(without_canonical) > 10:
            print(f"  ... and {len(without_canonical) - 10} more")
    
    # Check for old/backup files
    potential_dupes = identify_old_backup_pages()
    
    if potential_dupes['old_versions']:
        print(f"\n📁 OLD VERSION FILES ({len(potential_dupes['old_versions'])}):")
        for file in potential_dupes['old_versions']:
            print(f"  🗂️ {file}")
    
    if potential_dupes['backup_versions']:
        print(f"\n📁 BACKUP VERSION FILES ({len(potential_dupes['backup_versions'])}):")
        for file in potential_dupes['backup_versions']:
            print(f"  🗂️ {file}")
    
    if potential_dupes['new_versions']:
        print(f"\n📁 NEW VERSION FILES ({len(potential_dupes['new_versions'])}):")
        for file in potential_dupes['new_versions']:
            print(f"  🗂️ {file}")
    
    # Check for similar names
    similar_groups = {k: v for k, v in potential_dupes['similar_names'].items() if len(v) > 0}
    if similar_groups:
        print(f"\n📁 SIMILAR FILENAME GROUPS:")
        for base, versions in similar_groups.items():
            print(f"  Base: {base}")
            for version in versions:
                print(f"    🔄 {version}")
    
    # Check for duplicate titles
    duplicate_titles = check_title_duplicates()
    if duplicate_titles:
        print(f"\n📄 DUPLICATE PAGE TITLES ({len(duplicate_titles)} groups):")
        for title, files in duplicate_titles.items():
            print(f"  Title: {title[:60]}...")
            for file in files:
                print(f"    📄 {file}")
    
    print(f"\n📊 SUMMARY")
    print("=" * 60)
    print(f"Total HTML files: {len(without_canonical) + len(with_canonical)}")
    print(f"Missing canonical tags: {len(without_canonical)} ({len(without_canonical)/(len(without_canonical) + len(with_canonical))*100:.1f}%)")
    print(f"Old/backup files: {len(potential_dupes['old_versions']) + len(potential_dupes['backup_versions'])}")
    print(f"Duplicate titles: {len(duplicate_titles)}")
    
    print(f"\n🚨 CRITICAL ISSUES:")
    if len(without_canonical) > 60:
        print("  ❌ Most pages missing canonical tags")
    if potential_dupes['old_versions'] or potential_dupes['backup_versions']:
        print("  ❌ Old/backup files may cause duplicate content")
    if duplicate_titles:
        print("  ❌ Multiple pages with same titles")
    
    print(f"\n💡 RECOMMENDED ACTIONS:")
    print("  1. Add canonical tags to all pages")
    print("  2. Remove or noindex old/backup files")
    print("  3. Fix duplicate page titles")
    print("  4. Review similar content for consolidation")

if __name__ == "__main__":
    main()