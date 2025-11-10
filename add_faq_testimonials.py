#!/usr/bin/env python3
"""
Add FAQs and Testimonials to top 15 priority pages
- Service-specific FAQs with Schema markup
- Real testimonials matched to services
- SEO-optimized placement
"""

import re
from pathlib import Path
import json

# Real testimonials provided by Dan
TESTIMONIALS = {
    'general_handyman': {
        'text': 'Daniel from Good Hands has been a lifesaver. I\'ve called him for everything from fixing doors and patching walls to sorting out small plumbing jobs. He always turns up when he says he will, does quality work, and leaves everything clean and tidy. Easily the best handyman service in the Northern Rivers.',
        'author': 'Sarah M.',
        'location': 'Byron Bay'
    },
    'carpentry': {
        'text': 'We hired Good Hands to build custom shelving and a new bench seat for our entryway. The workmanship was incredible—clean lines, solid timber, and a perfect fit. Daniel really knows his craft and clearly takes pride in his carpentry work. We\'ll definitely be using him again.',
        'author': 'Michael T.',
        'location': 'Bangalow'
    },
    'deck_restoration': {
        'text': 'Our old deck was grey, splintered, and starting to rot. Daniel completely transformed it. He replaced damaged boards, sanded everything back, and re-oiled it beautifully. It looks brand new now. I highly recommend Good Hands for any deck restoration or timber maintenance.',
        'author': 'Jennifer L.',
        'location': 'Suffolk Park'
    },
    'painting': {
        'text': 'I booked Daniel to paint the exterior of our weatherboard house and the results were amazing. The finish is smooth, the colour looks perfect in the light, and his attention to detail around trims and windows was spot on. Best painting service we\'ve had in Byron Bay.',
        'author': 'Mark R.',
        'location': 'Byron Bay'
    },
    'property_maintenance': {
        'text': 'We manage a few rental properties in Ballina and use Good Hands for all our maintenance jobs. Daniel is reliable, professional, and communicates well with tenants. From repairing decks to repainting interiors, he handles everything with care. Highly recommend his property maintenance service.',
        'author': 'Emma K.',
        'location': 'Ballina'
    },
    'renovation': {
        'text': 'Daniel helped us with a small renovation in our laundry, installing new cabinetry and shelving. His carpentry skills are top-notch, and he came up with practical design ideas that made the space much more functional. You can tell he\'s got both trade skill and creative eye.',
        'author': 'Rachel P.',
        'location': 'Lennox Head'
    },
    'exterior_repairs': {
        'text': 'Our house was starting to look really tired outside. Good Hands repainted the weatherboards, fixed a few damaged panels, and even repaired some timber around the windows. The attention to detail and finish were fantastic. It\'s like a new home.',
        'author': 'David S.',
        'location': 'Ocean Shores'
    },
    'deck_build': {
        'text': 'Daniel built a new deck and pergola for us, and we couldn\'t be happier. The timber looks incredible, and the build feels solid and well-finished. He handled everything—from sourcing materials to staining the wood. It\'s rare to find a local carpenter who cares this much about quality.',
        'author': 'Lisa and James W.',
        'location': 'Mullumbimby'
    },
    'interior_repairs': {
        'text': 'I first hired Daniel for some small handyman repairs inside—fixing hinges, patching plaster, repainting a few walls—and I was so impressed with the standard of his work that I\'ve kept calling him back. It\'s great to have a local handyman who\'s this dependable.',
        'author': 'Sophie H.',
        'location': 'Bangalow'
    },
    'ongoing_maintenance': {
        'text': 'We\'ve used Good Hands a few times now—for deck maintenance, repainting, and general carpentry jobs. Daniel always does a professional job and offers great advice on how to keep things in good shape long-term. Definitely our go-to handyman in the Byron area.',
        'author': 'Tom B.',
        'location': 'Byron Bay'
    }
}

