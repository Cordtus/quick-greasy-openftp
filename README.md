# quick-greasy-openftp

##runs on caddy with native filetransfer protocol
##requires python and pip


## Install Flask
`pip install Flask`
<br>
## create+configure web UI

### file structure

```
your_project_directory/
|-- app.py
|-- templates/
|   |-- upload.html
```

### directory/allowed filetypes settings [app.py]

```
UPLOAD_FOLDER = '/root/fileserv'  # Replace with your directory path
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}  # Allowed file types
```

### interface/port for app to listen on [app.py]

```
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)  # Replace with your desired host and port
```

## caddy config

### pre-existing caddy ftp block

```
ftp.your.domain {
    log {
        output file /var/log/ftp.log
        format json
    }
    root * /path/to/ftp/dir
    file_server browse
}
```

### add to the block for your desired domain

`reverse_proxy /upload localhost:8000`


## Running the Application

Start your Flask application by running python app.py.
Access the form by navigating to <http://your-server-ip:8000> in your web browser.
