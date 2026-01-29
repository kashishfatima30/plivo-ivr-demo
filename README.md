# Plivo IVR Demo System

A multi-level Interactive Voice Response (IVR) system built with Plivo's Voice API, demonstrating outbound calling and branching menu logic.

## 🎯 Features

- **Outbound Call Initiation**: Trigger calls programmatically via web interface
- **Multi-Level IVR Menu**:
  - **Level 1**: Language Selection (English/Spanish)
  - **Level 2**: Action Selection (Play Audio/Connect to Associate)
- **DTMF Input Handling**: Robust digit capture and validation
- **Error Handling**: Graceful handling of invalid inputs with menu repetition
- **Web Interface**: Simple UI to trigger calls

## 📋 Prerequisites

- Python 3.8 or higher
- Plivo account (sign up at https://console.plivo.com/)
- A phone number rented from Plivo
- ngrok (for local development) or a publicly accessible server

## 🚀 Quick Start

### 1. Clone or Download the Repository

```bash
# If you have git
git clone <your-repo-url>
cd ivr-demo

# Or extract the zip file and navigate to the directory
```

### 2. Install Dependencies

```bash
# Create a virtual environment (recommended)
python -m venv venv

# Activate the virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Install required packages
pip install -r requirements.txt
```

### 3. Set Up Plivo Account

1. **Create a Plivo Account**
   - Go to https://console.plivo.com/
   - Sign up for a free trial account

2. **Get Your Credentials**
   - Navigate to Dashboard
   - Copy your **Auth ID** and **Auth Token**

3. **Rent a Phone Number**
   - Go to Phone Numbers → Buy Numbers
   - Purchase a phone number (trial accounts get free credits)
   - Note down the number in E.164 format (e.g., +12025551234)

### 4. Configure Environment Variables

```bash
# Copy the example environment file
cp .env.example .env

# Edit the .env file with your credentials
# Use any text editor:
nano .env
# or
vim .env
# or open in your IDE
```

Update the following values in `.env`:

```env
PLIVO_AUTH_ID=your_actual_auth_id
PLIVO_AUTH_TOKEN=your_actual_auth_token
PLIVO_PHONE_NUMBER=+1234567890  # Your Plivo number
ASSOCIATE_NUMBER=+1987654321    # Test number for call forwarding
BASE_URL=http://your-ngrok-url.ngrok.io  # Update after setting up ngrok
```

### 5. Set Up ngrok (For Local Development)

Plivo needs a public URL to send webhooks. ngrok creates a tunnel to your localhost.

```bash
# Download and install ngrok from https://ngrok.com/download

# Start ngrok tunnel
ngrok http 5000

# You'll see output like:
# Forwarding  https://abc123.ngrok.io -> http://localhost:5000
```

**Copy the ngrok URL** (e.g., `https://abc123.ngrok.io`) and update it in your `.env` file:

```env
BASE_URL=https://abc123.ngrok.io
```

### 6. Add Audio Files (Optional)

The system can use Plivo's text-to-speech or play custom audio files.

If you want to use custom audio:

```bash
# Create the audio directory
mkdir -p static/audio

# Add your MP3 files
# Place sample_english.mp3 and sample_spanish.mp3 in static/audio/
```

Or use publicly hosted audio URLs by updating the `ENGLISH_AUDIO` and `SPANISH_AUDIO` variables in `app.py`.

### 7. Run the Application

```bash
# Make sure your virtual environment is activated
# Make sure ngrok is running in another terminal

# Start the Flask application
python app.py
```

You should see:
```
 * Running on http://0.0.0.0:5000
```

### 8. Test the IVR System

1. **Open your browser** and go to `http://localhost:5000`
2. **Enter a phone number** in E.164 format (e.g., +12025551234)
3. **Click "Initiate Call"**
4. **Answer the call** on your phone
5. **Follow the IVR prompts**:
   - Press 1 for English or 2 for Spanish
   - Press 1 to play audio or 2 to connect to associate

## 📞 IVR Flow Diagram

```
┌─────────────────────────────────────┐
│     Outbound Call Initiated         │
└──────────────┬──────────────────────┘
               │
               ▼
┌─────────────────────────────────────┐
│  Level 1: Language Selection        │
│  "Press 1 for English"              │
│  "Press 2 for Spanish"              │
└──────────────┬──────────────────────┘
               │
       ┌───────┴───────┐
       │               │
       ▼               ▼
   English         Spanish
       │               │
       └───────┬───────┘
               │
               ▼
┌─────────────────────────────────────┐
│  Level 2: Action Selection          │
│  "Press 1 for Audio Message"        │
│  "Press 2 for Live Associate"       │
└──────────────┬──────────────────────┘
               │
       ┌───────┴───────┐
       │               │
       ▼               ▼
  Play Audio    Connect to Agent
       │               │
       ▼               ▼
   Hangup          Transfer Call
```

## 🧪 Testing Checklist

- [ ] Call initiates successfully from web interface
- [ ] Level 1 menu plays correctly
- [ ] English selection (press 1) works
- [ ] Spanish selection (press 2) works
- [ ] Level 2 menu plays in correct language
- [ ] Audio playback (press 1) works
- [ ] Call forwarding (press 2) works
- [ ] Invalid input handling works (press 5, 9, etc.)
- [ ] No input timeout works (don't press anything)
- [ ] Call completes gracefully

## 🏗️ Project Structure

```
ivr-demo/
│
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── .env.example          # Environment variables template
├── .env                  # Your actual credentials (not in git)
├── .gitignore            # Files to exclude from git
├── README.md             # This file
│
├── templates/
│   └── index.html        # Web UI for call triggering
│
├── static/
│   └── audio/
│       ├── sample_english.mp3  # English audio file (optional)
│       └── sample_spanish.mp3  # Spanish audio file (optional)
│
└── venv/                 # Virtual environment (not in git)
```

## 🔧 Troubleshooting

### Issue: Call not connecting

**Solution:**
- Verify your Plivo credentials in `.env`
- Check that your Plivo phone number is in E.164 format
- Ensure ngrok is running and BASE_URL is updated
- Check Plivo console for error logs

### Issue: Webhooks not working

**Solution:**
- Confirm ngrok URL is correct in `.env`
- Restart the Flask app after updating `.env`
- Check ngrok dashboard (http://localhost:4040) for webhook requests
- Ensure Flask app is running when call is made

### Issue: Audio not playing

**Solution:**
- Verify audio files are in `static/audio/` directory
- Check audio file URLs are publicly accessible
- Use Plivo's text-to-speech as fallback (already implemented)

### Issue: Invalid phone number error

**Solution:**
- Use E.164 format: +[country code][number]
- Example: +12025551234 (not 202-555-1234)
- Include country code (1 for US/Canada)

## 🎥 Demo Video Script

When recording your demo video (3-5 minutes), cover these points:

1. **Introduction (30 seconds)**
   - Brief overview of the project
   - Technologies used (Python, Flask, Plivo)

2. **Code Walkthrough (1-2 minutes)**
   - Show project structure
   - Explain main components in app.py
   - Highlight key endpoints

3. **Live Demo (2-3 minutes)**
   - Open web interface
   - Enter phone number and initiate call
   - Answer the phone (use speakerphone)
   - Navigate Level 1 menu (select language)
   - Navigate Level 2 menu (select action)
   - Demonstrate audio playback
   - Demonstrate call forwarding
   - Show error handling (invalid input)

4. **Conclusion (30 seconds)**
   - Recap features demonstrated
   - Mention potential improvements

## 🚀 Deployment Options

### Option 1: Heroku

```bash
# Install Heroku CLI
# Login to Heroku
heroku login

# Create a new app
heroku create your-app-name

# Set environment variables
heroku config:set PLIVO_AUTH_ID=your_auth_id
heroku config:set PLIVO_AUTH_TOKEN=your_auth_token
heroku config:set PLIVO_PHONE_NUMBER=your_number
heroku config:set ASSOCIATE_NUMBER=your_associate_number

# Deploy
git push heroku main

# Get your app URL
heroku info
# Update BASE_URL with your Heroku URL
```

### Option 2: Railway

1. Go to https://railway.app/
2. Connect your GitHub repository
3. Add environment variables in Railway dashboard
4. Railway will auto-deploy
5. Get your deployment URL and update BASE_URL

### Option 3: Render

1. Go to https://render.com/
2. Create a new Web Service
3. Connect your repository
4. Add environment variables
5. Deploy

## 📚 API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/` | GET | Web UI for call initiation |
| `/make-call` | POST | Trigger outbound call |
| `/answer` | POST | Initial call answer webhook |
| `/language-menu` | POST | Level 1 menu handler |
| `/action-menu` | POST | Level 2 menu handler |
| `/invalid-input` | GET/POST | Invalid input handler |
| `/health` | GET | Health check endpoint |

## 🤝 Support

For Plivo-specific issues:
- Documentation: https://www.plivo.com/docs/
- Support: https://support.plivo.com/

For project issues:
- Review the troubleshooting section
- Check Plivo console logs
- Verify environment variables

## 📝 License

This project is for educational purposes as part of a technical assignment.

## ✨ Features to Add (Optional Enhancements)

- Call recording functionality
- Voicemail capability
- Multi-language support (add more languages)
- Call analytics and logging
- Database integration for call history
- SMS notifications
- Interactive call queuing
- Custom hold music

---

**Built with ❤️ for InspireWorks Technical Assignment**
