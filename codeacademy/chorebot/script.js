var doorImage1 = document.getElementById('door1');
var doorImage2 = document.getElementById('door2');
var doorImage3 = document.getElementById('door3');
var botDoorPath = "https://s3.amazonaws.com/codecademy-content/projects/chore-door/images/robot.svg";
var beachDoorPath = "https://s3.amazonaws.com/codecademy-content/projects/chore-door/images/beach.svg";
var spaceDoorPath = "https://s3.amazonaws.com/codecademy-content/projects/chore-door/images/space.svg";
var openDoor1 = botDoorPath;
var openDoor2 = beachDoorPath;
var openDoor3 = spaceDoorPath;
var closedDoorPath = "https://s3.amazonaws.com/codecademy-content/projects/chore-door/images/closed_door.svg";
var numClosedDoors = 3;
var startButton = document.getElementById("start-row");
var currentlyPlaying = true;
const randomChoreDoorGenerator = () => {
  var choreDoor = Math.floor(Math.random() * numClosedDoors);
  if (choreDoor === 0) {
    openDoor1 = botDoorPath;
    openDoor2 = beachDoorPath;
    openDoor3 = spaceDoorPath;
  } else if (choreDoor === 1) {
    openDoor2 = botDoorPath;
    openDoor1 = beachDoorPath;
    openDoor3 = spaceDoorPath;
  } else {
    openDoor3 = botDoorPath;
    openDoor1 = beachDoorPath;
    openDoor2 = spaceDoorPath;
  }
};

function changeImage1() {
  if (currentlyPlaying && !isClicked(doorImage1)) {
    doorImage1.src = openDoor1;
    console.log('door 1 clicked!');
    playDoor(doorImage1);
  }
}

function changeImage2() {
  if (currentlyPlaying && !isClicked(doorImage2)) {
    doorImage2.src = openDoor2;
    console.log('door 2 clicked!');
    playDoor(doorImage2);
  }
}

function changeImage3() {
  if (currentlyPlaying && !isClicked(doorImage3)) {
    doorImage3.src = openDoor3;
    console.log('door 3 clicked!');
    playDoor(doorImage3);
  }
}

doorImage1.onclick = changeImage1;
doorImage2.onclick = changeImage2;
doorImage3.onclick = changeImage3;

function isBot(door) {
  if (door.src === botDoorPath) {
    return true;
  }
  return false;
}

function isClicked(door) {
  if (door.src === closedDoorPath) {
    return false;
  }
  return true;
}

function playDoor(door) {
  numClosedDoors = numClosedDoors - 1;
  if (numClosedDoors === 0) {
    gameOver("win");
  } else if (isBot(door)) {
    gameOver();
  }
}

function gameOver(status) {
  if (status === "win") {
    startButton.innerHTML = "You win! Play again?";
  } else {
    startButton.innerHTML = "Game over! Play again?";
  }
  currentlyPlaying = false;
}

function startRound() {
  if (!currentlyPlaying) {
    var openDoor1 = botDoorPath;
    var openDoor2 = beachDoorPath;
    var openDoor3 = spaceDoorPath;
    doorImage1.src = closedDoorPath;
    doorImage2.src = closedDoorPath;
    doorImage3.src = closedDoorPath;
    numClosedDoors = 3;
    startButton.innerHTML = "Good luck!";
    currentlyPlaying = true;
    randomChoreDoorGenerator();
  }
}

startButton.onclick = startRound;

startRound();
