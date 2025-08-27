#!/usr/bin/env python3
"""
CSS Minification Script for Speed Optimization
Minifies all CSS across the website to reduce file sizes
"""

import os
import re
import glob
from pathlib import Path

def minify_css_content(css_content):
    """Minify CSS content by removing unnecessary characters"""
    # Remove comments
    css_content = re.sub(r'/\*.*?\*/', '', css_content, flags=re.DOTALL)
    
    # Remove extra whitespace
    css_content = re.sub(r'\s+', ' ', css_content)
    
    # Remove spaces around certain characters
    css_content = re.sub(r'\s*([{}:;,>+~])\s*', r'\1', css_content)
    
    # Remove trailing semicolons before closing braces
    css_content = re.sub(r';\s*}', '}', css_content)
    
    # Remove empty rules
    css_content = re.sub(r'[^{}]+{\s*}', '', css_content)
    
    # Remove leading/trailing whitespace
    css_content = css_content.strip()
    
    return css_content

def minify_inline_css_in_html(html_content):
    """Minify inline CSS within HTML files"""
    def minify_style_block(match):
        css_content = match.group(1)
        minified_css = minify_css_content(css_content)
        return f'<style>{minified_css}</style>'
    
    # Minify content within <style> tags
    html_content = re.sub(r'<style[^>]*>(.*?)</style>', minify_style_block, html_content, flags=re.DOTALL | re.IGNORECASE)
    
    return html_content

def process_css_files():
    """Process standalone CSS files"""
    css_files = glob.glob('/Users/danielneale/GoodHands_02/**/*.css', recursive=True)
    total_original_size = 0
    total_minified_size = 0
    
    print("=== PROCESSING STANDALONE CSS FILES ===")
    
    for css_file in css_files:
        try:
            with open(css_file, 'r', encoding='utf-8') as f:
                original_content = f.read()
            
            original_size = len(original_content.encode('utf-8'))
            minified_content = minify_css_content(original_content)
            minified_size = len(minified_content.encode('utf-8'))
            
            # Only write if there's actual minification benefit
            if minified_size < original_size:
                with open(css_file, 'w', encoding='utf-8') as f:
                    f.write(minified_content)
                
                reduction = ((original_size - minified_size) / original_size) * 100
                print(f"✅ {css_file}: {original_size} → {minified_size} bytes ({reduction:.1f}% reduction)")
                
                total_original_size += original_size
                total_minified_size += minified_size
            else:
                print(f"➖ {css_file}: Already optimized")
                
        except Exception as e:
            print(f"❌ Error processing {css_file}: {e}")
    
    return total_original_size, total_minified_size

def process_html_files():
    """Process inline CSS in HTML files"""
    html_files = glob.glob('/Users/danielneale/GoodHands_02/*.html')
    total_original_size = 0
    total_minified_size = 0
    files_processed = 0
    
    print("\n=== PROCESSING INLINE CSS IN HTML FILES ===")
    
    for html_file in html_files:
        try:
            with open(html_file, 'r', encoding='utf-8') as f:
                original_content = f.read()
            
            # Check if file has inline CSS
            if '<style' not in original_content.lower():
                continue
                
            original_size = len(original_content.encode('utf-8'))
            minified_content = minify_inline_css_in_html(original_content)
            minified_size = len(minified_content.encode('utf-8'))
            
            if minified_size < original_size:
                with open(html_file, 'w', encoding='utf-8') as f:
                    f.write(minified_content)
                
                reduction = ((original_size - minified_size) / original_size) * 100
                print(f"✅ {os.path.basename(html_file)}: {original_size} → {minified_size} bytes ({reduction:.1f}% reduction)")
                
                total_original_size += original_size
                total_minified_size += minified_size
                files_processed += 1
            else:
                print(f"➖ {os.path.basename(html_file)}: No CSS minification needed")
                
        except Exception as e:
            print(f"❌ Error processing {html_file}: {e}")
    
    return total_original_size, total_minified_size, files_processed

def main():
    """Main minification process"""
    print("🚀 STARTING CSS MINIFICATION FOR SPEED OPTIMIZATION")
    print("=" * 60)
    
    # Process standalone CSS files
    css_original, css_minified = process_css_files()
    
    # Process inline CSS in HTML files
    html_original, html_minified, html_count = process_html_files()
    
    # Calculate totals
    total_original = css_original + html_original
    total_minified = css_minified + html_minified
    
    print("\n" + "=" * 60)
    print("📊 CSS MINIFICATION RESULTS")
    print("=" * 60)
    
    if total_original > 0:
        total_reduction = ((total_original - total_minified) / total_original) * 100
        savings_kb = (total_original - total_minified) / 1024
        
        print(f"📁 Standalone CSS files: {css_original} → {css_minified} bytes")
        print(f"📄 HTML inline CSS: {html_original} → {html_minified} bytes ({html_count} files)")
        print(f"💾 Total CSS reduction: {total_original} → {total_minified} bytes")
        print(f"📈 Overall reduction: {total_reduction:.1f}% ({savings_kb:.1f}KB saved)")
        print(f"⚡ Speed benefit: Reduced CSS parse time and network transfer")
        
        if total_reduction > 20:
            print("🎉 EXCELLENT: Significant CSS size reduction achieved!")
        elif total_reduction > 10:
            print("✅ GOOD: Meaningful CSS optimization completed")
        else:
            print("📋 MINIMAL: CSS was already well-optimized")
    else:
        print("📋 No CSS files found to minify")
    
    print("\n🎯 Next: JavaScript minification and performance optimizations")

if __name__ == "__main__":
    main()