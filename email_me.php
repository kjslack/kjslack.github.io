<?php
$to = "kent.slack@gmail.com";
$name = $_POST["Name"];
$email = $_POST["Email"];
$message = $_POST["Message"];

$msg = wordwrap($message,70);

// send email
mail($to,"Email from kentslack.com",$msg);
?>