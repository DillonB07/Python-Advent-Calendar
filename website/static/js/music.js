var songs = Array(
  "/static/music/Away In A Manger - Audionautix.mp3",
  "/static/music/Carol Of The Bells - Audionautix.mp3",
  "/static/music/Canon and Variation - Twin Musicom.mp3",
  "/static/music/Deck the Halls - Kevin MacLeod.mp3",
  "/static/music/Deck the Halls B - Kevin MacLeod.mp3",
  "/static/music/Hark The Herald Angels Sing - Audionautix.mp3",
  "/static/music/Hip Hop Christmas - Twin Musicom.mp3",
  "/static/music/Jingle Bells - Kevin MacLeod.mp3",
  "/static/music/Jingle Bells 7 - Kevin MacLeod.mp3",
  "/static/music/Joy To The World - Audionautix.mp3",
  "/static/music/Noel - Audionautix.mp3",
  "/static/music/We Wish You a Merry Christmas - Twin Musicom.mp3",
  "/static/music/We Wish You A Merry Xmas - Audionautix.mp3"
);

function chooseRandomSong() {
  var randomSong = songs[Math.floor(Math.random() * songs.length)];
  document.getElementById("player").src = randomSong;
}

function playSong() {
  var audioPlayer = document.getElementById("player");
  if (audioPlayer.ended || audioPlayer.src == "") {
    chooseRandomSong();
    audioPlayer.play();
  } else {
    audioPlayer.play();
  }
}

function pauseSong() {
  var audioPlayer = document.getElementById("player");
  audioPlayer.pause();
}
