const canvas = document.getElementById('gameCanvas');
const ctx = canvas.getContext('2d');

canvas.width = window.innerWidth;
canvas.height = window.innerHeight;

const middleX = canvas.width / 2;
const middleY = canvas.height / 2;

let mouseX = 0;
let mouseY = 0;
let lastTime = 0;

canvas.addEventListener('mousemove', (event) => {
    const rect = canvas.getBoundingClientRect();
    mouseX = event.clientX - rect.left;
    mouseY = event.clientY - rect.top;
});

let playerX = mouseX;
let playerY = mouseY;
let playerRadius = 10;
let playerColor = 'blue';
let playerSpeed = 120;

let enemyX = middleX;
let enemyY = middleY;
let enemyRadius = 10;
let enemyColor = 'red';
let enemySpeed = 300;

let boundaryX = middleX;
let boundaryY = middleY;
let boundaryRadius = 400;
let boundaryColor = 'black';

function updatePlayerPosition(deltaTime) {
    const dx = mouseX - playerX;
    const dy = mouseY - playerY;
    const distance = Math.sqrt(dx * dx + dy * dy);
    const maxDistance = playerSpeed * deltaTime;
    if (distance > maxDistance) {
        playerX += (dx / distance) * maxDistance;
        playerY += (dy / distance) * maxDistance;
    } else {
        playerX = mouseX;
        playerY = mouseY;
    }
}

// the enemy must stay on the boundary
function updateEnemyPosition(deltaTime) {
    const playerAngle = Math.atan2(playerY - boundaryY, playerX - boundaryX);
    let enemyAngle = Math.atan2(enemyY - boundaryY, enemyX - boundaryX);
    const angleDifference = playerAngle - enemyAngle;
    const maxAngleChange = enemySpeed * deltaTime / boundaryRadius;
    if (Math.abs(angleDifference) > maxAngleChange) {
        if (angleDifference > 0) {
            enemyAngle += maxAngleChange;
        } else {
            enemyAngle -= maxAngleChange;
        }
    } else {
        enemyAngle = playerAngle;
    }
    enemyX = boundaryX + Math.cos(enemyAngle) * boundaryRadius;
    enemyY = boundaryY + Math.sin(enemyAngle) * boundaryRadius;
}

function drawEntity(x, y, radius, color) {
    ctx.fillStyle = color;
    ctx.beginPath();
    ctx.arc(x, y, radius, 0, Math.PI * 2);
    ctx.fill();
}

function drawBoundary() {
    ctx.strokeStyle = boundaryColor;
    ctx.lineWidth = 2;
    ctx.beginPath();
    ctx.arc(boundaryX, boundaryY, boundaryRadius, 0, Math.PI * 2);
    ctx.stroke();
}

function gameLoop(currentTime) {
    const deltaTime = (currentTime - lastTime) / 1000;
    lastTime = currentTime;

    updatePlayerPosition(deltaTime);
    updateEnemyPosition(deltaTime);

    ctx.clearRect(0, 0, canvas.width, canvas.height);
    drawBoundary();
    drawEntity(enemyX, enemyY, enemyRadius, enemyColor);
    drawEntity(playerX, playerY, playerRadius, playerColor);

    requestAnimationFrame(gameLoop);
}

requestAnimationFrame(gameLoop);