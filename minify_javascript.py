#!/usr/bin/env python3
"""
JavaScript Minification Script for Speed Optimization
Minifies all JavaScript across the website to reduce file sizes
"""

import os
import re
import glob
from pathlib import Path

def minify_js_content(js_content):
    """Basic JavaScript minification"""
    # Remove single-line comments (but preserve URLs)
    js_content = re.sub(r'(?<!:)//.*$', '', js_content, flags=re.MULTILINE)
    
    # Remove multi-line comments
    js_content = re.sub(r'/\*.*?\*/', '', js_content, flags=re.DOTALL)
    
    # Remove extra whitespace and line breaks
    js_content = re.sub(r'\s+', ' ', js_content)
    
    # Remove spaces around operators and punctuation
    js_content = re.sub(r'\s*([{}();,=+\-*/<>!&|?:])\s*', r'\1', js_content)
    
    # Remove spaces after 'function', 'if', 'for', 'while', etc.
    js_content = re.sub(r'(function|if|for|while|switch|catch)\s+', r'\1', js_content)
    
    # Remove trailing semicolons before closing braces
    js_content = re.sub(r';\s*}', '}', js_content)
    
    # Clean up extra spaces
    js_content = re.sub(r'\s+', ' ', js_content)
    
    # Remove leading/trailing whitespace
    js_content = js_content.strip()
    
    return js_content

def minify_inline_js_in_html(html_content):
    """Minify inline JavaScript within HTML files"""
    def minify_script_block(match):
        js_content = match.group(1)
        # Skip if it's JSON-LD or other structured data
        if '"@context"' in js_content or '"@type"' in js_content:
            return match.group(0)
        
        minified_js = minify_js_content(js_content)
        return f'<script{match.group(0)[7:match.group(0).find(">")]}>{minified_js}</script>'
    
    # Minify content within <script> tags (excluding JSON-LD)
    html_content = re.sub(r'<script([^>]*)>(.*?)</script>', minify_script_block, html_content, flags=re.DOTALL | re.IGNORECASE)
    
    return html_content

def process_js_files():
    """Process standalone JavaScript files"""
    js_files = glob.glob('/Users/danielneale/GoodHands_02/**/*.js', recursive=True)
    total_original_size = 0
    total_minified_size = 0
    
    print("=== PROCESSING STANDALONE JAVASCRIPT FILES ===")
    
    for js_file in js_files:
        try:
            with open(js_file, 'r', encoding='utf-8') as f:
                original_content = f.read()
            
            original_size = len(original_content.encode('utf-8'))
            minified_content = minify_js_content(original_content)
            minified_size = len(minified_content.encode('utf-8'))
            
            # Only write if there's actual minification benefit
            if minified_size < original_size:
                with open(js_file, 'w', encoding='utf-8') as f:
                    f.write(minified_content)
                
                reduction = ((original_size - minified_size) / original_size) * 100
                print(f"✅ {js_file}: {original_size} → {minified_size} bytes ({reduction:.1f}% reduction)")
                
                total_original_size += original_size
                total_minified_size += minified_size
            else:
                print(f"➖ {js_file}: Already optimized")
                
        except Exception as e:
            print(f"❌ Error processing {js_file}: {e}")
    
    return total_original_size, total_minified_size

def process_html_files():
    """Process inline JavaScript in HTML files"""
    html_files = glob.glob('/Users/danielneale/GoodHands_02/*.html')
    total_original_size = 0
    total_minified_size = 0
    files_processed = 0
    
    print("\n=== PROCESSING INLINE JAVASCRIPT IN HTML FILES ===")
    
    for html_file in html_files:
        try:
            with open(html_file, 'r', encoding='utf-8') as f:
                original_content = f.read()
            
            # Check if file has inline JavaScript
            if '<script' not in original_content.lower():
                continue
                
            original_size = len(original_content.encode('utf-8'))
            minified_content = minify_inline_js_in_html(original_content)
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
                print(f"➖ {os.path.basename(html_file)}: No JS minification needed")
                
        except Exception as e:
            print(f"❌ Error processing {html_file}: {e}")
    
    return total_original_size, total_minified_size, files_processed

def main():
    """Main JavaScript minification process"""
    print("🚀 STARTING JAVASCRIPT MINIFICATION FOR SPEED OPTIMIZATION")
    print("=" * 60)
    
    # Process standalone JS files
    js_original, js_minified = process_js_files()
    
    # Process inline JS in HTML files
    html_original, html_minified, html_count = process_html_files()
    
    # Calculate totals
    total_original = js_original + html_original
    total_minified = js_minified + html_minified
    
    print("\n" + "=" * 60)
    print("📊 JAVASCRIPT MINIFICATION RESULTS")
    print("=" * 60)
    
    if total_original > 0:
        total_reduction = ((total_original - total_minified) / total_original) * 100
        savings_kb = (total_original - total_minified) / 1024
        
        print(f"📁 Standalone JS files: {js_original} → {js_minified} bytes")
        print(f"📄 HTML inline JS: {html_original} → {html_minified} bytes ({html_count} files)")
        print(f"💾 Total JS reduction: {total_original} → {total_minified} bytes")
        print(f"📈 Overall reduction: {total_reduction:.1f}% ({savings_kb:.1f}KB saved)")
        print(f"⚡ Speed benefit: Faster script parsing and execution")
        
        if total_reduction > 20:
            print("🎉 EXCELLENT: Significant JavaScript size reduction achieved!")
        elif total_reduction > 10:
            print("✅ GOOD: Meaningful JavaScript optimization completed")
        else:
            print("📋 MINIMAL: JavaScript was already well-optimized")
    else:
        print("📋 No JavaScript files found to minify")
    
    print("\n🎯 Next: Additional performance optimizations")

if __name__ == "__main__":
    main()