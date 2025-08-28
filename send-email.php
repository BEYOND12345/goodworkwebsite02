<?php
if ($_POST) {
    $name = $_POST['name'];
    $email = $_POST['email'];
    $phone = $_POST['phone'];
    $location = $_POST['location'];
    $service = $_POST['service'];
    $message = $_POST['message'];
    
    $to = 'danhandywork@gmail.com';
    $subject = 'New Quote Request from GoodHands Website';
    
    $body = "New quote request received:\n\n";
    $body .= "Name: " . $name . "\n";
    $body .= "Email: " . $email . "\n";
    $body .= "Phone: " . $phone . "\n";
    $body .= "Location: " . $location . "\n";
    $body .= "Service: " . $service . "\n";
    $body .= "Message: " . $message . "\n";
    $body .= "\nSubmitted from: https://goodhandshandyman.com.au/contact.html";
    
    $headers = "From: " . $email . "\r\n";
    $headers .= "Reply-To: " . $email . "\r\n";
    $headers .= "X-Mailer: PHP/" . phpversion();
    
    if (mail($to, $subject, $body, $headers)) {
        header('Location: /thank-you.html');
        exit;
    } else {
        echo "Sorry, there was an error sending your message. Please call 0481 457271 directly.";
    }
} else {
    header('Location: /contact.html');
    exit;
}
?>