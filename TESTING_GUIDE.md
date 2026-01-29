# Testing Guide

## Pre-Testing Setup

### 1. Environment Verification
- [ ] All environment variables set in `.env`
- [ ] Virtual environment activated
- [ ] All dependencies installed (`pip install -r requirements.txt`)
- [ ] ngrok running and URL updated in `.env`
- [ ] Flask application running (`python app.py`)

### 2. Plivo Account Verification
- [ ] Plivo account created and verified
- [ ] Phone number rented/purchased
- [ ] Sufficient credits available
- [ ] Auth credentials correct

---

## Test Cases

### Test 1: Application Health Check
**Objective**: Verify the application is running correctly

**Steps**:
1. Open browser to `http://localhost:5000`
2. Verify web interface loads
3. Check `http://localhost:5000/health`

**Expected Result**:
- Web interface displays correctly
- Health endpoint returns: `{"status": "healthy", "service": "Plivo IVR Demo"}`

**Status**: ⬜ Pass / ⬜ Fail

---

### Test 2: Outbound Call Initiation
**Objective**: Test basic outbound calling functionality

**Steps**:
1. Navigate to `http://localhost:5000`
2. Enter valid phone number in E.164 format (e.g., +12025551234)
3. Click "Initiate Call" button
4. Observe status message

**Expected Result**:
- Success message appears
- Call UUID displayed
- Phone rings within 5-10 seconds

**Status**: ⬜ Pass / ⬜ Fail

**Notes**: _____________________

---

### Test 3: Level 1 Menu - English Selection
**Objective**: Test English language selection

**Steps**:
1. Initiate call to your phone
2. Answer the call
3. Listen to greeting message
4. Press `1` for English

**Expected Result**:
- Greeting plays in both English and Spanish
- After pressing 1, confirmation: "You have selected English"
- Level 2 menu plays in English

**Status**: ⬜ Pass / ⬜ Fail

**Notes**: _____________________

---

### Test 4: Level 1 Menu - Spanish Selection
**Objective**: Test Spanish language selection

**Steps**:
1. Initiate call to your phone
2. Answer the call
3. Listen to greeting message
4. Press `2` for Spanish

**Expected Result**:
- Greeting plays in both languages
- After pressing 2, confirmation: "Has seleccionado español"
- Level 2 menu plays in Spanish

**Status**: ⬜ Pass / ⬜ Fail

**Notes**: _____________________

---

### Test 5: Audio Playback (English)
**Objective**: Test audio message playback in English

**Steps**:
1. Initiate call
2. Press `1` for English
3. Press `1` for audio message

**Expected Result**:
- Announcement: "Playing your audio message now"
- Audio file plays successfully
- Thank you message plays
- Call ends gracefully

**Status**: ⬜ Pass / ⬜ Fail

**Notes**: _____________________

---

### Test 6: Audio Playback (Spanish)
**Objective**: Test audio message playback in Spanish

**Steps**:
1. Initiate call
2. Press `2` for Spanish
3. Press `1` for audio message

**Expected Result**:
- Announcement: "Reproduciendo tu mensaje de audio ahora"
- Audio file plays successfully
- Thank you message in Spanish
- Call ends gracefully

**Status**: ⬜ Pass / ⬜ Fail

**Notes**: _____________________

---

### Test 7: Call Transfer to Associate (English)
**Objective**: Test call forwarding functionality in English

**Steps**:
1. Initiate call
2. Press `1` for English
3. Press `2` to connect to associate

**Expected Result**:
- Announcement: "Connecting you to a live associate. Please hold."
- Call attempts to dial the associate number
- If answered, call connects successfully
- If not answered, goodbye message plays

**Status**: ⬜ Pass / ⬜ Fail

**Notes**: _____________________

---

### Test 8: Call Transfer to Associate (Spanish)
**Objective**: Test call forwarding functionality in Spanish

**Steps**:
1. Initiate call
2. Press `2` for Spanish
3. Press `2` to connect to associate

**Expected Result**:
- Announcement: "Conectándote con un asociado en vivo. Por favor espera."
- Call attempts to dial the associate number
- Spanish thank you message after call

**Status**: ⬜ Pass / ⬜ Fail

**Notes**: _____________________

---

### Test 9: Invalid Input - Level 1
**Objective**: Test error handling for invalid input at language selection

**Steps**:
1. Initiate call
2. Press `5` or `9` (invalid option)

**Expected Result**:
- System says: "Invalid selection. Please try again."
- Returns to language selection menu
- Menu repeats

**Status**: ⬜ Pass / ⬜ Fail

**Notes**: _____________________

---

### Test 10: Invalid Input - Level 2
**Objective**: Test error handling for invalid input at action selection

**Steps**:
1. Initiate call
2. Select language (press 1 or 2)
3. Press `7` or `9` (invalid option)

**Expected Result**:
- System says: "Invalid selection. Returning to main menu."
- Returns to language selection
- Can navigate through menus again

