<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="styles.css">
    <title>My Website</title>
</head>

<form method="post" id="content_id" action= "content_loaders.php" target="_blank" >
    <input type="radio" name="content_option" value="pictures" id="pictures" checked>
    <label for="pictures">Pictures</label><br>
    <input type="radio" name="content_option" value="videos" id="videos">
    <label for="videos">Videos</label><br>
    <input type="radio" name="content_option" value="everything" id="everything">
    <label for="videos">Everything</label><br>
</form>
<?php

$dir = "./contents/";



$contents = new DirectoryIterator($dir);

foreach ($contents as $content) {
    if($content->isDir() && !$content->isDot()) {
        $filename = $content->getFilename();
        ?>
        <input type="submit" name="submit" value="<?php echo $filename?>" form="content_id" </input>
    <?php

    }
}
?>
</html>