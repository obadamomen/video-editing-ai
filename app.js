function uploadVideo() {
    const videoFile = document.getElementById('videoFile').files[0];
    if (!videoFile) {
        alert('Please select a video file.');
        return;
    }

    const formData = new FormData();
    formData.append('video', videoFile);

    fetch('/edit-video', {
        method: 'POST',
        body: formData
    })
    .then(response => response.blob())
    .then(blob => {
        const url = URL.createObjectURL(blob);
        const a = document.createElement('a');
        a.href = url;
        a.download = 'edited_video.mp4';
        document.body.appendChild(a);
        a.click();
        a.remove();
    })
    .catch(error => console.error('Error:', error));
}
