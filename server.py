from flask import Flask, request, send_file
from moviepy.editor import VideoFileClip

app = Flask(__name__)

@app.route('/edit-video', methods=['POST'])
def edit_video():
    video = request.files['video']
    video.save('input_video.mp4')

    # مثال بسيط لتحسين الفيديو وإضافة مؤثرات
    clip = VideoFileClip('input_video.mp4')
    edited_clip = clip.fx(vfx.colorx, 1.2)  # تحسين الألوان
    edited_clip.write_videofile('edited_video.mp4')

    return send_file('edited_video.mp4', as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
