<html>
    <head>
        <meta charset="UTF-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />
        <title>Dashboard!</title>
        <link rel="shortcut icon" href="favi/unlock.png" type="image/x-icon" />
        <link rel="stylesheet" href="register.css" />
      </head>
    <div class="navbar">
        <div style="margin-left: 1%; float: left">
          <a class="buttons" href="home.html">Logout</a>
        </div>
        <div style="width: 90%; margin-right: 7%; text-align: center">
          <?php 
            $user = $_GET["uname"]; 
          ?>

          <h1>Welcome back, <?php echo $user; ?>!</h1>
        </div>
    </div>


</html>