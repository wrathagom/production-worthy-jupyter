# Production Worthy Jupyter
I believe Jupyter to be a very capable, even production worthy, tool for Data Engineering, Analysis, and Science. Jupyter gets a bad rap mostly because how it is commonly used, but most all "proper" coding ideas can be applied to Jupyter. In this repo I am laying the foundation for a robust, scaleable, shareable, modular solution almost entirely built on Jupyter.

In this repo I'll demonstrate how I can explore, analyze, and develop in a Notebook. I can perform tasks as a Data Engineer, Analyst, or Scientist. I can string together multiple notebooks together to form a pipeline of notebooks and lastly I can take that pipeline and schedule it to run.

## Quick Start

To get started with this repo you need to make sure you have Docker and Docker Compose installed. From there it's just two commands away:

 - `git clone https://github.com/wrathagom/production-worthy-jupyter.git`
 - `cd production-worthy-jupyter && docker-compose up`

## How To Use This Repo

### Creating Your Own Project

The above just gets you into Jupyter as fast as possible, but really this repo is designed to be used as boilerplate for scaleable ata projects. When I want to create a new project from this repo, here's what I do:

1. Create a folder for my project to live in `mkdir my-new-project`
2. Change directories into the new project folder `cd my-new-project`
3. Clone this repo into that folder `git clone https://github.com/wrathagom/production-worthy-jupyter.git .`
4. Create a new repo on Github or Gitlab
5. Change the origin URL to the new repo `git remote set-url origin new_url`

### Customizing Your Packages

There are two primary ways of customizing which packages are available inside the container and to the notebooks:

 - Modifying the `requirements.txt` file and re-building the image. This approach is best for packages that are shared across multiple notebooks or packages that are needed outside of a notebook, but inside of a container.

 - Adding a `!pip install package_name` to te first cell of your notebook. This approach is best for packages used by a single notebook.

When I am building a notebook and I encounter a package that is not installed I first like to `!pip install` it directly in the notebook. This does a few things: it allows me to troubleshoot installing the package, it allows me to get the version of the package installed, and it doesn't slow down my Notebook development at all. When you use this method you should get an output similar to the below:

```

```

Once I've done this and it is working I tend to use the version from the above install method and modify the requirements file. So for the above example I would add the below to `requirements.txt`

```

```



### Clone to a different folder

When I want to create a new project based on

Robust, production worthy, ready to go Jupyter Notebooks
