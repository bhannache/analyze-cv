from bottle import route, request, run
import os

@route('/hello')
def hello():
    return "this is live"

@route('/upload')
def upload(): 
    return '''
    <form action="/upload" method="post" enctype="multipart/form-data">
    Category: <input type="text" name="category" />
    Select a file: <input type="file" name="upload" />
    <input type="submit" value="Start upload" />
    </form>
'''

@route('/upload', method='POST')
def do_upload():
    category = request.forms.get('category')
    upload = request.files.get('upload')
    name, ext = os.path.splitext(upload.filename)
    if ext not in ('.png','.jpg','.jpeg', ".docx"):
        return 'File extension not allowed.'
    
    #save_path = get_save_path_for_category(category)
    save_path = '/'
    upload.save(save_path) # appends upload.filename automatically
    return 'OK'

run(host='0.0.0.0', port=8090, debug=True)
