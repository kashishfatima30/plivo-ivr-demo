"""
Plivo IVR Demo Application - FIXED VERSION
Multi-level IVR system with language selection and call routing
"""

from flask import Flask, request, render_template, jsonify
import plivo
from plivo import plivoxml
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

# Plivo Configuration
PLIVO_AUTH_ID = os.getenv('PLIVO_AUTH_ID', 'MANZJJOGRLNZK0ZMZIMM')
PLIVO_AUTH_TOKEN = os.getenv('PLIVO_AUTH_TOKEN', 'NmU2ZmRhMjYtOTE1OS00YWRiLWJlNmEtNTIxYzUy')
PLIVO_PHONE_NUMBER = os.getenv('PLIVO_PHONE_NUMBER', '918031274121')
ASSOCIATE_NUMBER = os.getenv('ASSOCIATE_NUMBER', '918826389434')  

client = plivo.RestClient(auth_id=PLIVO_AUTH_ID, auth_token=PLIVO_AUTH_TOKEN)

BASE_URL = os.getenv('BASE_URL', 'http://localhost:5000')


@app.route('/')
def index():
    """Home page with call trigger form"""
    return render_template('index.html')


@app.route('/make-call', methods=['POST'])
def make_call():
    """Initiate outbound call"""
    try:
        data = request.get_json()
        to_number = data.get('phone_number')
        
        if not to_number:
            return jsonify({'error': 'Phone number is required'}), 400
        
        print(f"\n📞 Making call to: {to_number}")
        
        response = client.calls.create(
            from_=PLIVO_PHONE_NUMBER,
            to_=to_number,
            answer_url=f'{BASE_URL}/answer',
            answer_method='POST'
        )
        
        call_uuid = response.request_uuid if hasattr(response, 'request_uuid') else 'Unknown'
        print(f"✅ Call UUID: {call_uuid}\n")

        return jsonify({
            'success': True,
            'message': 'Call initiated successfully',
            'call_uuid': call_uuid
        })
    
    except Exception as e:
        print(f"❌ Error: {str(e)}")
        return jsonify({'error': str(e)}), 500


@app.route('/answer', methods=['POST'])
def answer_call():
    """Level 1: Language Selection"""
    print("\n" + "="*60)
    print("📞 CALL ANSWERED")
    print("="*60)
    
    response = plivoxml.ResponseElement()
    
    speak = plivoxml.SpeakElement(
        "Welcome to Inspire Works I V R demo. "
        "For English, press 1. "
        "Para español, oprima dos."
    )
    response.add(speak)
    
    get_digits = plivoxml.GetDigitsElement(
        action=f'{BASE_URL}/language-menu',
        method='POST',
        timeout=5,
        num_digits=1,
        retries=1
    )
    response.add(get_digits)
    
    speak_retry = plivoxml.SpeakElement("We did not receive your input.")
    response.add(speak_retry)
    
    redirect = plivoxml.RedirectElement(f'{BASE_URL}/answer')
    response.add(redirect)
    
    # CRITICAL FIX: Convert to string properly
    xml_output = response.to_string()
    print(f"XML Output:\n{xml_output}")
    print("="*60 + "\n")
    
    return xml_output, 200, {'Content-Type': 'text/xml; charset=utf-8'}


@app.route('/language-menu', methods=['POST'])
def language_menu():
    """Level 2: Action Menu"""
    digit = request.form.get('Digits', '')
    print(f"\n🔢 Language Menu - Digit: {digit}")
    print(f"Full request data: {dict(request.form)}")
    
    response = plivoxml.ResponseElement()
    
    if digit == '1':
        language = 'english'
        menu_text = (
            "You have selected English. "
            "Press 1 to play a short audio message. "
            "Press 2 to connect to a live associate."
        )
    elif digit == '2':
        language = 'spanish'
        menu_text = (
            "Has seleccionado español. "
            "Presiona 1 para reproducir un mensaje de audio. "
            "Presiona 2 para conectarte con un asociado en vivo."
        )
    else:
        speak = plivoxml.SpeakElement("Invalid selection. Please try again.")
        response.add(speak)
        redirect = plivoxml.RedirectElement(f'{BASE_URL}/answer')
        response.add(redirect)
        
        xml_output = response.to_string()
        print(f"XML: {xml_output}\n")
        return xml_output, 200, {'Content-Type': 'text/xml; charset=utf-8'}
    
    speak = plivoxml.SpeakElement(menu_text)
    response.add(speak)
    
    get_digits = plivoxml.GetDigitsElement(
        action=f'{BASE_URL}/action-menu?language={language}',
        method='POST',
        timeout=10,
        num_digits=1,
        retries=2,
        redirect=True
    )
    response.add(get_digits)
    
    xml_output = response.to_string()
    print(f"XML: {xml_output}\n")
    return xml_output, 200, {'Content-Type': 'text/xml; charset=utf-8'}


