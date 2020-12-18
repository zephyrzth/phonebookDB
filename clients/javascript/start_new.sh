if [[ -n "${BASEURL}" ]]; then
  sed -i "s=http://0.0.0.0:32000=${BASEURL}=" ./index.html
fi
python3 -m http.server 9999
