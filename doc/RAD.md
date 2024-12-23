# Requirements analysis document

This is document contains the high level userstories and some other core ideas.

## The mountain

This is the highest level user story

### Minesweeper With Friends

As a gamer with friends I want to be able to play MineSweeper online with them.

#### Definition of done

- [x] Implement the game
- [ ] Make a functional web API
- [ ] Implement a web user interface
- [ ] Make it possible to host a game
- [ ] Make it possible to join a game

## The Boulders

These are slightly smaller pieces of the system that should be smaller and more managable.

### Web user interface

As a user I want to be able to play the game in my webbrowser.

#### Definition of done

- [ ] Make it possible to show the game board
- [ ] Make it possible to interact with the cells on the board
- [ ] Have a main menu

### Make a functional web API

As a web interface developer I need an API to get information about the game state from the host.

#### Definition of done

- [ ] Make it possible to get the game state
- [ ] Make it possible to send click commands to the game
- [ ] Make it possible to have multiple users connected to the same game

### *Implement the game*

As an API developer I need an implementation of the game to make it possible to send and recieve commands.

#### Definition of done

- [x] Make it possible to create a game
- [x] Make it possible to click on a cell
- [x] Make it possible to get the game state

### Host a game

As a user I want to be able to host a game so that my friends can join.

#### Definition of done

- [ ] Make it possible to create a game with a unique id
- [ ] Make it possible to set a password for the game
- [ ] Make it possible to set a username in the game

### Join a game

As a user I want to be able to join a game so that I can play with my friends.

#### Definition of done

- [ ] Make it possible to join a game with a unique id
- [ ] Make it possible to set a username in the game
