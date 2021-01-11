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

### twirp-app
- `cd twirp-app`
- `poetry install`
- `./bin/run-dev.sh`
- Test with 
    ```
    curl --request "POST" \
        --header "Content-Type: application/json" \
        --data '{"inches":"2"}' \
        https://next-twirp-test-twirp-app.herokuapp.com//twirp/twirp.example.haberdasher.Haberdasher/MakeHat
    ```

### next-app
- `nvm use 15`
- `cd next-app`
- copy `.env.template` to `.env.local` and fill out variables
- `npm ci`
- `./bin/run-dev.sh`
- Go to `http://localhost:3000`


# Heroku Setup
- install heroku cli
- `heroku create next-twirp-test-next-app --remote heroku-next-app`
- `heroku stack:set -a next-twirp-test-next-app container`
- `heroku create next-twirp-test-twirp-app --remote heroku-twirp-app`
- `heroku stack:set -a next-twirp-test-twirp-app container`