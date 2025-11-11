#!/usr/bin/env python3
"""
Add FAQs and testimonials to 10 new property prep blog posts
"""

import re
from pathlib import Path
import json

# Testimonials to use
TESTIMONIALS = {
    'general_handyman': {
        'text': 'Daniel from Good Hands has been a lifesaver. I\'ve called him for everything from fixing doors and patching walls to sorting out small plumbing jobs. He always turns up when he says he will, does quality work, and leaves everything clean and tidy. Easily the best handyman service in the Northern Rivers.',
        'author': 'Sarah M.',
        'location': 'Byron Bay'
    },
    'property_maintenance': {
        'text': 'We manage a few rental properties in Ballina and use Good Hands for all our maintenance jobs. Daniel is reliable, professional, and communicates well with tenants. From repairing decks to repainting interiors, he handles everything with care. Highly recommend his property maintenance service.',
        'author': 'Emma K.',
        'location': 'Ballina'
    },
    'deck_restoration': {
        'text': 'Our old deck was grey, splintered, and starting to rot. Daniel completely transformed it. He replaced damaged boards, sanded everything back, and re-oiled it beautifully. It looks brand new now. I highly recommend Good Hands for any deck restoration or timber maintenance.',
        'author': 'Jennifer L.',
        'location': 'Suffolk Park'
    },
    'ongoing_maintenance': {
        'text': 'We\'ve used Good Hands a few times now—for deck maintenance, repainting, and general carpentry jobs. Daniel always does a professional job and offers great advice on how to keep things in good shape long-term. Definitely our go-to handyman in the Byron area.',
        'author': 'Tom B.',
        'location': 'Byron Bay'
    }
}