**Status**: ⬜ Pass / ⬜ Fail

**Notes**: _____________________

---

### Test 11: No Input Timeout - Level 1
**Objective**: Test behavior when user doesn't press any key

**Steps**:
1. Initiate call
2. Wait without pressing any key for ~10 seconds

**Expected Result**:
- System waits for input
- After timeout, repeats the menu or redirects
- Provides 2 retry attempts

**Status**: ⬜ Pass / ⬜ Fail

**Notes**: _____________________

---

### Test 12: No Input Timeout - Level 2
**Objective**: Test timeout handling at action selection

**Steps**:
1. Initiate call
2. Select language (press 1)
3. Wait without pressing any key

**Expected Result**:
- System waits for input
- After timeout, repeats Level 2 menu
- Eventually redirects or ends call

**Status**: ⬜ Pass / ⬜ Fail

**Notes**: _____________________

---

### Test 13: Phone Number Validation
**Objective**: Test input validation on web interface

**Steps**:
1. Try entering invalid phone numbers:
   - `1234567890` (missing +)
   - `+1` (too short)
   - `abc123` (letters)
   - Empty field

**Expected Result**:
- Error message for each invalid format
- Call not initiated
- User prompted to use E.164 format

**Status**: ⬜ Pass / ⬜ Fail

**Notes**: _____________________

---

### Test 14: Webhook Connectivity
**Objective**: Verify webhooks are receiving requests from Plivo

**Steps**:
1. Open ngrok dashboard at `http://localhost:4040`
2. Initiate a call
3. Monitor incoming webhook requests

**Expected Result**:
- Requests visible in ngrok dashboard
- `/answer` endpoint receives POST request
- Subsequent endpoints (`/language-menu`, `/action-menu`) receive requests
- All return 200 status codes

**Status**: ⬜ Pass / ⬜ Fail

**Notes**: _____________________

---

### Test 15: Concurrent Calls
**Objective**: Test system behavior with multiple simultaneous calls

**Steps**:
1. Initiate call to Phone A
2. Immediately initiate call to Phone B
3. Answer and navigate both calls

**Expected Result**:
- Both calls connect successfully
- Each call maintains independent state
- No interference between calls
- Both complete successfully

**Status**: ⬜ Pass / ⬜ Fail

**Notes**: _____________________

---

### Test 16: Call Logs and Debugging
**Objective**: Verify logging and debugging capabilities

**Steps**:
1. Check Flask console output
2. Initiate a call
3. Observe log messages

**Expected Result**:
- Clear log messages for each request
- Webhook requests logged
- No error messages in console
- Easy to trace call flow

**Status**: ⬜ Pass / ⬜ Fail

**Notes**: _____________________

---

## Edge Case Testing

### Edge Case 1: Rapid Key Presses
**Test**: Press multiple keys quickly in succession

**Expected**: System handles first valid input, ignores extras

**Status**: ⬜ Pass / ⬜ Fail

---

### Edge Case 2: International Numbers
**Test**: Call international number (e.g., +44...)

**Expected**: Call connects if Plivo supports the country

**Status**: ⬜ Pass / ⬜ Fail

---

### Edge Case 3: Network Interruption
**Test**: Disconnect internet during call

**Expected**: Call continues (handled by Plivo), graceful error handling

**Status**: ⬜ Pass / ⬜ Fail

---

## Performance Testing

### Performance Test 1: Response Time
- [ ] Webhook responds within 1 second
- [ ] Menu prompts play immediately
- [ ] No noticeable delays

### Performance Test 2: Audio Quality
- [ ] Voice prompts are clear
- [ ] No audio distortion
- [ ] Appropriate volume level

### Performance Test 3: Call Quality
- [ ] No dropped calls
- [ ] Consistent audio throughout
- [ ] Smooth transitions between menus

---

## Browser Compatibility (Web UI)

- [ ] Chrome
- [ ] Firefox
- [ ] Safari
- [ ] Edge

---

## Mobile Testing

- [ ] Test receiving calls on iOS
- [ ] Test receiving calls on Android
- [ ] DTMF tones work on both platforms

---

## Test Summary

| Category | Total Tests | Passed | Failed | Skipped |
|----------|-------------|--------|--------|---------|
| Core Functionality | 8 | | | |
| Error Handling | 4 | | | |
| Validation | 1 | | | |
| Integration | 2 | | | |
| Edge Cases | 3 | | | |
| Performance | 3 | | | |
| **TOTAL** | **21** | **___** | **___** | **___** |

---

## Issues Found

| Test # | Issue Description | Severity | Status |
|--------|------------------|----------|--------|
| | | | |
| | | | |

---

## Notes and Observations

_Use this space for any additional observations during testing:_

---

## Sign-off

**Tested by**: _____________________

**Date**: _____________________

**Overall Assessment**: ⬜ Ready for Demo / ⬜ Needs Fixes

**Comments**: 
_______________________________________________________
_______________________________________________________
_______________________________________________________
