from flask import Flask, render_template, request, send_file
from PIL import Image
from io import BytesIO

app = Flask(__name__)

@app.route('/', methods=["POST", "GET"])
def index():
    if request.method == "POST":
        image_file = request.files['image']
        width = request.form.get('width')
        height = request.form.get('height')
        quality = request.form.get('quality')
        
        if not image_file:
            return "Did not recieve image."
        img = Image.open(image_file)
        
        if width and height:
            img = img.resize((int(width), int(height)), Image.Resampling.LANCZOS)
            
        # buffer
        buffer = BytesIO() # empty space to save the result
        format = "JPEG" if img.format != 'PNG' else 'PNG'
        quality = int(quality) if quality else 85
        
        img.save(buffer, format=format, quality=quality, optimize=True)
        buffer.seek(0)
        return send_file(buffer, as_attachment=True, download_name="opt_"+image_file.filename, mimetype='image/jpg')
    return render_template("index.html")

if __name__ == "__main__":
    app.run()