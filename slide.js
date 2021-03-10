function swapTiles(cell1,cell2) {
    var temp = document.getElementById(cell1).className;
    document.getElementById(cell1).className = document.getElementById(cell2).className;
    document.getElementById(cell2).className = temp;
  }
  
  function shuffle() {
  //Use nested loops to access each cell of the 3x3 grid
  for (var row=1;row<=3;row++) { //For each row of the 3x3 grid
     for (var col=1;col<=3;col++) { //For each col in this row
    
      var row2=Math.floor(Math.random()*3 + 1); //Pick a random row from 1 to 3
      var col2=Math.floor(Math.random()*3 + 1); //Pick a random col from 1 to 3
       
      swapTiles("cell"+row+col,"cell"+row2+col2); //Swap the look & feel of both cells
    } 
  } 
  }
  
  function clickTile(row,col) {
    var cell = document.getElementById("cell"+row+col);
    var tile = cell.className;
    if (tile!="tile9") { 
         //Checking if white tile on the right
         if (col<3) {
           if ( document.getElementById("cell"+row+(col+1)).className=="cell9") {
             swapTiles("cell"+row+col,"cell"+row+(col+1));
             return;
           }
         }
         //Checking if white tile on the left
         if (col>1) {
           if ( document.getElementById("cell"+row+(col-1)).className=="cell9") {
             swapTiles("cell"+row+col,"cell"+row+(col-1));
             return;
           }
         }
           //Checking if white tile is above
         if (row>1) {
           if ( document.getElementById("cell"+(row-1)+col).className=="cell9") {
             swapTiles("cell"+row+col,"cell"+(row-1)+col);
             return;
           }
         }
         //Checking if white tile is below
         if (row<3) {
           if ( document.getElementById("cell"+(row+1)+col).className=="cell9") {
             swapTiles("cell"+row+col,"cell"+(row+1)+col);
             return;
           }
         } 
    }
    
  }