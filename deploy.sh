#!/bin/bash
echo "Deploying Property Manager Services page..."
echo "Files ready for deployment:"
echo "- property-manager-services.html (NEW)"
echo "- Updated footer navigation on all pages"
echo ""
echo "Attempting to push to GitHub..."
git push origin main
echo ""
echo "If push succeeds, Netlify will auto-deploy."
echo "If push fails, manually drag /Users/danielneale/GoodHands_02/ folder to Netlify dashboard."