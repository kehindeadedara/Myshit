var pass = "";
function swapTiles(cell1,cell2) {
    var temp = document.getElementById(cell1).className;
    document.getElementById(cell1).className = document.getElementById(cell2).className;
    document.getElementById(cell2).className = temp;
  }
  
  function clickTile(row,col) {
    var cell = document.getElementById("cell"+row+col);
    var tile = cell.className;
    
    if (tile!="cell9") { 
         //Checking if white tile on the right
         if (col<3) {
           if ( document.getElementById("cell"+row+(col+1)).className=="cell9") {
            pass += row.toString() + col.toString();
            swapTiles("cell"+row+col,"cell"+row+(col+1));
            console.log(pass);
            return;
           }
         }
         //Checking if white tile on the left
         if (col>1) {
           if ( document.getElementById("cell"+row+(col-1)).className=="cell9") {
            pass += row.toString() + col.toString();
            swapTiles("cell"+row+col,"cell"+row+(col-1));
            console.log(pass);
            return;
           }
         }
           //Checking if white tile is above
         if (row>1) {
           if ( document.getElementById("cell"+(row-1)+col).className=="cell9") {
            pass += row.toString() + col.toString();
            swapTiles("cell"+row+col,"cell"+(row-1)+col);
            console.log(pass);
            return;
           }
         }
         //Checking if white tile is below
         if (row<3) {
           if ( document.getElementById("cell"+(row+1)+col).className=="cell9") {
            pass += row.toString() + col.toString();
            swapTiles("cell"+row+col,"cell"+(row+1)+col);
            console.log(pass);
            return;
           }
         } 
    }
    
  }