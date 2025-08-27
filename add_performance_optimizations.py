#!/usr/bin/env python3
"""
Performance Optimizations Script
Adds critical performance optimizations to achieve 90+ PageSpeed score
"""

import os
import re
import glob
from pathlib import Path

def add_preload_hints(html_content):
    """Add preload hints for critical resources"""
    # Look for the first external CSS or important images to preload
    preloads = []
    
    # Find critical CSS files to preload
    css_matches = re.findall(r'<link[^>]*href=["\']([^"\']*\.css)["\']', html_content)
    for css_file in css_matches[:2]:  # Preload first 2 CSS files
        if 'external' not in css_file.lower():
            preloads.append(f'    <link rel="preload" href="{css_file}" as="style">')
    
    # Find hero images to preload
    img_matches = re.findall(r'<img[^>]*src=["\']([^"\']*\.(webp|jpg|jpeg|png))["\']', html_content)
    for img_src, ext in img_matches[:1]:  # Preload first critical image
        if 'hero' in img_src.lower() or 'banner' in img_src.lower():
            preloads.append(f'    <link rel="preload" href="{img_src}" as="image">')
    
    if preloads:
        preload_block = '\n' + '\n'.join(preloads) + '\n'
        # Insert after existing meta tags but before title
        html_content = re.sub(r'(<meta[^>]*>\s*)+', lambda m: m.group(0) + preload_block, html_content, count=1)
    
    return html_content

def add_dns_prefetch(html_content):
    """Add DNS prefetch for external domains"""
    dns_prefetch = [
        '    <link rel="dns-prefetch" href="//fonts.googleapis.com">',
        '    <link rel="dns-prefetch" href="//www.google.com">',
        '    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
    ]
    
    # Check if we already have DNS prefetch
    if 'dns-prefetch' not in html_content:
        prefetch_block = '\n' + '\n'.join(dns_prefetch) + '\n'
        # Insert in head section
        html_content = re.sub(r'(<head[^>]*>)', r'\1' + prefetch_block, html_content, count=1)
    
    return html_content

def optimize_images_loading(html_content):
    """Add loading optimizations for images"""
    # Add loading="lazy" to non-critical images
    def add_lazy_loading(match):
        img_tag = match.group(0)
        # Skip if already has loading attribute
        if 'loading=' in img_tag:
            return img_tag
        # Skip hero/banner images (first image usually)
        if 'hero' in img_tag.lower() or 'banner' in img_tag.lower():
            return img_tag
        # Add lazy loading
        return img_tag.replace('<img ', '<img loading="lazy" ')
    
    # Apply lazy loading to images (skip first few critical images)
    img_count = 0
    def selective_lazy_loading(match):
        nonlocal img_count
        img_count += 1
        if img_count <= 2:  # First 2 images are critical, don't lazy load
            return match.group(0)
        return add_lazy_loading(match)
    
    html_content = re.sub(r'<img[^>]*>', selective_lazy_loading, html_content)
    
    # Add width and height attributes where missing (prevents CLS)
    def add_dimensions(match):
        img_tag = match.group(0)
        if 'width=' not in img_tag and 'height=' not in img_tag:
            # Add default dimensions - this should be customized per image
            return img_tag.replace('<img ', '<img width="400" height="300" ')
        return img_tag
    
    # Note: In production, you'd want to measure actual image dimensions
    # html_content = re.sub(r'<img[^>]*>', add_dimensions, html_content)
    
    return html_content

def add_critical_css_inline(html_content):
    """Move critical CSS inline for faster rendering"""
    # This is a simplified version - in practice you'd identify truly critical CSS
    critical_css = """
    <style>
        body{font-family:Arial,sans-serif;margin:0;padding:0}
        .container{max-width:1200px;margin:0 auto;padding:0 20px}
        header{background:#fff;box-shadow:0 2px 4px rgba(0,0,0,0.1)}
        .btn{display:inline-block;padding:12px 24px;background:#007bff;color:#fff;text-decoration:none;border-radius:4px}
        .hero{background-size:cover;background-position:center;min-height:400px;display:flex;align-items:center}
    </style>
    """
    
    # Only add if we don't already have significant inline styles
    existing_styles = re.findall(r'<style[^>]*>.*?</style>', html_content, flags=re.DOTALL)
    total_inline_css = sum(len(style) for style in existing_styles)
    
    if total_inline_css < 1000:  # Less than 1KB of inline CSS
        # Insert critical CSS in head
        html_content = re.sub(r'(<head[^>]*>)', r'\1\n' + critical_css, html_content, count=1)
    
    return html_content

