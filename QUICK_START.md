# 🚀 QUICK START GUIDE

Get your Plivo IVR Demo running in 10 minutes!

---

## ⚡ Speed Run (For the Impatient)

```bash
# 1. Extract files
unzip ivr-demo.zip
cd ivr-demo

# 2. Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Set up environment variables
cp .env.example .env
nano .env  # Add your Plivo credentials

# 5. Start ngrok (in another terminal)
ngrok http 5000

# 6. Update BASE_URL in .env with ngrok URL

# 7. Run the app
python app.py

# 8. Open browser to http://localhost:5000
# 9. Make a test call!
```

---

## 📝 Step-by-Step (Beginner Friendly)

### Step 1: Get Plivo Credentials (5 minutes)

1. Go to https://console.plivo.com/
2. Sign up for free trial account
3. Navigate to Dashboard
4. Copy your **Auth ID** and **Auth Token**
5. Go to Phone Numbers → Buy Number
6. Purchase a phone number (you get free credits)

### Step 2: Set Up Project (2 minutes)

```bash
# Navigate to project directory
cd ivr-demo

# Create virtual environment
python -m venv venv

# Activate it
# macOS/Linux:
source venv/bin/activate
# Windows:
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### Step 3: Configure Environment (2 minutes)

```bash
# Copy template
cp .env.example .env

# Edit with your favorite editor
nano .env
# or
code .env
# or
vim .env
```

Add your credentials:
```env
PLIVO_AUTH_ID=your_actual_auth_id_here
PLIVO_AUTH_TOKEN=your_actual_auth_token_here
PLIVO_PHONE_NUMBER=+12025551234
ASSOCIATE_NUMBER=+19876543210
BASE_URL=http://localhost:5000  # Will update in next step
PORT=5000
```

### Step 4: Set Up ngrok (1 minute)

```bash
# Download from https://ngrok.com/download
# Or install via package manager:
# macOS: brew install ngrok
# Windows: choco install ngrok

# Start ngrok in a NEW terminal window
ngrok http 5000

# You'll see something like:
# Forwarding https://abc123.ngrok.io -> http://localhost:5000

# Copy that URL (https://abc123.ngrok.io)
```

**Update .env:**
```env
BASE_URL=https://abc123.ngrok.io  # Your ngrok URL
```

### Step 5: Run the Application (30 seconds)

```bash
# Make sure you're in the project directory
# and virtual environment is activated

python app.py

# You should see:
# * Running on http://0.0.0.0:5000
```

### Step 6: Make Your First Call! (30 seconds)

1. Open browser: http://localhost:5000
2. Enter your phone number (with country code): `+12025551234`
3. Click "Initiate Call"
4. Answer your phone
5. Follow the prompts!

---

## 🎯 Testing the IVR

When you answer the call:

**Level 1: Language Selection**
- Press `1` for English
- Press `2` for Spanish

**Level 2: Action Selection**
- Press `1` to play audio message
- Press `2` to connect to associate

---

## 🔧 Troubleshooting Quick Fixes

### Problem: "Call initiated" but phone doesn't ring

**Solution:**
- Check Plivo console for errors
- Verify phone number format: `+[country code][number]`
- For trial accounts, verify the destination number in Plivo console

### Problem: Call connects but silent

**Solution:**
- Make sure ngrok is running
- Verify BASE_URL in .env matches ngrok URL exactly
- Restart Flask app after changing .env

### Problem: Module not found

**Solution:**
```bash
# Make sure virtual environment is activated
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate     # Windows

# Reinstall dependencies
pip install -r requirements.txt
```

---

## 📹 Recording Your Demo Video

Once everything works:

1. **Read DEMO_SCRIPT.md** for full guide
2. **Use screen recording software:**
   - macOS: QuickTime
   - Windows: OBS Studio
   - Any OS: Loom (easiest)
3. **Follow this outline:**
   - Intro (30s): Explain the project
   - Code walkthrough (1-2 min): Show key files
   - Live demo (2-3 min): Make call, navigate menus
   - Conclusion (30s): Recap features
4. **Export as MP4** and upload

---

## 📤 Submitting Your Assignment

### Option 1: GitHub Repository (Recommended)

```bash
# Initialize git
git init
git add .
git commit -m "Initial commit: Plivo IVR Demo"

# Create repo on GitHub, then:
git remote add origin https://github.com/yourusername/ivr-demo.git
git push -u origin main
```

**Include in submission:**
- GitHub repository URL
- Demo video (upload to YouTube/Loom)
- Brief setup instructions

### Option 2: ZIP File

```bash
# Create a clean zip (exclude venv and .env)
zip -r ivr-demo-submission.zip . -x "venv/*" ".env" "__pycache__/*" "*.pyc"
```

**Include:**
- ZIP file with code
- Demo video
- README.md for setup

---

## ✅ Pre-Submission Checklist

- [ ] Code runs without errors
- [ ] All test cases pass (see TESTING_GUIDE.md)
- [ ] Demo video recorded (3-5 minutes)
- [ ] README.md updated with any custom notes
- [ ] No credentials in code (using .env)
- [ ] .gitignore properly configured
- [ ] Requirements.txt includes all dependencies
- [ ] Both web UI and CLI work
- [ ] All menu levels tested
- [ ] Documentation is clear

---

## 🆘 Need Help?

Check these files in order:
1. **README.md** - General setup and usage
2. **TESTING_GUIDE.md** - Test each feature
3. **DEPLOYMENT_GUIDE.md** - If deploying to production
4. **DEMO_SCRIPT.md** - For video recording

---

## 🎉 You're Ready!

Your Plivo IVR Demo demonstrates:
✅ Outbound calling capability
✅ Multi-level IVR navigation
✅ Language selection (English/Spanish)
✅ Audio playback
✅ Call forwarding
✅ Error handling
✅ Professional code structure
✅ Comprehensive documentation

**Good luck with your assignment!** 🚀

---

**Estimated Total Setup Time: 10 minutes**
**Estimated Testing Time: 5 minutes**
**Estimated Demo Recording: 15 minutes**
**Total: 30 minutes to complete assignment**
