# languagetutor

Install devcontainers extension
https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers

The extension may prompt you to reopen in devcontainer


## Run docker (Windows Powershell)
1. Install docker desktop from https://docs.docker.com/desktop/install/windows-install/
2. From the root of the project, run `docker buildx build . -t <NAME_OF_PREFERENCE_FOR_IMAGE>` (e.g. `docker buildx build . -t muh-image`)
3. Run `docker run <NAME_OF_PREFERENCE_FOR_IMAGE>` (you can also include `--name <NAME_OF_PREFERENCE_FOR_CONTAINER>` if you'd prefer to manually name your container, too)
4. In another instance of Powershell, run `docker ps` or check Docker Desktop's GUI as shown here
![Image of Docker Desktop with containers tab enclosed in red rectangle](https://i.ibb.co/m9NChm9/image.png)
In the case of Powershell, you should see something like this:
```
CONTAINER ID   IMAGE                                                                                  COMMAND                  CREATED          STATUS          PORTS     NAMES
37bdce2329ee   vsc-llang-tutor-7f86ff84fd09851d50183df0ed913a17735cb1904dfee9bb3eed39254af1f8b2-uid   "/bin/sh -c 'echo Co…"   2 hours ago      Up 50 minutes             funny_golick
```
