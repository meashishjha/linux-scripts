#!/bin/bash

# source the script to be tested
. ./script.sh

# define test cases
test_missing_mandatory_param() {
  # unset the mandatory parameter
  unset VAULT_ENV
  # expect the script to exit with non-zero status
  assertFalse "missing mandatory parameter should fail" get_params
}

test_all_params_from_command_line() {
  # pass all parameters as command line arguments
  local params=(-u "alice" -v "prod" -k "secret" -b "dGVzdA==" -f "data.txt" -p "/home/alice" -a "dev")
  # expect the script to succeed and set the parameters correctly
  assertTrue "all parameters from command line should succeed" get_params "${params[@]}"
  assertEquals "username should be alice" "alice" "$USERNAME"
  assertEquals "vault_env should be prod" "prod" "$VAULT_ENV"
  assertEquals "app_env should be dev" "dev" "$APP_ENV"
  assertEquals "vault_key should be secret" "secret" "$VAULT_KEY"
  assertEquals "filename should be data.txt" "data.txt" "$FILENAME"
  assertEquals "file_path should be /home/alice" "/home/alice" "$FILE_PATH"
  assertEquals "b64_string should be dGVzdA==" "dGVzdA==" "$B64_STRING"
}

test_optional_params_from_command_line() {
  # pass only the mandatory and optional parameters as command line arguments
  local params=(-u "alice" -v "prod" -k "secret" -b "dGVzdA==")
  # expect the script to succeed and set the parameters correctly, with empty strings for the optional parameters
  assertTrue "optional parameters from command line should succeed" get_params "${params[@]}"
  assertEquals "username should be alice" "alice" "$USERNAME"
  assertEquals "vault_env should be prod" "prod" "$VAULT_ENV"
  assertEquals "app_env should be empty" "" "$APP_ENV"
  assertEquals "vault_key should be secret" "secret" "$VAULT_KEY"
  assertEquals "filename should be empty" "" "$FILENAME"
  assertEquals "file_path should be empty" "" "$FILE_PATH"
  assertEquals "b64_string should be dGVzdA==" "dGVzdA==" "$B64_STRING"
}

test_all_params_from_env_vars() {
  # set all parameters as environment variables
  export USERNAME="bob"
  export VAULT_ENV="dev"
  export APP_ENV="test"
  export VAULT_KEY="my_key"
  export FILENAME="data.txt"
  export FILE_PATH="/tmp"
  export B64_STRING="dGhpcyBpcyBhIHRlc3Q="
  # expect the script to succeed and set the parameters correctly
  assertTrue "all parameters from environment variables should succeed" get_params
  assertEquals "username should be bob" "bob" "$USERNAME"
  assertEquals "vault_env should be dev" "dev" "$VAULT_ENV"
  assertEquals "app_env should be test" "test" "$APP_ENV"
  assertEquals "vault_key should be my_key" "my_key" "$VAULT_KEY"
  assertEquals "filename should be data.txt" "data.txt" "$FILENAME"
  assertEquals "file_path should be /tmp" "/tmp" "$FILE_PATH"
  assertEquals "b64_string should be dGhpcyBpcyBhIHRlc3Q=" "dGhpcyBpcyBhIHRlc3
