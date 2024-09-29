const output = document.getElementById("output")
const startButton = document.getElementById("startButton")

let finalTranscript = "";

const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;

const recognition = new SpeechRecognition();
recognition.lang = 'en-US'
recognition.interimResults = true;

startButton.addEventListener('result', (e) =>{
    
}
)
