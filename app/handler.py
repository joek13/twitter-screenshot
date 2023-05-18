import screenshotter
import urllib.parse
from io import BytesIO
import base64
import json

def lambda_handler(event, context):
    """Sample pure Lambda function

    Parameters
    ----------
    event: dict, required
        API Gateway Lambda Proxy Input Format

        Event doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html#api-gateway-simple-proxy-for-lambda-input-format

    context: object, required
        Lambda Context runtime methods and attributes

        Context doc: https://docs.aws.amazon.com/lambda/latest/dg/python-context-object.html

    Returns
    ------
    API Gateway Lambda Proxy Output Format: dict

        Return doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html
    """

    try:
        path_params = event["pathParameters"]
        if path_params is None or not path_params.get("tweet_url"):
            raise ValueError("Path parameter 'tweet_url' is required.")

        tweet_url = urllib.parse.unquote(path_params["tweet_url"])

        browser = screenshotter.driver.get_driver()

        image = screenshotter.twitter.screenshot_tweet(browser, tweet_url)
        image = screenshotter.imgutil.pad_square(image, (255,255,255,255))
        buffer = BytesIO()
        image.save(buffer, "png")
    except ValueError as e:
        print(f"Caught {e}")
        return {
            "statusCode": 400,
            "isBase64Encoded": False,
            "body": json.dumps({ "message": str(e) })
        }

    return {
        "statusCode": 200,
        "headers": { "Content-Type": "image/png" },
        "body": base64.b64encode(buffer.getvalue()).decode("utf-8"),
        "isBase64Encoded": True
    }