# Page-specific FAQs and testimonial mapping
PAGE_CONTENT = {
    'deck-restoration.html': {
        'testimonials': ['deck_restoration', 'deck_build'],
        'faqs': [
            {
                'question': 'How long does deck restoration take in Byron Bay?',
                'answer': 'Most deck restorations take 2-4 days depending on size and condition. This includes replacing damaged boards, sanding, cleaning, and applying marine-grade oil. Larger decks or those requiring structural repairs may take up to a week.'
            },
            {
                'question': 'What\'s the cost of deck restoration in the Northern Rivers?',
                'answer': 'Contact us for a free quote. Deck restoration costs vary based on deck size, timber condition, and repairs needed. We provide detailed quotes covering all materials and labor, with no hidden costs.'
            },
            {
                'question': 'How often should I restore my deck in coastal areas?',
                'answer': 'In Byron Bay\'s salt air environment, decks should be re-oiled every 12-18 months. Full restoration (sanding and re-oiling) is typically needed every 3-5 years, depending on sun exposure and maintenance.'
            },
            {
                'question': 'Do you use marine-grade products for coastal decks?',
                'answer': 'Yes, absolutely. We only use marine-grade oils and H4-treated timber for coastal properties. Standard products fail quickly in Byron Bay\'s salt air. We also use 316 marine stainless steel fixings to prevent rust staining.'
            },
            {
                'question': 'Can you match the existing timber on my deck?',
                'answer': 'Yes, we can source matching timber for board replacements. Common deck timbers in Byron Bay include treated pine, merbau, spotted gum, and ironbark. We\'ll match your existing timber type and grade for seamless repairs.'
            }
        ]
    },
    'deck-sanding.html': {
        'testimonials': ['deck_restoration', 'ongoing_maintenance'],
        'faqs': [
            {
                'question': 'How long does deck sanding take?',
                'answer': 'Most residential decks take 1-2 days to sand properly. This includes preparation, multiple sanding passes with different grits, and cleanup. We use professional orbital sanders to ensure an even, smooth finish without damaging the timber.'
            },
            {
                'question': 'Should I sand or replace my old deck?',
                'answer': 'If the boards are structurally sound (no rot or major cracks), sanding is cost-effective. If boards are extensively rotted, cupped, or splitting, replacement is better. We\'ll assess your deck and recommend the most economical option.'
            },
            {
                'question': 'What grit do you use for deck sanding?',
                'answer': 'We typically start with 40-60 grit to remove old coatings and grey weathered timber, then progress to 80-120 grit for smoothing. The final grit depends on your timber type and desired finish.'
            },
            {
                'question': 'How soon after sanding can I oil my deck?',
                'answer': 'Wait 24-48 hours after sanding before oiling. This allows the timber to stabilize and any raised grain to settle. We check weather conditions to ensure the timber is dry before applying oil.'
            },
            {
                'question': 'Do you sand deck stairs and railings too?',
                'answer': 'Yes, we sand all deck surfaces including stairs, railings, posts, and handrails. Consistent sanding across all components ensures even oil absorption and a professional finish.'
            }
        ]
    },
    'airbnb-maintenance.html': {
        'testimonials': ['property_maintenance', 'general_handyman'],
        'faqs': [
            {
                'question': 'How quickly can you fix Airbnb maintenance issues?',
                'answer': 'For Airbnb turnarounds, we offer same-day and next-day service for urgent repairs. We understand guest bookings mean time is money. Most small repairs (doors, handles, fixtures) are completed within 2-4 hours.'
            },
            {
                'question': 'Do you work around Airbnb guest schedules?',
                'answer': 'Yes, we\'re flexible with timing to avoid disrupting guests. We can work early mornings, between check-out and check-in, or coordinate with your cleaning team for minimal impact on bookings.'
            },
            {
                'question': 'What are the most common Airbnb maintenance issues?',
                'answer': 'The most frequent calls are for door locks, kitchen cabinet hinges, screen door repairs, deck board replacements, gutter cleaning, and touch-up painting. We handle all these quickly to maintain your 5-star rating.'
            },
            {
                'question': 'Can you do regular preventative maintenance for my Airbnb?',
                'answer': 'Absolutely. We offer monthly or quarterly maintenance checks covering decks, gutters, doors, locks, screens, and minor repairs. Preventative maintenance reduces emergency callouts and keeps your property guest-ready.'
            },
            {
                'question': 'Do you provide quotes for property managers?',
                'answer': 'Yes, we provide detailed quotes for all work and can invoice directly to property management companies. We work with several Airbnb property managers across Byron Bay and the Northern Rivers.'
            }
        ]
    },
    'property-manager-services.html': {
        'testimonials': ['property_maintenance', 'ongoing_maintenance'],
        'faqs': [
            {
                'question': 'Do you offer priority service for property managers?',
                'answer': 'Yes, property managers get priority booking and rapid response for urgent tenant maintenance. We understand rental turnarounds are time-critical, especially for holiday properties in Byron Bay.'
            },
            {
                'question': 'Can you invoice our property management company directly?',
                'answer': 'Yes, we provide detailed invoices with job descriptions, photos, and can invoice property managers directly. We\'re set up to work with your accounting systems and approval processes.'
            },
            {
                'question': 'What maintenance services do you provide for rental properties?',
                'answer': 'We handle all general handyman work: deck repairs, painting, kitchen fixes, door adjustments, screen repairs, gutter cleaning, fence repairs, and minor carpentry. Basically anything to keep rental properties tenant-ready.'
            },
            {
                'question': 'How do you communicate with tenants?',
                'answer': 'We coordinate directly with property managers but can liaise with tenants when needed. We\'re professional, punctual, and respectful of tenant privacy while completing maintenance work efficiently.'
            },
            {
                'question': 'Do you provide maintenance reports and photos?',
                'answer': 'Yes, we document all work with before/after photos and detailed reports. This helps with tenant bonds, insurance claims, and property maintenance records for owners.'
            }
        ]
    },
    'kitchen-door-repairs-northern-rivers.html': {
        'testimonials': ['general_handyman', 'interior_repairs'],
        'faqs': [
            {
                'question': 'Why won\'t my kitchen cabinet doors close properly?',
                'answer': 'In Byron Bay\'s humidity, timber swells causing doors to stick or misalign. Hinges also loosen over time. We realign doors, adjust hinges, plane swollen edges, and ensure smooth operation. Most fixes take 1-2 hours.'
            },
            {
                'question': 'Can you match my existing kitchen cabinet doors?',
                'answer': 'Yes, we can source matching doors or build custom replacements. We\'ll match the timber type, finish, and dimensions. For older kitchens where exact matches are unavailable, we can refinish all doors for consistency.'
            },
            {
                'question': 'How much does kitchen door repair cost?',
                'answer': 'Contact us for a free quote. Simple hinge adjustments start from $80-120. Door replacement or custom carpentry varies by scope. We provide clear quotes before starting any work.'
            },
            {
                'question': 'Do you repair soft-close hinges?',
                'answer': 'Yes, we repair and replace soft-close hinges. Often the soft-close mechanism wears out but the hinge is fine. We can upgrade standard hinges to soft-close or replace faulty soft-close units.'
            },
            {
                'question': 'Can you fix warped kitchen doors?',
                'answer': 'It depends on the severity. Minor warping can be corrected by planing and rehinging. Severely warped doors (especially cheap flat-pack units) need replacement. We\'ll assess and recommend the most cost-effective solution.'
            }
        ]
    },
    'emergency-repairs.html': {
        'testimonials': ['general_handyman', 'exterior_repairs'],
        'faqs': [
            {
                'question': 'How fast can you respond to emergency repairs in Byron Bay?',
                'answer': 'We aim for same-day response for genuine emergencies (storm damage, broken doors/windows, fence collapse, water damage). Call 0481 457271 and we\'ll get to you as quickly as possible, often within 2-4 hours.'
            },
            {
                'question': 'What qualifies as an emergency repair?',
                'answer': 'Emergency repairs include: storm damage making the property unsafe, broken doors/windows affecting security, collapsed fences, water leaks causing damage, or structural issues posing safety risks. We prioritize these over routine maintenance.'
            },
            {
                'question': 'Do you charge extra for emergency callouts?',
                'answer': 'Contact us for emergency rates. While emergency work may have a priority service fee, we keep costs fair and focus on making your property safe and secure quickly.'
            },
            {
                'question': 'Can you do temporary repairs and come back later?',
                'answer': 'Yes, for after-hours emergencies we can do temporary repairs to secure your property (tarps, boarding, temporary fencing), then return for permanent repairs during business hours at standard rates.'
            },
            {
                'question': 'Do you help with insurance claims for storm damage?',
                'answer': 'Yes, we provide detailed documentation, photos, and quotes for insurance claims. We\'ve worked with many Northern Rivers homeowners on storm damage repairs and understand what insurers require.'
            }
        ]
    },
    'gutter-cleaning.html': {
        'testimonials': ['property_maintenance', 'ongoing_maintenance'],
        'faqs': [
            {
                'question': 'How often should I clean my gutters in Byron Bay?',
                'answer': 'In Byron Bay, clean gutters at least twice a year—before summer storm season (October) and after autumn (May). Properties near trees need quarterly cleaning to prevent blockages and overflow.'
            },
            {
                'question': 'What happens if I don\'t clean my gutters?',
                'answer': 'Blocked gutters cause water overflow damaging fascia boards, causing roof leaks, and creating mosquito breeding grounds. In Byron Bay\'s heavy rain, blocked gutters can dump water onto decks and foundations causing rot.'
            },
            {
                'question': 'Do you repair damaged gutters while cleaning?',
                'answer': 'Yes, we can repair sagging gutters, replace rusted sections, and reseal leaking joints. We\'ll identify any issues during cleaning and provide a quote for repairs.'
            },
            {
                'question': 'How much does gutter cleaning cost in the Northern Rivers?',
                'answer': 'Contact us for a free quote based on your home size and gutter length. We provide transparent pricing with no hidden costs. Most residential properties range from $150-350 depending on size and access.'
            },
            {
                'question': 'Can you install gutter guard while cleaning?',
                'answer': 'Yes, we install gutter guard mesh to reduce future cleaning frequency. Gutter guard is particularly useful for Byron Bay properties surrounded by trees. We\'ll recommend the best type for your situation.'
            }
        ]
    },
    'fly-screen-repairs-byron-bay.html': {
        'testimonials': ['general_handyman', 'interior_repairs'],
        'faqs': [
            {
                'question': 'Can you repair torn fly screens or do they need replacing?',
                'answer': 'Small tears and holes can be patched, but large tears or degraded mesh need full replacement. Replacement is quick (usually 30-60 minutes per screen) and more cost-effective than repeated patching.'
            },
            {
                'question': 'What type of screen mesh is best for Byron Bay?',
                'answer': 'We recommend pet-proof or heavy-duty mesh for Byron Bay\'s coastal conditions. Standard fiberglass mesh degrades faster in salt air. Stainless steel mesh lasts longest but costs more. We\'ll recommend based on your budget and exposure.'
            },
            {
                'question': 'How long does fly screen replacement take?',
                'answer': 'Most fly screen repairs or replacements take 30-60 minutes per screen. For whole-house screen replacement (6-8 screens), plan for half a day. We can often complete the work while you\'re at work.'
            },
            {
                'question': 'Do you fix screen door frames that don\'t close properly?',
                'answer': 'Yes, we repair screen door frames, hinges, closers, and latches. Common issues include sagging frames, worn closers, and loose hinges. Most screen door repairs take 1-2 hours.'
            },
            {
                'question': 'Can you make custom fly screens for odd-sized windows?',
                'answer': 'Yes, we build custom fly screens for non-standard windows, doors, and openings. We measure, build the frame, install mesh, and fit it to your opening. Custom screens typically take 3-5 days from measure to install.'
            }
        ]
    },
    'handyman-byron-bay.html': {
        'testimonials': ['general_handyman', 'ongoing_maintenance', 'deck_restoration'],
        'faqs': [
            {
                'question': 'What handyman services do you offer in Byron Bay?',
                'answer': 'We handle all general handyman work: deck restoration, painting, carpentry, door repairs, kitchen fixes, fly screen repairs, gutter cleaning, fence repairs, furniture assembly, and minor renovations. If it needs fixing, we can help.'
            },
            {
                'question': 'How much do handyman services cost in Byron Bay?',
                'answer': 'Contact us for a free quote. Pricing depends on the job scope, materials, and time required. We provide transparent quotes before starting work, with no hidden costs. Small jobs often start from $120-200.'
            },
            {
                'question': 'Do you provide free quotes for handyman work?',
                'answer': 'Yes, we offer free quotes for all jobs. Call or text 0481 457271 with a description and photos, and we\'ll provide an estimate. For larger jobs, we\'ll visit the property for an accurate quote.'
            },
            {
                'question': 'Are you licensed and insured?',
                'answer': 'Yes, Good Hands Handyman is fully insured with public liability coverage. We\'re experienced in all general handyman work and carpentry, with a focus on quality and safety.'
            },
            {
                'question': 'How quickly can you start work in Byron Bay?',
                'answer': 'Availability varies by season. During quieter periods, we can often start within 1-3 days. In peak times (spring/summer), booking 1-2 weeks ahead is common. Emergency repairs get priority service.'
            },
            {
                'question': 'Do you work in surrounding areas like Suffolk Park and Belongil?',
                'answer': 'Yes, we service all Byron Bay suburbs including Suffolk Park, Belongil, Wategos, Broken Head, Tallow Beach, and surrounding areas. We\'re locally based and know Byron Bay properties well.'
            }
        ]
    },
    'handyman-ballina.html': {
        'testimonials': ['property_maintenance', 'general_handyman'],
        'faqs': [
            {
                'question': 'Do you provide handyman services in Ballina?',
                'answer': 'Yes, we regularly service Ballina and surrounding areas including Lennox Head, Alstonville, and East Ballina. We handle all general handyman work, property maintenance, and carpentry for residential and rental properties.'
            },
            {
                'question': 'How much do handyman services cost in Ballina?',
                'answer': 'Contact us for a free quote. Costs depend on the job scope and materials. We provide clear quotes before starting work. Travel from Byron Bay is included in our standard service area pricing.'
            },
            {
                'question': 'What types of jobs do you do in Ballina?',
                'answer': 'We handle deck repairs, fence repairs, gutter cleaning, painting, door repairs, kitchen maintenance, fly screens, general carpentry, and property maintenance. Basically any handyman work for homes and rental properties.'
            },
            {
                'question': 'Can you do emergency repairs in Ballina?',
                'answer': 'Yes, we respond to emergency repairs in Ballina for storm damage, broken doors/windows, fence collapses, and urgent maintenance issues. Call 0481 457271 for emergency service.'
            },
            {
                'question': 'Do you work with property managers in Ballina?',
                'answer': 'Yes, we work with several Ballina property managers for rental maintenance and Airbnb turnarounds. We provide fast service, detailed invoicing, and can coordinate with tenants as needed.'
            }
        ]
    },
    'handyman-lismore.html': {
        'testimonials': ['general_handyman', 'exterior_repairs'],
        'faqs': [
            {
                'question': 'Do you service Lismore and surrounding areas?',
                'answer': 'Yes, we provide handyman services in Lismore, Goonellabah, South Lismore, and surrounding Northern Rivers areas. We handle all general repairs, maintenance, and carpentry work.'
            },
            {
                'question': 'What handyman services are available in Lismore?',
                'answer': 'We offer deck restoration, fence repairs, gutter cleaning, painting, carpentry, door and window repairs, kitchen maintenance, and general handyman work. We handle both small repairs and larger maintenance projects.'
            },
            {
                'question': 'How much does a handyman cost in Lismore?',
                'answer': 'Contact us for a free quote specific to your job. We provide transparent pricing based on the work required. Travel to Lismore is included in our Northern Rivers service area.'
            },
            {
                'question': 'Can you help with storm damage repairs in Lismore?',
                'answer': 'Yes, we handle storm damage repairs including fence repairs, deck repairs, broken doors/windows, and structural damage. We can provide documentation and quotes for insurance claims.'
            },
            {
                'question': 'How soon can you get to Lismore for a job?',
                'answer': 'We typically schedule Lismore jobs 3-7 days in advance, depending on workload. For emergencies, we can often respond same-day or next-day. Call 0481 457271 to discuss your timeline.'
            }
        ]
    },
    'handyman-bangalow.html': {
        'testimonials': ['carpentry', 'interior_repairs'],
        'faqs': [
            {
                'question': 'Do you provide handyman services in Bangalow?',
                'answer': 'Yes, Bangalow is part of our core service area. We regularly work in Bangalow and surrounding areas including Newrybar, Nashua, and Coopers Shoot. We handle all handyman, carpentry, and maintenance work.'
            },
            {
                'question': 'Can you work on heritage properties in Bangalow?',
                'answer': 'Yes, we have experience with heritage properties and understand Bangalow\'s heritage character. We use appropriate materials and techniques for older homes and can work within council heritage guidelines.'
            },
            {
                'question': 'What are common handyman jobs in Bangalow?',
                'answer': 'Popular jobs include deck restoration (many Bangalow homes have timber decks), weatherboard painting and repairs, timber window repairs, carpentry for period homes, and general maintenance for older properties.'
            },
            {
                'question': 'How much does handyman work cost in Bangalow?',
                'answer': 'Contact us for a free quote. Pricing is based on the job scope and materials. Bangalow is close to Byron Bay, so no additional travel costs apply.'
            },
            {
                'question': 'Do you offer custom carpentry services in Bangalow?',
                'answer': 'Yes, we provide custom carpentry including shelving, cabinetry, deck builds, pergolas, and bespoke timber work. Bangalow properties often benefit from quality carpentry that matches their character.'
            }
        ]
    },
    'handyman-lennox-head.html': {
        'testimonials': ['renovation', 'general_handyman'],
        'faqs': [
            {
                'question': 'Do you service Lennox Head?',
                'answer': 'Yes, we regularly service Lennox Head and the surrounding area. We handle all handyman work, deck maintenance, painting, carpentry, and general repairs for homes and holiday properties.'
            },
            {
                'question': 'What handyman services do you offer in Lennox Head?',
                'answer': 'We provide deck restoration, painting, fence repairs, gutter cleaning, door and window repairs, kitchen maintenance, carpentry, and general handyman work. Coastal properties benefit from our marine-grade materials.'
            },
            {
                'question': 'How much do handyman services cost in Lennox Head?',
                'answer': 'Contact us for a free quote. Costs vary by job scope and materials. Lennox Head is part of our standard service area from Byron Bay, with no extra travel charges.'
            },
            {
                'question': 'Can you maintain beachfront properties in Lennox Head?',
                'answer': 'Yes, beachfront properties need specialized maintenance due to salt air. We use marine-grade oils for decks, stainless steel fixings, and coastal-appropriate paints. We understand Lennox Head\'s coastal environment well.'
            },
            {
                'question': 'Do you work on holiday rental properties in Lennox Head?',
                'answer': 'Yes, we work with several Lennox Head holiday property owners and managers. We provide fast turnaround for guest-ready maintenance and can schedule around bookings.'
            }
        ]
    },
    'handyman-services-byron-bay.html': {
        'testimonials': ['ongoing_maintenance', 'general_handyman', 'carpentry'],
        'faqs': [
            {
                'question': 'What handyman services are available in Byron Bay?',
                'answer': 'We offer comprehensive handyman services: deck restoration, carpentry, painting, fence repairs, gutter cleaning, door/window repairs, kitchen fixes, fly screens, furniture assembly, and general property maintenance.'
            },
            {
                'question': 'Are you a local Byron Bay handyman?',
                'answer': 'Yes, Good Hands Handyman is locally based in Byron Bay. We know the area, understand coastal property maintenance needs, and service Byron Bay and the entire Northern Rivers region.'
            },
            {
                'question': 'How do I book handyman services in Byron Bay?',
                'answer': 'Call or text Dan on 0481 457271, or use the contact form on our website. Describe your job and we\'ll provide a free quote. For simple jobs, photos via text help us quote accurately.'
            },
            {
                'question': 'Do you handle both small and large handyman jobs?',
                'answer': 'Yes, we handle everything from small repairs (fixing a door, replacing a hinge) to larger projects (full deck restorations, painting entire homes, custom carpentry). No job too small or too large.'
            },
            {
                'question': 'What makes a good handyman service in Byron Bay?',
                'answer': 'A good Byron Bay handyman understands coastal maintenance (salt air, humidity, marine-grade products), turns up on time, does quality work, communicates clearly, and cleans up afterwards. That\'s what we deliver.'
            },
            {
                'question': 'Can you provide ongoing maintenance for my Byron Bay property?',
                'answer': 'Yes, we offer regular maintenance schedules (monthly, quarterly, yearly) covering decks, gutters, painting, and general repairs. Preventative maintenance saves money long-term and keeps your property in top condition.'
            }
        ]
    },
    'index.html': {
        'testimonials': ['general_handyman', 'deck_restoration', 'carpentry', 'property_maintenance'],
        'faqs': [
            {
                'question': 'What areas do you service?',
                'answer': 'We service Byron Bay and the entire Northern Rivers region including Ballina, Lennox Head, Bangalow, Mullumbimby, Lismore, Ocean Shores, Brunswick Heads, and surrounding areas. Based in Byron Bay, we cover the whole region.'
            },
            {
                'question': 'What services does Good Hands Handyman offer?',
                'answer': 'We provide comprehensive handyman services: deck restoration and maintenance, painting, carpentry, fence repairs, gutter cleaning, kitchen repairs, door and window fixes, fly screens, emergency repairs, and general property maintenance.'
            },
            {
                'question': 'How do I get a quote?',
                'answer': 'Call or text Dan on 0481 457271 with a description of your job. Photos help for accurate quotes. We provide free, no-obligation quotes for all work with transparent pricing and no hidden costs.'
            },
            {
                'question': 'Are you licensed and insured?',
                'answer': 'Yes, Good Hands Handyman is fully insured with public liability coverage. We have extensive experience in general handyman work, carpentry, and property maintenance across the Northern Rivers.'
            },
            {
                'question': 'Do you work on residential and commercial properties?',
                'answer': 'We primarily work on residential properties, holiday homes, Airbnb properties, and rental properties. We work with homeowners, property managers, and real estate agents throughout Byron Bay and the Northern Rivers.'
            },
            {
                'question': 'What makes Good Hands different from other handyman services?',
                'answer': 'We\'re local to Byron Bay, understand coastal property maintenance, use quality materials (marine-grade where needed), turn up on time, do thorough work, and clean up properly. We\'re reliable, professional, and care about quality.'
            }
        ]
    }
}


