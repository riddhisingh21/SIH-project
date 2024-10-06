document.getElementById("translate-text-btn").addEventListener("click", function() {
    const textInput = document.getElementById("text-input").value;
    if (textInput) {
        document.getElementById("isl-translation").innerText = `Translating: "${textInput}" into ISL...`;
    } else {
        alert("Please enter some text to translate.");
    }
});

document.getElementById("start-speech-btn").addEventListener("click", function() {
    if ('webkitSpeechRecognition' in window) {
        const recognition = new webkitSpeechRecognition();
        recognition.lang = 'en-IN';
        recognition.onstart = function() {
            document.getElementById("speech-status").innerText = "Listening...";
        };
        recognition.onresult = function(event) {
            const speechResult = event.results[0][0].transcript;
            document.getElementById("speech-status").innerText = `You said: "${speechResult}"`;
            document.getElementById("isl-translation").innerText = `Translating: "${speechResult}" into ISL...`;
        };
        recognition.onerror = function() {
            document.getElementById("speech-status").innerText = "Error recognizing speech. Please try again.";
        };
        recognition.start();
    } else {
        alert("Speech recognition is not supported in your browser. Please use Chrome.");
    }
});
