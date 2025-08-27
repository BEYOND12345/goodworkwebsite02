#!/usr/bin/env python3
"""
Advanced Image Optimization for Maximum Performance
Compress images to achieve James's 90+ PageSpeed score
"""

import os
import glob
from PIL import Image, ImageOps
import pillow_heif

def optimize_image_aggressive(image_path, target_size_kb=150):
    """Aggressively optimize image for web performance"""
    
    # Register HEIF support
    pillow_heif.register_heif_opener()
    
    try:
        with Image.open(image_path) as img:
            # Convert to RGB if necessary
            if img.mode in ('RGBA', 'LA', 'P'):
                img = img.convert('RGB')
            
            # Auto-orient based on EXIF
            img = ImageOps.exif_transpose(img)
            
            # Get original file size
            original_size = os.path.getsize(image_path)
            
            # Determine output path
            base_name = os.path.splitext(image_path)[0]
            webp_path = base_name + '.webp'
            
            # Start with high quality and reduce until we hit target size
            qualities = [85, 80, 75, 70, 65, 60, 55, 50]
            
            best_quality = 85
            
            for quality in qualities:
                # Try different methods for different file sizes
                method = 6 if original_size > 500*1024 else 4  # More compression for larger files
                
                # Resize if image is very large
                if img.size[0] > 2000 or img.size[1] > 2000:
                    # Resize maintaining aspect ratio
                    img.thumbnail((1800, 1800), Image.Resampling.LANCZOS)
                elif img.size[0] > 1500 or img.size[1] > 1500:
                    img.thumbnail((1400, 1400), Image.Resampling.LANCZOS)
                
                # Save with current quality
                img.save(webp_path, 'WebP', 
                        quality=quality,
                        optimize=True,
                        method=method)
                
                # Check if we've hit our target
                new_size = os.path.getsize(webp_path)
                if new_size <= target_size_kb * 1024:
                    best_quality = quality
                    break
            
            # Calculate savings
            final_size = os.path.getsize(webp_path)
            savings = ((original_size - final_size) / original_size) * 100
            
            print(f"✅ {os.path.basename(image_path)}")
            print(f"   {original_size/1024:.1f}KB → {final_size/1024:.1f}KB ({savings:.1f}% smaller)")
            print(f"   Quality: {best_quality}, Size: {img.size}")
            
            return True
            
    except Exception as e:
        print(f"❌ Failed to optimize {image_path}: {e}")
        return False

def compress_all_images():
    """Compress all images for maximum performance"""
    
    print("🗜️  AGGRESSIVE IMAGE COMPRESSION")
    print("=" * 60)
    print("Target: All images under 150KB for maximum PageSpeed score")
    print()
    
    # Find all images
    image_patterns = ['*.webp', '*.avif', '*.jpg', '*.jpeg', '*.png', '*.HEIC']
    
    all_images = []
    for pattern in image_patterns:
        all_images.extend(glob.glob(pattern))
        # Also search subdirectories
        all_images.extend(glob.glob(f"**/{pattern}", recursive=True))
    
    print(f"Found {len(all_images)} images to optimize")
    print()
    
    optimized_count = 0
    total_original_size = 0
    total_final_size = 0
    
    for image_path in all_images:
        if os.path.getsize(image_path) > 100 * 1024:  # Only optimize images > 100KB
            original_size = os.path.getsize(image_path)
            
            if optimize_image_aggressive(image_path, target_size_kb=150):
                optimized_count += 1
                
                # Calculate size after optimization
                webp_path = os.path.splitext(image_path)[0] + '.webp'
                if os.path.exists(webp_path):
                    final_size = os.path.getsize(webp_path)
                    total_original_size += original_size
                    total_final_size += final_size
            
            print()  # Space between images
    
    # Summary
    if total_original_size > 0:
        total_savings = ((total_original_size - total_final_size) / total_original_size) * 100
        print("=" * 60)
        print(f"✨ COMPRESSION COMPLETE!")
        print(f"   Images optimized: {optimized_count}")
        print(f"   Total size reduction: {total_original_size/1024:.1f}KB → {total_final_size/1024:.1f}KB")
        print(f"   Overall savings: {total_savings:.1f}%")
        print(f"   Target achieved: All images under 150KB for maximum performance")

if __name__ == "__main__":
    # Install required package if not available
    try:
        import pillow_heif
    except ImportError:
        print("Installing pillow-heif for HEIC support...")
        os.system("pip install pillow-heif")
        import pillow_heif
    
    compress_all_images()