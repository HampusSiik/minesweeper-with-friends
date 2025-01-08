const host = location.host;

const apiBaseUrl = `http://${host}`;
const socket = io(apiBaseUrl);

const roomId = location.pathname.split("/")[2];

const joinRoom = () => {
    socket.emit("join_room",
        {
            room_id: roomId
        }
    );
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

const updateGrid = (board, won, lost) => {
    const grid = document.getElementById("grid");
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
    await fetch(`${apiBaseUrl
        }/left_click`,
        {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                room_id: roomId, position: {
                    row, col
                }
            }),
        }
    );
};

const handleRightClick = async (row, col) => {
    await fetch(`${apiBaseUrl
        }/right_click`,
        {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                room_id: roomId, position: {
                    row, col
                }
            }),
        }
    );
};

socket.on("update_room", (data) => {
    updateGrid(data.show_board, data.is_won, data.is_lost);
    console.log("update_room", data);
});

document.getElementById("back-to-menu").addEventListener("click", () => {
    window.location.href = "/";
});

joinRoom();
