// script.js

let currentPlayer = 'X';
let gameBoard = ["", "", "", "", "", "", "", "", ""]; // Represents the game board
let gameActive = true; // Flag to prevent further moves after a win or draw

// Function to handle player turns
function playerTurn(cellIndex) {
  if (gameBoard[cellIndex] === "" && gameActive) {
    gameBoard[cellIndex] = currentPlayer;
    document.getElementById("cell-" + cellIndex).innerText = currentPlayer;

    if (checkWinner()) {
      displayResult("Player " + currentPlayer + " wins!");
      gameActive = false;
      return;
    }

    if (isDraw()) {
      displayResult("It's a draw!");
      gameActive = false;
      return;
    }

    currentPlayer = currentPlayer === 'X' ? 'O' : 'X';
    console.log("Current player: " + currentPlayer);
  } else {
    console.log("Cell already occupied");
  }
}

// Function to check for a winner
function checkWinner() {
  const winPatterns = [
    [0, 1, 2], [3, 4, 5], [6, 7, 8], // Rows
    [0, 3, 6], [1, 4, 7], [2, 5, 8], // Columns
    [0, 4, 8], [2, 4, 6]             // Diagonals
  ];

  for (const pattern of winPatterns) {
    const [a, b, c] = pattern;
    if (gameBoard[a] && gameBoard[a] === gameBoard[b] && gameBoard[a] === gameBoard[c]) {
      return true;
    }
  }
  return false;
}

// Function to check for a draw
function isDraw() {
  return !gameBoard.includes("");
}

// Function to display the result
function displayResult(message) {
  const resultElement = document.getElementById("result");
  if (resultElement) {
    resultElement.innerText = message;
  } else {
    alert(message); // Fallback if the result element doesn't exist
  }
}

// Function to reset the game
function resetGame() {
  currentPlayer = 'X';
  gameBoard = ["", "", "", "", "", "", "", "", ""];
  gameActive = true;
  for (let i = 0; i < 9; i++) {
    document.getElementById("cell-" + i).innerText = "";
  }
  const resultElement = document.getElementById("result");
  if (resultElement) {
    resultElement.innerText = ""; // Clear the result message
  }
  console.log("Game reset");
}

// Add event listeners to each cell
for (let i = 0; i < 9; i++) {
  document.getElementById("cell-" + i).addEventListener("click", () => playerTurn(i));
}