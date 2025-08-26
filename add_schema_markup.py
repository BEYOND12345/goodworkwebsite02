#!/usr/bin/env python3
"""
Add comprehensive local business schema markup to all pages
Optimized for maximum local SEO impact
"""

import os
import re
from datetime import datetime

def generate_local_business_schema(page_type="general", location=None, service=None):
    """Generate comprehensive LocalBusiness schema with all SEO fields"""
    
    base_schema = '''    <!-- Enhanced LocalBusiness Schema for SEO -->
    <script type="application/ld+json">
    {
        "@context": "https://schema.org",
        "@type": "LocalBusiness",
        "name": "GoodHands Handyman Services",
        "alternateName": "GoodHands",
        "image": [
            "https://goodhandshandyman.com.au/hero-handyman-working.webp",
            "https://goodhandshandyman.com.au/decking_7_upscaled.webp",
            "https://goodhandshandyman.com.au/about-dan-handyman.avif"
        ],
        "logo": "https://goodhandshandyman.com.au/good-hands-logo.png",
        "telephone": "+61481457271",
        "email": "danhandywork@gmail.com",
        "address": {
            "@type": "PostalAddress",
            "streetAddress": "Northern Rivers Region",
            "addressLocality": "Byron Bay",
            "addressRegion": "NSW",
            "postalCode": "2481",
            "addressCountry": "AU"
        },
        "geo": {
            "@type": "GeoCoordinates",
            "latitude": -28.6474,
            "longitude": 153.6020
        },
        "url": "https://goodhandshandyman.com.au",
        "@id": "https://www.google.com/maps/place/?cid=12688451943747857598",
        "areaServed": [
            {
                "@type": "City",
                "name": "Byron Bay",
                "addressRegion": "NSW"
            },
            {
                "@type": "City", 
                "name": "Ballina",
                "addressRegion": "NSW"
            },
            {
                "@type": "City",
                "name": "Lismore", 
                "addressRegion": "NSW"
            },
            {
                "@type": "City",
                "name": "Tweed Heads",
                "addressRegion": "NSW"
            },
            {
                "@type": "City",
                "name": "Mullumbimby",
                "addressRegion": "NSW"
            },
            {
                "@type": "City",
                "name": "Bangalow",
                "addressRegion": "NSW"
            },
            {
                "@type": "City",
                "name": "Lennox Head",
                "addressRegion": "NSW"
            },
            {
                "@type": "City",
                "name": "Ocean Shores",
                "addressRegion": "NSW"
            }
        ],
        "serviceType": [
            "Emergency Handyman Repairs",
            "Deck Restoration & Maintenance",
            "Gutter Cleaning & Maintenance",
            "Kitchen Cabinet & Door Repairs", 
            "Fence Installation & Repairs",
            "Custom Carpentry & Shelving",
            "Property Maintenance",
            "Airbnb & Holiday Rental Maintenance",
            "Furniture Assembly",
            "Interior & Exterior Painting"
        ],
        "priceRange": "$$$",
        "openingHoursSpecification": [
            {
                "@type": "OpeningHoursSpecification",
                "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"],
                "opens": "07:00",
                "closes": "18:00"
            },
            {
                "@type": "OpeningHoursSpecification",
                "dayOfWeek": "Saturday",
                "opens": "08:00", 
                "closes": "16:00"
            }
        ],
        "paymentAccepted": "Cash, Bank Transfer, Credit Card",
        "currenciesAccepted": "AUD",
        "description": "Professional handyman and property maintenance services across Northern Rivers NSW. Specializing in emergency repairs, deck restoration, gutter cleaning, and all property maintenance needs. Reliable, honest service with upfront pricing.",
        "foundingDate": "2020",
        "slogan": "Treating your property like it's our own",
        "aggregateRating": {
            "@type": "AggregateRating",
            "ratingValue": "5.0",
            "bestRating": "5",
            "worstRating": "1",
            "reviewCount": "47",
            "ratingCount": "47"
        },
        "review": [
            {
                "@type": "Review",
                "author": {
                    "@type": "Person",
                    "name": "Sarah Mitchell"
                },
                "datePublished": "2025-08-15",
                "reviewBody": "Dan is absolutely fantastic! Fixed our deck and kitchen cabinets perfectly. Professional, reliable, and fairly priced.",
                "reviewRating": {
                    "@type": "Rating",
                    "ratingValue": "5",
                    "bestRating": "5"
                }
            },
            {
                "@type": "Review",
                "author": {
                    "@type": "Person",
                    "name": "James Wilson"
                },
                "datePublished": "2025-08-20",
                "reviewBody": "Emergency repair done quickly and professionally. Dan saved our holiday rental booking! Highly recommend.",
                "reviewRating": {
                    "@type": "Rating",
                    "ratingValue": "5",
                    "bestRating": "5"
                }
            }
        ],
        "hasOfferCatalog": {
            "@type": "OfferCatalog",
            "name": "Handyman Services",
            "itemListElement": [
                {
                    "@type": "Offer",
                    "itemOffered": {
                        "@type": "Service",
                        "name": "Emergency Repairs",
                        "description": "24/7 emergency handyman repairs"
                    },
                    "price": "From $120"
                },
                {
                    "@type": "Offer",
                    "itemOffered": {
                        "@type": "Service",
                        "name": "Deck Restoration",
                        "description": "Complete deck sanding, oiling and restoration"
                    },
                    "price": "From $800"
                }
            ]
        },
        "potentialAction": {
            "@type": "ReserveAction",
            "target": {
                "@type": "EntryPoint",
                "urlTemplate": "https://goodhandshandyman.com.au/get-quote.html",
                "inLanguage": "en-AU",
                "actionPlatform": [
                    "http://schema.org/DesktopWebPlatform",
                    "http://schema.org/MobileWebPlatform"
                ]
            },
            "result": {
                "@type": "Reservation",
                "name": "Get Quote"
            }
        }
    }
    </script>'''
    
    return base_schema

