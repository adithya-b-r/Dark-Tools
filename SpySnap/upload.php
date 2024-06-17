<?php
// Check if image data was sent
if (isset($_POST['image'])) {
    // Get the base-64 encoded data
    $base64_image = $_POST['image'];

    // Remove the data prefix and decode
    $base64_image = str_replace('data:image/png;base64,', '', $base64_image);
    $base64_image = str_replace(' ', '+', $base64_image);
    $image_data = base64_decode($base64_image);

    // Generate a unique filename
    $filename = 'photo_' . time() . '.png';
    $filepath = 'uploads/' . $filename;

    // Save the image file
    if (file_put_contents($filepath, $image_data)) {
        echo "Photo saved successfully as $filename";
    } else {
        echo "Failed to save photo.";
    }
} else {
    echo "No image data received.";
}
?>
