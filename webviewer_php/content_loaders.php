<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="styles.css">
    <title>My Website</title>
</head>

<?php
function show_picture($file) {
    echo '<img src="'.$file.'" /><br />';
}

function show_video($file) {
    echo "<video controls src='$file' width='560' height='315'></video>";
}

$dir = $_POST["submit"];
$content_option = $_POST["content_option"];

$image_display = array('jpg', 'jpeg', 'png', 'gif', 'webp');
$video_display = array("mp4", "webm", "mov");

$dir_name = "./contents/".$dir."/";
$images = glob($dir_name."*.*", GLOB_BRACE);

foreach($images as $image) {
    $ext = strtolower(pathinfo($image, PATHINFO_EXTENSION));
    if($content_option == "pictures") {
        if(in_array($ext, $image_display)){   
            show_picture($image);
        }
    }elseif($content_option == "videos"){
        if(in_array($ext, $video_display)){ 
            show_video($image);
        }
    }elseif($content_option == "everything") {
        if(in_array($ext, $image_display)){   
            show_picture($image);
        }elseif(in_array($ext, $video_display)){ 
            show_video($image);
        }
    }
}

?>

</html>