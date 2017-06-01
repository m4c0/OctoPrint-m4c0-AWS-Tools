# OctoPrint-m4c0-AWS-Tools

This plugin integrates OctoPrint with AWS. Currently, it supports nothing.

Planned features (in order of priority):

* Publish metrics to Amazon Cloud Watch (this enables alarms via SNS ans such)
* Send notifications thru Amazon SNS (ex: M117 messages, print ended, etc)
* Backup logs in Amazon S3 (which can be consumed by other AWS tools)
* Whatever I get from user's feedback

## Setup

Install via the bundled [Plugin Manager](https://github.com/foosel/OctoPrint/wiki/Plugin:-Plugin-Manager)
or manually using this URL:

    https://github.com/m4c0/OctoPrint-m4c0-AWS-Tools/archive/master.zip

This document assumes you already have a working AWS account. Explaining how it works and how to
setup an account is beyond the scope of this document. You should also keep track of your bill.
This plugin tries to be as frugal as possible, but AWS does have an associated cost and tracking
them is not covered.

Also, don't use your root account with this plugin. Create a new IAM user, and add the permissions
as needed. Example for publishing Cloud Watch metrics:

    {
        "Version": "2012-10-17",
        "Statement": [
            {
                "Sid": "Stmt1496303376000",
                "Effect": "Allow",
                "Action": [
                    "cloudwatch:PutMetricData"
                ],
                "Resource": [
                    "*"
                ]
            }
        ]
    }

As a personal recommendation, it's useful to also install [AWS CLI](http://aws.amazon.com/cli/).
This plugin uses [Boto3](https://aws.amazon.com/sdk-for-python/) to integrate with AWS, and that
library can use the same configuration from AWS CLI. This allows you to do your own custom
AWS integrations.

## Configuration

**TODO:** Describe your plugin's configuration options (if any).

