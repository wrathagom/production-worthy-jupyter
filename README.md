# Production Worthy Jupyter
I believe Jupyter to be a very capable, even production worthy, tool for Data Engineering, Analysis, and Science. Jupyter gets a bad rap mostly because how it is commonly used, but most all "proper" coding ideas can be applied to Jupyter. In this repo I am laying the foundation for a robust, scaleable, shareable, modular solution almost entirely built on Jupyter.

In this repo I'll demonstrate how I can explore, analyze, and develop in a Notebook. I can perform tasks as a Data Engineer, Analyst, or Scientist. I can string together multiple notebooks together to form a pipeline of notebooks and lastly I can take that pipeline and schedule it to run.

## Quick Start

To get started with this repo you need to make sure you have Docker and Docker Compose installed. From there it's just two commands away:

 - `git clone https://github.com/wrathagom/production-worthy-jupyter.git`
 - `cd production-worthy-jupyter && docker-compose up`

## How To Use This Repo

### Creating Your Own Project

The above just gets you into Jupyter as fast as possible, but really this repo is designed to be used as boilerplate for scaleable data projects. When I want to create a new project from this repo, I have a couple of options:

#### Github Templates

This repo is marked as a template, so on Github you should see a green **Use this template** button. If you click that you will be prompted to create a new repository by giving it a name, etc.

This is certainly the easiest way to get started with this repo and it's a cool newish feature added by Github.

#### The Old Way

Alternatively you can clone this repo and do a few extra steps to set it up on a repo of your own:

1. Create a folder for my project to live in `mkdir my-new-project`
2. Change directories into the new project folder `cd my-new-project`
3. Clone this repo into that folder `git clone https://github.com/wrathagom/production-worthy-jupyter.git .`
4. Create a new repo on Github or Gitlab
5. Change the origin URL to the new repo `git remote set-url origin new_url`

### Customizing Your Packages

There are two primary ways of customizing which packages are available inside the container and to the notebooks:

 - Modifying the `requirements.txt` file and re-building the image. This approach is best for packages that are shared across multiple notebooks or packages that are needed outside of a notebook, but inside of a container. I've added a `# Custom tools for your project` seciont to the requirements.txt. This is where I put custom package requirments for my projects, just to keep them all together.

 - Adding a `!pip install package_name` to te first cell of your notebook. This approach is best for packages used by a single notebook.

When I am building a notebook and I encounter a package that is not installed I first like to `!pip install` it directly in the notebook. This does a few things: it allows me to troubleshoot installing the package, it allows me to get the version of the package installed, and it doesn't slow down my Notebook development at all. When you use this method you should get an output similar to the below:

```
Collecting gpxpy
  Downloading gpxpy-1.6.0-py3-none-any.whl.metadata (5.9 kB)
Downloading gpxpy-1.6.0-py3-none-any.whl (42 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 42.6/42.6 kB 601.1 kB/s eta 0:00:000:00:01
Installing collected packages: gpxpy
Successfully installed gpxpy-1.6.0

```

Once I've done this and it is working I tend to use the version from the above install method and modify the requirements file. So for the above example I would add the below to `requirements.txt`

```
gpxpy==1.6.0
```

### Saving Secrets and Credentials

In the `data/notebooks` directory there is a secrets.yml.example file. If the project I am working on requires credentials or secrets of any sorts I start out by duplicating this file and renaming it to just `secrets.yml`. This file is ignored by git using a .gitignore file and wont be committed back to the repository.

Then I can use a snippt like the below to load the file and utilize the credentials stored within.

```
import yaml

with open("config.yml", 'r') as ymlfile:
    cfg = yaml.safe_load(ymlfile)
```

Obviously care must be taken not to print these or any other secrets out when using the notebook else they could still be committed and made public. But this method provides a reasonable way of managing credentials in your notebooks.

### Creating a Pipeline

To create a pipeline I am using another notebook! The notebook uses Papermill to execute a series of notebook in sequence. If I wanted to get fancy I could have some of them execute in parallel and I may do that, but for now, this works.

This pipeline is stored in the `entrypoint.ipynb` by default.

### Scheduling Your Pipeline

Now that you have everything working just the way you want it we can schedule our pipeline to run. The command we're going to use when scheduling is:

```
docker-compose run --rm --entrypoint "./run.sh entrypoint.ipynb" jupyter
```

This command tells docker to run the service in the compose file called `jupyter` we override the default entrypoint, the command ran inside the container, to run the `entrypoint.ipynb` notebook.

Now that we now the command, we can use our favorite scheduling tool to schedule it. On most unix systems, the easiest tool to do that would be cron.
