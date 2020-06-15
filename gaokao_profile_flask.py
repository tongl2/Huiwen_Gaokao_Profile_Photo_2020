from flask import Blueprint, send_from_directory, request
from PIL import Image
from base64 import b64encode
from io import BytesIO
import json
from datetime import datetime, timedelta, timezone

blueprint = Blueprint(
    'gaokao_profile', __name__,
    static_folder='assets', static_url_path='/assets/',
    url_prefix='/gaokao2020/'
)

MODULE_PATH = "."

def process_img(img):
    try:
        frame_img = Image.open(MODULE_PATH + '/frame.png')
        target = Image.new('RGBA', frame_img.size, (0, 0, 0, 0))
        box = (0, 0, 380, 380)
        img = img.convert('RGBA')
        img = img.resize((box[2] - box[0], box[3] - box[1]))
        target.paste(img, box)
        target.paste(frame_img, (0, 0), frame_img)
        target = target.convert('RGB')
        visit_cnt()
        return 'success', target
    except:
        return 'error', None


def visit_cnt():
    t = datetime.now(timezone(timedelta(hours=8)))
    time_str = t.strftime(r"%H:%M:%S / %B %d, %Y  / %A")
    open(MODULE_PATH + '/visit_history.txt', 'a').write(time_str + "\n")


@blueprint.route('/api', methods=['POST'])
def gaokao_api():
    img = request.files.get('file')
    status, res_img = process_img(Image.open(img))
    resp_dict = {'status': status}
    if res_img:
        output_buffer = BytesIO()
        res_img.save(output_buffer, format='JPEG')
        byte_data = b64encode(output_buffer.getvalue())
        resp_dict['image'] = byte_data.decode('utf-8')
    return json.dumps(resp_dict)


@blueprint.route('/')
def gaokao():
    return send_from_directory(MODULE_PATH, 'gaokao_profile.html')
