#!/usr/bin/env bash

PROXY_HOST=...
PROXY_PORT=...
PROXY_USER=...
PROXY_PWD=...
PROXY_PWD_ENC=...
PROXY_NONPROXY=..

PROXY=http://$PROXY_USER:$PROXY_PWD_ENC@$PROXY_HOST:$PROXY_PORT

use_proxy=true
if ! $1 ; then
  use_proxy=false
fi

###############################
# Export proxy in .bash_profile
# Clear proxy setting first
sed -i _bak '/export HTTP/d' ~/.bash_profile

# and then set it
if $use_proxy ; then
sed -i _bak "$ a\ 
export HTTP_PROXY=$PROXY\\
export HTTPS_PROXY=$PROXY\\
" ~/.bash_profile
fi

##################
# Set gradle proxy
# Clear proxy setting first
sed -i _bak '/^systemProp.http/d' ~/.gradle/gradle.properties

# and then set it
if $use_proxy ; then
sed -i _bak "$ a\  
systemProp.http.proxyHost=$PROXY_HOST\\
systemProp.http.proxyPort=$PROXY_PORT\\
systemProp.http.proxyUser=$PROXY_USER\\
systemProp.http.proxyPassword=$PROXY_PWD\\
systemProp.http.nonProxyHosts=$PROXY_NONPROXY\\
systemProp.https.proxyHost=$PROXY_HOST\\
systemProp.https.proxyPort=$PROXY_PORT\\
systemProp.https.proxyUser=$PROXY_USER\\
systemProp.https.proxyPassword=$PROXY_PWD\\
systemProp.https.nonProxyHosts=$PROXY_NONPROXY\\
" ~/.gradle/gradle.properties
fi

###################
# Set proxy for git
# Clear first
sed -i _bak '/^\[http\]/d' ~/.gitconfig
sed -i _bak '/proxy = /d' ~/.gitconfig

# then set
if $use_proxy ; then
sed -i _bak "$ a\ 
[http]\\
\        proxy = $PROXY\\
" ~/.gitconfig
fi

#################
# Set bower proxy
# Clear
sed -i _bak '/proxy"/d' ~/.bowerrc

# then set
if $use_proxy ; then
sed -i _bak "/{/ a\ 
\  \"proxy\": \"$PROXY\",\\
\  \"https-proxy\": \"$PROXY\"\\
" ~/.bowerrc
fi

###########
# NPM proxy
# Clear
sed -i _bak '/proxy=/d' ~/.npmrc

# then set
if $use_proxy ; then
sed -i _bak "$ a\ 
proxy=$PROXY\\
https-proxy=$PROXY\\
" ~/.npmrc
fi