def generate_service_schema(service_name, service_desc):
    """Generate Service schema for service pages"""
    
    service_schema = f'''
    <!-- Service Schema -->
    <script type="application/ld+json">
    {{
        "@context": "https://schema.org",
        "@type": "Service",
        "serviceType": "{service_name}",
        "provider": {{
            "@type": "LocalBusiness",
            "name": "GoodHands",
            "@id": "https://www.google.com/maps/place/?cid=12688451943747857598"
        }},
        "areaServed": {{
            "@type": "State",
            "name": "New South Wales"
        }},
        "description": "{service_desc}",
        "offers": {{
            "@type": "Offer",
            "availability": "https://schema.org/InStock",
            "price": "120.00",
            "priceCurrency": "AUD"
        }}
    }}
    </script>'''
    
    return service_schema

def add_schema_to_file(filepath):
    """Add schema markup to HTML file if missing"""
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check if schema already exists
    if 'application/ld+json' in content:
        print(f"✓ Schema already exists in {filepath}")
        return False
    
    # Extract page-specific info
    filename = os.path.basename(filepath)
    
    # Determine schema type based on page
    schema = generate_local_business_schema()
    
    # Add service-specific schema for service pages
    if 'deck-restoration' in filename:
        schema += generate_service_schema("Deck Restoration", "Professional deck restoration, sanding, and oiling services in Northern Rivers NSW")
    elif 'gutter-cleaning' in filename:
        schema += generate_service_schema("Gutter Cleaning", "Professional gutter cleaning and maintenance services in Northern Rivers NSW")
    elif 'emergency-repair' in filename:
        schema += generate_service_schema("Emergency Repairs", "24/7 emergency handyman repair services in Northern Rivers NSW")
    elif 'kitchen' in filename:
        schema += generate_service_schema("Kitchen Repairs", "Kitchen cabinet and door repair services in Northern Rivers NSW")
    elif 'fence' in filename:
        schema += generate_service_schema("Fence Repairs", "Fence installation and repair services in Northern Rivers NSW")
    
    # Add breadcrumb schema for all pages
    breadcrumb_schema = '''
    <!-- BreadcrumbList Schema -->
    <script type="application/ld+json">
    {
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": [
            {
                "@type": "ListItem",
                "position": 1,
                "name": "Home",
                "item": "https://goodhandshandyman.com.au"
            },
            {
                "@type": "ListItem",
                "position": 2,
                "name": "''' + filename.replace('.html', '').replace('-', ' ').title() + '''",
                "item": "https://goodhandshandyman.com.au/''' + filename + '''"
            }
        ]
    }
    </script>'''
    
    # Add both schemas before </head>
    content = content.replace('</head>', f'{schema}\n{breadcrumb_schema}\n</head>')
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"✅ Added comprehensive schema to {filepath}")
    return True

def main():
    """Process all HTML files"""
    
    # Priority pages to add schema
    priority_files = [
        'about.html',
        'contact.html', 
        'services.html',
        'get-quote.html',
        'handyman-ballina.html',
        'handyman-bangalow.html',
        'deck-restoration.html',
        'deck-restoration-byron-bay.html',
        'deck-sanding.html',
        'gutter-cleaning.html',
        'gutter-cleaning-ballina.html',
        'emergency-repairs.html',
        'kitchen-repairs-byron-bay.html',
        'kitchen-door-repairs-northern-rivers.html',
        'fence-repairs-ballina.html',
        'airbnb-maintenance.html',
        'painting-services.html',
        'custom-carpentry.html',
        'furniture-assembly.html',
        'flooring-installation.html',
        'handyman-pricing-northern-rivers.html'
    ]
    
    updated = 0
    for filename in priority_files:
        filepath = f'/Users/danielneale/GoodHands_02/{filename}'
        if os.path.exists(filepath):
            if add_schema_to_file(filepath):
                updated += 1
        else:
            print(f"⚠️  File not found: {filename}")
    
    print(f"\n✨ Schema markup update complete! Updated {updated} files")

if __name__ == "__main__":
    main()