# Blog-specific FAQs and testimonials
BLOG_CONTENT = {
    'bought-house-byron-bay-move-in-checklist.html': {
        'testimonials': ['general_handyman', 'ongoing_maintenance'],
        'faqs': [
            {
                'question': 'How much does a pre-move inspection cost in Byron Bay?',
                'answer': 'A comprehensive pre-move inspection costs $120-$250 depending on property size. This includes a detailed walk-through, photo documentation of all issues found, prioritized repair list, and cost estimates for each fix.'
            },
            {
                'question': 'Can you do the inspection if I\'m still interstate?',
                'answer': 'Yes, absolutely. Most of my pre-move inspections are for interstate property owners. I send a detailed photo report showing every issue, organized by priority (urgent, important, can wait), so you can make informed decisions remotely.'
            },
            {
                'question': 'What\'s the typical cost to get a Byron Bay property move-in ready?',
                'answer': 'For a standard 3-bedroom Byron Bay property, basic move-in prep (inspection, minor repairs, cleaning, gutter cleaning) costs $850-$1,500. If you need painting, deck work, or more extensive repairs, budget $2,500-$5,000.'
            },
            {
                'question': 'How long before move-in should I organize the inspection?',
                'answer': 'Ideally 4-6 weeks before your move-in date. This gives you time to organize any repairs while the property is still empty. If you\'re on a tighter timeline, I can often fit inspections in within a week.'
            },
            {
                'question': 'Do you coordinate all the repairs or just inspect?',
                'answer': 'I do both. I can inspect and provide a report for you to organize repairs yourself, or I can handle everything—inspection, coordinating trades, completing repairs, and sending you progress updates. Most interstate owners prefer the full service.'
            }
        ]
    },
    'hidden-repairs-new-byron-properties-move-in.html': {
        'testimonials': ['general_handyman', 'deck_restoration'],
        'faqs': [
            {
                'question': 'Why do building inspectors miss these repairs?',
                'answer': 'Building inspectors focus on structural issues, pests, and major defects that affect property value. They\'re not checking if cupboard doors close properly, if flyscreens work, or if silicone needs replacing—things that affect livability but not structural safety.'
            },
            {
                'question': 'Can I get these repairs done before settlement?',
                'answer': 'Sometimes, but it depends on your contract and the seller\'s cooperation. Most commonly, these repairs are done in the 1-2 weeks after settlement before you move in, while the property is still empty.'
            },
            {
                'question': 'How do you check deck substructure without damaging anything?',
                'answer': 'I crawl underneath the deck with a torch and inspect bearers, joists, and posts. I also walk the deck feeling for soft spots and test railings for stability. It\'s non-invasive inspection that identifies problems without causing damage.'
            },
            {
                'question': 'What\'s the most commonly missed issue in Byron Bay properties?',
                'answer': 'Deck substructure rot. Everyone looks at the deck boards, but the timber underneath rots first in Byron\'s coastal humidity. I find this on about 60% of Byron Bay properties I inspect for new owners.'
            },
            {
                'question': 'Should I fix everything before moving in or can some wait?',
                'answer': 'I prioritize repairs into urgent (safety or prevents damage), important (affects livability), and can wait (cosmetic). Fix urgent and important before move-in. Cosmetic stuff can wait until you\'re settled in.'
            }
        ]
    },
    'byron-bay-home-rent-ready-one-week.html': {
        'testimonials': ['property_maintenance', 'ongoing_maintenance'],
        'faqs': [
            {
                'question': 'Is one week really enough time to get a property rent-ready?',
                'answer': 'For a standard tenancy turnover (minor repairs, cleaning, touch-ups), yes. But if you need extensive work like full room repainting or deck restoration, you need 2-3 weeks minimum. I\'ll tell you honestly what\'s realistic for your timeline.'
            },
            {
                'question': 'Do you work with property managers in Byron Bay?',
                'answer': 'Yes, I work with several Byron Bay and Northern Rivers property managers on regular rental turnarounds. Property managers get priority service because I understand vacant days cost you money.'
            },
            {
                'question': 'What if you find additional problems during the work?',
                'answer': 'I send photos and a quote for any additional work found. You decide if it needs doing now or can wait. No surprises—you approve everything before I proceed.'
            },
            {
                'question': 'Can you coordinate cleaning and gardening too?',
                'answer': 'Yes, I coordinate professional cleaners and gardeners as part of the rental prep service. You deal with me, I organize the rest, and you get one invoice for everything.'
            },
            {
                'question': 'How much notice do you need for a one-week turnaround?',
                'answer': 'Contact me as soon as your tenants give notice. If I have availability, I can slot you in. During busy periods (spring/summer), 2-3 weeks notice is better, but I prioritize urgent rental turnarounds where possible.'
            }
        ]
    },
    'remote-buyers-byron-bay-finding-reliable-trades.html': {
        'testimonials': ['general_handyman', 'property_maintenance'],
        'faqs': [
            {
                'question': 'Why don\'t Byron Bay tradies respond to my enquiries?',
                'answer': 'Most Byron Bay tradies are fully booked with local repeat clients and don\'t need to chase new work. Remote enquiries often go to the bottom of the list. You need someone who specializes in working with interstate owners.'
            },
            {
                'question': 'How do I know a tradie is reliable if I can\'t meet them in person?',
                'answer': 'Ask for references from other interstate property owners, check if they provide written quotes and photo updates, and see if they communicate professionally. A reliable tradie working remotely will have systems in place for this.'
            },
            {
                'question': 'Should I pay a deposit for remote work?',
                'answer': 'Yes, 50% deposit is normal for remote work. It secures your booking and shows you\'re serious. Never pay 100% upfront, but deposit plus payment on completion (with photos) is standard and fair.'
            },
            {
                'question': 'What if the work isn\'t done properly and I\'m not there to check?',
                'answer': 'Work with tradies who send progress photos and final completion photos. You should see before, during, and after shots of all work. If something doesn\'t look right, raise it immediately before making final payment.'
            },
            {
                'question': 'Can I organize multiple trades or should I find one coordinator?',
                'answer': 'One coordinator is way easier when you\'re remote. Find a reliable handyman who can do general work and coordinate specialists (electricians, plumbers) when needed. You deal with one person instead of five.'
            }
        ]
    },
    'first-week-keys-byron-bay-property-checklist.html': {
        'testimonials': ['general_handyman', 'deck_restoration'],
        'faqs': [
            {
                'question': 'What if I discover major problems in the first week after settlement?',
                'answer': 'Document everything with photos immediately. Some issues might be grounds for legal action if they weren\'t disclosed. Contact a solicitor if it\'s serious. For most issues, budget for repairs and get quotes to fix them before move-in.'
            },
            {
                'question': 'Should I do the first week inspection myself or hire someone?',
                'answer': 'If you\'re on-site, you can do a basic inspection yourself. If you\'re interstate, definitely hire someone local who knows what to look for in Byron Bay properties. They\'ll catch things you\'d miss and provide detailed documentation.'
            },
            {
                'question': 'How long does it take to get utilities connected in Byron Bay?',
                'answer': 'Electricity and water transfers are usually instant if you organize them on settlement day. Internet can take 2-4 weeks in Byron Bay, so order it early. Gas (if applicable) is usually 1-3 days.'
            },
            {
                'question': 'What\'s the most important thing to do in the first week?',
                'answer': 'Test everything that affects safety and livability: hot water, locks, electrical, plumbing. These are things that need to work from day one. Cosmetic stuff can wait, but you need the basics functioning before move-in.'
            },
            {
                'question': 'Can repairs be done while I\'m living in the property?',
                'answer': 'Yes, but it\'s disruptive. Painting, deck work, and messy repairs are much easier when the property is empty. If possible, schedule major work before you move in, then handle minor stuff after you\'re settled.'
            }
        ]
    },
    'byron-bay-rental-ready-cost-guide.html': {
        'testimonials': ['property_maintenance', 'general_handyman'],
        'faqs': [
            {
                'question': 'Why does rental prep cost more in Byron Bay than other areas?',
                'answer': 'Byron Bay\'s coastal environment requires marine-grade materials and specialized maintenance. Decks need specific treatments, salt air damages fixtures faster, and the rental market expects high presentation standards. Quality work costs more but protects your investment.'
            },
            {
                'question': 'Can I save money by doing some of the work myself?',
                'answer': 'If you\'re local and handy, yes. But if you\'re interstate, your time flying to Byron and back costs more than hiring someone local. DIY also risks mistakes that cost more to fix later. Professional work done right the first time is usually cheaper overall.'
            },
            {
                'question': 'Should I upgrade fixtures or just maintain what\'s there?',
                'answer': 'Depends on your rental target. Basic maintenance is fine for long-term rentals. If you\'re targeting Airbnb or premium rentals, upgrading fixtures, painting, and improving presentation gets you higher rental returns.'
            },
            {
                'question': 'How do I know if I\'m getting a fair price?',
                'answer': 'Get 2-3 quotes for major work. For Byron Bay, expect to pay 10-20% more than regional NSW due to coastal location and demand. Super cheap quotes often mean poor quality or corners being cut.'
            },
            {
                'question': 'Is preventative maintenance really worth it for rentals?',
                'answer': 'Absolutely. $500/year in preventative maintenance (gutter cleaning, deck oiling, minor repairs) prevents $2,000-5,000 in emergency repairs between tenants. It also reduces vacancy time because the property stays rent-ready.'
            }
        ]
    },
    'buying-sight-unseen-byron-bay-safety-checklist.html': {
        'testimonials': ['general_handyman', 'ongoing_maintenance'],
        'faqs': [
            {
                'question': 'Is buying sight-unseen in Byron Bay risky?',
                'answer': 'It has risks, but they\'re manageable. Get a thorough building inspection before settlement, then a detailed pre-move inspection after settlement. With good inspections and a local contact for repairs, most sight-unseen purchases work out fine.'
            },
            {
                'question': 'What safety issues should I be most concerned about?',
                'answer': 'Deck stability (rotted railings or substructure), electrical safety (old wiring, broken outlets), security (broken locks), and water leaks (can cause structural damage if ignored). These are the urgent fixes before move-in.'
            },
            {
                'question': 'How detailed should the pre-move inspection be?',
                'answer': 'Very detailed. You want 100+ photos covering every room, all fixtures, deck condition, outdoor areas, under the house, and any issues found. The inspection should answer "Can I move in tomorrow?" or "What needs fixing first?"'
            },
            {
                'question': 'What if the property is worse than the photos suggested?',
                'answer': 'This happens occasionally with sight-unseen purchases. Budget 15-20% extra for unexpected repairs. If major undisclosed issues appear, you might have legal recourse depending on your contract and vendor disclosure.'
            },
            {
                'question': 'Should I delay move-in if safety issues are found?',
                'answer': 'Yes, if they\'re genuine safety issues like unstable decks, electrical hazards, or major water leaks. Better to delay a week and arrive to a safe property than move in with these problems unresolved.'
            }
        ]
    },
    'byron-bay-home-maintenance-schedule-new-owners.html': {
        'testimonials': ['ongoing_maintenance', 'deck_restoration'],
        'faqs': [
            {
                'question': 'Is Byron Bay maintenance really that different from other areas?',
                'answer': 'Yes, significantly. Salt air, high UV, humidity, and coastal weather damage buildings faster. What works in Brisbane or Sydney doesn\'t work in Byron Bay. You need marine-grade products and more frequent maintenance.'
            },
            {
                'question': 'Can I skip monthly maintenance and just do annual checks?',
                'answer': 'Not recommended for Byron Bay coastal properties. Monthly deck hosing and quick checks take 15 minutes but prevent thousands in rot damage. Skipping monthly maintenance means you\'ll pay for it in repairs later.'
            },
            {
                'question': 'What happens if I can\'t maintain the schedule because I\'m interstate?',
                'answer': 'Hire someone local for quarterly maintenance visits. I offer this service—I visit the property every 3 months, complete the checklist, send photos, and report any issues. Costs $180-$280 per visit, much cheaper than flying to Byron quarterly.'
            },
            {
                'question': 'Which maintenance tasks are most critical in Byron Bay?',
                'answer': 'Gutter cleaning before wet season, deck treatment annually, monthly salt removal from timber, and mold checks quarterly. These four tasks prevent 80% of expensive Byron Bay property problems.'
            },
            {
                'question': 'How much should I budget annually for Byron Bay property maintenance?',
                'answer': 'For a standard 3-bedroom coastal property: $1,500-$3,000 per year. This covers gutter cleaning, deck treatment, minor repairs, and preventative maintenance. Neglecting maintenance costs way more when things fail.'
            }
        ]
    },
    'line-up-trades-before-moving-byron-bay.html': {
        'testimonials': ['general_handyman', 'property_maintenance'],
        'faqs': [
            {
                'question': 'How early should I start organizing trades before moving to Byron Bay?',
                'answer': '4-6 weeks before your move-in date is ideal. Good Byron Bay tradies book out weeks ahead. Starting early gives you time to find reliable people, get quotes, and schedule work without stress.'
            },
            {
                'question': 'Should I organize trades before or after settlement?',
                'answer': 'After settlement for most work, because you need property access and can\'t legally arrange work before you own it. However, you can line up quotes and bookings before settlement to start work immediately after.'
            },
            {
                'question': 'What if trades can\'t access the property because I\'m not there?',
                'answer': 'Organize key access through your real estate agent, conveyancer, or a trusted neighbor. Make it easy for trades to access the property without you being on-site. Clear access arrangements prevent delays.'
            },
            {
                'question': 'Is it better to hire one person to coordinate everything or multiple trades?',
                'answer': 'One coordinator is much easier when you\'re interstate. They handle general work, coordinate specialists, manage the timeline, and you get one point of contact instead of chasing five different people.'
            },
            {
                'question': 'What should I budget for unexpected issues during pre-move work?',
                'answer': 'Add 15-20% to your budget for unexpected problems. Almost every Byron Bay property reveals additional issues once work starts. Better to have it budgeted and not need it than get caught short.'
            }
        ]
    },
    'inspecting-newly-bought-home-northern-rivers-checklist.html': {
        'testimonials': ['general_handyman', 'deck_restoration'],
        'faqs': [
            {
                'question': 'What\'s the difference between a building inspection and your pre-move inspection?',
                'answer': 'Building inspections focus on structural issues and major defects affecting property value. My pre-move inspections focus on livability—will everything work when you move in? Do doors close, taps work, deck is safe? Practical stuff building inspectors don\'t check.'
            },
            {
                'question': 'Do you climb on the roof during inspections?',
                'answer': 'No, that requires specific insurance and qualifications. I check roofs from ground level and with a ladder where safe. For detailed roof inspections, I recommend licensed roof inspectors.'
            },
            {
                'question': 'How long does a comprehensive property inspection take?',
                'answer': 'About 90 minutes for a standard 3-bedroom Byron Bay property. Larger properties or those with extensive issues take longer. I\'m thorough—I check everything that affects whether the property is genuinely move-in ready.'
            },
            {
                'question': 'Can you provide the inspection report in a specific format?',
                'answer': 'I provide photos (100-150 typically), written report in three priority sections (urgent, important, can wait), cost estimates for each repair, and recommended timeline. If you need a specific format, let me know.'
            },
            {
                'question': 'What should I do if the inspection finds major unexpected problems?',
                'answer': 'If it\'s before settlement, you might have legal options depending on vendor disclosure. If it\'s after settlement, budget for repairs and prioritize by urgency. I provide clear cost estimates so you can make informed decisions.'
            }
        ]
    }
}


