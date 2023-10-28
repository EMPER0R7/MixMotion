const audio = new Audio('music/phiraur.mp3');
const disc = document.querySelector('.disc');

function rotateDisc() {
  const currentTime = audio.currentTime;
  const rotationAngle = (currentTime * 360) / 5;
  disc.style.transform = `rotate(${rotationAngle}deg)`;
}

let spacebarPressed = false;

document.addEventListener('keydown', function (event) {
  if (event.key === 'b' && !spacebarPressed) {
    audio.play();
    disc.style.animationPlayState = 'running';
    spacebarPressed = true;
  }
});

document.addEventListener('keydown', function (event) {
  if (event.key === 'n') {
    audio.pause();
    disc.style.animationPlayState = 'paused';
    spacebarPressed = false;
    rotateDisc();
  }
});

const volumeControl = document.getElementById('volume');
volumeControl.addEventListener('input', function () {
  audio.volume = volumeControl.value / 100;
});

const speedControl = document.getElementById('speed-control');
speedControl.addEventListener('input', function () {
  const speed = parseFloat(speedControl.value);
  audio.playbackRate = speed;
});



const seekBar = document.getElementById('seek-bar');
seekBar.addEventListener('input', function () {
    const seekTime = parseFloat(this.value);
    audio.currentTime = seekTime;
  });
  
  audio.addEventListener('timeupdate', function () {
    seekBar.value = audio.currentTime;
    seekBar.max = audio.duration;
  });