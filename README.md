# twitter-screenshot
REST service for generating pretty screenshots of Tweets.
It uses [Selenium](https://www.selenium.dev/) to take screenshots inside of an [AWS Lambda](https://aws.amazon.com/lambda/).

## Overview
`twitter-screenshot` is an [AWS SAM](https://aws.amazon.com/serverless/sam/) application that deploys an API containing a single endpoint, `/screenshot/{tweet_url}`.

When you `GET /screenshot/{tweet_url}`, where `tweet_url` is a [URL-encoded](https://en.wikipedia.org/wiki/URL_encoding) Tweet URL, the service takes a screenshot and returns the PNG image in the response body.

### Example

```
GET /screenshot/https%3A%2F%2Ftwitter.com%2Fgabebergado%2Fstatus%2F1317104551032442880%3Fs%3D20
```
![example Tweet screenshot](example_screenshot.png)

## Features
- Actually opens a browser and screenshots the Tweet, so it'll look just like a screenshot on your device.
- Automatically excludes like/share/retweet controls and hides like/share/retweet/etc. counts and view counts.
- Pads resulting image to a square, so it is suitable to post on other social media.

## Known issues
- High latency—the remote service takes several seconds to launch Chrome and load the Tweet before it can take a screenshot. In fact, sometimes, the endpoint times out.
- Layout quirks—e.g., very tall images can get clipped.

## Project structure
```
.
├── README.md
├── __init__.py
├── app                             -- application code
│   ├── Dockerfile                  -- container image Dockerfile for Lambda runtime
│   ├── __init__.py
│   ├── handler.py                  -- Lambda handler code
│   ├── install-browsers.sh         -- script to install Chrome and WebDriver in container
│   ├── requirements.txt            -- Python dependencies including Selenium and Pillow
│   └── screenshotter               -- Wrapper around Selenium for screenshotting Tweets
│       └── ...
└── template.yaml                   -- declares resources for SAM serverless API
```

## Endpoints

### `/screenshot/{tweet_url}`: Take Screenshot
**Path parameters:**
- `tweet_url`: either:
    - URL-encoded tweet URL (e.g., `https%3A%2F%2Ftwitter.com%2Fgabebergado%2Fstatus%2F1317104551032442880%3Fs%3D20`)
    - URL-encoded tweet path (after `https://twitter.com/`) (e.g., `gabebergado%2Fstatus%2F1317104551032442880%3Fs%3D20`) 
**Response codes:**
- **200 OK:** Success. Response body is screenshot PNG.
- **400 Bad Request:** invalid Tweet URL, or some other error. See `message` in response body JSON.

API Gateway may return other error codes. See [documentation](https://docs.aws.amazon.com/apigateway/latest/developerguide/supported-gateway-response-types.html) for more details.

## Deploying
0. Make sure [AWS CLI](https://aws.amazon.com/cli/) and [SAM CLI](https://aws.amazon.com/serverless/sam/) are installed.
1. Make sure the [AWS CLI can access your AWS account credentials](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-configure.html).
2. In the project root, run `sam build && sam deploy --guided`
3. Enter deployment configuration.
4. Try it! Copy the endpoint URL from `Outputs` and paste a URL-encoded Tweet URL, such as `https%3A%2F%2Ftwitter.com%2Fgabebergado%2Fstatus%2F1317104551032442880%3Fs%3D20`.