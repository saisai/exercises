how to install go

# https://golang.org/dl/
wget -c https://golang.org/dl/go1.15.2.linux-amd64.tar.gz 
shasum -a 256 go1.7.3.linux-amd64.tar.gz
sudo tar -C /usr/local -xvzf go1.15.2.linux-amd64.tar.gz
or 
sudo tar -C /opt -xvzf go1.15.2.linux-amd64.tar.gz
mkdir -p ~/go/{bin,src,pkg}


export PATH=$PATH:/opt/go/bin
export GOPATH="$HOME/go"
export GOBIN="$GOPATH/bin"
export GOROOT=/opt/go
export PATH=$PATH:$GOROOT/bin

source ~/.bash_profile
go version
go env

# 
# https://www.tecmint.com/install-go-in-linux/
# 

# go install modules
go mod init tidy
go mod tidy
go get -u github.com/fogleman/gg


https://www.digitalocean.com/community/tutorials/how-to-install-go-on-ubuntu-18-04
https://golang.org/doc/tutorial/getting-started
https://dev.to/takakd/go-package-is-not-in-goroot-3pec