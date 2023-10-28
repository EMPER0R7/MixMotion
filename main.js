const audio = new Audio('music/M83.mp3');
const audio2=new Audio('music/M83.mp3');
const audio3=new Audio('music/M83.mp3');
const audio4=new Audio('music/M83.mp3');
const disc = document.querySelector('.disc');

function rotateDisc() {
  const currentTime = audio.currentTime;
  const rotationAngle = (currentTime * 360) / 5;
  disc.style.transform = `rotate(${rotationAngle}deg`;
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
    audio2.pause();
        audio3.pause();
        audio4.pause();
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

  const lOOp = document.getElementById('loop');
  lOOp.addEventListener('click', function(){

        audio.currentTime -=1.5;

  })

  const echo = document.getElementById('echo');
  var t=0;
  echo.addEventListener('click',function(){
    if(t%2===0)
    {
        audio2.currentTime=audio.currentTime-0.1;
        audio3.currentTime=audio.currentTime-0.2;
        audio4.currentTime=audio.currentTime-0.3;
        audio2.play();
        audio3.play();
        audio4.play();
        audio2.volume=audio.volume-0.3;
        audio3.volume=audio.volume-0.6;
        audio4.volume=audio.volume-0.9;
        t++;
    }
    else{
        audio2.pause();
        audio3.pause();
        audio4.pause();
        t++;
    }
  })