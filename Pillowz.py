#!/usr/bin/env python3
"""
Pillow (PIL) Image Processing Demonstration
Image manipulation, filtering, and enhancement techniques
"""

from PIL import Image, ImageFilter, ImageEnhance, ImageDraw, ImageFont
import numpy as np
import os

def create_sample_image():
    """Create a sample image for demonstration"""
    print("Creating sample image...")
    
    # Create a colorful gradient image
    width, height = 400, 300
    image = Image.new('RGB', (width, height))
    
    # Create gradient
    for y in range(height):
        for x in range(width):
            r = int(255 * x / width)
            g = int(255 * y / height)
            b = int(255 * (x + y) / (width + height))
            image.putpixel((x, y), (r, g, b))
    
    # Add some shapes
    draw = ImageDraw.Draw(image)
    draw.ellipse([50, 50, 150, 150], fill=(255, 255, 0))
    draw.rectangle([250, 100, 350, 200], fill=(255, 0, 255))
    
    image.save('sample_image.jpg')
    print("✓ Sample image created: sample_image.jpg")
    return image

def basic_image_operations():
    """Demonstrate basic image operations"""
    print("\n=== Basic Image Operations ===")
    
    # Create or load image
    if os.path.exists('sample_image.jpg'):
        image = Image.open('sample_image.jpg')
        print("✓ Loaded existing sample image")
    else:
        image = create_sample_image()
    
    print(f"Image size: {image.size}")
    print(f"Image mode: {image.mode}")
    print(f"Image format: {image.format}")
    
    # Basic transformations
    print("\nApplying basic transformations...")
    
    # Resize
    resized = image.resize((200, 150))
    resized.save('my_resized_image.jpg')
    print("✓ Resized image saved: my_resized_image.jpg")
    
    # Rotate
    rotated = image.rotate(45, expand=True)
    rotated.save('rotated_image.jpg')
    print("✓ Rotated image saved: rotated_image.jpg")
    
    # Flip
    flipped = image.transpose(Image.FLIP_LEFT_RIGHT)
    flipped.save('my_flipped_image.jpg')
    print("✓ Flipped image saved: my_flipped_image.jpg")
    
    return image

def image_filters_demo(image):
    """Demonstrate various image filters"""
    print("\n=== Image Filters Demo ===")
    
    filters = [
        (ImageFilter.BLUR, 'blurred'),
        (ImageFilter.SHARPEN, 'sharpened'),
        (ImageFilter.EMBOSS, 'embossed'),
        (ImageFilter.EDGE_ENHANCE, 'edge_enhanced'),
        (ImageFilter.SMOOTH, 'smoothed')
    ]
    
    for img_filter, name in filters:
        filtered = image.filter(img_filter)
        filename = f'my_{name}_image.jpg'
        filtered.save(filename)
        print(f"✓ {name.title()} filter applied: {filename}")

def image_enhancement_demo(image):
    """Demonstrate image enhancement techniques"""
    print("\n=== Image Enhancement Demo ===")
    
    # Brightness
    brightness = ImageEnhance.Brightness(image)
    bright_image = brightness.enhance(1.5)  # 50% brighter
    bright_image.save('bright_image.jpg')
    print("✓ Brightness enhanced: bright_image.jpg")
    
    # Contrast
    contrast = ImageEnhance.Contrast(image)
    contrast_image = contrast.enhance(1.3)  # 30% more contrast
    contrast_image.save('contrast_image.jpg')
    print("✓ Contrast enhanced: contrast_image.jpg")
    
    # Color saturation
    color = ImageEnhance.Color(image)
    saturated = color.enhance(1.5)  # 50% more saturated
    saturated.save('saturated_image.jpg')
    print("✓ Color saturation enhanced: saturated_image.jpg")
    
    # Sharpness
    sharpness = ImageEnhance.Sharpness(image)
    sharp = sharpness.enhance(2.0)  # Double sharpness
    sharp.save('sharp_image.jpg')
    print("✓ Sharpness enhanced: sharp_image.jpg")

def color_manipulation_demo(image):
    """Demonstrate color manipulation"""
    print("\n=== Color Manipulation Demo ===")
    
    # Convert to grayscale
    grayscale = image.convert('L')
    grayscale.save('grayscale_image.jpg')
    print("✓ Grayscale conversion: grayscale_image.jpg")
    
    # Convert back to RGB and colorize
    colorized = grayscale.convert('RGB')
    
    # Apply color tint (sepia effect)
    width, height = colorized.size
    for y in range(height):
        for x in range(width):
            r, g, b = colorized.getpixel((x, y))
            # Sepia formula
            tr = int(0.393 * r + 0.769 * g + 0.189 * b)
            tg = int(0.349 * r + 0.686 * g + 0.168 * b)
            tb = int(0.272 * r + 0.534 * g + 0.131 * b)
            
            # Ensure values don't exceed 255
            tr = min(255, tr)
            tg = min(255, tg)
            tb = min(255, tb)
            
            colorized.putpixel((x, y), (tr, tg, tb))
    
    colorized.save('sepia_image.jpg')
    print("✓ Sepia effect applied: sepia_image.jpg")

