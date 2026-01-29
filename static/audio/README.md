# Audio Files Setup

This directory should contain your audio files for the IVR system.

## Required Files

1. **sample_english.mp3** - English audio message
2. **sample_spanish.mp3** - Spanish audio message

## Options for Audio Files

### Option 1: Use Text-to-Speech (Recommended for Testing)
The application already uses Plivo's built-in text-to-speech, so you don't need audio files to test the system.

### Option 2: Create Your Own Audio Files
You can create custom audio messages using:

1. **Online TTS Services**:
   - https://ttsmp3.com/
   - https://www.naturalreaders.com/online/
   - Google Cloud Text-to-Speech

2. **Record Your Own**:
   - Use your phone's voice recorder
   - Use Audacity (free audio editor)
   - Use GarageBand (Mac) or Voice Recorder (Windows)

3. **Professional TTS**:
   - Amazon Polly
   - Google Cloud TTS
   - Microsoft Azure TTS

### Option 3: Use Publicly Hosted Audio
Update the audio URLs in `app.py`:

```python
# Example with publicly hosted audio
ENGLISH_AUDIO = "https://your-domain.com/audio/english.mp3"
SPANISH_AUDIO = "https://your-domain.com/audio/spanish.mp3"
```

## Sample Audio Script

### English Message (sample_english.mp3)
> "Thank you for choosing InspireWorks. This is a demonstration of our IVR system. 
> We appreciate your interest in our voice API capabilities. Have a great day!"

**Duration**: ~10-15 seconds

### Spanish Message (sample_spanish.mp3)
> "Gracias por elegir InspireWorks. Esta es una demostración de nuestro sistema IVR.
> Apreciamos su interés en nuestras capacidades de API de voz. ¡Que tenga un buen día!"

**Duration**: ~10-15 seconds

## Audio File Requirements

- **Format**: MP3
- **Bitrate**: 128 kbps or higher
- **Sample Rate**: 44.1 kHz or 48 kHz
- **Channels**: Mono or Stereo
- **Duration**: 10-30 seconds (keep it concise)
- **File Size**: Under 1 MB

## Hosting Audio Files

If you don't want to serve audio from your Flask app:

1. **GitHub** (for small files):
   - Upload to your repo
   - Get the raw file URL

2. **AWS S3**:
   - Upload to a public bucket
   - Use the public URL

3. **Google Drive**:
   - Upload and set to "Anyone with link"
   - Use direct download link

4. **Cloudinary** (free tier available):
   - Upload audio files
   - Get public URL

## Testing Without Audio Files

The system will work fine without these files because:
1. Text-to-speech is used for all menu prompts
2. You can test the call flow logic
3. For demo purposes, TTS is sufficient

If you add the audio files later, just place them in this directory and restart the Flask application.

## Troubleshooting

**Issue**: Audio file not playing
- Check file format (must be MP3)
- Verify URL is publicly accessible
- Test URL in browser (should download/play)
- Check Plivo console for errors

**Issue**: Poor audio quality
- Use higher bitrate (192 kbps)
- Ensure no background noise
- Normalize audio levels

**Issue**: File too large
- Compress with Audacity or online tools
- Reduce bitrate to 96-128 kbps
- Trim silence at beginning/end
