# Demo Video Script (3-5 minutes)

## Preparation Checklist
- [ ] Application running locally
- [ ] ngrok tunnel active
- [ ] Phone ready (speakerphone mode recommended)
- [ ] Screen recording software ready (OBS, Loom, or QuickTime)
- [ ] Browser window open at http://localhost:5000
- [ ] Code editor open with project files

---

## Scene 1: Introduction (30 seconds)

**[Screen: Show your face or project overview slide]**

> "Hello! I'm [Your Name], and today I'll be demonstrating my Plivo IVR demo system built for the InspireWorks technical assignment."

**[Screen: Show project folder structure]**

> "This is a multi-level Interactive Voice Response system built with Python, Flask, and Plivo's Voice API. It demonstrates outbound calling, language selection, and interactive menu navigation."

---

## Scene 2: Code Walkthrough (1-2 minutes)

**[Screen: Open app.py in code editor]**

> "Let me quickly walk you through the code structure."

**[Scroll to show imports and setup]**

> "We're using Flask as our web framework and the Plivo SDK for voice API integration."

**[Highlight the /answer endpoint]**

> "The entry point is the /answer endpoint, which presents our Level 1 menu for language selection—English or Spanish."

**[Highlight the /language-menu endpoint]**

> "Based on the user's selection, we route to the language-menu handler which captures their choice and presents Level 2 options."

**[Highlight the /action-menu endpoint]**

> "Finally, the action-menu handler either plays an audio message or connects the caller to a live associate, depending on their selection."

**[Show the templates/index.html]**

> "I've also created a simple web interface to trigger the outbound calls."

---

## Scene 3: Live Demonstration (2-3 minutes)

**[Screen: Browser showing the web interface]**

> "Now let's see it in action. I'm on the web interface at localhost:5000."

**[Type in your phone number]**

> "I'll enter my phone number in E.164 format—that's the international format starting with a plus sign."

**[Click the Initiate Call button]**

> "When I click 'Initiate Call,' the system uses Plivo's API to place an outbound call to my number."

**[Show success message on screen]**

> "And we can see the call was initiated successfully."

**[Answer the phone - use speakerphone so audio is captured]**

> "I'm answering the call now..."

**[Listen to the greeting]**

*System speaks: "Welcome to InspireWorks IVR demo. Para español, oprima dos. For English, press 1. For Spanish, press 2."*

> "The system greets me and asks for my language preference. I'll press 1 for English."

**[Press 1 on phone keypad]**

**[Listen to Level 2 menu]**

*System speaks: "You have selected English. Press 1 to play a short audio message. Press 2 to connect to a live associate."*

> "Perfect! Now I'm at Level 2. Let me first demonstrate the audio playback feature by pressing 1."

**[Press 1 on phone keypad]**

**[Listen to audio]**

*System plays audio message*

> "Great! The system played the audio message and is now thanking me and ending the call."

---

## Scene 4: Second Call - Demonstrating Transfer Feature (1 minute)

**[Screen: Back to web interface]**

> "Let me make another call to demonstrate the call transfer feature."

**[Initiate another call, answer it]**

> "This time, I'll select English again by pressing 1..."

**[Press 1]**

> "And now I'll press 2 to be connected to a live associate."

**[Press 2]**

*System speaks: "Connecting you to a live associate. Please hold."*

> "The system is now attempting to transfer me to the associate number configured in the environment variables."

**[Show the call being transferred]**

> "In a production environment, this would connect to a real support line."

---

## Scene 5: Error Handling Demo (30 seconds)

**[Optional: Make a third call]**

> "Let me quickly demonstrate the error handling. If I press an invalid option..."

**[Press 5 or 9]**

*System speaks: "Invalid selection. Please try again."*

> "The system gracefully handles invalid input and prompts me to try again, ensuring a robust user experience."

---

## Scene 6: Conclusion (30 seconds)

**[Screen: Show project structure or GitHub repo]**

> "To summarize, this IVR system successfully demonstrates:"
> "- Outbound call initiation through a web interface"
> "- Multi-level menu navigation with language support"
> "- DTMF input capture and validation"
> "- Audio playback and call forwarding"
> "- Graceful error handling"

**[Screen: Show README or documentation]**

> "The complete code, setup instructions, and documentation are available in the repository. Thank you for watching!"

---

## Recording Tips

1. **Audio Quality**
   - Use a good microphone
   - Record in a quiet environment
   - Speak clearly and at a moderate pace

2. **Video Quality**
   - Use 1080p resolution if possible
   - Ensure good lighting (if showing face)
   - Keep screen uncluttered

3. **Screen Recording Best Practices**
   - Close unnecessary applications
   - Hide desktop icons (if messy)
   - Use a clean browser window (close extra tabs)
   - Zoom in on important code sections

4. **Pacing**
   - Don't rush through explanations
   - Pause briefly between sections
   - Give viewers time to read code on screen

5. **Professional Touch**
   - Practice once before final recording
   - Add simple intro/outro cards (optional)
   - Consider adding background music at low volume (optional)
   - Edit out long pauses or mistakes

## Recommended Recording Tools

- **macOS**: QuickTime, ScreenFlow
- **Windows**: OBS Studio, Camtasia
- **Cross-platform**: Loom, OBS Studio
- **Browser-based**: Loom Chrome Extension

## After Recording

- [ ] Review the video
- [ ] Check audio quality
- [ ] Ensure all features were demonstrated
- [ ] Verify video length (3-5 minutes)
- [ ] Export in MP4 format
- [ ] Upload to YouTube (unlisted) or include with submission

---

Good luck with your recording! 🎥
