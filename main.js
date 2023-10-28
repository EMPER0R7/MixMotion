const audio = new Audio('music/phiraur.mp3');
const disc  = document.querySelector('.disc');

function rotateDisc() {
    const Time = audio.currentTime;
    let rotationAngle = Time*360/5; 
    disc.style.transform = `rotate(${rotationAngle}deg)`; 
}
let spacebarPressed = false;
document.addEventListener('keydown', function(event){
    if(event.key === 'b'&& !spacebarPressed)
    {
        audio.play();
        disc.style.animationPlayState = 'running';
        spacebarPressed = true;
    }

})

document.addEventListener('keydown',function(event){
    if(event.key === 'n')
    {
        audio.pause();
        disc.style.animationPlayState = 'paused';
        spacebarPressed = false;
        rotateDisc();
    }
})


const volumeControl = document.getElementById("volume");
volumeControl.addEventListener("input", function () {
    audio.volume = volumeControl.value/100;
});

const speedControl = document.getElementById('speed-control');
speedControl.addEventListener('input', function(){
    const speed = parseFloat(speedControl.value);
    audio.playbackRate = speed;
});

const bassSlider=document.getElementById('bass');

const audioContext = new window.AudioContext();

const bassFilter=audioContext.createBiquadFilter();
bassFilter.type="lowshelf";
bassFilter.frequency.value = 60;
bassFilter.gain.value =0;
bassFilter.connect(audioContext.destination);
const oscillator=audioContext.createOscillator();
oscillator.connect(bassFilter);
// oscillator.start();

bassSlider.addEventListener("input",function(){
    // const bassL = parseFloat(this.value);
    bassFilter.gain.value = (bassSlider.value-50)/10;
})


const pitchSlider = document.getElementById("pitch");

// const source = audioContext.createMediaElementSource(audio);



// const gainNode = audioContext.createGain();
// source.connect(gainNode);
// gainNode.connect(audioContext.destination);

// source.connect(audioContext.destination);



pitchSlider.addEventListener("input", function(){
    audio.mozPreservesPitch = false;
    audio.playbackRate = pitchSlider.value;
    
});

// Start audio playback