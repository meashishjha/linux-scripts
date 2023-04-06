#!/bin/bash

# Define default values for the parameters
username=""
vault_env=""
app_env=""
vault_key=""
filename=""
file_path=""
b64_string=""

# Define the functions to check for individual parameters
get_username() {
  if [ -n "$1" ]; then
    username="$1"
  elif [ -n "$USERNAME" ]; then
    username="$USERNAME"
  elif [ -f "config.cfg" ]; then
    source config.cfg
  fi
}

get_vault_env() {
  if [ -n "$1" ]; then
    vault_env="$1"
  elif [ -n "$VAULT_ENV" ]; then
    vault_env="$VAULT_ENV"
  elif [ -f "config.cfg" ]; then
    source config.cfg
  fi
}

get_app_env() {
  if [ -n "$1" ]; then
    app_env="$1"
  elif [ -n "$APP_ENV" ]; then
    app_env="$APP_ENV"
  elif [ -f "config.cfg" ]; then
    source config.cfg
  fi
}

get_vault_key() {
  if [ -n "$1" ]; then
    vault_key="$1"
  elif [ -n "$VAULT_KEY" ]; then
    vault_key="$VAULT_KEY"
  elif [ -f "config.cfg" ]; then
    source config.cfg
  fi
}

get_filename() {
  if [ -n "$1" ]; then
    filename="$1"
  elif [ -n "$FILENAME" ]; then
    filename="$FILENAME"
  elif [ -f "config.cfg" ]; then
    source config.cfg
  fi
}

get_file_path() {
  if [ -n "$1" ]; then
    file_path="$1"
  elif [ -n "$FILE_PATH" ]; then
    file_path="$FILE_PATH"
  elif [ -f "config.cfg" ]; then
    source config.cfg
  fi
}

get_b64_string() {
  if [ -n "$1" ]; then
    b64_string="$1"
  elif [ -n "$B64_STRING" ]; then
    b64_string="$B64_STRING"
  elif [ -f "config.cfg" ]; then
    source config.cfg
  fi
}

# Check if parameters are passed through command line
while getopts "u:v:a:k:f:p:b:" opt; do
  case $opt in
    u) get_username "$OPTARG";;
    v) get_vault_env "$OPTARG";;
    a) get_app_env "$OPTARG";;
    k) get_vault_key "$OPTARG";;
    f) get_filename "$OPTARG";;
    p) get_file_path "$OPTARG";;
    b) get_b64_string "$OPTARG";;
    \?) echo "Invalid option -$OPTARG" >&2; exit 1;;
  esac
done

# Check for any mandatory parameters that have not been set
if [ -z "$username" ]; then
  echo "Missing username"
  exit 1
fi

if [ -z "$vault_env" ]; then
  echo "Missing vault_env"
  exit 1
fi

if [ -z "$filename" ]; then
  echo "Missing filename"
  exit 1
fi

if [ -z "$b64_string" ]; then
  echo "Missing b64_string"
  exit 1
fi

# Print the values of the parameters
echo "username: $username"
echo "vault_env: $vault_env"
echo "app_env: $app_env"
echo "
