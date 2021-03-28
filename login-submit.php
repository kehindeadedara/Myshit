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
    <div class="centerpre">
        <!-- <dl>
            <dt>Username </dt>
            <dd><?= $_GET["uname"]; ?></dd>
            <dt>Password</dt>
            <dd><?= $_GET['pics'];?></dd>
        </dl> -->

        <?php
            session_save_path("session");
            session_start();
            echo "<pre>";
            if(empty($_GET["uname"]) || empty($_GET["pics"])){
                echo "Please enter a username and / or password!<br>";
            }
            else if(isset($_GET["uname"]) && isset($_GET["pics"])){
                $fh=fopen("data.html","r");
                $count = 0;
                while($line=fgets($fh)){
                    $piece=explode(",",$line);
                    if($piece[3]==$_GET["uname"]){
                        $password=$piece[5];
                        $uname=$piece[3];
                        $img=$piece[4];
                        $count++;
                    }
                }
                if($count=0){
                    echo "Username or password not found. Please try again! <br>";
                }
                else if((strcmp(trim($_COOKIE["PW"]) , trim($password)) == 0) && (strcmp(trim($_GET["pics"]) , trim($img)) == 0)){
                    //insert code here to sign them in
                    //$_SESSION["uname"] = $_GET["uname"];
                    $user = $_GET["uname"];
                    $_SESSION["uname"] = $user;
                    echo "sesh" . $_SESSION["uname"];
                    header("Location: dashboard.php?uname=" . $user);
                    echo "test";
                    
                }
                else{
                    //header('Location: validation.php'); //link to error page
                    echo "Incorrect Password: Please try again!<br>";
                    
                }
            }else{
                echo "Error: Please try again later.<br>";
            }
            echo "<pre>";
        ?>
    </div>
    

  </body>
</html>
