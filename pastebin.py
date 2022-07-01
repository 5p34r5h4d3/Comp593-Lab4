import requests


def post_new_paste(title, body_text, expiration='N', listed=True):

    print('Posting a new paste to PasteBin...' , end='')
    
    P = { 
        'api_dev_key': 'Wk2gBzlFUbTmMCEaST5KpINUFBUn0Y9M ',
        'api_option': 'paste', 'api_paste_code': body_text,
        'api_paste_name': title,
        'api_paste private': 0 if listed else 1,
        'api_paste expire_date': expiration
        }

    paste_url = 'https://pastebin.com/api/api_post.php'
    resp_msg = requests.post(paste_url, data= P)

    if resp_msg.status_code == requests.codes.OK:
        print('success')
        return resp_msg.text
   
    else:
        print('failed')
        print(f'Status code: {resp_msg.status_code}, Error reason: {resp_msg.reason}')
        return None

