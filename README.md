# Overview
As sample app that uses NextJS on the frontend and twirp on the backend. Test out a sample call by loading the frontend and clicking on the `Twirp Test Button` on the UI

# Setup

## Dependencies
- `brew install python3`
- `brew install poetry`
- `brew install nvm`
- `brew install go`
- `brew install protoc-gen-go`
- Setup `GOPATH` and `GOROOT` if necessary
    ```
    export GOPATH="${HOME}/.go"
    export GOROOT="$(brew --prefix golang)/libexec"
    export PATH="$PATH:${GOPATH}/bin:${GOROOT}/bin"
    ```
- `go get github.com/verloop/twirpy/protoc-gen-twirpy`

### Server
- `cd server`
- `poetry install`
- `protoc --python_out=./generated --twirpy_out=./generated --proto_path=../protobufs ../protobufs/*.proto`
- `poetry run uvicorn server:app --port=3001`
- Test with 
    ```
    curl --request "POST" \
        --header "Content-Type: application/json" \
        --data '{"inches":"2"}' \
        http://localhost:3001/twirp/twirp.example.haberdasher.Haberdasher/MakeHat
    ```

### web-client
- `nvm use 15`
- `cd web-client`
- `npm ci`
- `protoc --plugin=./node_modules/.bin/protoc-gen-ts --ts_out ./generated --proto_path ../protobufs ../protobufs/*.proto`
- `npm run dev`
- Go to `http://localhost:3000`