@app.route('/action-menu', methods=['POST'])
def action_menu():
    """Handle Play Audio or Connect to Associate"""
    digit = request.form.get('Digits', '')
    language = request.args.get('language', 'english')
    
    print(f"\n🎬 Action Menu - Digit: '{digit}', Language: {language}")
    print(f"Full request data: {dict(request.form)}")
    print(f"Query params: {dict(request.args)}")
    
    response = plivoxml.ResponseElement()
    
    if digit == '1':
        print("✅ Option 1 selected - Playing audio message")
        # Play audio message (TTS)
        if language == 'english':
            speak1 = plivoxml.SpeakElement("Playing your audio message now.")
            response.add(speak1)
            
            speak2 = plivoxml.SpeakElement(
                "This is a sample audio message from Inspire Works. "
                "Thank you for testing our I V R system. "
                "We appreciate your interest in our voice technology solutions."
            )
            response.add(speak2)
            
            speak3 = plivoxml.SpeakElement(
                "Thank you for using Inspire Works I V R demo. Goodbye."
            )
            response.add(speak3)
        else:
            speak1 = plivoxml.SpeakElement("Reproduciendo tu mensaje de audio ahora.")
            response.add(speak1)
            
            speak2 = plivoxml.SpeakElement(
                "Este es un mensaje de audio de muestra de Inspire Works. "
                "Gracias por probar nuestro sistema I V R. "
                "Apreciamos su interés en nuestras soluciones de tecnología de voz."
            )
            response.add(speak2)
            
            speak3 = plivoxml.SpeakElement(
                "Gracias por usar la demostración de I V R de Inspire Works. Adiós."
            )
            response.add(speak3)
        
        hangup = plivoxml.HangupElement()
        response.add(hangup)
        
    elif digit == '2':
        print(f"✅ Option 2 selected - Connecting to associate: {ASSOCIATE_NUMBER}")
        # Connect to associate
        if language == 'english':
            speak = plivoxml.SpeakElement(
                "Connecting you to a live associate. Please hold."
            )
        else:
            speak = plivoxml.SpeakElement(
                "Conectándote con un asociado en vivo. Por favor espera."
            )
        response.add(speak)
        
        dial = plivoxml.DialElement()
        dial.add_number(ASSOCIATE_NUMBER)
        response.add(dial)
        
        if language == 'english':
            speak_end = plivoxml.SpeakElement("Thank you for calling. Goodbye.")
        else:
            speak_end = plivoxml.SpeakElement("Gracias por llamar. Adiós.")
        response.add(speak_end)
        
    else:
        print(f"❌ Invalid digit received: '{digit}'")
        # Invalid input
        if language == 'english':
            speak = plivoxml.SpeakElement("Invalid selection. Returning to main menu.")
        else:
            speak = plivoxml.SpeakElement("Selección inválida. Regresando al menú principal.")
        response.add(speak)
        
        redirect = plivoxml.RedirectElement(f'{BASE_URL}/language-menu')
        response.add(redirect)
    
    xml_output = response.to_string()
    print(f"XML: {xml_output}\n")
    return xml_output, 200, {'Content-Type': 'text/xml; charset=utf-8'}


@app.route('/health', methods=['GET'])
def health_check():
    """Health check"""
    return jsonify({
        'status': 'healthy',
        'service': 'Plivo IVR Demo'
    })


if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    print("\n" + "="*70)
    print("🚀 PLIVO IVR DEMO")
    print("="*70)
    print(f"Port: {port}")
    print(f"Base URL: {BASE_URL}")
    print(f"Phone: +{PLIVO_PHONE_NUMBER}")
    print("="*70 + "\n")
    app.run(host='0.0.0.0', port=port, debug=True)