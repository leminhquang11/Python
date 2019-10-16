"""Retrieve an attachment from a Message.
"""

import base64
from apiclient import errors


def GetAttachments(service, user_id, msg_id, store_dir):
  """Get and store attachment from Message with given id.

  Args:
    service: Authorized Gmail API service instance.
    user_id: User's email address. The special value "me"
    can be used to indicate the authenticated user.
    msg_id: ID of Message containing attachment.
    store_dir: The directory used to store attachments.
  """
  try:
    message = service.users().messages().get(userId=user_id, id=msg_id).execute()

    for part in message['payload']['parts']:
      if part['filename']:

        file_data = base64.urlsafe_b64decode(part['body']['data']
                                             .encode('UTF-8'))

        path = ''.join([store_dir, part['filename']])

        f = open(path, 'w')
        f.write(file_data)
        f.close()

  except errors.HttpError:
    print ('An error occurred: %s' % error)
