from flask import Flask, request, redirect, jsonify
import qrcode
import io

app = Flask(__name__)

# In-memory dictionary to store the URL mappings
url_mapping = {}

@app.route('/api/shorten', methods=['POST'])
def shorten_url():
    long_url = request.json['url']
    if long_url in url_mapping:
        short_url = url_mapping[long_url]
    else:
        short_url = generate_short_url(long_url)
        url_mapping[long_url] = short_url
    return jsonify({'short_url': short_url})

@app.route('/<short_url>', methods=['GET'])
def redirect_to_long_url(short_url):
    for long_url, stored_short_url in url_mapping.items():
        if stored_short_url == short_url:
            return redirect(long_url)
    return 'Invalid short URL', 404

@app.route('/api/qrcode/<short_url>', methods=['GET'])
def generate_qr_code(short_url):
    for long_url, stored_short_url in url_mapping.items():
        if stored_short_url == short_url:
            img = qrcode.make(f'http://localhost:5000/{short_url}')
            img_bytes = io.BytesIO()
            img.save(img_bytes, format='PNG')
            return img_bytes.getvalue(), 200, {'Content-Type': 'image/png'}
    return 'Invalid short URL', 404

def generate_short_url(long_url):
    # TODO: Implement a more robust short URL generation mechanism
    return f"short-{len(url_mapping) + 1}"

if __name__ == '__main__':
    app.run(debug=True)