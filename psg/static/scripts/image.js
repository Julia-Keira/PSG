function openFullScreen(element) {
  document.getElementById("fullscreen-img").src = element.src;
  if(document.getElementById("fullscreen-image").className != "fullscreen-image fullscreen-image-visible"){
    document.getElementById("overlay").className += " fullscreen-image-visible";
    document.getElementById("fullscreen-image").className += " fullscreen-image-visible";
  }
}

function closeFullScreen() {
  document.getElementById("overlay").className = "overlay";
  document.getElementById("fullscreen-image").className = "fullscreen-image";
}