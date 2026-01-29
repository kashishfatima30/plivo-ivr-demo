#!/usr/bin/env python3
"""
Plivo IVR Demo - CLI Version
Command-line interface to trigger outbound calls
"""

import plivo
import os
from dotenv import load_dotenv
import argparse
import sys

# Load environment variables
load_dotenv()

# Plivo Configuration
PLIVO_AUTH_ID = os.getenv('PLIVO_AUTH_ID')
PLIVO_AUTH_TOKEN = os.getenv('PLIVO_AUTH_TOKEN')
PLIVO_PHONE_NUMBER = os.getenv('PLIVO_PHONE_NUMBER')
BASE_URL = os.getenv('BASE_URL', 'http://localhost:5000')


def validate_config():
    """Validate that all required configuration is present"""
    if not PLIVO_AUTH_ID:
        print("❌ Error: PLIVO_AUTH_ID not set in environment variables")
        return False
    if not PLIVO_AUTH_TOKEN:
        print("❌ Error: PLIVO_AUTH_TOKEN not set in environment variables")
        return False
    if not PLIVO_PHONE_NUMBER:
        print("❌ Error: PLIVO_PHONE_NUMBER not set in environment variables")
        return False
    return True


def validate_phone_number(phone_number):
    """Validate phone number format (E.164)"""
    if not phone_number.startswith('+'):
        print("❌ Error: Phone number must start with '+' (E.164 format)")
        print("   Example: +12025551234")
        return False
    
    # Remove + and check if remaining is digits
    digits = phone_number[1:]
    if not digits.isdigit():
        print("❌ Error: Phone number must contain only digits after '+'")
        return False
    
    if len(digits) < 10 or len(digits) > 15:
        print("❌ Error: Phone number should be 10-15 digits long")
        return False
    
    return True


def make_call(to_number):
    """Initiate an outbound call to the specified number"""
    
    print(f"\n📞 Initiating call to {to_number}...")
    print(f"   From: {PLIVO_PHONE_NUMBER}")
    print(f"   Webhook URL: {BASE_URL}/answer")
    
    try:
        # Initialize Plivo client
        client = plivo.RestClient(auth_id=PLIVO_AUTH_ID, auth_token=PLIVO_AUTH_TOKEN)
        
        # Make the call
        response = client.calls.create(
            from_=PLIVO_PHONE_NUMBER,
            to_=to_number,
            answer_url=f'{BASE_URL}/answer',
            answer_method='POST'
        )
        
        print("\n✅ Call initiated successfully!")
        print(f"   Call UUID: {response.call_uuid}")
        print(f"   Status: {response.message}")
        print("\n📱 Please answer your phone and follow the IVR prompts:")
        print("   Level 1: Press 1 for English, 2 for Spanish")
        print("   Level 2: Press 1 for audio, 2 to connect to associate")
        print()
        
        return True
        
    except plivo.exceptions.PlivoRestError as e:
        print(f"\n❌ Plivo API Error: {e}")
        print("   Please check your credentials and phone number.")
        return False
        
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")
        return False


def display_config():
    """Display current configuration"""
    print("\n⚙️  Current Configuration:")
    print(f"   Auth ID: {PLIVO_AUTH_ID[:8]}... (hidden)")
    print(f"   Auth Token: {PLIVO_AUTH_TOKEN[:8]}... (hidden)")
    print(f"   Plivo Number: {PLIVO_PHONE_NUMBER}")
    print(f"   Webhook Base URL: {BASE_URL}")
    print()


def main():
    """Main CLI function"""
    parser = argparse.ArgumentParser(
        description='Plivo IVR Demo - CLI Interface',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog='''
Examples:
  python cli.py +12025551234
  python cli.py +12025551234 --show-config
  python cli.py --config

Make sure your Flask application is running before making calls!
        '''
    )
    
    parser.add_argument(
        'phone_number',
        nargs='?',
        help='Phone number to call (E.164 format, e.g., +12025551234)'
    )
    
    parser.add_argument(
        '-c', '--config',
        action='store_true',
        help='Show current configuration'
    )
    
    parser.add_argument(
        '-s', '--show-config',
        action='store_true',
        help='Show configuration before making call'
    )
    
    args = parser.parse_args()
    
    # Display banner
    print("\n" + "="*60)
    print("  📞 Plivo IVR Demo - CLI Interface")
    print("  InspireWorks Technical Assignment")
    print("="*60)
    
    # Show config if requested
    if args.config or args.show_config:
        if not validate_config():
            print("\n❌ Configuration incomplete. Please check your .env file.")
            sys.exit(1)
        display_config()
    
    # If only showing config, exit
    if args.config and not args.phone_number:
        sys.exit(0)
    
    # Validate phone number is provided
    if not args.phone_number:
        print("\n❌ Error: Phone number is required")
        print("\nUsage: python cli.py <phone_number>")
        print("Example: python cli.py +12025551234")
        print("\nFor help: python cli.py --help")
        sys.exit(1)
    
    # Validate configuration
    if not validate_config():
        print("\n💡 Tip: Copy .env.example to .env and add your credentials")
        sys.exit(1)
    
    # Validate phone number format
    if not validate_phone_number(args.phone_number):
        sys.exit(1)
    
    # Make the call
    success = make_call(args.phone_number)
    
    sys.exit(0 if success else 1)


if __name__ == '__main__':
    main()
