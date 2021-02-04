import json
import os

from config import ROOT_DIR, DOC_DOMAIN

def error_out(data={}, msg='fail', status='fail', code=0):
    data = {
        "data": data,
        "msg": msg,
        "status": status,
        "code": code
    }
    return json.dumps(data,ensure_ascii=False)


def success_out(data={}, msg='success', status='success', code=1):
    data = {
        "data": data,
        "msg": msg,
        "status": status,
        "code": code
    }
    return json.dumps(data,ensure_ascii=False)


def validation_error(e):
    try:
        messages = e.messages
        print(type(messages))
        if isinstance(messages, dict):
            for key, message in messages.items():
                while isinstance(message, dict):
                    message = message.values()[0]
                    key = message.keys()[0]
                if isinstance(message, list):
                    error_message = "{}:{}".format(message[0],key)
                    return error_out(msg=error_message)
                else:
                    error_message = "{}:{}".format(message[0],key)
                    return error_out(msg=error_message)
        else:
            return error_out(msg=message)
        
    except:
        return error_out()


def get_doc_url(path):
    doc_url = ''
    if path:
        doc_url = os.path.join(DOC_DOMAIN, path.replace('/tmp/',''))
    
    return doc_url
    
        

    