def create_faq_schema(faqs):
    """Create FAQ Schema markup"""
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


def add_faq_testimonial_sections(filepath, config):
    """Add FAQ and testimonial sections before </article>"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        # Check if already has FAQs
        if 'Frequently Asked Questions' in content:
            return False, "already has FAQs"

        # Create testimonial HTML
        testimonial_html = []
        for t_key in config['testimonials'][:2]:  # Max 2 testimonials
            t = TESTIMONIALS[t_key]
            testimonial_html.append(f'''
                <div style="background: white; padding: 24px; border-radius: 8px; border-left: 4px solid #3182CE;">
                    <p style="font-size: 1rem; color: #2D3748; margin-bottom: 16px; line-height: 1.6;">"{t['text']}"</p>
                    <p style="font-size: 0.875rem; color: #718096; margin: 0;"><strong>{t['author']}</strong> - {t['location']}</p>
                </div>''')

        # Create FAQ HTML
        faq_html = []
        for faq in config['faqs']:
            faq_html.append(f'''
            <div style="margin-bottom: 24px;">
                <h3 style="font-size: 1.125rem; font-weight: 600; color: #2D3748; margin-bottom: 8px;">{faq['question']}</h3>
                <p style="font-size: 1rem; color: #4A5568; line-height: 1.6;">{faq['answer']}</p>
            </div>''')

        # Create FAQ Schema
        faq_schema = create_faq_schema(config['faqs'])

        # Build sections
        sections = f'''
    <!-- Testimonials -->
    <section style="padding: 60px 0; background: #EDF2F7;">
        <div class="container" style="max-width: 1200px; margin: 0 auto; padding: 0 24px;">
            <h2 style="font-size: 1.75rem; font-weight: 700; margin-bottom: 32px; color: #2D3748;">What Our Customers Say</h2>
            <div style="display: grid; gap: 24px;">
{''.join(testimonial_html)}
            </div>
        </div>
    </section>

    <!-- FAQ Section -->
    <section style="padding: 60px 0; background: white;">
        <div class="container" style="max-width: 1200px; margin: 0 auto; padding: 0 24px;">
            <h2 style="font-size: 1.75rem; font-weight: 700; margin-bottom: 32px; color: #2D3748;">Frequently Asked Questions</h2>
{''.join(faq_html)}
        </div>
    </section>

    <!-- FAQ Schema for SEO -->
    <script type="application/ld+json">
{faq_schema}
    </script>
'''

        # Find </article> tag
        article_match = re.search(r'</article>', content, re.IGNORECASE)
        if not article_match:
            return False, "no article tag found"

        # Insert before </article>
        updated_content = content[:article_match.start()] + sections + '\n        ' + content[article_match.start():]

        # Write
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(updated_content)

        return True, "success"

    except Exception as e:
        return False, str(e)


def main():
    print("Adding FAQs and Testimonials to 10 property prep blogs...")
    print("=" * 70)

    updated = 0
    for filename, config in BLOG_CONTENT.items():
        filepath = Path(filename)
        if filepath.exists():
            success, message = add_faq_testimonial_sections(filepath, config)
            if success:
                print(f"✓ {filename}")
                print(f"  - Added {len(config['testimonials'])} testimonials")
                print(f"  - Added {len(config['faqs'])} FAQs with Schema markup")
                updated += 1
            else:
                print(f"⊘ {filename} - {message}")
        else:
            print(f"✗ {filename} - not found")

    print("=" * 70)
    print(f"\n✅ RESULTS:")
    print(f"   {updated}/10 property prep blogs updated with FAQs + Testimonials")
    print(f"\n📊 SEO IMPROVEMENTS:")
    print(f"   - FAQ Schema markup for rich snippets")
    print(f"   - 50+ new FAQ targets for long-tail keywords")
    print(f"   - Social proof with real customer testimonials")
    print(f"   - Increased page content depth")

if __name__ == "__main__":
    main()
