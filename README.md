# Git By Doing Level 9 

Find out the criminals.

## TASK
Your task is to report the criminals to the police. 

1. Find out which bank were they initially planning to rob.
2. Who were the criminals.

After finding out the criminals to report run `python report.py` command in terminal.

## Story

There were 3 criminals who once tried to become rich quickly by robbing. First there was one mastermind, who planned something huge, but the other 2 guys said that this might be too risky, so we can do something small. Their intentions stayed the same, and they robbed a "--------". After 2 years one of them was caught, and they found a pendrive plugged into a laptop in his old appartment, which had one file in it, named `robbery.zip`. When the police tried to open it and explore what was inside, they could not find anything other than the `.git` folder and `README.md`, which had these contents.


```markdown
# Data erased
Ha ha, you wont find who did this.
```

So the police asked you to find out who the criminals were, and report them.



### How to play?
1. Clone this repo.
```bash
git clone https://github.com/aruncs31s/git_by_doing_level_9.git
```
2. unzip `robbery.zip` file.
3. Go to the unzipped folder.
4. Open terminal in that folder


## Git remote. 
"basically a bookmark for a different repository from which you may wish to pull or push code" 

if you have cloned this repo, run the following command
```bash
git remote
```
You will see something like this
```
origin
```

### What can i do with remote?
Imagine if you have forked one of my repository. And imagine you are working on some new features in that repo, when you fork it becomes your repo , so you have full permission to do anything you want , you can read from the online repo , you can write to the online repo.
you can read using this 
```bash
git pull origin main
```
you can write using this 
```bash
git push origin main
```

And what if I update my repo? Like you've cloned my repository and when you do `git pull origin main` you are pulling from your repo not mine. 

One way is to go to github.com and press the sync button. But you can setup multiple remotes too 
for example 

```bash
git remote add upstream https://github.com/aruncs31s/repo.git
```
now to pull from my repo you can do this 
```bash
git pull upstream main
```
and to push to your repo you can do this 
```bash
git push origin main
```
But there is a problem , since it is not your repo you can't push to it. Like if you want to have write access to my repository i would have to add you as a collaborator ( ie assign write access to you. )

Also you can see all the remotes using this command 
```bash
git remote -v
```
it will show you something like this 

![alt text](./imgs/image.png)


after adding upstream remote you will see something like this 

![alt text](./imgs/image-1.png)