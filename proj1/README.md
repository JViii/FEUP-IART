# FEUP-IART
# How to run

## Windows
Run the executable located at Windows/game.exe

## Linux
Run the executable located at Linux/game

**You might need to give it the permission to execute**
```bash
$ chmod +x Linux/game
```

## Or
### Install dependencies
```bash 
python3 -m pip install pygame 
python3 game.py 
```

### Run Backup Text Interface
There's also a text based interface available

```bash
python3 -c "import solve; solve.text_interface()"
```

# Instructions

## Human Mode
In this mode, you can fill and unfill the aquarium to reach the goal. Also, you have a hint button to help you know which aquarium to fill/unfill next. If a cell has a negative value, it means it is empty. On the other hand, if it has a positive value, the cell is filled. The goal is to fill the number of cells in a row/column represented by the numbers outside the grid.

## PC Mode
In this mode, you can choose which algorithm you want use to find the solution for the puzzle.

#
# Elements:
* Diogo Santos
* Jéssica Nascimento
* João Vitor Fernandes
