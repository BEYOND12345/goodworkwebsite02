#!/bin/bash

# Script to fix all meta descriptions to optimal 120-160 character length

echo "Fixing all meta descriptions to optimal length..."

# Fix areas.html (213 chars -> shorten)
sed -i '' 's/meta name="description" content="Service Areas - Byron Bay, Ballina, Lismore, Bangalow, Ocean Shores, Lennox Head, Northern Rivers NSW. Professional handyman services throughout the region. Same day emergency repairs, deck restoration, kitchen repairs across all areas."/meta name="description" content="Service areas: Byron Bay, Ballina, Lismore, Northern Rivers NSW. Professional handyman services, emergency repairs, deck restoration. Call Dan 0481 457271"/' areas.html

# Fix privacy-policy.html (96 chars -> lengthen)
sed -i '' 's/meta name="description" content="Privacy Policy - Good Hands Handyman Byron Bay Northern Rivers NSW"/meta name="description" content="Privacy Policy for Good Hands Handyman services in Byron Bay and Northern Rivers NSW. How we protect your personal information. Call 0481 457271"/' privacy-policy.html

echo "Meta description fixes applied!"
echo "Run verification script to check results..."