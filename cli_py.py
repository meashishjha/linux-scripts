def get_params():
    parser = argparse.ArgumentParser()
    parser.add_argument("-u", "--username", help="Username")
    parser.add_argument("-v", "--vault_env", help="Vault environment")
    parser.add_argument("-a", "--app_env", help="App environment")
    parser.add_argument("-k", "--vault_key", help="Vault key")
    parser.add_argument("-f", "--filename", help="Filename")
    parser.add_argument("-p", "--file_path", help="File path")
    parser.add_argument("-b", "--b64_string", help="Base64 encoded string")
    args = parser.parse_args()

    config = configparser.ConfigParser()
    config.read('config.cfg')

    # Check for environment variables and use them as fallback values
    if not args.username:
        args.username = os.environ.get('USERNAME', '')
    if not args.vault_env:
        args.vault_env = os.environ.get('VAULT_ENV', '')
    if not args.app_env:
        args.app_env = os.environ.get('APP_ENV', config.get('DEFAULT', 'APP_ENV', fallback=''))
    if not args.vault_key:
        args.vault_key = os.environ.get('VAULT_KEY', '')
    if not args.filename:
        args.filename = os.environ.get('FILENAME', config.get('DEFAULT', 'FILENAME', fallback=''))
    if not args.file_path:
        args.file_path = os.environ.get('FILE_PATH', config.get('DEFAULT', 'FILE_PATH', fallback=''))
    if not args.b64_string:
        args.b64_string = os.environ.get('B64_STRING', '')

    mandatory_params = ['username', 'vault_env', 'vault_key', 'b64_string']
    for param in mandatory_params:
        if not getattr(args, param):
            sys.exit(f"Missing mandatory parameter: {param}")

    # base64 decode the string
    b64_decoded_str = base64.b64decode(args.b64_string).decode('utf-8')

    # convert the decoded string to dictionary
    try:
        b64_decoded_dict = json.loads(b64_decoded_str)
    except ValueError:
        sys.exit("Error: Invalid base64 string provided.")

    # add the decoded dictionary to the args object
    setattr(args, 'b64_decoded_dict', b64_decoded_dict)

    return args
