const fileInput = document.getElementById('file-input');
const selectAudioButton = document.getElementById('select-audio-button');
let filePath='music/M83.mp3';



const audio = new Audio(filePath);
const audio2=new Audio(filePath);
const audio3=new Audio(filePath);
const audio4=new Audio(filePath);
const audio5=new Audio('music/b.mp3')
const disc = document.querySelector('.disc');

function rotateDisc() {
  const currentTime = audio.currentTime;
  const rotationAngle = (currentTime * 360) / 5;
  disc.style.transform = rotate(${rotationAngle}deg;
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
        audio5.pause();
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


  document.addEventListener('keydown', function(event){
    if (event.key==='w')
    {
      volumeControl.value++;
      audio.volume = volumeControl.value / 100;
    }
  })
  document.addEventListener('keydown', function(event){
    if (event.key==='s')
    {
      volumeControl.value-=1;
      audio.volume = volumeControl.value / 100;
    }
  })
  document.addEventListener('keydown', function(event){
    if (event.key==='e')
    {
      speedControl.value++;
      const speed = parseFloat(speedControl.value);
  audio.playbackRate = speed;
    }
  })
  document.addEventListener('keydown', function(event){
    if (event.key==='d')
    {
      speedControl.value-=1;
      const speed = parseFloat(speedControl.value);
  audio.playbackRate = speed;
    }
  })

  document.addEventListener('keydown', function(event){
    if (event.key==='z')
    {
      // lOOp
      audio.currentTime -=1.5;
    }
  })
  document.addEventListener('keydown', function(event){
    if (event.key==='x')
    {
      //echo
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
  }})

  

  var g=0;
  const jiggle=document.getElementById('jiggle');
  document.addEventListener('keydown',function(event){
    if (event.key === 'v') {

      if(t%2===0){
        audio5.play();
        g++;
      }
      else{
        audio5.pause();
        g++;
      }
    }
    
  })