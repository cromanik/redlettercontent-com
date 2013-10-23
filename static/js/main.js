/* check device orientation */
function checkOrientation() {
  var viewport = document.querySelector("meta[name=viewport]");
  if (viewport == null) {
    return;
  }

  if (window.orientation === 90 || window.orientation === -90) {
    return viewport.setAttribute("content", "width:device-width, initial-scale=1.0, user-scalable=1");
  } else {
    return viewport.setAttribute("content", "width:device-width, initial-scale=0.6, user-scalable=1");
  }
};

window.onorientationchange = function() {
  return checkOrientation();
};

checkOrientation();