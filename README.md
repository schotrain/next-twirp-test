# Overview
As sample app that uses NextJS on the frontend and twirp on the backend. Test out a sample call by loading the frontend and clicking on the `Twirp Test Button` on the UI

See [here](https://sequencediagram.org/index.html?presentationMode=readOnly#initialData=C4S2BsFMAIEEFdgAtoDJoCVIHMQGdgAnAQ1AHsA7aAMXDIHcAoZgOUgA9g4AHbgWgB8ASQAmABQBcAGTK4qWESEKQAxsEZtOPbgB4+oyQqWquAIWIqA1ho5dYvQbDFDoAZUiEAbh4nQA9ADikMCwKiqQeHgAKmSWkBQAFAYANNAGICKpeEjEyiLuKsrAAJQ2Wva6fE4u7l4+0ACqeB6h4ZExcRRldg4C1W4e3oS+gcFNHkIUAGZkANrjhK0R0bHxALoJpZo9lf21Q74slJDd2oLb2hJGymrQMdAAwsqkMAvQYsTYJxcVjs4DdWG-lcxG8C0mM3mzUIHXWCVw3goLGIAFtIKkpqiQOAAJ7ItGpSAo4jY1LcEBqeDKLa2bR6PaDerg6ZkRhAA) for a sequence diagram outlining the auth flow

# Setup

## Dependencies
- `brew install python3`
- `brew install poetry`
- `brew install nvm`
- `brew install go`
- `brew install protoc-gen-go`
- `brew install libvips`
- Setup `GOPATH` and `GOROOT` if necessary
    ```
    export GOPATH="${HOME}/.go"
    export GOROOT="$(brew --prefix golang)/libexec"
    export PATH="$PATH:${GOPATH}/bin:${GOROOT}/bin"
    ```
- `go get github.com/verloop/twirpy/protoc-gen-twirpy`

### twirp-app
- `cd twirp-app`
- copy `.env.template` to `.env.local` and fill out variables
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