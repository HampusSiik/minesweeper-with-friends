# Requirements analysis document

This is document contains the high level userstories and some other core ideas.

## The mountain

This is the highest level user story

### *Minesweeper With Friends*

As a gamer with friends I want to be able to play MineSweeper online with them.

#### Definition of done

- [x] Implement the game
- [x] Make a functional web API
- [x] Implement a web user interface
- [x] Make it possible to host a game
- [x] Make it possible to join a game

### Enhanced user experience

As a player I want the game to be fast and responsive and look nicer.

#### Definition of done

- [ ] Clarify the game state
- [x] Make new game in room
- [ ] Make the game more responsive

## The Boulders

These are slightly smaller pieces of the system that should be smaller and more managable.

### *Web user interface*

As a user I want to be able to play the game in my webbrowser.

#### Definition of done

- [x] Make it possible to show the game board
- [x] Make it possible to interact with the cells on the board
- [x] Have a main menu

### *Make a functional web API*

As a web interface developer I need an API to get information about the game state from the host.

#### Definition of done

- [x] Make it possible to get the game state
- [x] Make it possible to send click commands to the game
- [x] Make it possible to have multiple users connected to the same game

### *Implement the game*

As an API developer I need an implementation of the game to make it possible to send and recieve commands.

#### Definition of done

- [x] Make it possible to create a game
- [x] Make it possible to click on a cell
- [x] Make it possible to get the game state

### *Host a game*

As a user I want to be able to host a game so that my friends can join.

#### Definition of done

- [x] Make it possible to create a game with a unique id
- [x] Make it possible to set a username in the game

### *Join a game*

As a user I want to be able to join a game so that I can play with my friends.

#### Definition of done

- [x] Make it possible to join a game with a unique id
- [x] Make it possible to set a username in the game

### Clarify the game state

As a player I want it to be clear wether I have won or lost the game.

#### Definition of done

- [ ] Make it clear to the user when the game is won.
- [ ] Make it clear to the user when the game is lost.

### *Make new game in room*

As a host I want to be able to start a new game without having to make a new room.

#### Definition of done

- [x] Add a new game functionality in the API.
- [x] Add new game button in the game.

### Make the game more responsive

As a player I want the game to be more responsive.

#### Definition of done

- [ ] Reduce the package sent on update.
- [x] Disable context menu in between cells.