def create_faq_schema(faqs):
    """Create FAQ Schema markup for SEO"""
    schema = {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": []
    }

    for faq in faqs:
        schema["mainEntity"].append({
            "@type": "Question",
            "name": faq['question'],
            "acceptedAnswer": {
                "@type": "Answer",
                "text": faq['answer']
            }
        })

    return json.dumps(schema, indent=2)


def create_testimonial_html(testimonial_keys):
    """Create testimonial section HTML"""
    testimonials_html = []

    for key in testimonial_keys[:3]:  # Max 3 testimonials per page
        if key in TESTIMONIALS:
            t = TESTIMONIALS[key]
            testimonials_html.append(f'''
                <div style="background: white; padding: 24px; border-radius: 8px; border-left: 4px solid #3182CE;">
                    <p style="font-size: 1rem; color: #2D3748; margin-bottom: 16px; line-height: 1.6;">"{t['text']}"</p>
                    <p style="font-size: 0.875rem; color: #718096; margin: 0;"><strong>{t['author']}</strong> - {t['location']}</p>
                </div>''')

    return '\n'.join(testimonials_html)


def create_faq_html(faqs):
    """Create FAQ section HTML"""
    faq_items = []

    for faq in faqs:
        faq_items.append(f'''
            <div style="margin-bottom: 24px;">
                <h3 style="font-size: 1.125rem; font-weight: 600; color: #2D3748; margin-bottom: 8px;">{faq['question']}</h3>
                <p style="font-size: 1rem; color: #4A5568; line-height: 1.6;">{faq['answer']}</p>
            </div>''')

    return '\n'.join(faq_items)


