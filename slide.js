var pass = "";
var maxmove = 10;
var current = 0;
function swapTiles(cell1,cell2) {
    var temp = document.getElementById(cell1).className;
    document.getElementById(cell1).className = document.getElementById(cell2).className;
    document.getElementById(cell2).className = temp;
    console.log("password: ", pass);
  }
function setCookie(){
    var cookieString = "PW=" + pass;
    document.cookie = cookieString;
}
function setImage(imageSelect){
    console.log("awd", imageSelect);   
    var img = imageSelect == "1" ? "cellimage1" : imageSelect == "2" ? "cellimage2" : imageSelect == "3" ? "cellimage3" : "" ; 
    console.log(img);
    // var sq = document.getElementsByClassName("cellimage");

    // console.log(document.getElementsByClassName("cellimage")[0].classList);
    var matches;
    
    var matches1 = document.getElementsByClassName("cellimage1");
    var matches2 = document.getElementsByClassName("cellimage2");
    var matches3 = document.getElementsByClassName("cellimage3");
    //debugger;
    if (matches1.length > 0)
        matches = matches1;
    else if (matches2.length > 0)
        matches = matches2;
    else if (matches3.length > 0)
        matches = matches3;
    else{
        console.log("error");
        return
    }
    console.log(matches);
    
    while (matches.length > 0 ) {
        //debugger;
        matches.item(0).classList.add(img);
        console.log(matches.length);
        if(imageSelect == "1"){
            if(matches[0].classList.contains("cellimage2"));
                matches[0].classList.remove('cellimage2');
            if(matches[0].classList.contains("cellimage3"));
                matches[0].classList.remove('cellimage3');
        }else if(imageSelect == "2"){
            if(matches[0].classList.contains("cellimage1"));
                matches[0].classList.remove('cellimage1');
            if(matches[0].classList.contains("cellimage3"));
                matches[0].classList.remove('cellimage3');
        }else if(imageSelect == "3"){
            if(matches[0].classList.contains("cellimage1"));
                matches[0].classList.remove('cellimage1');
            if(matches[0].classList.contains("cellimage2"));
                matches[0].classList.remove('cellimage2');
        }
        else return;
            
    }
    
    
}
function clickTile(row,col) {
    var cell = document.getElementById("cell"+row+col);
    var tile = cell.className;
    if (current < maxmove){
        if (tile!="cell9") { 
            //Checking if white tile on the right
            if (col<3) {
                if ( document.getElementById("cell"+row+(col+1)).classList.contains("cell9")) {
                    pass += row.toString() + col.toString();
                    swapTiles("cell"+row+col,"cell"+row+(col+1));
                    current += 1;
                    
                    return;
                }
            }
            //Checking if white tile on the left
            if (col>1) {
                if ( document.getElementById("cell"+row+(col-1)).classList.contains("cell9")) {
                    pass += row.toString() + col.toString();
                    swapTiles("cell"+row+col,"cell"+row+(col-1));
                    current += 1;
                    
                    return;
                }
            }
            //Checking if white tile is above
            if (row>1) {
                if ( document.getElementById("cell"+(row-1)+col).classList.contains("cell9")) {
                    pass += row.toString() + col.toString();
                    swapTiles("cell"+row+col,"cell"+(row-1)+col);
                    current += 1;
                    
                    return;
                }
            }
            //Checking if white tile is below
            if (row<3) {
                if ( document.getElementById("cell"+(row+1)+col).classList.contains("cell9")) {
                    pass += row.toString() + col.toString();
                    swapTiles("cell"+row+col,"cell"+(row+1)+col);
                    current += 1;
                    
                    return;
                }
            } 
        }
    }
}