const host = location.host;

const apiBaseUrl = `http://${host}`;
const socket = io(apiBaseUrl);

let gameId = null;

const emitJoinGame = () => {
    socket.emit("join_game", { game_id: gameId });
}

const fetchBoard = async () => {
    try {
        const response = await fetch(`${apiBaseUrl}/get_board/${gameId}`);
        if (!response.ok) throw new Error("Failed to fetch board");
        const data = await response.json();
        updateGrid(data.board);
    } catch (error) {
        console.error("Error fetching board:", error);
    }
};

const createGame = async (rows, cols, mines) => {
    console.log(apiBaseUrl);
    try {
        const response = await fetch(`${apiBaseUrl}/create_game`, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ rows, cols, mines }),
        });
        if (!response.ok) throw new Error("Failed to create game");
        const data = await response.json();
        gameId = data.game_id;
        fetchBoard();
    } catch (error) {
        console.error("Error creating game:", error);
    }
    emitJoinGame();
};

const createCell = (rowIndex, colIndex) => {
    const cell = document.createElement("div");
    cell.classList.add("cell");
    cell.addEventListener("click", () => handleLeftClick(rowIndex, colIndex));
    cell.addEventListener("contextmenu", (event) => {
        event.preventDefault();
        handleRightClick(rowIndex, colIndex);
    });
    return cell;
}

const updateGrid = (board) => {
    const grid = document.getElementById("grid");
    grid.innerHTML = "";
    grid.style.gridTemplateColumns = `repeat(${board[0].length}, 1fr)`;
    grid.style.gridTemplateRows = `repeat(${board.length}, 1fr)`;
    board.forEach((row, rowIndex) => {
        row.forEach((cell, colIndex) => {
            const cellElement = createCell(rowIndex, colIndex);
            if (cell.is_revealed) {
                cellElement.classList.add("revealed");
                cellElement.textContent = cell.is_mine ? "💣" : cell.adjacent_mines || "";
            } else if (cell.is_flagged) {
                cellElement.textContent = "🚩";
            }
            grid.appendChild(cellElement);
        });
    });
};

const handleLeftClick = async (row, col) => {
    socket.emit("left_click", { game_id: gameId, position: { row, col } });
};

const handleRightClick = async (row, col) => {
    socket.emit("right_click", { game_id: gameId, position: { row, col } });
};

socket.on("update_board", (data) => {
    updateGrid(data.board);
});

createGame(10, 10, 10);
