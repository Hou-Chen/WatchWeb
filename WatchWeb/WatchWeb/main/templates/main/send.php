<?php
if (isset($_POST["Send"])) {
	$to = "houchen691@gmail.com";
	$name = $_POST['name'];
	$email = $_POST['email'];
	$subject = "WatchWeb";
	$message = $_POST['message'];
	
	$header = "From: $email \nReply-To: $email \n";
	
	if (mail($to, $subject, $message, $header))
		echo "送出成功 <br/>";
	else
		echo "送出失敗 <br/>";
}
?>