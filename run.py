#!/usr/bin/env python3
"""
Sentiment Analysis Bot Runner
Author: RSK World (https://rskworld.in)
Founded by: Molla Samser
Designer & Tester: Rima Khatun
Contact: help@rskworld.in, +91 93305 39277
Year: 2026
"""

import os
import sys
from app import app

def main():
    """Main entry point for the application"""
    
    # Print startup banner
    print("=" * 60)
    print("🤖 SENTIMENT ANALYSIS BOT")
    print("=" * 60)
    print("📊 Features: Real-time sentiment analysis, emotion detection")
    print("🎯 Capabilities: Response adaptation, feedback collection")
    print("🌐 Web Interface: http://localhost:5000")
    print("📈 API Endpoints: /api/chat, /api/report, /api/reset")
    print("-" * 60)
    print("👤 Created by RSK World (https://rskworld.in)")
    print("📞 Contact: help@rskworld.in | +91 93305 39277")
    print("👨‍💻 Founder: Molla Samser")
    print("👩‍💻 Designer & Tester: Rima Khatun")
    print("📅 Year: 2026")
    print("📍 Nutanhat, Mongolkote, Purba Burdwan, West Bengal, India")
    print("=" * 60)
    
    # Check if running in production mode
    if os.environ.get('FLASK_ENV') == 'production':
        print("🚀 Running in PRODUCTION mode")
        print("⚠️  Make sure all security configurations are set")
    else:
        print("🔧 Running in DEVELOPMENT mode")
    
    print("🌟 Starting server...")
    print("-" * 60)
    
    # Run the Flask application
    try:
        app.run(
            host=os.environ.get('HOST', '0.0.0.0'),
            port=int(os.environ.get('PORT', 5000)),
            debug=os.environ.get('FLASK_DEBUG', 'True').lower() == 'true'
        )
    except KeyboardInterrupt:
        print("\n👋 Server stopped by user")
        sys.exit(0)
    except Exception as e:
        print(f"❌ Error starting server: {e}")
        sys.exit(1)

if __name__ == '__main__':
    main()
