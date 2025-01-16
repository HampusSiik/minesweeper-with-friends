const host = location.host;

const apiBaseUrl = `http://${host}`;
const socket = io(apiBaseUrl);

const roomId = location.pathname.split("/")[2];

const resetEmoji = (isWon, isLost) => {
    if (isWon) {
        return "😎";
    } else if (isLost) {
        return "😵";
    } else {
        return "🙂";
    }
}

const joinRoom = () => {
    socket.emit("join_room",
        {
            room_id: roomId
        }
    );
}

const createCellObject = (character) => {
    is_revealed = !"#F".includes(character);
    is_mine = character === "*";
    is_flagged = character === "F";
    adjacent_mines = "0123456789".includes(character) ? parseInt(character) : 0;
    return {
        is_revealed,
        is_mine,
        is_flagged,
        adjacent_mines
    };
}

const createBoardObject = (board) => {

    return board.split('\n').map(row => Array.from(row).map(createCellObject));
}

const createCell = (rowIndex, colIndex, won, lost) => {
    const cell = document.createElement("div");
    cell.classList.add("cell");
    if (!(won || lost)) {
        cell.addEventListener("click", () => handleLeftClick(rowIndex, colIndex));
        cell.addEventListener("contextmenu", (event) => {
            event.preventDefault();
            handleRightClick(rowIndex, colIndex);
        });
    }
    return cell;
}

const makeResetOopsFace = () => {
    const button = document.getElementById("restart-game");
    button.textContent = "😮";
    return button;
}

const resetResetEmoji = () => {
    const button = document.getElementById("restart-game");
    button.textContent = resetEmoji(false, false);
    return button;
}

const updateGrid = (board, won, lost) => {
    const grid = document.getElementById("grid");
    grid.addEventListener("mousedown", () => makeResetOopsFace());
    grid.addEventListener("mouseup", () => resetResetEmoji());
    grid.addEventListener("contextmenu", (event) => event.preventDefault());
    grid.innerHTML = "";
    grid.style.gridTemplateColumns = `repeat(${board[
        0
    ].length
        },
    1fr)`;
    grid.style.gridTemplateRows = `repeat(${board.length
        },
    1fr)`;
    board.forEach((row, rowIndex) => {
        row.forEach((cell, colIndex) => {
            const cellElement = createCell(rowIndex, colIndex, won, lost);
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
    socket.emit("left_click", {
        room_id: roomId,
        position: {
            row, col
        }
    });
};

const handleRightClick = async (row, col) => {
    socket.emit("right_click", {
        room_id: roomId,
        position: {
            row, col
        }
    });
};

socket.on("update_room", (data) => {
    updateGrid(createBoardObject(data.show_board), data.is_won, data.is_lost);
    document.getElementById("restart-game").textContent = resetEmoji(data.is_won, data.is_lost);
    console.log("update_room", data);
});

const toMainMenu = () => {
    window.location.href = "/";
};
document.getElementById("back-to-menu").addEventListener("click", toMainMenu);

const makeRestartButton = (button) => {
    button.addEventListener("click", () => {
        socket.emit("reset_game", {
            room_id: roomId
        });
    });
    return button;
}

makeRestartButton(document.getElementById("restart-game"));

joinRoom();
