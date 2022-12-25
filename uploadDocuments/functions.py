# function to store a file in a Postgres database using Django

def handle_uploaded_file(f):
    with open('uploadDocuments/upload/'+f.name, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)