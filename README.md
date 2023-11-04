# SimpleJenkinsDeploy
This project is about deploying a web service with Jenkins when a commit is made


## Deploy

To deploy, simply commit to the repository or run a build in the Jenkins website [here](https://ec2-52-57-150-144.eu-central-1.compute.amazonaws.com/jenkins/) <br />
Credentials:
- Username: admin
- Password: admin
The service can be accessed [here](http://ec2-52-57-150-144.eu-central-1.compute.amazonaws.com/)

## Issues I have faced
The most challenging task was deploying the Jenkins service with HTTPS. Initially, I encountered a timeout issue when attempting to access it outside of the VM.

After thorough investigation, I discovered an IPTables rule that seemed to be causing the problem. Once I removed it, everything worked flawlessly.
<br />
```
1    DNAT       tcp  --  anywhere             anywhere             tcp dpt:https to:127.0.0.1:8443
```

To make Jenkins accessible externally, I opted to expose it through an HAProxy reverse proxy.

The Docker container is configured with the `--restart unless-stopped` restart policy. <br />
With the `--restart unless-stopped` policy, the container will automatically restart if it exits, regardless of the exit status.
It ensures that the container remains running under normal circumstances. <br />
Importantly, the container will not restart if it is manually stopped. In other words, if you explicitly stop the container, it will not be automatically restarted.

If, for any reason, the service crashes and is not being restarted automatically, redeploying it is as easy as hitting the `Build Now` button on the Jenkins job.

## Notes

I wasn't entirely sure about the branch parameter requirement,  so for now, I've set up the pipeline to trigger every time a commit is pushed to the `*/couter-service` branch. If you meant that any branch can trigger the pipeline, leave the branch selector blank.