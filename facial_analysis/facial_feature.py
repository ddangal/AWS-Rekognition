import boto3
import base64
import json
import os
print(os.environ['SATKAR'])

# os.environ['aws_session_token'] = 'FwoGZXIvYXdzEDQaDHRAMkQECLlDVNECQiLKAXG1EBS3wrfo1R7tDy0DENqARRqljB8E22DPgTTc466m5GEq00Zbq35UM2IGRv9gQo69JAA4NymFa9iyRGU9D3eZbmPZsTX+zVW7wo1AXkoNHJS6kmHDoipEf/CvlvWkX2ydp8cvKZDOBNf+HFdrES4alEoiVTj7+Bk2ghgmcqo1o+g+12PwJRCOj47Xm6FgAiMBVdjO/jq6JnVPs7CHh3OtiInjVALdVUTB9eObKUBOBadnwDtsHmAHf1T3pxXz0cToWh6vkrfEN1Ao/f7s+QUyLVsrj/X0W7X8vfpj8B7C80hHhQReiFL+JS80/xpd2YJwzS2RHzObphSsGnw/bg=='
# os.environ['aws_access_key_id'] = 'ASIATW5MAJVHTHMUR6EE'
# os.environ['aws_secret_access_key'] = 'XAM+l4nJnjECJcPEAzDhgmKdEHEtHhKDbZd/R4hm'
# rekognition_client = boto3.client('rekognition',aws_session_token='FwoGZXIvYXdzEDQaDHRAMkQECLlDVNECQiLKAXG1EBS3wrfo1R7tDy0DENqARRqljB8E22DPgTTc466m5GEq00Zbq35UM2IGRv9gQo69JAA4NymFa9iyRGU9D3eZbmPZsTX+zVW7wo1AXkoNHJS6kmHDoipEf/CvlvWkX2ydp8cvKZDOBNf+HFdrES4alEoiVTj7+Bk2ghgmcqo1o+g+12PwJRCOj47Xm6FgAiMBVdjO/jq6JnVPs7CHh3OtiInjVALdVUTB9eObKUBOBadnwDtsHmAHf1T3pxXz0cToWh6vkrfEN1Ao/f7s+QUyLVsrj/X0W7X8vfpj8B7C80hHhQReiFL+JS80/xpd2YJwzS2RHzObphSsGnw/bg==', aws_access_key_id='ASIATW5MAJVHTHMUR6EE', aws_secret_access_key='XAM+l4nJnjECJcPEAzDhgmKdEHEtHhKDbZd/R4hm', region_name='us-east-1')
# rekognition_client = boto3.client('rekognition', aws_session_token=os.getenv('aws_session_token'), aws_access_key_id=os.getenv('aws_access_key_id'), aws_secret_access_key=os.getenv('aws_secret_access_key'), region_name='us-east-1')
# rekognition_client = boto3.client('rekognition')

# file = open('img1.jpg','rb').read()
# print(os.getenv('aws_session_token'))

# response = rekognition_client.detect_faces(
#     Image={
#         'Bytes': file
#     },
#     Attributes=['ALL']
# )
# for face in response['FaceDetails']:
#     print(json.dumps(face, indent=4, sort_keys=True))

# print(json.dumps(response['FaceDetails']))