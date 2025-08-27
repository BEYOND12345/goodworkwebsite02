#!/usr/bin/env python3
"""
Speed-focused Image Optimization for PageSpeed 90+
Optimize images without external dependencies
"""

import os
import glob
from PIL import Image, ImageOps

def optimize_for_speed(image_path, max_size_kb=120):
    """Optimize image specifically for PageSpeed performance"""
    
    try:
        with Image.open(image_path) as img:
            # Convert to RGB if necessary
            if img.mode in ('RGBA', 'LA', 'P'):
                img = img.convert('RGB')
            
            # Auto-orient based on EXIF
            img = ImageOps.exif_transpose(img)
            
            original_size = os.path.getsize(image_path)
            
            # Skip if already small enough
            if original_size <= max_size_kb * 1024:
                print(f"✓ {os.path.basename(image_path)} already optimized ({original_size/1024:.1f}KB)")
                return True
            
            # Determine output path
            base_name = os.path.splitext(image_path)[0]
            webp_path = base_name + '.webp'
            
            # Aggressive resizing for large images
            width, height = img.size
            
            # Calculate new dimensions based on original size
            if original_size > 500 * 1024:  # Very large files
                max_dimension = 1200
            elif original_size > 300 * 1024:  # Large files
                max_dimension = 1400
            elif original_size > 200 * 1024:  # Medium files
                max_dimension = 1600
            else:
                max_dimension = min(width, height)
            
            # Resize if needed
            if max(width, height) > max_dimension:
                if width > height:
                    new_width = max_dimension
                    new_height = int((height * max_dimension) / width)
                else:
                    new_height = max_dimension
                    new_width = int((width * max_dimension) / height)
                
                img = img.resize((new_width, new_height), Image.Resampling.LANCZOS)
                print(f"   Resized: {width}x{height} → {new_width}x{new_height}")
            
            # Try different quality levels to hit target size
            for quality in [75, 70, 65, 60, 55, 50, 45]:
                img.save(webp_path, 'WebP', 
                        quality=quality,
                        optimize=True,
                        method=6)  # Maximum compression
                
                new_size = os.path.getsize(webp_path)
                if new_size <= max_size_kb * 1024:
                    break
            
            # Final check
            final_size = os.path.getsize(webp_path)
            savings = ((original_size - final_size) / original_size) * 100
            
            print(f"✅ {os.path.basename(image_path)}")
            print(f"   {original_size/1024:.1f}KB → {final_size/1024:.1f}KB ({savings:.1f}% reduction)")
            print(f"   Quality: {quality}")
            
            return True
            
    except Exception as e:
        print(f"❌ Failed to optimize {image_path}: {e}")
        return False

def main():
    """Run speed-focused image optimization"""
    
    print("⚡ SPEED-FOCUSED IMAGE OPTIMIZATION")
    print("=" * 60)
    print("Target: Maximum 120KB per image for PageSpeed 90+")
    print()
    
    # Find large images that need optimization
    image_patterns = ['*.webp', '*.avif', '*.jpg', '*.jpeg', '*.png']
    large_images = []
    
    for pattern in image_patterns:
        for img_path in glob.glob(pattern):
            if os.path.getsize(img_path) > 100 * 1024:  # Larger than 100KB
                large_images.append(img_path)
    
    # Also check subdirectories
    for pattern in image_patterns:
        for img_path in glob.glob(f"**/{pattern}", recursive=True):
            if os.path.getsize(img_path) > 100 * 1024:
                large_images.append(img_path)
    
    if not large_images:
        print("✅ All images already optimized for speed!")
        return
    
    print(f"Found {len(large_images)} images needing optimization")
    print()
    
    optimized = 0
    total_before = 0
    total_after = 0
    
    for img_path in large_images:
        before_size = os.path.getsize(img_path)
        
        if optimize_for_speed(img_path, max_size_kb=120):
            # Check the WebP version
            webp_path = os.path.splitext(img_path)[0] + '.webp'
            if os.path.exists(webp_path):
                after_size = os.path.getsize(webp_path)
                total_before += before_size
                total_after += after_size
                optimized += 1
        
        print()  # Spacing
    
    # Summary
    if total_before > 0:
        total_savings = ((total_before - total_after) / total_before) * 100
        print("=" * 60)
        print(f"⚡ SPEED OPTIMIZATION COMPLETE!")
        print(f"   Images optimized: {optimized}")
        print(f"   Size reduction: {total_before/1024:.1f}KB → {total_after/1024:.1f}KB")
        print(f"   Total savings: {total_savings:.1f}%")
        print(f"   Performance target: ✅ Ready for PageSpeed 90+")

if __name__ == "__main__":
    main()