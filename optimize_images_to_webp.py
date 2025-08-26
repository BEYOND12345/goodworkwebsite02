#!/usr/bin/env python3
"""
Convert all JPG/PNG images to WebP format for SEO optimization
Uses PIL (Pillow) to maintain high quality while reducing file size
"""

import os
import sys
from PIL import Image
import glob

def convert_to_webp(image_path, quality=85):
    """Convert an image to WebP format with optimization"""
    
    try:
        # Open the image
        with Image.open(image_path) as img:
            # Convert to RGB if necessary (for PNG with transparency)
            if img.mode in ('RGBA', 'LA', 'P'):
                img = img.convert('RGB')
            
            # Generate WebP filename
            webp_path = os.path.splitext(image_path)[0] + '.webp'
            
            # Skip if WebP already exists and is newer
            if os.path.exists(webp_path):
                if os.path.getmtime(webp_path) > os.path.getmtime(image_path):
                    print(f"✓ WebP already up-to-date: {webp_path}")
                    return True
            
            # Save as WebP with optimization
            img.save(webp_path, 'WebP', 
                    quality=quality, 
                    optimize=True,
                    method=6)  # Best compression method
            
            # Get file sizes for comparison
            original_size = os.path.getsize(image_path)
            webp_size = os.path.getsize(webp_path)
            savings = ((original_size - webp_size) / original_size) * 100
            
            print(f"✅ Converted: {image_path}")
            print(f"   → {webp_path}")
            print(f"   Size: {original_size:,} bytes → {webp_size:,} bytes ({savings:.1f}% smaller)")
            
            return True
            
    except Exception as e:
        print(f"❌ Failed to convert {image_path}: {e}")
        return False

def update_html_references(old_path, new_path):
    """Update HTML files to reference WebP instead of original format"""
    
    old_filename = os.path.basename(old_path)
    new_filename = os.path.basename(new_path)
    
    # Find all HTML files
    html_files = glob.glob("*.html")
    
    updated_files = []
    
    for html_file in html_files:
        try:
            with open(html_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Check if this file references the old image
            if old_filename in content:
                # Replace the reference
                updated_content = content.replace(old_filename, new_filename)
                
                with open(html_file, 'w', encoding='utf-8') as f:
                    f.write(updated_content)
                
                updated_files.append(html_file)
        
        except Exception as e:
            print(f"Warning: Could not update {html_file}: {e}")
    
    if updated_files:
        print(f"   📝 Updated HTML references in: {', '.join(updated_files)}")
    
    return len(updated_files)

def main():
    """Process all images in the directory"""
    
    print("🖼️  Starting image optimization to WebP format...")
    print("="*60)
    
    # Find all image files
    image_extensions = ['*.jpg', '*.jpeg', '*.JPG', '*.JPEG', '*.png', '*.PNG']
    image_files = []
    
    for ext in image_extensions:
        image_files.extend(glob.glob(ext))
        # Also search in subdirectories
        image_files.extend(glob.glob(f"**/{ext}", recursive=True))
    
    if not image_files:
        print("No image files found to convert.")
        return
    
    print(f"Found {len(image_files)} images to process...")
    print()
    
    converted = 0
    html_updates = 0
    
    for image_path in image_files:
        print(f"Processing: {image_path}")
        
        if convert_to_webp(image_path, quality=85):
            converted += 1
            
            # Update HTML file references
            webp_path = os.path.splitext(image_path)[0] + '.webp'
            html_updates += update_html_references(image_path, webp_path)
        
        print()  # Add space between conversions
    
    print("="*60)
    print(f"✨ Image optimization complete!")
    print(f"   Converted: {converted} images")
    print(f"   HTML files updated: {html_updates}")
    print(f"   Total space saved: Check individual file savings above")
    print()
    print("💡 Note: Original files are kept for backup.")
    print("   You can manually delete them once you've verified the WebP versions work correctly.")

if __name__ == "__main__":
    # Check if PIL is available
    try:
        from PIL import Image
    except ImportError:
        print("❌ PIL (Pillow) is required. Install with: pip install Pillow")
        sys.exit(1)
    
    main()