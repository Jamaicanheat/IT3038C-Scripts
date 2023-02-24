# Create a new instance of the SpeechSynthesizer class
Add-Type -AssemblyName System.speech
$speaker = New-Object System.Speech.Synthesis.SpeechSynthesizer

# Set the voice to use (optional)
$speaker.SelectVoice("Microsoft Zira Desktop")

# Set the volume and rate of speech (optional)
$speaker.Volume = 100
$speaker.Rate = 0

# Set the message to speak
$message = "Hello, world! This is a test message."

# Speak the message aloud
$speaker.Speak($message)
