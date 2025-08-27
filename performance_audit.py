#!/usr/bin/env python3
"""
Website Performance Audit & Optimization
Implementing James's speed optimization strategy for 90+ PageSpeed scores
"""

import os
import glob
import re
from pathlib import Path

def audit_current_performance():
    """Audit current website performance baseline"""
    
    print("📊 PERFORMANCE BASELINE AUDIT")
    print("=" * 60)
    
    # File size analysis
    html_files = glob.glob("*.html")
    css_sizes = []
    js_sizes = []
    image_sizes = []
    
    total_html_size = 0
    
    for file in html_files:
        if not any(x in file for x in ['master', 'old', 'backup', 'test']):
            size = os.path.getsize(file)
            total_html_size += size
            
            # Extract inline CSS
            with open(file, 'r', encoding='utf-8') as f:
                content = f.read()
                css_matches = re.findall(r'<style[^>]*>(.*?)</style>', content, re.DOTALL)
                for css in css_matches:
                    css_sizes.append(len(css.encode('utf-8')))
                
                # Extract inline JS
                js_matches = re.findall(r'<script[^>]*>(.*?)</script>', content, re.DOTALL)
                for js in js_matches:
                    if 'application/ld+json' not in js:
                        js_sizes.append(len(js.encode('utf-8')))
    
    # Image file analysis
    image_extensions = ['*.webp', '*.avif', '*.jpg', '*.jpeg', '*.png']
    for ext in image_extensions:
        for img in glob.glob(ext):
            image_sizes.append(os.path.getsize(img))
    
    # Calculate metrics
    avg_html_size = total_html_size / len([f for f in html_files if not any(x in f for x in ['master', 'old', 'backup', 'test'])]) if html_files else 0
    total_css_size = sum(css_sizes)
    total_js_size = sum(js_sizes)
    total_image_size = sum(image_sizes)
    
    print(f"📄 HTML Files: {len(html_files)} files")
    print(f"   Average size: {avg_html_size/1024:.1f} KB")
    print(f"   Total size: {total_html_size/1024:.1f} KB")
    
    print(f"🎨 CSS (inline): {len(css_sizes)} blocks")
    print(f"   Total size: {total_css_size/1024:.1f} KB")
    print(f"   Largest block: {max(css_sizes)/1024:.1f} KB" if css_sizes else "   No CSS found")
    
    print(f"⚡ JavaScript: {len(js_sizes)} blocks")
    print(f"   Total size: {total_js_size/1024:.1f} KB")
    
    print(f"🖼️  Images: {len(image_sizes)} files")
    print(f"   Total size: {sum(image_sizes)/1024:.1f} KB")
    print(f"   Average size: {(sum(image_sizes)/len(image_sizes))/1024:.1f} KB" if image_sizes else "   No images")
    print(f"   Largest image: {max(image_sizes)/1024:.1f} KB" if image_sizes else "")
    
    # Performance issues identification
    print(f"\n⚠️  PERFORMANCE ISSUES IDENTIFIED:")
    
    issues = []
    if avg_html_size > 100 * 1024:  # 100KB
        issues.append(f"• HTML files too large (avg {avg_html_size/1024:.1f}KB)")
    
    if total_css_size > 50 * 1024:  # 50KB
        issues.append(f"• CSS too large ({total_css_size/1024:.1f}KB)")
    
    if any(size > 200 * 1024 for size in image_sizes):  # 200KB
        large_images = [i for i, size in enumerate(image_sizes) if size > 200 * 1024]
        issues.append(f"• {len(large_images)} images over 200KB")
    
    if not css_sizes:
        issues.append("• No CSS minification detected")
    
    for issue in issues:
        print(issue)
    
    if not issues:
        print("• No major issues detected")
    
    return {
        'html_files': len(html_files),
        'avg_html_size': avg_html_size,
        'total_css_size': total_css_size,
        'total_js_size': total_js_size,
        'total_image_size': sum(image_sizes),
        'image_count': len(image_sizes),
        'issues': issues
    }

if __name__ == "__main__":
    audit_current_performance()