def image_composition_demo():
    """Demonstrate image composition and drawing"""
    print("\n=== Image Composition Demo ===")
    
    # Create a new image for drawing
    canvas = Image.new('RGB', (500, 400), (255, 255, 255))
    draw = ImageDraw.Draw(canvas)
    
    # Draw various shapes
    draw.rectangle([50, 50, 150, 100], fill=(255, 0, 0), outline=(0, 0, 0), width=2)
    draw.ellipse([200, 50, 300, 150], fill=(0, 255, 0), outline=(0, 0, 0), width=2)
    draw.polygon([(350, 50), (400, 100), (450, 50), (450, 150), (350, 150)], 
                 fill=(0, 0, 255), outline=(0, 0, 0))
    
    # Draw lines
    draw.line([(50, 200), (450, 200)], fill=(255, 0, 255), width=3)
    draw.line([(250, 180), (250, 220)], fill=(255, 0, 255), width=3)
    
    # Add text
    try:
        # Try to use a default font, fallback to basic if not available
        font = ImageFont.load_default()
        draw.text((150, 250), "Pillow Demo", fill=(0, 0, 0), font=font)
        draw.text((150, 280), "Image Processing", fill=(128, 128, 128), font=font)
    except:
        draw.text((150, 250), "Pillow Demo", fill=(0, 0, 0))
        draw.text((150, 280), "Image Processing", fill=(128, 128, 128))
    
    canvas.save('my_artistic_image.jpg')
    print("✓ Artistic composition created: my_artistic_image.jpg")
    
    return canvas

def thumbnail_generation_demo(image):
    """Demonstrate thumbnail generation"""
    print("\n=== Thumbnail Generation Demo ===")
    
    # Create thumbnails of different sizes
    sizes = [(128, 128), (64, 64), (32, 32)]
    
    for size in sizes:
        # Create thumbnail (maintains aspect ratio)
        thumb = image.copy()
        thumb.thumbnail(size, Image.Resampling.LANCZOS)
        
        filename = f'thumbnail_{size[0]}x{size[1]}.jpg'
        thumb.save(filename)
        print(f"✓ Thumbnail created: {filename} (actual size: {thumb.size})")

def advanced_operations_demo(image):
    """Demonstrate advanced image operations"""
    print("\n=== Advanced Operations Demo ===")
    
    # Image cropping
    width, height = image.size
    left = width // 4
    top = height // 4
    right = 3 * width // 4
    bottom = 3 * height // 4
    
    cropped = image.crop((left, top, right, bottom))
    cropped.save('cropped_image.jpg')
    print("✓ Image cropped (center quarter): cropped_image.jpg")
    
    # Image paste (combining images)
    background = Image.new('RGB', (600, 400), (200, 200, 200))
    
    # Paste original image
    background.paste(image, (10, 10))
    
    # Paste cropped image
    background.paste(cropped, (420, 10))
    
    # Paste a small version
    small = image.resize((150, 100))
    background.paste(small, (10, 320))
    
    background.save('combined_image.jpg')
    print("✓ Combined image created: combined_image.jpg")
    
    # Split and merge channels
    if image.mode == 'RGB':
        r, g, b = image.split()
        
        # Create false color image by swapping channels
        false_color = Image.merge('RGB', (g, b, r))  # Green, Blue, Red
        false_color.save('false_color_image.jpg')
        print("✓ False color image created: false_color_image.jpg")

def batch_processing_demo():
    """Demonstrate batch processing of images"""
    print("\n=== Batch Processing Demo ===")
    
    # Get all jpg files in current directory
    image_files = [f for f in os.listdir('.') if f.lower().endswith('.jpg')]
    
    if not image_files:
        print("No JPG files found for batch processing")
        return
    
    print(f"Found {len(image_files)} images for batch processing")
    
    # Create a batch processed folder
    batch_folder = 'batch_processed'
    if not os.path.exists(batch_folder):
        os.makedirs(batch_folder)
    
    processed_count = 0
    for filename in image_files[:5]:  # Process first 5 images only
        try:
            with Image.open(filename) as img:
                # Apply consistent processing
                processed = img.resize((300, 200))
                processed = processed.filter(ImageFilter.SHARPEN)
                
                # Enhance contrast
                enhancer = ImageEnhance.Contrast(processed)
                processed = enhancer.enhance(1.2)
                
                # Save to batch folder
                output_path = os.path.join(batch_folder, f'processed_{filename}')
                processed.save(output_path)
                processed_count += 1
                
        except Exception as e:
            print(f"✗ Error processing {filename}: {e}")
    
    print(f"✓ Batch processed {processed_count} images in '{batch_folder}' folder")

def main():
    """Main function to run all demonstrations"""
    print("Pillow (PIL) Image Processing Demonstration")
    print("=" * 60)
    
    try:
        # Run all demonstrations
        image = basic_image_operations()
        image_filters_demo(image)
        image_enhancement_demo(image)
        color_manipulation_demo(image)
        image_composition_demo()
        thumbnail_generation_demo(image)
        advanced_operations_demo(image)
        batch_processing_demo()
        
        print("\n" + "=" * 60)
        print("Pillow demonstration completed!")
        print("Check your directory for all the generated image files.")
        print("\nGenerated files include:")
        print("- Various filtered and enhanced versions")
        print("- Thumbnails of different sizes")
        print("- Artistic compositions")
        print("- Batch processed images")
        
    except Exception as e:
        print(f"Error during demonstration: {e}")
        print("Make sure Pillow is installed: pip install Pillow")

if __name__ == "__main__":
    main()
