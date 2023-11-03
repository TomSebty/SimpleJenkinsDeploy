# SimpleJenkinsDeploy
This project is about deploying a web service with Jenkins when a commit is made


## Deploy 
    To deploy, simply commit to the repository or run a build in the Jenkins website [here](https://ec2-52-57-150-144.eu-central-1.compute.amazonaws.com/jenkins/)
    Credentials:
    - Username: admin
    - Password: admin

    The service can be accessed [here](http://ec2-52-57-150-144.eu-central-1.compute.amazonaws.com/)

## Issues I have faced
The most difficult objective was deploying the Jenkins service on https. For some reason it was giving me
a timeout when trying to access it outside of the VM.
After some investigation, I found this IPTables rule that seemed off, and after removing it, everything worked!
`1    DNAT       tcp  --  anywhere             anywhere             tcp dpt:https to:127.0.0.1:8443`

I decided to expose the Jenkins through an HAProxy reverse proxy.