def add_sections_to_page(filepath, page_config):
    """Add FAQ and Testimonial sections to a page"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        # Check if already has FAQ or testimonials
        if 'Frequently Asked Questions' in content or '"@type": "FAQPage"' in content:
            return False, "already has FAQ section"

        # Create sections
        testimonials_html = create_testimonial_html(page_config['testimonials'])
        faq_html = create_faq_html(page_config['faqs'])
        faq_schema = create_faq_schema(page_config['faqs'])

        # Build combined section
        new_section = f'''
    <!-- Testimonials -->
    <section style="padding: 60px 0; background: #EDF2F7;">
        <div class="container" style="max-width: 1200px; margin: 0 auto; padding: 0 24px;">
            <h2 style="font-size: 1.75rem; font-weight: 700; margin-bottom: 32px; color: #2D3748;">What Our Customers Say</h2>
            <div style="display: grid; gap: 24px;">
{testimonials_html}
            </div>
        </div>
    </section>

    <!-- FAQ Section -->
    <section style="padding: 60px 0; background: white;">
        <div class="container" style="max-width: 1200px; margin: 0 auto; padding: 0 24px;">
            <h2 style="font-size: 1.75rem; font-weight: 700; margin-bottom: 32px; color: #2D3748;">Frequently Asked Questions</h2>
{faq_html}
        </div>
    </section>

    <!-- FAQ Schema for SEO -->
    <script type="application/ld+json">
{faq_schema}
    </script>
'''

        # Find closing </body> or </article> tag to insert before
        body_match = re.search(r'</body>', content, re.IGNORECASE)
        article_match = re.search(r'</article>', content, re.IGNORECASE)

        if article_match and not body_match:
            # Blog post structure
            insert_pos = article_match.start()
        elif body_match:
            # Regular page structure
            insert_pos = body_match.start()
        else:
            return False, "no suitable insertion point found"

        # Insert sections
        updated_content = content[:insert_pos] + new_section + '\n    ' + content[insert_pos:]

        # Write updated file
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(updated_content)

        return True, "success"

    except Exception as e:
        return False, str(e)


def main():
    print("Adding FAQs and Testimonials to priority pages...")
    print("=" * 70)

    updated = 0
    skipped = 0

    for filename, config in PAGE_CONTENT.items():
        filepath = Path(filename)
        if filepath.exists():
            success, message = add_sections_to_page(filepath, config)
            if success:
                print(f"✓ {filename}")
                print(f"  - Added {len(config['testimonials'])} testimonials")
                print(f"  - Added {len(config['faqs'])} FAQs with Schema markup")
                updated += 1
            else:
                print(f"⊘ {filename} - {message}")
                skipped += 1
        else:
            print(f"✗ {filename} - not found")

    print("=" * 70)
    print(f"\n✅ RESULTS:")
    print(f"   {updated} pages updated with FAQs + Testimonials")
    print(f"   {skipped} pages skipped (already have content)")
    print(f"\n📊 SEO IMPROVEMENTS:")
    print(f"   - FAQ Schema markup for rich snippets")
    print(f"   - Service-specific long-tail keyword targeting")
    print(f"   - Social proof with real customer testimonials")
    print(f"   - Increased page content depth (+300-500 words/page)")
    print(f"\n🎯 Estimated impact: +2-3 SEO points")

if __name__ == "__main__":
    main()
