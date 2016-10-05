# Zappa IP API

API to retrieve your IP using [Zappa][zappa] for [AWS Lambda][aws-lambda] and [Bottle][bottle]

## Requirements

This project use [zappa][zappa] to package the WSGI app for [AWS Lambda][aws-lambda].
You will need to get your ACCESS and SECRET key from [Amazon AWS][aws-security-credentials].

## Quickstart

```shell
virtualenv env
source env/bin/activate
pip install -r requirements.txt
zappa deploy dev
```


[aws-lambda]: https://aws.amazon.com/lambda/
[bottle]: http://bottlepy.org
[zappa]: https://www.zappa.io/
[aws-security-credentials]: https://console.aws.amazon.com/iam/home#security_credential