def optimize_fonts_loading(html_content):
    """Optimize font loading for better performance"""
    # Add font-display: swap for better loading experience
    font_css_additions = '''
    <style>
        @font-face {
            font-display: swap;
        }
        * {
            font-display: swap;
        }
    </style>
    '''
    
    # Only add if using custom fonts
    if 'font-family' in html_content and 'font-display' not in html_content:
        html_content = re.sub(r'(</head>)', font_css_additions + r'\1', html_content, count=1)
    
    return html_content

def add_viewport_meta(html_content):
    """Ensure proper viewport meta tag exists"""
    viewport_meta = '<meta name="viewport" content="width=device-width, initial-scale=1.0">'
    
    if 'name="viewport"' not in html_content:
        # Add viewport meta tag
        html_content = re.sub(r'(<head[^>]*>)', r'\1\n    ' + viewport_meta, html_content, count=1)
    
    return html_content

def add_performance_hints(html_content):
    """Add various performance hints"""
    performance_hints = '''
    <!-- Performance optimizations -->
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="format-detection" content="telephone=no">
    '''
    
    # Add if not already present
    if 'X-UA-Compatible' not in html_content:
        html_content = re.sub(r'(<head[^>]*>)', r'\1\n' + performance_hints, html_content, count=1)
    
    return html_content

def process_html_files():
    """Apply performance optimizations to all HTML files"""
    html_files = glob.glob('/Users/danielneale/GoodHands_02/*.html')
    files_processed = 0
    total_optimizations = 0
    
    print("=== APPLYING PERFORMANCE OPTIMIZATIONS ===")
    
    for html_file in html_files:
        try:
            with open(html_file, 'r', encoding='utf-8') as f:
                original_content = f.read()
            
            optimized_content = original_content
            optimizations_applied = []
            
            # Apply optimizations
            new_content = add_preload_hints(optimized_content)
            if new_content != optimized_content:
                optimizations_applied.append("preload hints")
                optimized_content = new_content
            
            new_content = add_dns_prefetch(optimized_content)
            if new_content != optimized_content:
                optimizations_applied.append("DNS prefetch")
                optimized_content = new_content
            
            new_content = optimize_images_loading(optimized_content)
            if new_content != optimized_content:
                optimizations_applied.append("lazy loading")
                optimized_content = new_content
            
            new_content = add_viewport_meta(optimized_content)
            if new_content != optimized_content:
                optimizations_applied.append("viewport meta")
                optimized_content = new_content
            
            new_content = add_performance_hints(optimized_content)
            if new_content != optimized_content:
                optimizations_applied.append("performance hints")
                optimized_content = new_content
            
            # Write optimized content
            if optimized_content != original_content:
                with open(html_file, 'w', encoding='utf-8') as f:
                    f.write(optimized_content)
                
                print(f"✅ {os.path.basename(html_file)}: {len(optimizations_applied)} optimizations ({', '.join(optimizations_applied)})")
                files_processed += 1
                total_optimizations += len(optimizations_applied)
            else:
                print(f"➖ {os.path.basename(html_file)}: Already optimized")
                
        except Exception as e:
            print(f"❌ Error processing {html_file}: {e}")
    
    return files_processed, total_optimizations

def main():
    """Main performance optimization process"""
    print("🚀 ADDING PERFORMANCE OPTIMIZATIONS FOR 90+ PAGESPEED SCORE")
    print("=" * 60)
    
    files_processed, total_optimizations = process_html_files()
    
    print("\n" + "=" * 60)
    print("📊 PERFORMANCE OPTIMIZATION RESULTS")
    print("=" * 60)
    
    print(f"📄 Files processed: {files_processed}")
    print(f"⚡ Total optimizations applied: {total_optimizations}")
    print(f"🎯 Key optimizations:")
    print(f"   • DNS prefetching for external resources")
    print(f"   • Resource preloading for critical assets")
    print(f"   • Lazy loading for non-critical images")
    print(f"   • Proper viewport configuration")
    print(f"   • Performance hints and meta tags")
    
    if total_optimizations > 20:
        print("🎉 EXCELLENT: Comprehensive performance optimization completed!")
    elif total_optimizations > 10:
        print("✅ GOOD: Significant performance improvements applied")
    else:
        print("📋 MINIMAL: Basic optimizations added")
    
    print(f"\n💡 Additional manual optimizations for 90+ score:")
    print(f"   • Server-side compression (gzip/brotli)")
    print(f"   • CDN implementation")
    print(f"   • Browser caching headers")
    print(f"   • HTTP/2 or HTTP/3")
    print(f"   • Critical rendering path optimization")
    
    print("\n🎯 Next: PageSpeed Insights testing simulation")

if __name__ == "__main__":
    main()