<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Register!</title>
    <link rel="shortcut icon" href="favi/lock.png" type="image/x-icon" />
    <link rel="stylesheet" href="register.css" />
  </head>
  <body class="body">
    <div class="navbar">
      <div style="margin-left: 1%; float: left">
        <a class="buttons" href="home.html">Home</a>
      </div>
      <div style="width: 90%; text-align: center">
        <h1>Submission</h1>
      </div>
      <div style="margin-right: 1%; float: right">
        <a class="buttons" href="login.html">Login</a>
      </div>
    </div>
    <div >
        <dl>
            <dt>First Name</dt>
            <dd><?= $_POST["fname"]; ?></dd>
            <dt>Last Name</dt>
            <dd><?= $_POST["lname"]; ?></dd>
            <dt>Email Address</dt>
            <dd><?= $_POST["email"]; ?></dd>
            <dt>Confirm Email Address</dt>
            <dd><?= $_POST["cemail"]; ?></dd>
            <dt>Username</dt>
            <dd><?= $_POST["uname"]; ?></dd>
            <dt>Picture</dt>
            <dd><?= $_POST["pics"]; ?></dd>
            <dt>Password</dt>
            <dd><?= $_COOKIE['PW'];?></dd>
            
        </dl>
        <?php
            if(isset($_POST["fname"]) && isset($_POST["lname"]) && isset($_POST["email"]) && isset($_POST["uname"]) && (!empty($_POST["pics"])) && (!empty($_COOKIE['PW']))){
                echo "<pre>";
                $error = "false";
                if (is_numeric($_POST["fname"])) {
                    echo "First name must not be a number.\n";
                    $error = "true";
                }
                if (is_numeric($_POST["lname"])) {
                    echo "Last name must not be a number.\n";
                    $error = "true";
                }
                if( strcmp($_POST["email"] , $_POST["cemail"]) != 0){
                    echo "Emails provided do not match.\n";
                    $error = "true";
                }
                $fh=fopen("data.html","r");
                $count = 0;
                //echo "nametakem before fakse" . $nametaken. "<br>";
                $nametaken = "false";
                //echo "nametakem after false" . $nametaken. "<br>";
                while($line=fgets($fh)){
                  
                    //echo "LINE: " . $line. "<br>";
                    $piece=explode(",",$line);
                    //echo "piece3 ". trim($piece[3]) . "<br>";
                    //echo "uname " . trim($_POST["uname"]). "<br>";
                    //echo "STMP: " . strcmp(trim($piece[3]),trim($_POST["uname"])). "<br>"; 
                    //echo "nametakem loop" . $nametaken. "<br>";
                    if(strcmp(trim($piece[3]),trim($_POST["uname"])) == 0){
                        //echo "hello";
                        $error = "true";
                        $nametaken = "true";
                        
                    }
                }
                //echo "nametakem after loop" . $nametaken. "<br>";
                if($nametaken == "true"){
                    echo "Error: Username already taken!<br>";
                    $error = "true";
                }
                
                if($error == "true"){
                    echo "Please try again.";
                }else{
                    $data = $_POST["fname"] . "," .$_POST["lname"] . "," .$_POST["email"] . "," .$_POST["uname"] . "," .$_POST["pics"] . "," . $_COOKIE['PW'] . "\r\n"; 
                    echo $data . "<br><br>";
                    $saved = file_put_contents("data.html", $data, FILE_APPEND | LOCK_EX);
                    //echo $saved;
                    echo file_get_contents("data.html") . "<br>";
                }
                echo "</pre>";
            }else{

            }
        ?>
    </div>
    

  </body>
</html>
