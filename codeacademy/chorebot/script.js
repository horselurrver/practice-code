var doorImage1 = document.getElementById('door1');
var doorImage2 = document.getElementById('door2');
var doorImage3 = document.getElementById('door3');
var botDoorPath = "https://s3.amazonaws.com/codecademy-content/projects/chore-door/images/robot.svg";
var beachDoorPath = "https://s3.amazonaws.com/codecademy-content/projects/chore-door/images/beach.svg";
var spaceDoorPath = "https://s3.amazonaws.com/codecademy-content/projects/chore-door/images/space.svg";
function changeImage1() {
  doorImage1.src = botDoorPath;
}
function changeImage2() {
  doorImage2.src = beachDoorPath;
}
function changeImage3() {
  doorImage3.src = spaceDoorPath;
}
doorImage1.onclick = changeImage1;
doorImage2.onclick = changeImage2;
doorImage3.onclick = changeImage3;
